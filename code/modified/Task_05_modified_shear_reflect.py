import numpy as np
import matplotlib.pyplot as plt

# MODIFIED CASE: a graphics app applies "italic" shear and a mirror
# reflection to the outline of an arrow-shaped road sign.
points = np.array([
    [0.0, 0.0], [2.0, 0.0], [2.0, -0.5], [3.0, 0.5],
    [2.0, 1.5], [2.0, 1.0], [0.0, 1.0], [0.0, 0.0]
])

shear = np.array([[1.0, 0.4],      # x' = x + 0.4y  (slant to the right)
                  [0.0, 1.0]])
reflect_y = np.array([[-1.0, 0.0],  # mirror about the y-axis
                      [0.0, 1.0]])

transformation = reflect_y @ shear
new_points = points @ transformation.T

def area(p):  # shoelace formula
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x[:-1], y[1:]) - np.dot(x[1:], y[:-1]))

print("Transformation matrix:\n", transformation)
print("Determinant:", np.linalg.det(transformation))
print(f"Original area:    {area(points):.3f}")
print(f"Transformed area: {area(new_points):.3f}")

plt.plot(points[:, 0], points[:, 1], marker="o", label="Original sign")
plt.plot(new_points[:, 0], new_points[:, 1], marker="s", label="Sheared + reflected")
plt.axvline(0, color="grey", linewidth=0.8)
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Shear followed by reflection")
plt.legend()
plt.grid(True)
plt.show()
