# Regression Template
# You can make changes in it according to your own needs and use it


#### Sci-Kit Learn makes everything easy ####


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('dataset.csv')            # enter path of the dataset
X = dataset.iloc[,].values                      # specify features for X
y = dataset.iloc[,].values                      # specify features for Y


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

# Fitting the Regression Model to the dataset
#
##
### Create your regressor here in this area
##
#


# Predicting a new result
y_pred = regressor.predict(6.5)     # make predictions here





##########   Visualizations   ##########


# Visualising the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title(' Regression Model ')
plt.xlabel(' Label X ')
plt.ylabel(' Label Y ')
plt.show()

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title(' Regression Model ')
plt.xlabel(' Label X ')
plt.ylabel(' Label Y ')
plt.show()