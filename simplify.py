import sympy as sp
import subprocess
import os
from func_timeout import func_timeout

TINYGP_DIR = "TinyGP"
SIMPLIFIER_FILENAME = "Simplifier.java"
INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "individual.txt"
INPUT_PATH = os.path.join(TINYGP_DIR, INPUT_FILENAME)
OUTPUT_PATH = os.path.join(TINYGP_DIR, OUTPUT_FILENAME)
SIMPLIFIER_PATH = os.path.join(TINYGP_DIR, SIMPLIFIER_FILENAME)

def simplify(individual):
    return str(sp.simplify(individual))


def simplify_java(individual):
    with open(INPUT_PATH, "w") as f:
        f.write(individual)
    with open(OUTPUT_PATH, "w") as f:
        command = f"java {SIMPLIFIER_PATH} {INPUT_PATH}"
        subprocess.run(
            command, shell=True, stdout=f, text=True, 
        )
    with open(OUTPUT_PATH) as f:
        individual = f.read().strip()
    return str(sp.parse_expr(individual))

def simplify_timeout(individual, timeout=600):
    try:
        return func_timeout(timeout, simplify, args=(individual,))
    except:
        return simplify_java(individual)

if __name__ == "__main__":
    individual = "((7.899137104221815 + COS(COS(((COS(-6.934971343785334) * (-4.312735372935304 / COS((((X1  * (COS((-7.621511195025152 + 9.572399722858165)) + -8.103538990896338)) - ((((7.17112770912507 * (1.0607783822213452 + (((7.6343000420386495 + (((COS((9.315459301070302 + (((-4.033260746067517 / -0.9823956554276148) + -8.033741773519276) * (((4.95755183239557 * -5.392202751865911) * -5.466848216455857) + (((-4.630711247555521 - -5.392202751865911) - -8.103538990896338) * (-4.033260746067517 * (7.592447037741678 * 7.17112770912507))))))) * 4.442468240084661) + ((4.596862882337415 + (COS(4.26295329973639) - ((-6.276376957616357 * -8.667222369315873) * -3.4856178996322518))) + (X1  + -2.702221860712717))) * ((-4.568932305156148 * ((5.2571269264762535 / -0.07915512265216584) + 3.5003541312483897)) * 7.529064899166222))) + (X1  / ((9.315459301070302 + ((-7.826890189069569 * (-4.312735372935304 / ((-8.985337700713751 * 7.529064899166222) * -4.568932305156148))) + 7.187782853272942)) / 6.049071625186933))) * (-4.312735372935304 / COS((((X1  * (COS(-6.276376957616357) + -8.103538990896338)) - ((((7.17112770912507 * (1.0607783822213452 + (((7.6343000420386495 + (X1  * (SIN(9.315459301070302) * 7.529064899166222))) + (X1  / ((9.315459301070302 + ((-7.826890189069569 * (-4.312735372935304 / ((-8.985337700713751 * 7.529064899166222) * -4.568932305156148))) + 7.187782853272942)) / 6.049071625186933))) * 1.178126174791526))) * 6.7154764020086155) - COS(((6.049071625186933 * 4.596862882337415) + 8.499784388445836))) * COS(4.26295329973639))) - ((8.453358706472685 + ((7.187782853272942 * (-9.569639007473945 - COS(-8.667222369315873))) / (0.3545159616031146 / -7.826890189069569))) + (COS((5.126798254770071 + (8.453358706472685 / (COS((-8.667222369315873 + ((-2.2363663894822716 - -4.568932305156148) + -6.001416736709116))) / (((-9.76161103251403 * 7.6343000420386495) * (((4.26295329973639 - ((-7.427116149213264 - 8.453358706472685) / -6.276376957616357)) - 4.26295329973639) * (9.572399722858165 + 0.6672148028317331))) - (((COS(SIN(1.5412020919410718)) + (7.6343000420386495 + ((((((-8.033741773519276 + 5.126798254770071) - (3.9264634449785625 * 4.676533553785038)) * 4.442468240084661) + ((COS(COS(8.499784388445836)) + 6.475429617952777) + (X1  + -2.702221860712717))) + (X1  + (SIN(COS(SIN(-5.392202751865911))) * (SIN((2.64221048010997 + 5.126798254770071)) / (((-9.76161103251403 * X1 ) - ((9.315459301070302 * 4.596862882337415) * 5.2571269264762535)) * 9.979106068803741))))) * (9.529377996052837 / 1.0607783822213452)))) - (-6.256290147143282 + COS(((-3.813383168168542 + COS(8.63462086574685)) - (COS(COS((((SIN(COS((9.315459301070302 + (((((SIN(4.95755183239557) * COS(-6.934971343785334)) - (7.6343000420386495 + (4.676533553785038 * ((9.315459301070302 + 7.529064899166222) * -6.276376957616357)))) / -0.9823956554276148) + -8.033741773519276) * (((4.95755183239557 * -5.392202751865911) * -5.466848216455857) + (((-4.630711247555521 - -5.392202751865911) - -8.103538990896338) * (-4.033260746067517 * (7.592447037741678 * 7.17112770912507)))))))) / (-5.466848216455857 * -1.2120775401922845)) * 9.529377996052837) + ((((SIN(1.5412020919410718) + ((2.132902781527722 + (X1  + (SIN(COS(SIN(-5.392202751865911))) * (SIN(((7.187782853272942 * 5.353564002528689) + (8.528411740243076 - (-8.985337700713751 * -6.5691660920075545)))) / (SIN((((SIN((7.899137104221815 - 0.3545159616031146)) + (3.9264634449785625 * 4.676533553785038)) + -1.5920644998853462) * -0.07915512265216584)) * (0.16860564629930685 - ((X1  + (COS(4.26295329973639) - ((-6.276376957616357 * -8.667222369315873) * -3.4856178996322518))) + 4.26295329973639))))))) - (8.528411740243076 - X1 ))) - (8.528411740243076 - X1 )) + COS(4.26295329973639)) / 4.676533553785038)))) * -0.07915512265216584))))) - -6.276376957616357)))))) - -2.736662902969429)))))))) * 6.7154764020086155) - COS(((6.049071625186933 * 4.596862882337415) + 8.499784388445836))) * COS(4.26295329973639))) - ((8.453358706472685 + ((7.187782853272942 * (-9.569639007473945 - COS(-8.667222369315873))) / (0.3545159616031146 / -7.826890189069569))) + (COS((5.126798254770071 + (8.453358706472685 / (COS((((-3.931076474776787 * -3.931076474776787) + (COS(4.26295329973639) - ((-6.276376957616357 * -8.667222369315873) * -3.4856178996322518))) + ((-2.2363663894822716 - -4.568932305156148) + -6.001416736709116))) / (((-9.76161103251403 * 7.6343000420386495) * (((4.26295329973639 - ((-7.427116149213264 - 8.453358706472685) / -6.276376957616357)) - 4.26295329973639) * (9.572399722858165 + 0.6672148028317331))) - (((COS(SIN(1.5412020919410718)) + (COS(((X1  + ((((-5.392202751865911 - -8.033741773519276) * ((((COS(COS(8.499784388445836)) + (0.5016682542607125 - (((7.17112770912507 - -5.081632679976109) - COS(((COS(X1 ) + SIN(-7.427116149213264)) * 9.572399722858165))) * -3.4856178996322518))) + (X1  + -2.702221860712717)) + (8.453358706472685 * 8.499784388445836)) + 5.126798254770071)) + 5.446076329706546) + (((X1  / 2.091226606820978) + (8.63462086574685 * ((8.528411740243076 + -8.985337700713751) + ((8.528411740243076 + COS(COS(7.899137104221815))) * 7.17112770912507)))) * (-8.985337700713751 * -6.5691660920075545)))) - -5.466848216455857)) + ((((2.64221048010997 * 4.442468240084661) + ((COS(COS(8.499784388445836)) + (-5.466848216455857 - ((-6.276376957616357 * -8.667222369315873) * -3.4856178996322518))) + (X1  + -2.702221860712717))) + (X1  + (SIN(COS(SIN(-5.392202751865911))) * (SIN((2.64221048010997 + 5.126798254770071)) / (((((X1  + (5.446076329706546 / -4.530024128105814)) / (3.5003541312483897 - SIN((-0.9823956554276148 / -2.765779824009571)))) * X1 ) - ((9.315459301070302 * 4.596862882337415) * 5.2571269264762535)) * 9.979106068803741))))) * (9.529377996052837 / 1.0607783822213452)))) - (-6.256290147143282 + COS(((-3.813383168168542 + COS(8.63462086574685)) - (COS(COS((((SIN(COS((9.315459301070302 + (((((SIN(4.95755183239557) * COS(-6.934971343785334)) - (7.6343000420386495 + (4.676533553785038 * ((9.315459301070302 + 7.529064899166222) * -6.276376957616357)))) / -0.9823956554276148) + -8.033741773519276) * (((4.95755183239557 * -5.392202751865911) * -5.466848216455857) + (X1  + ((((-5.392202751865911 - -8.033741773519276) * ((((COS(COS(8.499784388445836)) + (0.5016682542607125 - (((((9.315459301070302 + 7.529064899166222) * -6.276376957616357) - -5.081632679976109) - COS(((COS(X1 ) + SIN(-7.427116149213264)) * 9.572399722858165))) * -3.4856178996322518))) + (X1  + -2.702221860712717)) + (8.453358706472685 * 8.499784388445836)) + 5.126798254770071)) + 5.446076329706546) + (((X1  / 2.091226606820978) + (8.63462086574685 * ((8.528411740243076 + -8.985337700713751) + ((8.528411740243076 + COS(COS(7.899137104221815))) * 7.17112770912507)))) * (-8.985337700713751 * -6.5691660920075545))))))))) / (-5.466848216455857 * -1.2120775401922845)) * 9.529377996052837) + -1.9965267128109971))) * -0.07915512265216584))))) - -6.276376957616357)))))) - -2.736662902969429)))))) + -1.9965267128109971)))) + (1.0141956489712527 - ((((2.132902781527722 + SIN(((-4.568932305156148 * ((5.2571269264762535 / -0.07915512265216584) + 3.5003541312483897)) * 6.475429617952777))) - (8.528411740243076 - X1 )) - ((0.16860564629930685 - ((((SIN(((X1  + -2.702221860712717) * (2.132902781527722 + (4.442468240084661 + -6.529134838670458)))) * ((7.6343000420386495 + (4.676533553785038 * (SIN(9.315459301070302) * 7.529064899166222))) + (X1  / ((9.315459301070302 + ((SIN(2.209190203828957) * ((X1  * ((-6.988937114909435 - (-5.081632679976109 + 7.6343000420386495)) + (((-0.07915512265216584 - -8.103538990896338) / -4.108063299608766) + -6.529134838670458))) / ((-8.857317573688558 * 7.529064899166222) * -4.568932305156148))) + 7.187782853272942)) / 6.049071625186933)))) - (7.6343000420386495 + (4.676533553785038 * ((9.315459301070302 + 7.529064899166222) * -6.276376957616357)))) / -0.9823956554276148) + (COS(SIN(4.442468240084661)) - -4.312735372935304))) * -9.569639007473945)) * -6.001416736709116)))"
    print("Original:", individual)
    print("Simplified:", simplify_timeout(individual))