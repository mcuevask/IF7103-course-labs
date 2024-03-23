# Import necessary libraries
import numpy as np  # NumPy is used for numerical computing
import matplotlib.pyplot as plt  # Matplotlib is used for data visualization
from sklearn.model_selection import train_test_split  # For splitting the data into training and testing sets
from sklearn.linear_model import LinearRegression  # Linear regression model from scikit-learn
from sklearn.metrics import mean_squared_error  # For evaluating model performance using mean squared error

# Generate example data
np.random.seed(0)  # Setting seed for reproducibility
X = 2 * np.random.rand(100, 1)  # Generating random values for house size (independent variable)
y = 5 + 3 * X + np.random.randn(100, 1)  # Generating house prices (dependent variable) with some random noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""
The data is divided into training and testing sets using train_test_split function.
test_size=0.2 specifies that 20% of the data will be used for testing, and 80% for training.
random_state=0 ensures reproducibility by fixing the random seed.
"""

# Create the linear regression model
model = LinearRegression()


# Train the model using the training data
model.fit(X_train, y_train)
"""
The fit method is used to train the linear regression model using the training data.
It learns the coefficients for the linear equation that best fits the data.
"""

# Make predictions on the test data
y_pred = model.predict(X_test)

"""
The predict method is used to make predictions on the test data using the trained model.
"""

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""
Mean squared error (MSE) is calculated to evaluate the performance of the model.
It measures the average of the squares of the errors, i.e., the average squared difference
between the actual and predicted values.
"""

# Visualize the data and the regression line
plt.scatter(X_test, y_test, color='blue')  # Scatter plot of the test data points
plt.plot(X_test, y_pred, color='red')  # Plotting the regression line
plt.title('Simple Linear Regression')  # Title of the plot
plt.xlabel('House Size')  # Label for the x-axis
plt.ylabel('House Price')  # Label for the y-axis
plt.show()
"""
This block of code visualizes the test data points along with the regression line.
The scatter plot shows the actual house sizes and prices, and the regression line represents
the relationship learned by the linear regression model.
"""