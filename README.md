# Matrix Solver Comparison
This project was created as part of a high school project (gymnasiearbete). The purpose is to compare different methods for solving systems of linear equations and to analyze how many arithmetic operations each method requires.

## Project description
The program generates random invertible matrices and solves the corresponding linear systems using three different methods:

- Gaussian elimination
- Matrix inverse method
- Cramer's rule

The script counts the number of arithmetic operations used by each method and visualizes the results in a graph. There is also a button in the plot that lets the user switch between logarithmic and linear scale.

## Why this project is interesting
This project demonstrates how different algorithms can solve the same problem but with very different computational costs. It is useful for understanding:

- algorithm efficiency
- numerical methods
- complexity of solving linear systems
- how mathematics and programming are connected

## Features
- Generates random matrices of different sizes
- Checks that each matrix is invertible
- Counts arithmetic operations for each solving method
- Plots the comparison in a graph
- Allows toggling between log and linear scale

## Technologies used
- Python
- NumPy
- Matplotlib

## Installation
Make sure Python is installed, then run:

```bash
pip install numpy matplotlib
```

## How to run
```bash
python main.py
```

This will display a graph comparing the operation counts for the three methods.

## Author

Ryan Singh
