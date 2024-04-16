import numpy as np
import scipy.signal


def correlate2d(x, W):
    correlated = np.zeros((x.shape[0] - W.shape[0] + 1, x.shape[1] - W.shape[1] + 1))
    for i in range(correlated.shape[0]):
        for j in range(correlated.shape[1]):
            correlated[i, j] = np.sum(x[i:i+W.shape[0], j:j+W.shape[1]] * W)
    return correlated

def convolve2d(x, W):
    convolved = np.zeros((x.shape[0] - W.shape[0] + 1, x.shape[1] - W.shape[1] + 1))
    for i in range(convolved.shape[0]):
        for j in range(convolved.shape[1]):
            convolved[i, j] = np.sum(x[i:i+W.shape[0], j:j+W.shape[1]] * np.flip(W))
    return convolved

x = np.array([[0.10, 0.20, 0.10, 0.10, 0.00],
               [0.80, 0.90, 1.00, 1.00, 0.90],
               [1.00, 1.00, 1.00, 1.00, 1.00],
               [0.90, 1.00, 1.00, 0.80, 1.00],
               [0.00, 0.10, 0.10, 0.20, 0.00]])

W = np.array([[1.00, 1.00, 1.00],
              [0.00, 0.00, 0.00],
              [-1.00, -1.00, -1.00]])

print("correlation: \n", correlate2d(x, W))
print("convolution: \n", convolve2d(x, W))

print()

print("scipy correlation: \n", scipy.signal.correlate2d(x,W, mode='valid'))
print("scipy convolution: \n", scipy.signal.convolve2d(x,W, mode='valid'))