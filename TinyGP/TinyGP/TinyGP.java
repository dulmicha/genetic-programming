/*
 * Program:   tiny_gp.java
 *
 * Author:    Riccardo Poli (email: rpoli@essex.ac.uk)
 *
 */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Random;
import java.util.StringTokenizer;
import java.lang.Math;

public class TinyGP {
    double[] fitness;
    char[][] pop;
    static Random rd = new Random();
    static double problemSolvedThreshold;
    static final int
            ADD = 110,
            SUB = 111,
            MUL = 112,
            DIV = 113,
            SIN = 114,
            COS = 115,
            FSET_START = ADD,
            FSET_END = COS;
    static double[] x = new double[FSET_START];
    static double minrandom, maxrandom;
    static char[] program;
    static int PC;
    static int varnumber, fitnesscases, randomnumber;
    static double fbestpop = 0.0, favgpop = 0.0;
    static long seed;
    static double avg_len;
    static final int
            MAX_LEN = 10000,
            POPSIZE = 50000,
            DEPTH = 5,
            GENERATIONS = 40,
            TSIZE = 2;
    public static final double
            PMUT_PER_NODE = 0.05,
            CROSSOVER_PROB = 0.9;
    static double[][] targets;

    double run() { /* Interpreter */
        char primitive = program[PC++];
        if (primitive < FSET_START)
            return x[primitive];
        switch (primitive) {
            case SIN:
                return Math.round(Math.sin(run()) * 100) / 100.0;
            case COS:
                return Math.round(Math.cos(run()) * 100) / 100.0;
            case ADD:
                return run() + run();
            case SUB:
                return run() - run();
            case MUL:
                return run() * run();
            case DIV: {
                double num = run(), den = run();
                if (Math.abs(den) <= 0.001)
                    den = 0.00001;
                return num / den;
            }
        }
        return 0.0; // should never get here
    }

    int traverse(char[] buffer, int buffercount) {
        if (buffer[buffercount] < FSET_START)
            return ++buffercount;

        switch (buffer[buffercount]) {
            case ADD:
            case SUB:
            case MUL:
            case DIV:
                return traverse(buffer, traverse(buffer, ++buffercount));
            case SIN:
            case COS:
                return traverse(buffer, ++buffercount);
        }
        return 0; // should never get here
    }

    void setupFitness(String fname) {
        try {
            int i, j;
            String line;

            BufferedReader in =
                    new BufferedReader(
                            new
                                    FileReader(fname));
            line = in.readLine();
            StringTokenizer tokens = new StringTokenizer(line);
            varnumber = Integer.parseInt(tokens.nextToken().trim());
            randomnumber = Integer.parseInt(tokens.nextToken().trim());
            minrandom = Double.parseDouble(tokens.nextToken().trim());
            maxrandom = Double.parseDouble(tokens.nextToken().trim());
            fitnesscases = Integer.parseInt(tokens.nextToken().trim());
            targets = new double[fitnesscases][varnumber + 1];
            if (varnumber + randomnumber >= FSET_START)
                System.out.println("too many variables and constants");

            for (i = 0; i < fitnesscases; i++) {
                line = in.readLine();
                tokens = new StringTokenizer(line);
                for (j = 0; j <= varnumber; j++) {
                    targets[i][j] = Double.parseDouble(tokens.nextToken().trim());
                }
            }
            in.close();
        } catch (FileNotFoundException e) {
            System.out.println("ERROR: Please provide a data file");
            System.exit(0);
        } catch (Exception e) {
            System.out.println("ERROR: Incorrect data format");
            System.exit(0);
        }
    }

    double fitnessFunction(char[] Prog) {
        int i = 0, len;
        double result, fit = 0.0;

        len = traverse(Prog, 0);
        for (i = 0; i < fitnesscases; i++) {
            for (int j = 0; j < varnumber; j++)
                x[j] = targets[i][j];
            program = Prog;
            PC = 0;
            result = run();
            fit += Math.abs(result - targets[i][varnumber]);
        }
        return -fit;
    }

