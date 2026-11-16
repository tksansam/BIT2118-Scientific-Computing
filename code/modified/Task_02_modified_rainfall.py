import numpy as np

# MODIFIED CASE: daily rainfall for one month (30 days) at a weather station.
# Values are illustrative sample data in millimetres.
rain_mm = np.array([
    0.0, 2.4, 11.8, 0.0, 0.0, 5.6, 23.1, 14.0, 0.0, 0.0,
    1.2, 0.0, 0.0, 8.9, 31.5, 12.2, 0.0, 0.0, 0.0, 4.4,
    0.0, 17.6, 9.3, 0.0, 0.0, 0.0, 2.0, 6.7, 0.0, 0.0
])

total_rain = np.sum(rain_mm)
mean_rain = np.mean(rain_mm)
wettest_day = np.argmax(rain_mm) + 1
rainy_days = np.count_nonzero(rain_mm >= 1.0)   # a "rain day" has at least 1 mm

# Vectorised conversion: millimetres to inches
rain_in = rain_mm / 25.4

# Boolean mask: heavy-rain days (at least 20 mm)
heavy_days = np.where(rain_mm >= 20)[0] + 1

print(f"Total monthly rainfall: {total_rain:.1f} mm ({total_rain/25.4:.2f} in)")
print(f"Mean daily rainfall: {mean_rain:.2f} mm")
print(f"Wettest day: day {wettest_day} with {rain_mm.max():.1f} mm")
print(f"Number of rain days (>= 1 mm): {rainy_days}")
print("Heavy-rain days (>= 20 mm):", heavy_days)
print("First seven days in inches:", np.round(rain_in[:7], 3))
