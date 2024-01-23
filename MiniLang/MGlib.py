from generate import Program, GenerationMethod
from interpreter import Interpreter
from parameters import Params
from fitness_functions import get_fitness_function
from antlr4 import *
import random
import os


class MGlib:
    inputs: list
    outputs: list
    parameters: Params

    def __init__(self, inputs=None, outputs=None, parameters=None, example=None):
        self.inputs = inputs
        self.outputs = outputs
        self.parameters = parameters
        self.population_size = parameters.population_size
        self.method = GenerationMethod.FULL
        self.max_iterations = 10
        self.example = example
        self.population = [
            self.create_individual() for _ in range(self.parameters.population_size)
        ]
        self.fitnesses = {
            i: self.compute_fitness(individual)
            for i, individual in enumerate(self.population)
        }
        self.best_idx = 0
        self.best_fitness = -1000000.0
        self.best_generation = 0
        self.best = None
        self.generation = 0
        self.avg_fitness = -1.0

    def fitness_function(self, program_output, expected_output):
        return get_fitness_function(self.example)(program_output, expected_output)

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
            self.max_iterations,
            -100,
            100,
        )

    def compute_fitness(self, individual):
        fitness = 0
        for idx in range(len(self.inputs)):
            ind = str(individual)
            program_output, *_ = Interpreter.run(ind, self.inputs[idx], from_file=False)
            fitness += self.fitness_function(program_output, self.outputs[idx])
        return fitness

    def compute_avg_fitness(self):
        return sum(self.fitnesses.values()) / len(self.fitnesses)

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

    def select_neg_tournament(self):
        pass

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
        p1, p2 = self.select_tournament(), self.select_tournament()
        parent1 = p1.root.copy()
        parent2 = p2.root.copy()
        return self._crossover(parent1, parent2)

    def _crossover(self, parent1, parent2) -> Program:
        iterations = 0
        while True:
            child1 = random.choice(parent1.children)
            child2 = random.choice(parent2.children)
            if child1.get_compatible_types() == child2.get_compatible_types():
                break
            parent1 = child1 if child1.children and random.random() < 0.7 else parent1
            parent2 = child2 if child2.children and random.random() < 0.7 else parent2
            iterations += 1
            if iterations > 10:
                print("Iterations exceeded")
                return self.crossover()

        parent1.replace_child(child1, child2)
        while not parent1.is_root:
            parent1 = parent1.parent

        return Program.from_root(parent1)

    def mutate(self) -> Program:
        p = self.select_tournament()
        parent1 = p.root.copy()
        parent2 = Program(
            self.parameters.max_depth,
            self.parameters.max_width,
            self.method
            if self.method == GenerationMethod.FULL
            else GenerationMethod.GROW,
            self.max_iterations,
        ).root
        return self._crossover(parent1, parent2)

    def run(self, serialize=False):
        found = False
        for gen in range(self.parameters.generations):
            i = self.select_best()
            print(
                f"Generation {gen + 1}, best fitness: {self.best_fitness}, avg fitness: {self.compute_avg_fitness()}\n"
            )
            if self.best_fitness == 0.0:
                self.save_result_to_file(i, True, self.best_fitness)
                print("Problem solved!\n")
                found = True
                break
            else:
                self.save_result_to_file(i, False, self.best_fitness)
            worst_index, worst_fitness = self.select_worst()
            new_fitness = worst_fitness
            while new_fitness <= worst_fitness:
                rand_prob = random.random()
                if rand_prob < self.parameters.crossover_prob:
                    new_individual = self.crossover()
                else:
                    new_individual = self.mutate()
                new_fitness = self.compute_fitness(new_individual)

            self.fitnesses[worst_index] = new_fitness
            self.population[worst_index] = new_individual
            self.generation += 1

        if not found:
            print(f"Problem not solved")
            print(f"Best fitness: {self.best_fitness}\n")
        
        if serialize:
            self.serialize_population()

    def print_individual(self, index: int):
        individual_program = self.population[index]
        ind_str = str(individual_program)
        print("---------------------")
        print("Program: ")
        print(individual_program)
        print("---------------------\n")
        return ind_str

    def save_result_to_file(self, best_index, found, best_fitness):
        path = "results.txt"
        with open(path, "w") as f:
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
        os.makedirs(self.example, exist_ok=True)
        for i, individual in enumerate(self.population):
            individual.save(os.path.join(self.example, f"individual{i}.pkl"))


def serialize_deserialize():
    genetic = MGlib(inputs=[], outputs=[], parameters=params)
    individual = genetic.create_individual()
    print("before saving:\n", individual)
    individual.save("individual1.pkl")
    individual2 = Program.load("individual1.pkl")
    print("after reading:\n", individual2)


if __name__ == "__main__":
    params = Params(
        max_depth=2,
        max_width=2,
        population_size=2,
        generations=5,
        tournament_size=3,
        crossover_prob=0.7,
        mutation_prob=0.1,
    )
    serialize_deserialize()
