# 1. Import necessary libraries: It imports the libraries for analysis data and its visualization.
# We use numpy for numeric operations, matplotlib.pyplot for data visualization,
# train_test_split of sklearn.model_selection to divide the data in training and test groups,
# and finally we use LinearRegression of sklearn.linear_model to implement the linear regression model.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 2. Prepare the data: It defines two arrays that represent the size (X_data) and price (Y_data) of the houses.
# Let's assume we have the housing data where X represents the size of the house and Y represents the price
X_data = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350]).reshape(-1, 1)  # Size of houses
Y_data = np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000])  # Prices of houses

# 3. Split the data into training and testing sets: we divide the data in two groups: training and test using
# train_test_split function.
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=42)

# 4. Create and train the model: We create a linear regression object using LinearRegression() and it fits
# to the training data using fit() method.
model = LinearRegression()
model.fit(X_train, Y_train)

# 5. Make predictions: we are going to use the test data to predict the houses' price using predict() method.
Y_pred = model.predict(X_test)

# 6. Visualize the results: it shows a scatter plot of the test data and draws the regression line to
# show how it fits to the data model.
plt.scatter(X_test, Y_test, color='blue')
plt.plot(X_test, Y_pred, color='red')
plt.title('Housing Price Prediction')
plt.xlabel('House Size')
plt.ylabel('Price')
plt.show()

# DESIGN CONSIDERATIONS #
# We chose to use the scikit-learn library to implement linear regression due to its efficiency and ease of use.
# It was decided to split the data into training and test sets to evaluate the performance of the model.
# It was chosen to visualize the results using a scatter plot and a regression line for a better understanding
# of the model.