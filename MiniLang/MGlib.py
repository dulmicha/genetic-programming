from .generate import Program, GenerationMethod
from .interpreter import Interpreter
from .parameters import Parameters
from .fitness_functions import get_fitness_function
from numpy import round
import random
import os
import time
from copy import deepcopy


class MGlib:
    def __init__(self, inputs=None, outputs=None, parameters=None, example=None, method=GenerationMethod.FULL):
        self.inputs = inputs
        self.outputs = outputs
        self.parameters = parameters
        self.population_size = parameters.population_size
        self.method = method
        self.example = example
        self.population = [
            self.create_individual() for _ in range(self.parameters.population_size)
        ]
        self.population_copy = deepcopy(self.population)
        self.fitnesses = {
            i: self.compute_fitness(individual, True)
            for i, individual in enumerate(self.population)
        }
        self.best_idx = 0
        self.best_fitness = -1000000.0
        self.best_generation = 0
        self.best = None
        self.generation = 0
        self.avg_fitness = -1.0
        self.start_time = time.strftime("%H-%M-%S")
        print("\nStart time: ", self.start_time)

    @classmethod
    def from_serialized_population(
        cls, population_path, inputs, outputs, parameters, example
    ):
        print("From serialized population: ", population_path)
        parameters.population_size = 1
        lib = cls(inputs, outputs, parameters, example)
        serialized_population_size = len(os.listdir(population_path))
        lib.population = [
            Program.load(os.path.join(population_path, f"individual{i}.pkl"))
            for i in range(serialized_population_size)
        ]
        lib.population.extend(
            [
                lib.create_individual()
                for _ in range(
                    lib.parameters.population_size - serialized_population_size
                )
            ]
        )
        lib.population_size = lib.parameters.population_size = len(lib.population)
        lib.population_copy = deepcopy(lib.population)
        lib.fitnesses = {
            i: lib.compute_fitness(individual, True)
            for i, individual in enumerate(lib.population)
        }
        return lib

    def fitness_function(self, program_output, expected_output, inputs=None):
        return get_fitness_function(self.example)(
            program_output, expected_output, inputs
        )

    def create_individual(self):
        method = (
            self.method
            if self.method != GenerationMethod.HALF_HALF
            else random.choice([GenerationMethod.FULL, GenerationMethod.GROW])
        )
        return Program(
            self.parameters.max_depth,
            self.parameters.max_width,
            method,
            self.parameters.min_int,
            self.parameters.max_int,
            self.parameters.max_expression_depth,
            True,
        )

    def compute_fitness(self, individual, progress=False):
        if progress:
            print(".", end="", flush=True)
        fitness = 0
        for idx in range(len(self.inputs)):
            ind = str(individual)
            program_output, *_, uninitialized_references = Interpreter.run(
                ind,
                self.inputs[idx],
                from_file=False,
                instruction_limit=self.parameters.instruction_limit,
            )
            fitness += self.fitness_function(
                program_output, self.outputs[idx], self.inputs[idx]
            ) - (uninitialized_references / len(self.inputs))
        return round(fitness, 2)

    def compute_avg_fitness(self):
        return round(sum(self.fitnesses.values()) / len(self.fitnesses))

    def display_population_fitness(self):
        for idx, individual in enumerate(self.population):
            print(f"Program {idx + 1}:\n{individual}\n{self.fitnesses[idx]}\n")

    def display_population(self):
        for idx, individual in enumerate(self.population):
            print(f"Program {idx + 1}:\n{individual}\n")

    def select_tournament(self):
        tournament = random.sample(
            self.fitnesses.keys(), self.parameters.tournament_size
        )
        best_idx = max(tournament, key=lambda key: self.fitnesses[key])
        return self.population[best_idx]

    def select_neg_tournament_idx(self):
        tournament = random.sample(
            self.fitnesses.keys(), self.parameters.tournament_size
        )
        worst_idx = min(tournament, key=lambda key: self.fitnesses[key])
        return worst_idx

    def select_best(self):
        best_idx = max(self.fitnesses, key=lambda key: self.fitnesses[key])
        best_fitness = self.fitnesses[best_idx]
        if best_fitness > self.best_fitness:
            self.best_fitness = best_fitness
            self.best_idx = best_idx
            self.best = self.population[best_idx]
        print(f"Best fitness: {self.best_fitness}")
        return best_idx

    def select_worst(self):
        worst_idx = min(self.fitnesses, key=lambda key: self.fitnesses[key])
        worst_fitness = self.fitnesses[worst_idx]
        return worst_idx, worst_fitness

    def crossover(self) -> Program:
        p1 = self.select_tournament()
        while True:
            p2 = self.select_tournament()
            if p1 != p2:
                break
        parent1 = p1.root.copy()
        parent2 = p2.root.copy()
        child = self._crossover(parent1, parent2)
        while child == p1 or child == p2:
            child = self.crossover()
        return child

    def _crossover(self, parent1, parent2) -> Program:
        iterations = 0
        while True:
            child1 = random.choice(parent1.children)
            child2 = random.choice(parent2.children)
            if (
                child2.n_type in child1.get_compatible_types()
                and child1 != child2
                and random.random() < 0.7
            ):  # avoid always choosing first matching node
                break
            parent1 = child1 if child1.children and random.random() < 0.7 else parent1
            parent2 = child2 if child2.children and random.random() < 0.7 else parent2
            iterations += 1
            if iterations > 100:
                return (
                    self.crossover()
                    if random.random() < self.parameters.crossover_prob
                    else self.mutate()
                )

        child2 = child2.copy()
        child2.parent = child1.parent.copy()
        child2.level = child1.level
        parent1.replace_child(child1, child2)
        while not parent1.is_root:
            parent1 = parent1.parent

        return Program.from_root(parent1)

    def mutate(self) -> Program:
        p = self.select_tournament()
        parent1 = p.root.copy()
        parent2 = self.create_individual().root
        child = self._crossover(parent1, parent2)
        while child == p:
            child = self.mutate()
        return child

    def escape_local_optimum(self):
        worst = sorted(self.fitnesses, key=lambda key: self.fitnesses[key])[
            : int(self.population_size * 0.01)
        ]
        for i in worst:
            self.population[i] = self.create_individual()
            self.fitnesses[i] = self.compute_fitness(self.population[i])

    def run(self, serialize=False):
        found = False
        for gen in range(self.parameters.generations):
            i = self.select_best()
            print(
                f"Generation {gen + 1}, best fitness: {self.best_fitness}, avg fitness: {self.compute_avg_fitness()}, "
                f"worst fitness {self.select_worst()[1]}\n"
            )
            if self.best_fitness == 0.0:
                self.save_result_to_file(i, True, self.best_fitness)
                print("Problem solved!\n")
                self.serialize_population()
                found = True
                break
            else:
                self.save_result_to_file(i, False, self.best_fitness)

            for i in range(self.population_size):
                print(f"Operation {i+1} of {self.population_size}", end="\r")
                worst_index = self.select_neg_tournament_idx()
                worst_fitness = self.fitnesses[worst_index] * 1.3
                new_fitness = worst_fitness - 1
                tries = 0
                while new_fitness < worst_fitness:
                    print(
                        f"\t\t\t Try {tries+1: >3} of 50, fitness to beat: {round(worst_fitness, 2): >10}",
                        end="\r",
                    )
                    rand_prob = random.random()
                    if rand_prob < self.parameters.crossover_prob:
                        new_individual = self.crossover()
                    else:
                        new_individual = self.mutate()
                    new_fitness = self.compute_fitness(new_individual)
                    tries += 1
                    if tries > 50:
                        worst_fitness *= 1.1
                        tries = 0

                self.fitnesses[worst_index] = new_fitness
                self.population_copy[worst_index] = new_individual

            self.population = deepcopy(self.population_copy)
            self.generation += 1
            print(end="\r")
            print("\n")

        if not found:
            print(f"Problem not solved")
            print(f"Best fitness: {self.best_fitness}\n")

    def print_individual(self, index: int):
        individual_program = self.population[index]
        ind_str = str(individual_program)
        print("---------------------")
        print("Program: ")
        print(individual_program)
        print("---------------------\n")
        return ind_str

    def save_result_to_file(self, best_index, found, best_fitness):
        example_path = os.path.join("results", self.example)
        os.makedirs(example_path, exist_ok=True)
        path = os.path.join(example_path, f"results_{self.start_time}.txt")
        with open(path, "w") as f:
            f.write(f"Parameters:\n{self.parameters}\n")
            if not found:
                f.write("Problem not solved\n")
            else:
                f.write(f"Problem solved\n")
            f.write(self.print_individual(best_index))
            f.write("\n")
            f.write(
                f"Fitness values: {best_fitness}, Generation: {self.generation + 1}\n"
            )

    def serialize_population(self):
        _dir = os.path.join("results", self.example, "population")
        os.makedirs(_dir, exist_ok=True)
        for i, individual in enumerate(self.population):
            individual.save(os.path.join(_dir, f"individual{i}.pkl"))


def serialize_deserialize():
    genetic = MGlib(inputs=[], outputs=[], parameters=params)
    individual = genetic.create_individual()
    print("before saving:\n", individual)
    individual.save("individual1.pkl")
    individual2 = Program.load("individual1.pkl")
    print("after reading:\n", individual2)


if __name__ == "__main__":
    params = Parameters(
        max_depth=2,
        max_width=2,
        population_size=2,
        generations=5,
        tournament_size=3,
        crossover_prob=0.7,
        mutation_prob=0.1,
    )
    serialize_deserialize()
