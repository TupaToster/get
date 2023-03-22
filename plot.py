import matplotlib.pyplot as plt
import numpy as np

input = [0, 5, 32, 64, 127, 255]
vals = [0.48, 0.48, 0.49, 0.82, 1.62, 3.25]

plt.grid ()
plt.plot (input, vals, 'db')
plt.plot (input, vals, '-r')
plt.show ()