from dataclasses import dataclass, field


@dataclass
class Parameters:
    population_size: int = field(default=1000)
    max_depth: int = field(default=2)
    max_width: int = field(default=4)
    max_expression_depth: int = field(default=3)
    generations: int = field(default=100)
    tournament_size: int = field(default=5)
    crossover_prob: float = field(default=0.7)
    min_int: int = field(default=-100)
    max_int: int = field(default=1000)
    instruction_limit: int = field(default=100)

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
