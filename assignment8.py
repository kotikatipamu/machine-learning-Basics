# -*- coding: utf-8 -*-
"""Assignment8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pHZ-kB7yPAzu7-esPxfTj38pmzSvfW-

# Assignment8
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

"""# How Much is Your Car Worth?

Data about the retail price of 2005 General Motors cars can be found in `car_data.csv`.

The columns are:

1. c: suggested retail price of the used 2005 GM car in excellent condition.
2. Mileage: number of miles the car has been driven
3. Make: manufacturer of the car such as Saturn, Pontiac, and Chevrolet
4. Model: specific models for each car manufacturer such as Ion, Vibe, Cavalier
5. Trim (of car): specific type of car model such as SE Sedan 4D, Quad Coupe 2D          
6. Type: body type such as sedan, coupe, etc.      
7. Cylinder: number of cylinders in the engine        
8. Liter: a more specific measure of engine size     
9. Doors: number of doors           
10. Cruise: indicator variable representing whether the car has cruise control (1 = cruise)
11. Sound: indicator variable representing whether the car has upgraded speakers (1 = upgraded)
12. Leather: indicator variable representing whether the car has leather seats (1 = leather)

## Tasks, Part 1

1. Find the linear regression equation for mileage vs price.
2. Chart the original data and the equation on the chart.
3. Find the equation's $R^2$ score (use the `.score` method) to determine whether the
equation is a good fit for this data. (0.8 and greater is considered a strong correlation.)

## Tasks, Part 2

1. Use mileage, cylinders, liters, doors, cruise, sound, and leather to find the linear regression equation.
2. Find the equation's $R^2$ score (use the `.score` method) to determine whether the
equation is a good fit for this data. (0.8 and greater is considered a strong correlation.)
3. Find the combination of the factors that is the best predictor for price.

## Tasks, Hard Mode

1. Research dummy variables in scikit-learn to see how to use the make, model, and body type.
2. Find the best combination of factors to predict price.
"""

df = pd.read_csv("/content/car_data.csv")
df.head(10)

"""#Part-1"""

X = df[['Mileage']]
y = df[['Price']]

lin_reg=linear_model.LinearRegression()
lin_reg=lin_reg.fit(X,y)
y_pred=lin_reg.predict(X)

print("intercept:" ,lin_reg.intercept_)
print('coefcient:' ,lin_reg.coef_)
print('r_sqared:' ,lin_reg.score(X,y))

plt.scatter(X,y,color='r')
plt.plot(X,y_pred,color='b')
plt.xlabel('MILEAGE')
plt.ylabel('PRICE')
plt.title("Mileage vs Price")
plt.legend(['predicted','actual']);

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

degrees = 5
fig, axs = plt.subplots(degrees, figsize = (10, 30))

for degree in range(degrees):
    model = Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('linear', linear_model.LinearRegression(fit_intercept=False))])

    points = 50000


    model = model.fit(X, y)
    model_score = model.score(X,y)

    subplot = axs[degree]
    subplot.plot(model.predict([[j] for j in range(points)]), color='r')
    subplot.scatter(X, y)
    subplot.set_title('{} degrees {} R-squeard'.format(degree, model_score))

plt.show()

"""#Part-2"""

Features= ['Mileage', 'Cylinder', 'Liter', 'Doors', 'Cruise', 'Sound', 'Leather']
X=df[Features]
y=df[['Price']]

lin_reg=linear_model.LinearRegression()
lin_reg=lin_reg.fit(X,y)

print('intercept :',lin_reg.intercept_)
print('coefficient:',lin_reg.coef_)
print("r_squared :",lin_reg.score(X,y))

