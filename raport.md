# Programowanie Genetyczne - raport końcowy
---
Autorzy: Michał Dul, Weronika Hilaszek

- [Programowanie Genetyczne - raport końcowy](#programowanie-genetyczne---raport-końcowy)
  - [Przykładowe zadania testowe](#przykładowe-zadania-testowe)
  - [Finalne testy systemu](#finalne-testy-systemu)
    - [Benchmarki](#benchmarki)
    - [Regresja boolowska](#regresja-boolowska)


## Przykładowe zadania testowe
- 1.1.A Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.
  - funkcja dopasowania:
  ```python
  def fitness_1_1_A(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 1 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit
  ```
  - parametry wejściowe i rezultat uczenia:
  ```
    Parameters:
    POPULATION_SIZE=100
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=5
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem solved
    print(1);

    Fitness values: 0.0, Generation: 42
  ```
- 1.1.B Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.
  - funkcja dopasowania:
  ```python
  def fitness_1_1_B(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    elif 789 in out:
        return 0.0
    return -min([abs(x - 789) for x in out])
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=200
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=20
    MIN_INT=-100
    MAX_INT=1000
    ----------------------------------

    Problem solved
    print(975);
    print(786);
    print(789);
    print(799);

    Fitness values: 0.0, Generation: 909
  ``` 

- 1.1.C Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415. Poza liczbą 31415 może też zwrócić inne liczby.
  - funkcja dopasowania:
  ```python
  def fitness_1_1_C(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 31415 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=150
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.3
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=2
    MIN_INT=-100
    MAX_INT=50000
    ----------------------------------

    Problem solved
    print(31396);
    X_0 = input();
    print(31436);
    print(31415);

    Fitness values: 0.0, Generation: 43
  
  ``` 

- 1.1.D Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.
  - funkcja dopasowania:
  ```python
  def fitness_1_1_D(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif out[0] == 1:
        return 0.0
    else:
        fit += -abs(out[0] - 1)
    return fit
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=30
    MIN_INT=-10
    MAX_INT=50000
    ----------------------------------

    Problem solved
    print((47611 / 35208));
    print(49477);
    X_0 = input();
    print((11218 / X_1));
    X_1 = (32995 + 43747);

    Fitness values: 0.0, Generation: 1

  ``` 

- 1.1.E Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.
  - funkcja dopasowania:
  ```python
  def fitness_1_1_E(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif out[0] == 789:
        return 0.0
    else:
        fit += -abs(out[0] - 789)
    return fit
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=200
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.5
    MUTATION_PROB=0.2
    GENERATIONS=1000
    TOURNAMENT_SIZE=10
    MIN_INT=-100
    MAX_INT=50000
    ----------------------------------

    Problem solved
    print((36580 - 35791));
    X_0 = input();
    print(818);
    print((43373 - 39694));
    print((43373 - 39694));

    Fitness values: 0.0, Generation: 72
  ``` 

- 1.1.F Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. Poza liczbą 1 NIE powinien nic więcej wygenerować.
  - funkcja dopasowania:
  ```python
  def fitness_1_1_F(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif len(out) == 1 and out[0] == 1:
        return 0.0
    else:
        fit = -len(out) * 10
    return fit
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=30
    MIN_INT=-10
    MAX_INT=10000
    ----------------------------------

    Problem solved
    X_0 = input();
    print(1);

    Fitness values: 0.0, Generation: 517
  ``` 

- 1.2.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]
  - funkcja dopasowania:
  ```python
  def fitness_1_2_A(out, expected, inputs):
    if len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1:
        if out[0] in inputs:
            return -10.0
        else:
            return -1000.0
    elif len(out) > 1 and expected[0] in out:
        return len(out) * -20
    else:
        return len(out) * -100 if len(out) > 1 else -100000
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=30
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem solved
    X_1 = input();
    X_0 = input();
    print((X_0 + X_1));
    X_0 = input();

    Fitness values: 0.0, Generation: 193
  ``` 

- 1.2.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]
  - funkcja dopasowania:
  ```python
  # taka sama jak 1.2.A
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=700
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=40
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem solved
    X_2 = input();
    X_1 = input();
    print((X_1 + X_2));

    Fitness values: 0.0, Generation: 531

  ``` 

- 1.2.C Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
  - funkcja dopasowania:
  ```python
    # taka sama jak 1.2.A
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=150
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.3
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=2
    MIN_INT=-100
    MAX_INT=50000
    ----------------------------------

    Problem solved
    X_2 = input();
    X_0 = (44068 * 20683);
    X_1 = input();
    print((X_1 + X_2));
    X_0 = 25939;

    Fitness values: 0.0, Generation: 25
  ``` 

- 1.2.D Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
  - funkcja dopasowania:
  ```python
    # taka sama jak 1.2.A
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=750
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=40
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem not solved
    X_0 = input();
    print((X_0 - X_1));
    X_0 = input();

    Fitness values: -1.0, Generation: 1000

  ``` 

- 1.2.E Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
  - funkcja dopasowania:
  ```python
    # taka sama jak 1.2.A
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=750
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.7
    MUTATION_PROB=0.1
    GENERATIONS=1000
    TOURNAMENT_SIZE=40
    MIN_INT=-1000
    MAX_INT=1000
    ----------------------------------

    Problem solved
    X_1 = input();
    X_2 = input();
    print((X_1 * X_2));

    Fitness values: 0.0, Generation: 611
  ``` 

- 1.3.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]
  - funkcja dopasowania:
  ```python
  def fitness_1_3_A(out, expected, inputs):
    if len(out) == 0:
        return -50.0
    elif len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1 and out[0] != expected[0]:
        if out[0] in inputs:
            return -20.0
        else:
            return -1000.0
    elif len(out) == 2 and out[0] in inputs and out[1] in inputs:
        if out[0] != out[1]:
            return -10.0
        return -15.0
    elif len(out) >=0 and any([x in inputs for x in out]):
        return len(out) * -100
    else:
        return len(out) * -1000 if len(out) > 1 else -100000
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=1000
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.5
    MUTATION_PROB=0.2
    GENERATIONS=1000
    TOURNAMENT_SIZE=20
    MIN_INT=-1000
    MAX_INT=1000
    ----------------------------------

    Problem not solved
    if (X_1 == X_0 or X_1 <= X_0) {
        X_2 = input();
        X_1 = -174;
        print(X_0);
        X_3 = input();
    }
    if (8 != 283) {
        X_0 = input();
        X_1 = input();
    }
    if (X_0 > X_1 and -345 <= 249 and 191 >= 153) {
        print(X_0);
    }

    Fitness values: -2.0, Generation: 1000

  ``` 

- 1.3.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]
  - funkcja dopasowania:
  ```python
    # taka sama jak 1.3.A
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=150
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.5
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem not solved
    if (X_0 <= X_1) {
        X_2 = input();
    }
    if (-21 != X_0) {
        X_1 = input();
        print(X_1);
        X_2 = 96;
    }
    while (52 == -84 or X_0 > X_1 or 5 == X_2) {
        X_3 = (X_4 * X_3);
        X_3 = X_1;
        X_4 = input();
    }
    if (79 == X_0) {
        print(X_0);
        X_1 = input();
        print((X_0 - X_1));
        print((X_0 / X_2));
    }

    Fitness values: -2.0, Generation: 25

  ``` 

- 1.4.A Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99]
  - funkcja dopasowania:
  ```python
  def fitness_1_4_A(out, expected, inputs):
    if len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1:
        if out[0] in inputs:
            return -100.0
        else:
            return -1000.0
    elif len(out) > 1 and expected[0] in out:
        return len(out) * -20 + -1000
    else:
        return len(out) * -100 + -1000 if len(out) > 1 else -100000
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=100
    MAX_DEPTH=2
    MAX_WIDTH=6
    CROSSOVER_PROB=0.5
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem not solved
    X_0 = input();
    if (42 != X_0 or X_0 >= -71) {
        print(X_0);
        print(X_0);
        X_0 = input();
        X_1 = input();
        print(X_1);
    }

    Fitness values: -1500.0, Generation: 101

  ``` 

