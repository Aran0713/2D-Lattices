#!/usr/bin/env python2
# -*- coding: utf-8 -*-
######### Sqaure  ##########

import matplotlib.pyplot as plt 
import numpy as np

x = np.empty([9])
y = np.empty([9])

a1 = ( [2.0,0.0] )
a2 = ( [0.0,2.0] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) 
        y[i+j] = j*float(a2[1]) 


plt.plot(x, y, 'o')
plt.arrow(0,0, 0,a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("a1", xy = (0.5*a1[0], 0.1))
plt.annotate("a2", xy = (0.1, 0.5*a2[1]))

plt.title("2D Square Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.show()

######### Reciprocal ###########

x = np.empty([9])
y = np.empty([9])

a1 = ( [np.pi,0.0] )
a2 = ( [0.0, np.pi] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) 
        y[i+j] = j*float(a2[1]) 

plt.plot(x, y, 'o')
plt.arrow(0,0, 0,a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("b1", xy = (0.5*a1[0], 0.1))
plt.annotate("b2", xy = (0.1, 0.5*a2[1]))

plt.title("Reciprocal of 2D Square Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.show()

######### Rectangular  ##########

import matplotlib.pyplot as plt 
import numpy as np

x = np.empty([9])
y = np.empty([9])

a1 = ( [2.0,0.0] )
a2 = ( [0.0,3.0] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) 
        y[i+j] = j*float(a2[1]) 


plt.plot(x, y, 'o')
plt.arrow(0,0, 0,a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("a1", xy = (0.5*a1[0], 0.1))
plt.annotate("a2", xy = (0.1, 0.5*a2[1]))

plt.title("2D Rectangular Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.show()

######### Reciprocal ###########

x = np.empty([9])
y = np.empty([9])

a1 = ( [np.pi,0.0] )
a2 = ( [0.0, 2*np.pi / 3] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) 
        y[i+j] = j*float(a2[1]) 


plt.plot(x, y, 'o')
plt.arrow(0,0, 0,a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("b1", xy = (0.5*a1[0], 0.1))
plt.annotate("b2", xy = (0.1, 0.5*a2[1]))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Reciprocal of 2D Rectangular Lattice")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.show()

######### Oblique  ##########

x = np.empty([9])
y = np.empty([9])

a1 = ( [2.0,0.0] )
a2 = ( [1.5,3.0*np.sqrt(3)/2] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) + j*float(a2[0]) 
        y[i+j] = j*float(a2[1]) 


plt.plot(x, y, 'o')
plt.arrow(0,0, a2[0],a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("a1", xy = (0.5*a1[0], 0.1))
plt.annotate("a2", xy = (0.1, 0.5*a2[1]))

plt.title("2D Oblique Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.show()

######### Reciprocal ###########

x = np.empty([9])
y = np.empty([9])

a1 = ( [ 1.0 *np.pi, -1/np.sqrt(3) ] )
a2 = ( [ 0.0, (4*np.pi) / (3*np.sqrt(3)) ] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) + j*float(a2[0]) 
        y[i+j] = j*float(a2[1]) + i*float(a1[1])


plt.plot(x, y, 'o')
plt.arrow(0,0, a2[0],a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],-a1[1] - a2[1] , shape = 'left')

plt.annotate("b1", xy = (0.5*a1[0], 0.1))
plt.annotate("b2", xy = (0.1, 0.5*a2[1]))

plt.title("Reciprocal of 2D Oblique Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-2, 10)
plt.ylim(-7, 10)
plt.show()

######### Hexagonal  ##########

x = np.empty([9])
y = np.empty([9])

a1 = ( [2.0,0.0] )
a2 = ( [-1.0, np.sqrt(3)] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) + j*float(a2[0]) 
        y[i+j] = j*float(a2[1]) 


plt.plot(x, y, 'o')
plt.arrow(0,0, a2[0],a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("a1", xy = (0.5*a1[0], 0.1))
plt.annotate("a2", xy = (0.1, 0.5*a2[1]))

plt.title("2D Hexagonal Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-5, 7)
plt.ylim(-2, 7)
plt.show()

######### Reciprocal ###########

x = np.empty([9])
y = np.empty([9])

a1 = ( [ np.pi, np.pi / np.sqrt(3) ] )
a2 = ( [ 0.0, 2*np.pi / np.sqrt(3) ] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) + j*float(a2[0]) 
        y[i+j] = j*float(a2[1]) + i*float(a1[1])


plt.plot(x, y, 'o')
plt.arrow(0,0, a2[0],a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],a1[1] + a2[1] , shape = 'left')

plt.annotate("b1", xy = (0.5*a1[0], 0.1))
plt.annotate("b2", xy = (0.1, 0.5*a2[1]))

plt.title("Reciprocal of 2D Hexagonal Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-5, 10)
plt.ylim(-5, 25)
plt.show()

######### Centered Rectangular  ##########

x = np.empty([13])
y = np.empty([13])

a1 = ( [2.0,0.0] )
a2 = ( [0.0, 3.0] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) + j*float(a2[0]) 
        y[i+j] = j*float(a2[1]) 
        

for i in range(0, 4, 2):
    for j in range(0,2):
        x[9 + i + j] = (a1[0] / 2.0) + (1.0 * j * a1[0])
        y[9 + i + j] = (a2[1] / 2.0) + (1.0 * i * a2[1] / 2.0)
        

plt.plot(x, y, 'o')
plt.arrow(0,0, a2[0],a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],0 , shape = 'left')

plt.annotate("a1", xy = (0.5*a1[0], 0.1))
plt.annotate("a2", xy = (0.1, 0.5*a2[1]))

plt.title("2D Centered Rectangular Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.show()

######### Reciprocal ###########

x = np.empty([13])
y = np.empty([13])

a1 = ( [ np.pi, 0.0 ] )
a2 = ( [ 0.0, 2*np.pi/ 3.0 ] )

for i in range(0, 9, 3):
    for j in range(0, 3):
        x[i+j] = (1.0 * i/3) * (float(a1[0])) + j*float(a2[0]) 
        y[i+j] = j*float(a2[1]) + i*float(a1[1])
        
for i in range(0, 4, 2):
    for j in range(0,2):
        x[9 + i + j] = (a1[0] / 2.0) + (1.0 * j * a1[0])
        y[9 + i + j] = (a2[1] / 2.0) + (1.0 * i * a2[1] / 2.0)


plt.plot(x, y, 'o')
plt.arrow(0,0, a2[0],a2[1] , shape = 'left')
plt.arrow(0,0, a1[0],a1[1] , shape = 'left')

plt.annotate("b1", xy = (0.5*a1[0], 0.1))
plt.annotate("b2", xy = (0.1, 0.5*a2[1]))

plt.title("Reciprocal of 2D Centered Rectangular Lattice")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.show()
