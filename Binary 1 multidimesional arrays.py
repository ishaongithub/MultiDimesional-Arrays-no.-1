# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:38:21 2022

@author: ramak
"""

import matplotlib.pyplot as plt

data = [[1,1,1,1,1,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,1,0,0,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,1,1,0,1,1,1],
        [1,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1]]

plt.imshow(data, cmap='Blues')

plt.show()
        