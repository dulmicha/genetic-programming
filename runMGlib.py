from MiniLang.MGlib import *
from MiniLang.read_data import read_data
from MiniLang.parameters import Parameters
import os


example = "1_1_A"
file_name = os.path.join("MiniLang", "examples", f"example_{example}.txt")
params = Parameters(
    max_depth=2,
    max_width=2,
    population_size=10,
    generations=5,
    tournament_size=3,
    crossover_prob=0.7,
    min_int=-100,
    max_int=1000,
)
inputs, outputs = read_data(file_name)
print("inputs: ", inputs)
print("outputs: ", outputs)
mglib = MGlib(inputs=inputs, outputs=outputs, parameters=params, example=example)
mglib.display_population_fitness()
mglib.run()
