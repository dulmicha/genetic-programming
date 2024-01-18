from generate import Program, GenerationMethod
from interpreter import Interpreter
from parameters import Params
from antlr4 import *
import random


def calculate_fitness_difference(
    program_output, expected_output
):  # fitness for number at random position in output
    fit = 0
    if len(program_output) == 0:
        return -100000.0
    elif 1 in program_output:
        return 0.0
    for i in range(len(expected_output)):
        fit += -abs(program_output[i] - expected_output[i])
    return fit


class MGlib:
    inputs: list
    outputs: list
    parameters: Params

    def __init__(self, inputs=None, outputs=None, parameters=None):
        self.inputs = inputs
        self.outputs = outputs
        self.parameters = parameters
        self.population_size = parameters.population_size
        self.method = GenerationMethod.FULL
        self.max_iterations = 10
        self.population = [
            self.create_individual() for _ in range(self.parameters.population_size)
        ]
        self.fitnesses = [
            self.compute_fitness(individual) for individual in self.population
        ]
        self.best_idx = 0
        self.best_fitness = -1000000.0
        self.best_generation = 0
        self.best = None
        self.generation = 0
        self.avg_fitness = -1.0

    def create_individual(self):
        if self.method == GenerationMethod.HALF_HALF:
            return Program(
                self.parameters.max_depth,
                self.parameters.max_width,
                random.choice([GenerationMethod.FULL, GenerationMethod.GROW]),
                self.max_iterations,
            )
        return Program(
            self.parameters.max_depth,
            self.parameters.max_width,
            self.method,
            self.max_iterations,
        )

    def compute_fitness(self, individual):
        fitness = 0
        for idx in range(len(self.inputs)):
            ind = str(individual)
            program_output, program_input, program_variables = Interpreter.run(
                ind, self.inputs[idx], False
            )
            fitness += calculate_fitness_difference(program_output, self.outputs[idx])
        return fitness

    def display_population_fitness(self):
        for idx, individual in enumerate(self.population):
            print(f"Program {idx + 1}:\n{individual}\n{self.fitnesses[idx]}\n")

    def display_population(self):
        for idx, individual in enumerate(self.population):
            print(f"Program {idx + 1}:\n{individual}\n")

    def select_tournament(self):
        tournament_size = self.parameters.tournament_size

    def select_neg_tournament(self):
        pass

    def select_best(self):
        best_fitness = max(self.fitnesses)
        best_idx = self.fitnesses.index(best_fitness)
        val = self.fitnesses[best_idx]
        if val > self.best_fitness:
            self.best_fitness = val
            self.best_idx = best_idx
            self.best = self.population[best_idx]
        print(f"Best fitness: {self.best_fitness}")
        return best_idx

    def select_worst(self):
        worst_fitness = min(self.fitnesses)
        worst_idx = self.fitnesses.index(worst_fitness)
        return worst_idx, worst_fitness

    def crossover(self):
        pass

    def mutate(self):
        pass

    def run(self):
        found = False
        for gen in range(self.parameters.generations):
            for idx, individual in enumerate(self.population):
                self.fitnesses[idx] = self.compute_fitness(individual)
            i = self.select_best()
            print(f"Generacja {gen + 1}, najlepszy fitness: {self.best_fitness}")
            if self.best_fitness == 0.0:
                self.save_result_to_file(i, True, self.best_fitness)
                print("Problem solved!\n")
                found = True
                break
            else:
                self.save_result_to_file(i, False, self.best_fitness)
            rand_prob = random.random()
            if rand_prob < self.parameters.crossover_prob:
                self.crossover()
            else:
                self.mutate()
            # worst_index, worst_fitness = self.select_worst()
            # worst = self.population[worst_index]
            # p = self.create_individual()
            # self.population[worst_index] = p
            self.generation += 1

        if not found:
            print(f"Problem not solved")
            print(f"Best fitness: {self.best_fitness}\n")

    def print_individual(self, index: int):
        individual_program = self.population[index]
        ind_str = str(individual_program)
        program_output, program_input, program_variables = Interpreter.run(
            ind_str, self.inputs[index], False
        )
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
