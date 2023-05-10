import numpy as np
import matplotlib.pyplot as plt
import math

T  = 66.73651480674744
dt = 0.0811879742174543
freq =  12.317095107233428
adc_step = 0.012890625

data = np.loadtxt ('data.txt') * adc_step

XDELTA = 10
YDELTA = 0.5
XLIML = -XDELTA
XLIMH = math.ceil (T / XDELTA) * XDELTA
YLIML = math.floor (min (data) / YDELTA) * YDELTA - YDELTA
YLIMH = math.ceil (max (data)  / YDELTA) * YDELTA

plt.figure (figsize = (16, 9), dpi = 200)
graph = plt.subplot ()

plt.xlim (XLIML, XLIMH)
plt.ylim (YLIML, YLIMH)
graph.set_xticks (np.arange (XLIML, XLIMH + XDELTA, XDELTA))
graph.set_yticks (np.arange (YLIML, YLIMH + YDELTA, YDELTA))
graph.set_xticks (np.arange (XLIML, XLIMH + XDELTA, XDELTA / 5), minor=True)
graph.set_yticks (np.arange (YLIML, YLIMH + YDELTA, YDELTA / 5), minor=True)

plt.xlabel ('Time, seconds')
plt.ylabel ('Voltage, volts')

plt.rcParams['text.usetex'] = True

graph.grid (which='major', linestyle = '-', alpha = 1, linewidth = 1)
graph.grid (which='minor', linestyle = '--', alpha = 1, linewidth = 0.4)

X = np.linspace (0, T, len (data))
graph.plot (X, data, 'b,-', label = r'$V_{RC} (t)$')
graph.plot (X[12::13], data[12::13], 'r.')
plt.title ('Dependency of voltage on C in RC countour from time')

plt.text (XLIMH - 3 * XDELTA, YLIMH - YDELTA, 'Charge time = ' + str (X[np.argmax (data)]) + '\nDischarge time = ' + str (T - X[np.argmax (data)]))

plt.legend ()
plt.show ()
plt.savefig ('graph.png')