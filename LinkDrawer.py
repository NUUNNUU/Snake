import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

from math import cos
from math import sin


def link_drawer(link_position):
    """Plots one link on the screen.
    
    Parameters
    ----------
    link_position : np.ndarray of size (6, 1)
        link_position (x, y, z, alpha, beta, gamma)
        Angle of each link is defined as extrinsic z-x-z euler angle
    """

    link_coords = link_position[0:3]  # (x, y, z) size (3, 1)
    link_angles = link_position[3:6]  # (alpha, beta, gamma) size (3, 1)

    a = link_angles[0]  # alpha
    b = link_angles[1]  # beta
    c = link_angles[2]  # gamma

    # set rotation matrix according to extrinsic z-x-z Euler angle (w.r.t. global coordinate)
    link_rotation_matrix = np.zeros((3, 3))

    link_rotation_matrix[0, 0] = cos(a) * cos(c) - cos(b) * sin(a) * sin(c)
    link_rotation_matrix[0, 1] = - cos(a) * sin(c) - cos(b) * cos(c) * sin(a)
    link_rotation_matrix[0, 2] = sin(a) * sin(b)

    link_rotation_matrix[1, 0] = cos(c) * sin(a) + cos(a) * cos(b) * sin(c)
    link_rotation_matrix[1, 1] = cos(a) * cos(b) * cos(c) - sin(a) * sin(c)
    link_rotation_matrix[1, 2] = - cos(a) * sin(b)

    link_rotation_matrix[2, 0] = sin(b) * sin(c)
    link_rotation_matrix[2, 1] = cos(c) * sin(b)
    link_rotation_matrix[2, 2] = cos(b)

    left_end = np.array([[0, 1, 0]]).T  # link's left end point
    right_end = np.array([[0, -1, 0]]).T  # link's right end point
    norm_vector = np.array([[1, 0, 0]]).T  # link's normal vector (a.k.a. front normal vector)

    left_end_rotated = np.dot(link_rotation_matrix, left_end)
    right_end_rotated = np.dot(link_rotation_matrix, right_end)
    norm_rotated = np.dot(link_rotation_matrix, norm_vector)
    
    # vectors which are created to plot the link
    left_repr_vector = link_coords + left_end_rotated
    right_repr_vector = link_coords + right_end_rotated
    norm_repr_vector = np.vstack((link_coords, norm_rotated))
    
    # 3D plotting
    X_line, Y_line, Z_line = zip(left_repr_vector.flatten(), right_repr_vector.flatten())
    X, Y, Z, U, V, W = zip(norm_repr_vector)

    ax.plot3D(X_line, Y_line, Z_line, c='red')
    ax.quiver(X, Y, Z, U, V, W)


if __name__ == "__main__":
    # set link positions
    link_pos = np.array([[1, 3, 2, 0.3, 0.6, 0.8]]).T
    link_pos_2 = np.array([[2, 3, 4, 0.5, 0.3, 0.1]]).T

    # set figure and axis
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # axis labels and limits
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-1, 5])
    ax.set_ylim([-1, 5])
    ax.set_zlim([-1, 5])

    # draw links as many as you want
    link_drawer(link_pos)
    link_drawer(link_pos_2)

    # show the figure
    plt.show()