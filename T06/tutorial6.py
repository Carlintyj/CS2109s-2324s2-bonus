import numpy as np

# Define the training data
X = np.array([[-2, -2], [-2, 1], [-2, 3], [0, 1], [2, 1]])
y_bar = np.array([-1, -1, 1, 1, 1])

# Construct the design matrix
X_design = np.column_stack((np.outer(X[:, 0], y_bar), np.outer(X[:, 1], y_bar), np.ones(len(X))))

# Solve for alpha and b for the green line
alpha_green, residuals_green, rank_green, singular_values_green = np.linalg.lstsq(X_design, y_bar, rcond=None)
b_green = alpha_green[-1]  # Last value is the intercept

# Solve for alpha and b for the purple line
y_bar_purple = np.array([-1, 1, -1, 1, 1])
alpha_purple, residuals_purple, rank_purple, singular_values_purple = np.linalg.lstsq(X_design, y_bar_purple, rcond=None)
b_purple = alpha_purple[-1]  # Last value is the intercept

# Print the coefficients and intercepts for the green line
print("Green Line:")
print("Alpha:", alpha_green[:-1])
print("Intercept (b):", b_green)

# Print the coefficients and intercepts for the purple line
print("\nPurple Line:")
print("Alpha:", alpha_purple[:-1])
print("Intercept (b):", b_purple)