- 1.4.B Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].
  - podejście:
    1. Wytrenować populację do wykonania pętli n razy, wczytywania liczby z wejścia w każdym przebiegu. Parametry wejściowe i znaleziony przez system rezultat dla pierwszego etapu:
    ``` 
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=5
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem not solved
    if (X_0 <= X_0 or X_0 >= X_1) {
      if (X_0 <= X_0 or X_0 >= X_1) {
        if (X_0 <= X_0 or X_0 >= X_1) {
          if (X_0 <= X_0 or X_0 >= X_1) {
            if (X_0 != X_0 or 0 <= 0 or X_0 < 1) {
              print((X_1 + 0));
            }
          }
        }
      }
    }
    if (0 > X_0 or X_0 != 1) {
      X_0 = input();
      X_1 = input();
      print(X_0);
      }
    if (X_0 <= X_0 or X_0 >= X_1) {
      print(X_1);
      }
    if (X_0 != 0 or X_1 >= X_1 or X_1 == 0) {
      X_1 = input();
      print(X_1);
      X_1 = input();
      print(X_1);
      X_0 = X_1;
      }

    Fitness values: -42000.0, Generation: 101
    ```
    2. Faktyczne trenowanie zrealizować korzystając z zserializowanej populacji z pkt. 1.
  - funkcja dopasowania:
  ```python
  def fitness_1_4_B(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    avg = sum(inputs[1:]) // inputs[0]
    if len(out) == 1 and out[0] == avg:
        return 0.0
    elif len(out) == 1 and out[0] != avg:
        return abs(out[0] - avg) * -100
    else:
        return len(out) * -1000
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
  ?
  ``` 


