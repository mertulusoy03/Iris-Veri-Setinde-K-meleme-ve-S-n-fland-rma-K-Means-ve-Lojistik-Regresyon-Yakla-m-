# -*- coding: utf-8 -*-
"""reg&conf.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wHa18QQuJfrw4sDVv71KggO_5nXMrf-N
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
# %matplotlib inline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,plot_confusion_matrix
from google.colab import drive
drive.mount('/content/drive/')
data=pd.read_csv("/content/drive/MyDrive/images/Iris.csv")
data=data.set_index('Id')
data.head(50)

data.info()

print(data.describe(),'\n') #ya da data.describe().T
data.hist()
plt.show()

data.isnull().sum()

sns.pairplot(data)

sns.pairplot(data, hue='Species',palette='icefire_r')

from sklearn.cluster import KMeans
import sklearn
from sklearn.datasets import load_iris
from sklearn import datasets
iris = datasets.load_iris()
x = data.iloc[:, 0:4].values
kmeans = KMeans(n_clusters=3)
y_kmeans3 = kmeans.fit_predict(x)
KMmodel = kmeans.fit(iris.data)

print(iris.feature_names)
print(iris.target_names)

for i in range(1, 8):
    kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 200, n_init = i, random_state = 77)
    kmeans.fit(x)
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 200, n_init = 5, random_state = 77)
y_kmeans = kmeans.fit_predict(x)

"""k-means++ ile k-means aynı basit mantığa sahiptir.
ağırllık merkezi seçilir, öklid mesafesi hesaplanır en uzak nokta seçilir bir sonraki merkeze atanır. Her nokta en yakın merkezle ilişkilenir.
Merkezler etrafında kümeleme işlemi gerçekleşir.
"""

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'orange', label = 'Setosa (Irish)')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'turquoise', label = 'Versicolour (Irish)')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Virginica (Irish)')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'black', label = 'Centroid Points')
plt.legend()

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 2], s = 100, c = 'orange', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 2], s = 100, c = 'turquoise', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 2], s = 100, c = 'green', label = 'Iris-virginica')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,2], s = 100, c = 'black', label = 'Centroids')
plt.legend()

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 3], s = 100, c = 'orange', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 3], s = 100, c = 'turquoise', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 3], s = 100, c = 'green', label = 'Iris-virginica')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,3], s = 100, c = 'black', label = 'Centroids')
plt.legend()

correlation=data.corr()
sns.heatmap(correlation,annot=True,cmap="Greens")

"""Fit(data) yöntemi, ölçeklendirme için daha fazla kullanılabilmek üzere belirli bir özelliğin ortalamasını ve standart sapmasını hesaplamak için kullanılır. Transform(data) yöntemi kullanılarak hesaplanan ortalama değerler ölçeklendirme yapmak için kullanılır."""

'''encoder = LabelEncoder()
data['Species'] = encoder.fit_transform(data['Species'])
data.head(50)'''

x = data.drop('Species',axis=1)
y = data['Species']
tr_x, test_x, tr_y, test_y = train_test_split(x,y,test_size=0.2)

print("Train x shape: ",tr_x.shape)
print("Test x shape: ",test_x.shape)
print("Train y shape: ",tr_y.shape)
print("Test y shape: ",test_y.shape)

print(iris.target_names)

""""liblinear", "newton-cg", "sag", "lbfgs" hakkında detaylı bilgilere erişmek için tıklayın."""

lr  = LogisticRegression(solver='liblinear').fit(tr_x, tr_y)
est_y_lr = lr.predict(test_x)
class_rep_LR = classification_report(test_y, est_y_lr)
print('\t\t\t Classification report:\n', class_rep_LR, '\n')
plot_confusion_matrix(lr, test_x, test_y)
plt.show()