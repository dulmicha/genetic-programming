# Genetic programming 

## Overview
This repository contains solutions for common GP problems - finding best individual for given task, which can be either approximating (ideally - seeking accurate) math function $R^n \to R, n \in N_+$ (`TinyGP` directory), or looking for program written in language we propose, which will give desired output (`MiniLang` directory).

### TinyGP
First part includes solutions search using TinyGP, extended with $sin$ and $cos$ functions, analysis of the obtained results and their simplification. 

### MiniLang
Second part includes grammaticaly correct programs generation with many adjustable parameters, their evaluation by the custom interpreter and evolution within the framework of genetic operators. Tuned population can also be used in the next search process.
