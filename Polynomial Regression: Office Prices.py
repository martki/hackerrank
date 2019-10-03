import fileinput
from pandas import DataFrame as df
#import matplotlib.pyplot as plt
import numpy as np


"""
^
Manual programming of a linear prediction model using method of least squares:
(which is not accurate enough for this task)
"""
def calculate_residual_linear(labels, feature):
    xtx_inverse = np.linalg.inv(np.matmul(np.transpose(labels), labels))
    xty = np.matmul(np.transpose(labels), feature)
    residual = np.matmul(xtx_inverse, xty)

    return residual

prediction_function = lambda labels, residual: np.matmul(labels, residual) 
predict_value = lambda new_labels, B: np.matmul(np.transpose(new_labels), B)
"""
^
"""


data = []
data_to_predict = []

for counter, line in enumerate(fileinput.input()):
    
    current_data_line = line.rstrip().split(" ")
    
    if counter == 0:
        features = int(current_data_line[0])
        data_rows = int(current_data_line[1])

    if counter > 0 and counter <= data_rows:
        data.append(current_data_line)

    if counter == data_rows+1:
        T = current_data_line
    
    if counter > data_rows+1:
        data_to_predict.append(current_data_line)


dataframe = df(data=data)
labels_added = dataframe[0].to_numpy(dtype=np.float) + dataframe[1].to_numpy(dtype=np.float)
price = dataframe[2].to_numpy(dtype=np.float)

# as linear solution is not precise enough, using numpy.polyfit() to calculate polynomial
Z = np.polyfit(labels_added, price, 2)
p = np.poly1d(Z)
xp = np.linspace(0.0, 2.0, 100)

"""
# For visualization of the solution, and comparison of linear to polynomial

xpp = np.linspace(0.0, 1.0, 100)
B = calculate_residual_linear(labels, price)
predicted_values = predict_value(np.array([xpp, xpp]), B)
labels = dataframe.iloc[:,0:2].to_numpy(dtype=np.float)
plt.scatter(labels_added, price)
plt.plot(xp, p(xp), color="red")
plt.plot(xp, predicted_values, color="green")
plt.ylim(0, 2000)
plt.xlim(0, 2)
plt.show()
"""

dataframe2 = df(data_to_predict)
predicted_values_ = p(dataframe2[0].to_numpy(dtype=np.float) + dataframe2[1].to_numpy(dtype=np.float))

for elem in predicted_values_:
    print(elem)