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
    det_A = np.linalg.det(mat)
    n_amount = mat.shape[0]
    x = np.zeros(n_amount)

    for i in range(n_amount):
        A_i = mat.copy()
        A_i[:, i] = y
        det_Ai = np.linalg.det(A_i)
        x[i] = det_Ai / det_A

    return x


# Storlekar på systemen
system_sizes = range(5, 101, 1)

# vart tiden sparas
gauss_times = []
inverse_times = []
cramer_times = []

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

    # Cramer's rule (OBS: mycket långsam för stora n)
    start = time.time()
    if n <= 10:  # Cramer's rule blir extremt långsam annars
        cramer_rule(A, b)
    else:
        cramer_times.append(np.nan)
        continue
    end = time.time()
    cramer_times.append(end - start)

# end time counter
end_total_time = time.time()

# find difference from start to end
dif_total_time = int(end_total_time - start_total_time)

# convert time
print(convert_to_time(dif_total_time))

# skapa grafen
plt.figure(figsize=(8, 6))
plt.plot(system_sizes, gauss_times, marker="o", label="Gauss-elimination (solve)")
plt.plot(system_sizes, inverse_times, marker="s", label="Inversmetoden (A^-1 * b)")
plt.plot(system_sizes[:len(cramer_times)], cramer_times, marker="^", label="Cramer's rule", linestyle="--")

plt.xlabel("Antal ekvationer / obekanta (n)")
plt.ylabel("Tid (sekunder)")
plt.title("Jämförelse av metoder för att lösa Ax = b")
plt.legend()
plt.grid(True)
plt.show()
