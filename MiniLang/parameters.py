class Params:
    population_size: int
    max_depth: int
    max_width: int
    max_expression_depth: int
    generations: int
    tournament_size: int
    mutation_prob: float
    crossover_prob: float
    min_int: int
    max_int: int

    def __init__(self, population_size: int = 5, max_depth: int = 2, max_width: int = 2, 
                 max_expression_depth: int = 2, generations: int = 10, tournament_size: int = 2,
                 crossover_prob: float = 0.8, min_int: int = -100, max_int: int = 100, instruction_limit: int = 50):
        self.population_size = population_size
        self.max_depth = max_depth
        self.max_width = max_width
        self.max_expression_depth = max_expression_depth
        self.generations = generations
        self.tournament_size = tournament_size
        self.crossover_prob = crossover_prob
        self.min_int = min_int
        self.max_int = max_int
        self.instruction_limit = instruction_limit

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
                + "\nGENERATIONS="
                + str(self.generations)
                + "\nTOURNAMENT_SIZE="
                + str(self.tournament_size)
                + "\nMIN_INT="
                + str(self.min_int)
                + "\nMAX_INT="
                + str(self.max_int)
                + "\n----------------------------------\n"
        )
