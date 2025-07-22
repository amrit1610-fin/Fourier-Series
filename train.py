import numpy as np
import math
from FourierSeries import FourierSeries
import matplotlib.pyplot as plt

def f(x):
    return x**2

n = 3
l1 = -math.pi
l2 =  math.pi

ser = FourierSeries()
series = ser.FourierSeries(f, l1, l2, num_terms=200)

x_values = np.linspace(l1, l2, 100) 
y_original = [f(x) for x in x_values]

y_fourier_series = [series(x) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_original, label='Original Function $f(x)$', color='blue', linestyle='--')
plt.plot(x_values, y_fourier_series, label='Fourier Series Approximation', color='red')
plt.title(f'Fourier Series Approximation of $f(x)$ on [{l1:.2f}, {l2:.2f}] with {ser.n} terms')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axvline(x=l1, color='gray', linestyle=':', linewidth=0.8)
plt.axvline(x=l2, color='gray', linestyle=':', linewidth=0.8)
plt.show()

print(f"Fourier series calculated with {200} terms.")
