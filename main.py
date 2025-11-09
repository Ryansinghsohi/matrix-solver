import numpy as np
import time
import datetime
import matplotlib.pyplot as plt


def convert_to_time(sek: float):
    delta = datetime.timedelta(seconds=sek)
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} days, {hours} hours, {minutes} min, {seconds} s"


def cramer_rule(mat, y):
    det = np.linalg.det(mat)

    # A_i
    mat1 = np.array([y, mat[1], mat[2]])
    mat2 = np.array([mat[0], y, mat[2]])
    mat3 = np.array([mat[0], mat[1], y])

    # det av A_i
    det1 = np.linalg.det(mat1)
    det2 = np.linalg.det(mat2)
    det3 = np.linalg.det(mat3)

    x3 = ((det1/det), (det2/det), (det3/det))

    return x3


# Storlekar på systemen
system_sizes = range(5, 501, 1)

# vart tiden sparas
gauss_times = []
inverse_times = []
cramer_time =[]

# start time counter
start_total_time = time.time()

for n in system_sizes:
    # göra random system Ax = b
    A = np.random.rand(n, n) * 10
    b = np.random.rand(n) * 10

    # Gauss-elimination
    start = time.time()
    x1 = np.linalg.solve(A, b)
    end = time.time()
    gauss_times.append(end - start)

    # Inversmetoden (A^-1 * b)
    start = time.time()
    A_inv = np.linalg.inv(A)
    x2 = A_inv.dot(b)
    end = time.time()
    inverse_times.append(end - start)

    # Cramer's rule
    start = time.time()
    cramer_rule(A, b)
    end = time.time()
    cramer_time.append(end - start)


# end time counter
end_total_time = time.time()

# find diffrence from start to end
dif_total_time = int(end_total_time - start_total_time)

# convert time
print(convert_to_time(dif_total_time))


# skapa grafen
plt.figure(figsize=(8, 6))
plt.plot(system_sizes, gauss_times, marker="o", label="Gauss-elimination (solve)")
plt.plot(system_sizes, inverse_times, marker="s", label="Inversmetoden (A^-1 * b)")

# olika labes
plt.xlabel("Antal ekvationer / obekanta (n)")
plt.ylabel("Tid (sekunder)")
plt.title("Jämförelse av metoder för att lösa Ax = b")
plt.legend()
plt.grid(True)
plt.show()
