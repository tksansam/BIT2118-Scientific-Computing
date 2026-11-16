import numpy as np
import matplotlib.pyplot as plt

# MODIFIED CASE: a matatu pulls away from a stage. A GPS logger records
# position every 2 s. Estimate speed AND acceleration using np.gradient
# (central differences inside, one-sided differences at the ends).
time = np.arange(0, 22, 2, dtype=float)
position = np.array([0.0, 3.1, 12.0, 27.5, 47.0, 70.2, 95.4, 121.0, 146.6, 172.0, 197.4])

speed = np.gradient(position, time)          # m/s
accel = np.gradient(speed, time)             # m/s^2

for t, x, v, a in zip(time, position, speed, accel):
    print(f"t={t:4.0f}s  x={x:6.1f}m  v={v:5.2f}m/s ({v*3.6:5.1f} km/h)  a={a:5.2f}m/s^2")
print(f"Top speed: {speed.max()*3.6:.1f} km/h")
print(f"Peak acceleration: {accel.max():.2f} m/s^2 at t={time[np.argmax(accel)]:.0f}s")

fig, ax1 = plt.subplots()
ax1.plot(time, speed, marker="o", label="Speed (m/s)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Speed (m/s)")
ax2 = ax1.twinx()
ax2.plot(time, accel, marker="s", linestyle="--", color="tab:red", label="Acceleration")
ax2.set_ylabel("Acceleration (m/s^2)")
ax1.set_title("Speed and acceleration from GPS data")
ax1.grid(True)
fig.legend(loc="center right", bbox_to_anchor=(0.86, 0.45))
plt.show()
