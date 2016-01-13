'''
Functions to be used in MNIST related tasks.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# get training data
def get_train_data():
    dir_path = '../'
    file_name = dir_path + 'train-images.idx3-ubyte'
    print file_name
    
    f = open(file_name, "rb")
    magic_number, list_size, image_hight, image_width  = np.fromfile(f, dtype='>i4', count=4)
    train_x = np.fromfile(f, dtype='>u1', count=list_size*image_hight*image_width)
    train_x = np.reshape(train_x, (list_size,image_hight*image_width))
    f.close()
    
    file_name = dir_path + 'train-labels.idx1-ubyte'
    f = open(file_name, "rb")
    magic_number, list_size = np.fromfile(f, dtype='>i4', count=2)
    train_y = np.fromfile(f, dtype='>u1', count=list_size*image_hight*image_width)
    f.close()
    
    return np.double(train_x), np.double(train_y)
    
#plot a MNIST digit
def plot_digit(img_raw):
    #img_raw = np.uint8(img_raw)
    plt.figure(figsize=(5,5))
    im = plt.imshow(np.reshape(img_raw,(28,28)), cmap=cm.gray_r,interpolation='none')
    plt.colorbar(im, fraction=0.046, pad=0.04)
    
