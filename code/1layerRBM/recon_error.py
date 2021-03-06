'''
Typical usage:
python -m code.1layerRBM.recon_error /home/liuq/apt/2ndYear/sDBN/theta/5420_b2_epoc10_cd.npy
'''
import sys
import random
import numpy as np
from ..utils import poisson_tools as pt
import matplotlib.pyplot as plt
from scipy.special import expit

def sigmoid_sampling(data, weight, bias):
    sum_data = np.dot(data, weight) + bias
    prob = expit(sum_data)
    rdm = np.random.random(prob.shape)
    index_on = rdm < prob
    samples = np.zeros(prob.shape)
    samples[index_on]=1.
    return samples


theta_file = sys.argv[1]
print theta_file
np.random.seed(0)
digit = 5
a,b,W = np.load(theta_file)

test_x, test_y = pt.get_test_data()
test_x = test_x > 50
label_list = np.array(test_y).astype(int)
index_digit = np.where(label_list==digit)[0]
test_num = len(index_digit)
index_test = index_digit[0:test_num]
test_v = np.array(test_x[index_test]).astype(float)

np.random.seed(0)
error_test = 0.
for i in range(test_num):  #(test_num):
    test = test_v[i]
    test_h = sigmoid_sampling(test, W, b)
    recon = sigmoid_sampling(test_h, W.transpose(), a)
    error_test += np.sum(np.abs(recon-test))

train_x, train_y = pt.get_train_data()
train_x = train_x > 50
label_list = np.array(train_y).astype(int)
index_digit = np.where(label_list==digit)[0]
train_num = len(index_digit)
index_train = index_digit[0:train_num]
train_v = np.array(train_x[index_train]).astype(float)

error_train = 0.
for i in range(train_num):  #(test_num):
    train = train_v[i]
    train_h = sigmoid_sampling(train, W, b)
    recon = sigmoid_sampling(train_h, W.transpose(), a)
    error_train += np.sum(np.abs(recon-train))


print error_test
print error_train


