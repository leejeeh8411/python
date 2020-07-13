import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('D:/1.jpg', cv.IMREAD_COLOR)
cv.imshow('img', img)
a = np.array([1,2,3])
print(a)
b = 10
c = 50
d = b + c
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)
plt.show()
print('hello')
print('hello2')