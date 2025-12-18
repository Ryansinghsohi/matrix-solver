import numpy as np
import matplotlib.pyplot as plt


USE_LOG_SCALE = False


# Operation counter
class OpCounter:
    def __init__(self):
        self.ops = 0

    def add(self, n=1):
        self.ops += n


# Gaussian elimination
def gauss_elimination_ops(A, b):
    n = len(b)
    counter = OpCounter()

    A = A.astype(float)
    b = b.astype(float)

    # Forward elimination
    for k in range(n):
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            counter.add(1)  # division

            for j in range(k, n):
                A[i, j] -= factor * A[k, j]
                counter.add(2)  # multiply + subtract

            b[i] -= factor * b[k]
            counter.add(2)

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i, j] * x[j]
            counter.add(2)

        x[i] = (b[i] - s) / A[i, i]
        counter.add(2)

    return x, counter.ops


# Matrix inverse (Gauss–Jordan)
def inverse_ops(A):
    n = A.shape[0]
    counter = OpCounter()

    A = A.astype(float)
    I = np.eye(n)

    for i in range(n):
        pivot = A[i, i]

        for j in range(n):
            A[i, j] /= pivot
            I[i, j] /= pivot
            counter.add(2)

        for k in range(n):
            if k != i:
                factor = A[k, i]
                counter.add(1)

                for j in range(n):
                    A[k, j] -= factor * A[i, j]
                    I[k, j] -= factor * I[i, j]
                    counter.add(4)

    return I, counter.ops


# Determinant with ops
def det_ops(A):
    n = A.shape[0]
    counter = OpCounter()
    A = A.copy().astype(float)

    for k in range(n):
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            counter.add(1)

            for j in range(k, n):
                A[i, j] -= factor * A[k, j]
                counter.add(2)

    det = 1
    for i in range(n):
        det *= A[i, i]
        counter.add(1)

    return det, counter.ops


# Cramer's rule
def cramer_ops(A, b):
    n = len(b)
    total_ops = 0

    _, ops = det_ops(A)
    total_ops += ops

    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        _, ops = det_ops(A_i)
        total_ops += ops

    return total_ops


# Run experiment
system_sizes = range(2, 30)

gauss_steps = []
inverse_steps = []
cramer_steps = []

for n in system_sizes:
    A = np.random.rand(n, n)
    b = np.random.rand(n)

    _, ops = gauss_elimination_ops(A.copy(), b.copy())
    gauss_steps.append(ops)

    _, ops = inverse_ops(A.copy())
    inverse_steps.append(ops)

    cramer_steps.append(cramer_ops(A.copy(), b.copy()))


# Plot
plt.figure(figsize=(8, 6))
plt.plot(system_sizes, gauss_steps, marker="o", label="Gauss elimination")
plt.plot(system_sizes, inverse_steps, marker="s", label="Inverse method")
plt.plot(system_sizes, cramer_steps, marker="^", label="Cramer's rule")

plt.xlabel("Number of equations (n)")
plt.ylabel("Counted arithmetic operations")
plt.title("Measured operation count comparison")
plt.legend()
plt.grid(True)

if USE_LOG_SCALE:
    plt.yscale("log")

plt.show()
