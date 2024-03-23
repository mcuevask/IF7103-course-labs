import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Generate example data
np.random.seed(0)
house_size = 2 * np.random.rand(100, 1)
house_price = 3 + 4 * house_size + np.random.randn(100, 1)

# Step 2: Divide the data in training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_size, house_price, test_size=0.2, random_state=42)

# Step 3: Create and train the lineal regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict results with the model
y_pred = model.predict(X_test)

# Step 5: Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Error Cuadrático Medio:", mse)

# Step 6: Calculate the r2 score
r2 = r2_score(y_test, y_pred)
print("Coeficiente de Determinación (R-cuadrado):", r2)

# Step 7: Visualize the results
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño Vivienda')
plt.ylabel('Precio Vivienda')
plt.show()
