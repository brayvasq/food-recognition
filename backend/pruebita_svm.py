# importacion del modulo de support vector machines
from sklearn import svm

# importación de la librería numpy para dar soporte de alto nivel a la operación con matrices y vectores
import numpy as np

# importación de la librería matplotlib.pyplot para generación de gráficos a partir listas o arrays
import matplotlib.pyplot as plt

# importación del módulo style de la librería matplotlib que genera una hoja de estilos para personalizar gráficos
from matplotlib import style

# define el estilo que utlizará para personalizar los gráficos
style.use("ggplot")

# Se crea un array con la función array de la librería numpy, estos valores van en pares y representan una coordenada
# Debemos introducir datos para el aprendizaje del algoritmo
X = np.array([["0", "1", "2", "3", "4", "-1"],
              ["0", "1", "6", "12", "-1", "-1"],  # paisa cafetero
              ["4", "6", "9", "-1", "-1", "-1"],
              ["0", "5", "7", "8", "-1", "-1"],
              ["5", "15", "-1", "-1", "-1", "-1"]])
# Damos "pesos" a los valores del array X, 0 para los puntos más "bajos" y 1 para los más "altos"
# Estos pesos los llamamos "objetivos"
# El primer valor de y, corresponde al primer par de valores de X, y así sucesivamente
y = [0, 1, 2, 3, 4]

# Utilizamos SVM (Máquina de vectores de soporte) y SVC (Clasificador de vectores de soporte)
# El kernel será lineal
# Utilizamos el margen de error en 1.0, predeterminado
# clf = svm.SVC(kernel='linear', C=1.0)
clf = svm.SVC(C=1000, gamma = 0.0001)

# Entrenamiento con los datos ingresados
model = clf.fit(X, y)

# Un par de ejemplos de predicción para unas coordenadas
print(clf.predict([["-1", "0", "-1", "-1", "1", "3"]]))
