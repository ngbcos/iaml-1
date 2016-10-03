import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_countour(x,y,z):
    # define grid.
    xi = np.linspace(-2.1, 2.1, 100)
    yi = np.linspace(-2.1, 2.1, 100)
    ## grid the data.

    #UNCOMMENT THIS LINE
    #zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

    levels = [0.2, 0.4, 0.6, 0.8, 1.0]
    # contour the gridded data, plotting dots at the randomly spaced data points.
    CS = plt.contour(xi,yi,zi,len(levels),linewidths=0.5,colors='k', levels=levels)
    #CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet)
    CS = plt.contourf(xi,yi,zi,len(levels),cmap=cm.Greys_r, levels=levels)
    plt.colorbar() # draw colorbar
    # plot data points.
    # plt.scatter(x, y, marker='o', c='b', s=5)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.title('griddata test (%d points)' % npts)
    plt.show()


# make up some randomly distributed data
#seed(1234)
#npts = 1000
#x = uniform(-2, 2, npts)
#y = uniform(-2, 2, npts)
#z = gauss(x, y, Sigma=np.asarray([[1.,.5],[0.5,1.]]), mu=np.asarray([0.,0.]))
#plot_countour(x, y, z)

X,Y=np.meshgrid(np.linspace(-1,1,10),np.linspace(-1,1,10));
mu,sigma=0,1; #suppose that mux=muy=mu=0 and sigmax=sigmay=sigma
G=np.exp(-((X-mu)**2+(Y-mu)**2)/2.0*sigma**2)
print G
fig=plt.figure();
ax=fig.add_subplot(111,projection='3d')
surf=ax.plot_surface(X,Y,G,'r')
plt.show()