## Finalne testy systemu
### Benchmarki
- Number IO (1 / Q 3.5.1) Given an integer and a float, print their sum.
  Reprezentacja floata: stałoprzecinkowa, np. 3.14 to dwa integery 3 i 14
  - funkcja dopasowania:
  ```python
  def fitness_int_float_sum(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    elif len(out) == 2 and out[0] == expected[0] and out[1] == expected[1]:
        return 0.0
    elif len(out) == 2 and out[0] == expected[0] and out[1] != expected[1]:
        return -10.0
    elif len(out) == 2 and out[0] != expected[0] and out[1] == expected[1]:
        return -15.0
    elif len(out) == 2 and out[0] in expected and out[1] in expected and out[0] != out[1]:
        return -5.0
    elif len(out) == 2 and out[0] != expected[0] and out[1] != expected[1] and any([o in inputs for o in out]):
        return (out[0] in inputs) * -10 + (out[1] in inputs) * -10
    elif len(out) == 2:
        return -100.0
    elif len(out) == 1 and (out[0] == expected[0] or out[0] == expected[1]):
        return -100.0
    elif len(out) == 1 and out[0] not in expected and out[0] in inputs:
        return -1000.0
    elif len(out) == 1 and out[0] not in expected and out[0] not in inputs:
        return -10000.0
    else:
        return -100000.0
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=2000
    MAX_DEPTH=1
    MAX_WIDTH=10
    CROSSOVER_PROB=0.6
    MUTATION_PROB=0.2
    GENERATIONS=1000
    TOURNAMENT_SIZE=10
    MIN_INT=-1000
    MAX_INT=1000
    ----------------------------------

    Problem solved
    X_1 = input();
    X_2 = input();
    X_0 = input();
    print((X_1 + X_2));
    X_2 = X_0;
    print(X_0);

    Fitness values: 0.0, Generation: 15

  ``` 