    int grow(char[] buffer, int pos, int max, int depth) {
        char prim = (char) rd.nextInt(2);
        int one_child;

        if (pos >= max)
            return -1;

        if (pos == 0)
            prim = 1;

        if (prim == 0 || depth == 0) {
            prim = (char) rd.nextInt(varnumber + randomnumber);
            buffer[pos] = prim;
            return pos + 1;
        } else {
            prim = (char) (rd.nextInt(FSET_END - FSET_START + 1) + FSET_START);
            switch (prim) {
                case ADD:
                case SUB:
                case MUL:
                case DIV:
                    buffer[pos] = prim;
                    one_child = grow(buffer, pos + 1, max, depth - 1);
                    if (one_child < 0)
                        return -1;
                    return grow(buffer, one_child, max, depth - 1);
                case SIN:
                case COS:
                    buffer[pos] = prim;
                    return grow(buffer, pos+1, max, depth - 1);
            }
        }
        return 0; // should never get here
    }

    int printIndiv(char[] buffer, int buffercounter) {
        int a1 = 0, a2 = 0;
        if (buffer[buffercounter] < FSET_START) {
            if (buffer[buffercounter] < varnumber)
                System.out.print("X" + (buffer[buffercounter] + 1) + " ");
            else
                System.out.print(x[buffer[buffercounter]]);
            return ++buffercounter;
        }
        switch (buffer[buffercounter]) {
            case SIN:
                System.out.print("SIN(");
                a2 = printIndiv(buffer, ++buffercounter);
                break;
            case COS:
                System.out.print("COS(");
                a2 = printIndiv(buffer, ++buffercounter);
                break;
            case ADD:
                System.out.print("(");
                a1 = printIndiv(buffer, ++buffercounter);
                System.out.print(" + ");
                a2 = printIndiv(buffer, a1);
                break;
            case SUB:
                System.out.print("(");
                a1 = printIndiv(buffer, ++buffercounter);
                System.out.print(" - ");
                a2 = printIndiv(buffer, a1);
                break;
            case MUL:
                System.out.print("(");
                a1 = printIndiv(buffer, ++buffercounter);
                System.out.print(" * ");
                a2 = printIndiv(buffer, a1);
                break;
            case DIV:
                System.out.print("(");
                a1 = printIndiv(buffer, ++buffercounter);
                System.out.print(" / ");
                a2 = printIndiv(buffer, a1);
                break;
        }
        System.out.print(")");
        return a2;
    }


    static char[] buffer = new char[MAX_LEN];

    char[] createRandomIndiv(int depth) {
        char[] ind;
        int len;

        len = grow(buffer, 0, MAX_LEN, depth);

        while (len < 0)
            len = grow(buffer, 0, MAX_LEN, depth);

        ind = new char[len];

        System.arraycopy(buffer, 0, ind, 0, len);
        return ind;
    }

    char[][] createRandomPop(int n, int depth, double[] fitness) {
        char[][] pop = new char[n][];
        int i;

        for (i = 0; i < n; i++) {
            pop[i] = createRandomIndiv(depth);
            fitness[i] = fitnessFunction(pop[i]);
        }
        return pop;
    }


    void stats(double[] fitness, char[][] pop, int gen) {
        int i, best = rd.nextInt(POPSIZE);
        int node_count = 0;
        fbestpop = fitness[best];
        favgpop = 0.0;

        for (i = 0; i < POPSIZE; i++) {
            node_count += traverse(pop[i], 0);
            favgpop += fitness[i];
            if (fitness[i] > fbestpop) {
                best = i;
                fbestpop = fitness[i];
            }
        }
        avg_len = (double) node_count / POPSIZE;
        favgpop /= POPSIZE;
        System.out.print("Generation=" + gen + " Avg Fitness=" + (-favgpop) +
                " Best Fitness=" + (-fbestpop) + " Avg Size=" + avg_len +
                "\nBest Individual: ");
        printIndiv(pop[best], 0);
        System.out.print("\n");
        System.out.flush();
    }

    int tournament(double[] fitness, int tsize) {
        int best = rd.nextInt(POPSIZE), i, competitor;
        double fbest = -1.0e34;

        for (i = 0; i < tsize; i++) {
            competitor = rd.nextInt(POPSIZE);
            if (fitness[competitor] > fbest) {
                fbest = fitness[competitor];
                best = competitor;
            }
        }
        return best;
    }

    int negativeTournament(double[] fitness, int tsize) {
        int worst = rd.nextInt(POPSIZE), i, competitor;
        double fworst = 1e34;

        for (i = 0; i < tsize; i++) {
            competitor = rd.nextInt(POPSIZE);
            if (fitness[competitor] < fworst) {
                fworst = fitness[competitor];
                worst = competitor;
            }
        }
        return worst;
    }

