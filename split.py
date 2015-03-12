from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_implicit(fn, bbox=(-2.5,2.5)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100) # resolution of the contour
    B = np.linspace(xmin, xmax, 100) # number of slices
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted
    print B
    for z in B: # plot contours in the XY plane
        X,Y = A1,A2
        Z = fn(X,Y,B)
        # print Z
        cset = ax.plot_surface(X, Y, Z)
        # [z] defines the only level to plot for this contour for this value of z
        break
    # for y in B: # plot contours in the XZ plane
    #     X,Z = A1,A2
    #     Y = fn(X,y,Z)
    #     cset = ax.plot_surface(X, Y+y, Z)

    # for x in B: # plot contours in the YZ plane
    #     Y,Z = A1,A2
    #     X = fn(x,Y,Z)
    #     cset = ax.plot_surface(X+x, Y, Z)

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)

    plt.show()

def goursat_tangle(x,y,z):
    # a,b,c = 0.0,-5.0,11.8
    # print type(x)
    return x**2+y
    # return x**4+y**4+z**4+a*(x**2+y**2+z**2)**2+b*(x**2+y**2+z**2)+c

print goursat_tangle
plot_implicit(goursat_tangle)