import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
vertices = np.empty((1,8,3))
def soln(i,j):
   return int((i+(2**0.5)*j)/(3**0.5))
#generating the interger vertices of the cubes that are cut by the plane
for i in range(0,10): #iterating through x axis
   for j in range(0,10):#iterating through y axis
    do = soln(i,j) #z value of the bottom square of cube
    up = do+1 #z value of the top square of the cube
    new1 = [[[i, j, do], [i+1, j, do], [i+1, j+1, do], [i, j+1, do],  # Bottom square
        [i, j, up], [i+1, j, up], [i+1, j+1, up], [i, j+1, up] ]]    #top square
    
    new2 = [[[i, j-1, do], [i+1, j-1, do], [i+1, j, do], [i, j, do],  # Bottom square
        [i, j-1, up], [i+1, j-1, up], [i+1, j, up], [i, j, up] ]]      #top square
    
    new3 = [[[i-1, j, do], [i, j, do], [i, j+1, do], [i-1, j+1, do],  # Bottom square
        [i-1, j, up], [i, j, up], [i, j+1, up], [i-1, j+1, up] ]]      #top square
    
    new4 = [[[i-1, j-1, do], [i, j-1, do], [i, j, do], [i-1, j, do],  # Bottom square
        [i-1, j-1, up], [i, j-1, up], [i, j, up], [i-1, j, up] ]]       #top square
    vertices=np.append(vertices,new1,axis =0)
    vertices=np.append(vertices,new2,axis =0)
    vertices=np.append(vertices,new3,axis =0)
    vertices=np.append(vertices,new4,axis =0)
#creating faces
faces = []
for square in vertices:
    faces.append([[square[0], square[1], square[2],square[3]],  # Bottom face
    [square[4], square[5], square[6], square[7]],  # Top face
    [square[0], square[1], square[5], square[4]],  # Side face 1
    [square[1], square[2], square[6], square[5]],  # Side face 2
    [square[2], square[3], square[7], square[6]],  # Side face 3
    [square[3], square[0], square[4], square[7]] ])


#message = learner.sol(i,j)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


"""x = [i for i in range(0,10,1)]
y = [i for i in range(0,10,1)]
x, y = np.meshgrid(x, y)
# Calculate z values using the quadratic equation
z = ((x+(2**0.5)*y)/(3**0.5))
ax.plot_surface(x, y, z,color ='y' ,alpha=0.5)"""


# Create a Poly3DCollection and add faces to it
for val in faces:
  face_colors = ['green', 'green', 'brown', 'brown', 'brown', 'brown']
  cube = Poly3DCollection(val, facecolors=face_colors, edgecolors='k')

# Add the collection to the plot
  ax.add_collection3d(cube)





# Customize plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

plt.show()