    char[] crossover(char[] parent1, char[] parent2) {
        int xo1start, xo1end, xo2start, xo2end;
        char[] offspring;
        int len1 = traverse(parent1, 0);
        int len2 = traverse(parent2, 0);
        int lenoff;

        xo1start = rd.nextInt(len1);
        xo1end = traverse(parent1, xo1start);

        xo2start = rd.nextInt(len2);
        xo2end = traverse(parent2, xo2start);

        lenoff = xo1start + (xo2end - xo2start) + (len1 - xo1end);

        offspring = new char[lenoff];

        System.arraycopy(parent1, 0, offspring, 0, xo1start);
        System.arraycopy(parent2, xo2start, offspring, xo1start,
                (xo2end - xo2start));
        System.arraycopy(parent1, xo1end, offspring,
                xo1start + (xo2end - xo2start),
                (len1 - xo1end));

        return offspring;
    }

    char[] mutation(char[] parent, double pmut) {
        int len = traverse(parent, 0), i;
        int mutsite;
        char[] parentcopy = new char[len];

        System.arraycopy(parent, 0, parentcopy, 0, len);
        for (i = 0; i < len; i++) {
            if (rd.nextDouble() < pmut) {
                mutsite = i;
                if (parentcopy[mutsite] < FSET_START)
                    parentcopy[mutsite] = (char) rd.nextInt(varnumber + randomnumber);
                else
                    switch (parentcopy[mutsite]) {
                        case ADD:
                        case SUB:
                        case MUL:
                        case DIV:
                            parentcopy[mutsite] =
                                    (char) (rd.nextInt(DIV - FSET_START + 1)
                                            + FSET_START);
                        case SIN:
                        case COS:
                            parentcopy[mutsite] =
                                    (char) (rd.nextInt(FSET_END - DIV)
                                            + DIV + 1);
                    }
            }
        }
        return parentcopy;
    }

    void printParms() {
        System.out.print("-- TINY GP (Java version) --\n");
        System.out.print("SEED=" + seed + "\nMAX_LEN=" + MAX_LEN +
                "\nPOPSIZE=" + POPSIZE + "\nDEPTH=" + DEPTH +
                "\nCROSSOVER_PROB=" + CROSSOVER_PROB +
                "\nPMUT_PER_NODE=" + PMUT_PER_NODE +
                "\nMIN_RANDOM=" + minrandom +
                "\nMAX_RANDOM=" + maxrandom +
                "\nGENERATIONS=" + GENERATIONS +
                "\nTSIZE=" + TSIZE +
                "\nSOLVING_THRESHOLD=" + problemSolvedThreshold +
                "\n----------------------------------\n");
    }

    public TinyGP(String fname, long s, double t) {
        fitness = new double[POPSIZE];
        seed = s;
        problemSolvedThreshold = t;
        if (seed >= 0)
            rd.setSeed(seed);
        setupFitness(fname);
        for (int i = 0; i < FSET_START; i++)
            x[i] = (maxrandom - minrandom) * rd.nextDouble() + minrandom;
        pop = createRandomPop(POPSIZE, DEPTH, fitness);
    }

    void evolve() {
        int gen = 0, indivs, offspring, parent1, parent2, parent;
        double newfit;
        char[] newind;
        printParms();
        stats(fitness, pop, 0);
        for (gen = 1; gen < GENERATIONS; gen++) {
            if (fbestpop > -problemSolvedThreshold) {
                System.out.print("PROBLEM SOLVED\n");
                System.exit(0);
            }
            for (indivs = 0; indivs < POPSIZE; indivs++) {
                if (rd.nextDouble() < CROSSOVER_PROB) {
                    parent1 = tournament(fitness, TSIZE);
                    parent2 = tournament(fitness, TSIZE);
                    newind = crossover(pop[parent1], pop[parent2]);
                } else {
                    parent = tournament(fitness, TSIZE);
                    newind = mutation(pop[parent], PMUT_PER_NODE);
                }
                newfit = fitnessFunction(newind);
                offspring = negativeTournament(fitness, TSIZE);
                pop[offspring] = newind;
                fitness[offspring] = newfit;
            }
            stats(fitness, pop, gen);
        }
        System.out.print("PROBLEM *NOT* SOLVED\n");
        System.exit(1);
    }

    public static void main(String[] args) {
        String fname = args[0];
        long s = -1;
        double t = 1e-5;
        if (args.length == 2)
            t = Double.parseDouble(args[1]);

        System.out.println(fname);
        TinyGP gp = new TinyGP(fname, s, t);
        gp.evolve();
    }
};
