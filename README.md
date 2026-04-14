# CPU Usage Monitor & Analysis

A Python project that monitors CPU usage in real time, visualizes the data using a graph, and calculates the area under the CPU usage curve.

## Features

* Collects CPU usage every second
* Stores readings for analysis
* Plots CPU usage over time using Matplotlib
* Calculates area under the curve using NumPy
* Simple and beginner-friendly project

## Technologies Used

* Python 3
* psutil
* matplotlib
* numpy

## Project Code

```python
import psutil
import time
import matplotlib.pyplot as plt
import numpy as np

cpu_data = []

print("Collecting CPU data...")

for i in range(40):
    usage = psutil.cpu_percent(interval=1)
    cpu_data.append(usage)
    print(f"CPU Usage: {usage}%")

# Plot graph
time_points = list(range(len(cpu_data)))

plt.plot(time_points, cpu_data, marker='o')
plt.title("CPU Usage Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("CPU Usage (%)")
plt.grid()
plt.show()

# Area calculation
area = np.trapz(cpu_data, dx=1)
print("Area under CPU usage curve:", area)
```

## Installation

Install the required libraries:

```bash
pip install psutil matplotlib numpy
```

## How to Run

```bash
python filename.py
```

## Example Output

```text
Collecting CPU data...
CPU Usage: 18%
CPU Usage: 22%
CPU Usage: 35%
...
Area under CPU usage curve: 457.0
```

## Use Cases

* System performance monitoring
* Learning data visualization
* Understanding CPU workload patterns
* Beginner Python practice project

## Future Improvements

* Add RAM monitoring
* Export data to CSV
* Live updating graph
* Detect high CPU spikes
* Save graph as image

## Author

Chanchal Karwasra
