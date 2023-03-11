import numpy as np
import sys

class LinearEquationSolver:
    def __init__(self, n):
        self.n = n
        self.augmented_matrix = np.zeros((n, n+1))

    def read_augmented_matrix(self):
        print('Enter Augmented Matrix Coefficients:')
        for i in range(self.n):
            for j in range(self.n+1):
                self.augmented_matrix[i][j] = float(input('a['+str(i)+']['+ str(j)+']='))

    def gauss_jordan_elimination(self):
        for i in range(self.n):
            if self.augmented_matrix[i][i] == 0.0:
                sys.exit('Divide by zero detected!')

            for j in range(self.n):
                if i != j:
                    ratio = self.augmented_matrix[j][i]/self.augmented_matrix[i][i]

                    for k in range(self.n+1):
                        self.augmented_matrix[j][k] = self.augmented_matrix[j][k] - ratio * self.augmented_matrix[i][k]

        for i in range(self.n):
            divisor = self.augmented_matrix[i][i]
            for j in range(self.n+1):
                self.augmented_matrix[i][j] /= divisor

    def solve(self):
        self.read_augmented_matrix()
        self.gauss_jordan_elimination()

    def display_solution(self):
        print('\nRequired solution is: ')
        for i in range(self.n):
            print('X%d = %0.2f' %(i, self.augmented_matrix[i][self.n]), end = '\t')


# Create an instance of LinearEquationSolver with n = 3
solver = LinearEquationSolver(4)

# Solve the linear equation system
solver.solve()

# Display the solution
solver.display_solution()