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
area = np.trapezoid(cpu_data, dx=1)

print("Area under CPU usage curve:", area,"unit seconds")