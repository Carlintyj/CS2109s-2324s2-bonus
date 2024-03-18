import pandas as pd
import numpy as np
from scipy.stats import entropy
from treelib import Tree

# Question 3a, b precision and recall
def question3a_b():
    confusion_matrix = [[10, 1], [1, 8]]
    TP = confusion_matrix[1][1]
    FP = confusion_matrix[0][1]
    FN = confusion_matrix[1][0]

    def precision(TP, FP):
        return TP / (TP + FP)
    
    def recall(TP, FN):
        return TP / (TP + FN)
    
    print("Precision: ", precision(TP, FP))
    print("Recall: ", recall(TP, FN))

# Question 4a using numpy matrices
def question4a():
    W = np.array([[4.2, -0.01, -0.12], [-20, -0.08, 35], [-1250, 0.82, 0.9]])
    X = np.array([[1, 4.2, 0.4], [1, 720, 2.4], [1, 2350, 5.5]])
    print("-X @ W.T: \n", -X @ W.T)
    print("P: \n", 1 / (1 + np.exp(-X @ W.T)))

# Question 5 illustration between MSE/MAE/BCE
def question5():
    y = np.array([0, 0, 1])
    y_hat1 = np.array([0.4, 0.4, 0.6])
    y_hat2 = np.array([0.1, 0.6, 0.9])

    print("M1")
    print("MSE: ", np.mean(1/2 * (y - y_hat1)**2))
    print("MAE: ", np.mean(1/2 * np.abs(y - y_hat1)))
    print("BCE: ", -np.mean(y * np.log(y_hat1) + (1 - y) * np.log(1 - y_hat1)))

    print("M2")
    print("MSE: ", np.mean(1/2 * (y - y_hat2)**2))
    print("MAE: ", np.mean(1/2 * np.abs(y - y_hat2)))
    print("BCE: ", -np.mean(y * np.log(y_hat2) + (1 - y) * np.log(1 - y_hat2)))

def main():
    print("Question 3a, b precision and recall")
    question3a_b()
    print()
    print("Question 4a using numpy matrices")
    question4a()
    print()
    print("Question 5 illustration between MSE/MAE/BCE")
    question5()

main()