class Params:
    population_size: int
    max_depth: int
    max_width: int
    generations: int
    tournament_size: int
    mutation_prob: float
    crossover_prob: float
    # method: str

    def __init__(self, population_size: int = 5, max_depth: int = 2, max_width: int = 2,
                 generations: int = 10, tournament_size: int = 2, mutation_prob: float = 0.2,
                 crossover_prob: float = 0.8):
        self.population_size = population_size
        self.max_depth = max_depth
        self.max_width = max_width
        self.generations = generations
        self.tournament_size = tournament_size
        self.mutation_prob = mutation_prob
        self.crossover_prob = crossover_prob

    def __repr__(self) -> str:
        return (
                "POPULATION_SIZE="
                + str(self.population_size)
                + "\nMAX_DEPTH="
                + str(self.max_depth)
                + "\nMAX_WIDTH="
                + str(self.max_width)
                + "\nCROSSOVER_PROB="
                + str(self.crossover_prob)
                + "\nMUTATION_PROB="
                + str(self.mutation_prob)
                + "\nGENERATIONS="
                + str(self.generations)
                + "\nTOURNAMENT_SIZE="
                + str(self.tournament_size)
                + "\n----------------------------------\n"
        )
