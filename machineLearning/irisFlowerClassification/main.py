import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class_labels']

df = pd.read_csv('iris.data', names=columns)


print(df.describe())

sns.pairplot(df, hue='Class_labels')

plt.show()