- Negative To Zero (21 / Q 9.6.8) Given a vector of integers, return the vector where all negative integers have been replaced by 0.
  - podejście: 
    1. Wytrenować populację dla pojedynczej liczby na zasadzie jak w opisie zadania. Parametry wejściowe i znaleziony przez system rezultat dla pierwszego etapu:
    ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=3
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=-5
    MAX_INT=5
    ----------------------------------

    Problem solved
    X_0 = input();
    if (-2 < -1 and X_0 < 1) {
        X_1 = input();
        X_1 = -4;
        X_0 = 0;
    }
    if (-1 <= 5) {
        print(X_0);
    }

    Fitness values: 0.0, Generation: 19
    ``` 
    2. Faktyczne trenowanie zrealizować korzystając z zserializowanej populacji z pkt. 1.
  - funkcja dopasowania:
  ```python
  def fitness_9_6_8(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    expexted_out_len = len(expected)
    fit = abs(len(out) - expexted_out_len) * -200.0
    for o_idx, o in enumerate(out):
        if o_idx >= expexted_out_len:
            o_idx = o_idx % expexted_out_len
        fit += min(abs(o - expected[o_idx]), 100) * -100.0
    return fit
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=3
    MAX_WIDTH=4
    CROSSOVER_PROB=0.6
    MUTATION_PROB=0.2
    GENERATIONS=1000
    TOURNAMENT_SIZE=2
    MIN_INT=-1000
    MAX_INT=1000
    ----------------------------------

    Problem not solved
    if (617 != -301 or 212 <= 460 or -746 <= -672) {
        X_0 = input();
        X_1 = X_0;
        X_0 = X_1;
        print(X_0);
    }
    if (-23 <= -488) {
        X_0 = 228;
    }

    Fitness values: -4100.0, Generation: 8
  ``` 
- Smallest (28) Given 4 integers, print the smallest of them
  - funkcja dopasowania:
  ```python
  def fitness_28(out, expected, inputs):
    if len(out) == 0:
        return -50.0
    elif len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1 and out[0] != expected[0]:
        if out[0] in inputs:
            return -20.0
        else:
            return -1000.0
    elif len(out) > 0 and any([x in inputs for x in out]):
        return len(out) * -1000
    else:
        return len(out) * -10000 if len(out) > 1 else -100000 
  ```
  - parametry wejściowe i znaleziony przez system rezultat:
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=5
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=-5
    MAX_INT=5
    ----------------------------------

    Problem not solved
    if (X_0 >= 5) {
        if (X_0 >= 5) {
            while (4 != X_0 or 1 <= 1 and X_1 > X_2) {
                while (2 <= -2) {
                    X_0 = -2;
                    X_1 = 1;
                    print(X_1);
                    print((X_2 + 1));
                }
                X_1 = input();
            }
        }
    }
    if (X_0 >= 5) {
        if (X_0 > X_0 or X_1 < 5 or X_0 >= X_1) {
             X_0 = X_1;
        }
    }
    print(X_0);
    if (X_0 >= 5) {
        if (X_0 > X_0 or X_1 < 5 or X_0 >= X_1) {
            X_0 = X_1;
        }
    }
    if (X_0 >= 5) {
        if (X_0 >= 5) {
            while (4 != X_0 or 1 <= 1 and X_1 > X_2) {
                while (X_0 > X_0) {
                    print((X_1 / X_2));
                }
                X_1 = input();
            }
        }
    }

    Fitness values: -122.96, Generation: 66

  ``` 

### Regresja boolowska
Funkcja przystosowania (jednakowa dla każdego przypadku):
```python
def fitness_boolean(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    if len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1 and out[0] != expected[0]:
        return abs(out[0] - expected[0]) * -100
    else:
        return len(out) * -1000
```
- `k = 1`
  - `D0`
  ```
    Parameters:
    POPULATION_SIZE=50
    MAX_DEPTH=1
    MAX_WIDTH=5
    CROSSOVER_PROB=0.45
    GENERATIONS=101
    TOURNAMENT_SIZE=3
    MIN_INT=-100
    MAX_INT=100
    ----------------------------------

    Problem solved
    X_0 = input();
    print(X_0);
    X_0 = -77;
    X_0 = -94;

    Fitness values: 0.0, Generation: 1
  ```
  - `NOT(D0)`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem solved
    X_0 = input();
    if (X_0 < 1) {
        X_1 = input();
        print((1 - 0));
        X_2 = 1;
    }
    X_1 = input();
    if (1 <= X_0 or X_0 != 0) {
        print(0);
        X_1 = input();
    }

    Fitness values: 0.0, Generation: 5

  ```
- `k = 2`
  - `D0 AND D1`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem solved
    if (0 != 1) {
        X_0 = input();
        X_0 = input();
        X_1 = input();
        X_2 = input();
    }
    print((X_0 * X_1));
    X_1 = input();

    Fitness values: 0.0, Generation: 14

  ```
  - `D0 OR D1`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem solved
    X_0 = input();
    if (0 <= 1 and 1 > X_0) {
        X_0 = input();
        X_1 = (1 - 0);
    }
    print(X_0);

    Fitness values: 0.0, Generation: 10

  ```
  - `D0 XOR D1`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem solved
    X_0 = 0;
    if (0 >= X_0) {
        X_0 = input();
        X_1 = input();
        X_2 = input();
        X_2 = (0 * 1);
    }
    if (0 >= X_0) {
        X_0 = input();
        X_1 = input();
        X_2 = input();
        X_2 = (0 * 1);
    }
    print((X_0 * (1 - X_1)));

    Fitness values: 0.0, Generation: 6

  ```
- `k = 3`
  - `D0 AND D1 AND D2`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem solved
    X_0 = input();
    if (1 >= X_0 or 1 < 0) {
        X_1 = input();
        X_2 = input();
    }
    print(((X_0 * X_1) * X_2));
    X_0 = input();

    Fitness values: 0.0, Generation: 31

  ```
  - `D0 OR D1 OR D2`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    From bool 2_2
    ----------------------------------

    Problem solved
    if (0 <= 1 and 1 > X_0) {
        X_0 = input();
        X_1 = (1 - 0);
    }
    if (0 <= 1 and 1 > X_0) {
        X_0 = input();
        X_1 = (1 - 0);
    }
    print(X_0);

    Fitness values: 0.0, Generation: 1
  ```
  - `D0 XOR D1 XOR D2`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    From bool 2 3
    ----------------------------------

    Problem solved
    if (X_1 < X_2) {
        X_1 = input();
    }
    if (1 <= X_2) {
        X_1 = 0;
    }
    if (0 >= X_0) {
        X_0 = input();
        X_1 = input();
        X_2 = input();
        X_2 = (0 * 1);
    }
    print((X_0 * (1 - X_1)));

    Fitness values: 0.0, Generation: 10
  ```
- `k = 4`
  - `D0 AND D1 AND D2 AND D3`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=4
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    From bool 3_1
    ----------------------------------

    Problem solved
    X_2 = input();
    if (0 != X_0) {
        X_0 = 0;
        X_0 = input();
    }
    print(((X_0 * X_1) * X_2));
    X_1 = input();

    Fitness values: 0.0, Generation: 2

  ```
  - `D0 OR D1 OR D2 OR D3`
  ```
  Parameters:
  POPULATION_SIZE=250
  MAX_DEPTH=2
  MAX_WIDTH=5
  CROSSOVER_PROB=0.55
  GENERATIONS=101
  TOURNAMENT_SIZE=10
  MIN_INT=0
  MAX_INT=1
  ----------------------------------

  Problem not solved
  if (1 == X_0 and 1 < X_1 or 0 < 1) {
    X_2 = input();
    print(1);
    print((0 * (X_3 / 0)));
    }
  while (X_0 <= 0 or 0 <= 0 or 0 != X_0) {
    X_0 = (1 * (1 / X_0));
    print((X_1 * X_2));
    X_3 = 0;
    X_4 = input();
    }

  Fitness values: -100.0, Generation: 101
  ```
  - `D0 XOR D1 XOR D2 XOR D3`
  ```
  Parameters:
  POPULATION_SIZE=500
  MAX_DEPTH=2
  MAX_WIDTH=4
  CROSSOVER_PROB=0.55
  GENERATIONS=101
  TOURNAMENT_SIZE=10
  MIN_INT=0
  MAX_INT=1
  ----------------------------------

  Problem not solved
  if (0 == X_0) {
    X_0 = input();
    }
  if (X_0 < 1) {
    X_0 = input();
    }
  if (X_4 != X_2) {
    X_5 = 0;
    X_3 = (X_6 + 0);
    }
  if (0 <= X_5) {
    print((X_6 - X_5));
    X_7 = (X_8 / (X_9 * X_7));
    X_10 = input();
    }

  Fitness values: -100.0, Generation: 101
  ```
- `k = 5`
  - `D0 AND D1 AND D2 AND D3 AND D4`
  ```
  Parameters:
  POPULATION_SIZE=250
  MAX_DEPTH=2
  MAX_WIDTH=5
  CROSSOVER_PROB=0.55
  GENERATIONS=101
  TOURNAMENT_SIZE=10
  MIN_INT=0
  MAX_INT=1
  ----------------------------------

  Problem not solved
  print(0);
  X_0 = (0 - (1 / 0));
  while (0 >= X_0 or X_0 >= 0 or X_1 < 0) {
    X_2 = (1 / 1);
    }
  while (1 != X_1 and 0 <= X_1 and X_2 == 1) {
    X_3 = input();
    print(((1 / X_4) + 1));
    print((X_5 / 1));
    }
  print((0 * X_3));

  Fitness values: -100.0, Generation: 101
  ```
  - `D0 OR D1 OR D2 OR D3 OR D4`
  ```
    Parameters:
    POPULATION_SIZE=500
    MAX_DEPTH=2
    MAX_WIDTH=7
    CROSSOVER_PROB=0.55
    GENERATIONS=101
    TOURNAMENT_SIZE=10
    MIN_INT=0
    MAX_INT=1
    ----------------------------------

    Problem not solved
    while (X_2 >= 0 and X_1 > X_0 and 1 < X_1) {
        X_0 = input();
        X_3 = X_1;
    }
    if (X_1 == X_1 and 0 != 0 and X_2 <= X_2) {
        X_1 = 0;
        X_3 = input();
        X_3 = X_2;
        print(((X_4 / X_5) * X_1));
        print((X_4 - 0));
        X_4 = input();
        X_0 = (X_6 / (1 + 1));
    }
    while (X_0 <= X_0) {
        X_1 = X_0;
        print(1);
        X_1 = ((1 + 0) / 0);
        print(0);
        print(X_0);
        X_1 = X_0;
    }

    Fitness values: -100.0, Generation: 101
  ```

Jak widać, system dla większych k zaczyna generalizować - dla `AND` decyduje się zwracać 0 (ponieważ tylko $\frac{1}{k^2}$ przypadków powinno zwracać 1), analogicznie dla `OR` i `XOR`.

<!-- - `k = 6`
- `k = 7`
- `k = 8`
- `k = 9`
- `k = 10` -->
