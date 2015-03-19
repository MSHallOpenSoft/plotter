# First, and before importing any Enthought packages, set the ETS_TOOLKIT
# environment variable to qt4, to tell Traits that we will use Qt.
import os
os.environ['ETS_TOOLKIT'] = 'qt4'
# By default, the PySide binding will be used. If you want the PyQt bindings
# to be used, you need to set the QT_API environment variable to 'pyqt'
#os.environ['QT_API'] = 'pyqt'

# To be able to use PySide or PyQt4 and not run in conflicts with traits,
# we need to import QtGui and QtCore from pyface.qt
#use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE
#if use_pyside:
    #from PySide import QtGui, QtCore
#else:

# Alternatively, you can bypass this line, but you need to make sure that
# the following lines are executed before the import of PyQT:
#   import sip
#   sip.setapi('QString', 2)
import sys
import sympyParsing
from sympy.plotting.experimental_lambdify import (vectorized_lambdify)
from sympy.utilities.lambdify import lambdify

import numpy as np
#import mayavi_3d
from mayavi import mlab
from pyface.qt import QtGui, QtCore
from sympy import symbols,sympify,latex,simplify,fraction,radsimp

from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from tvtk.pyface.api import Scene
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, \
        SceneEditor
x = symbols('x')
y = symbols('y')
z = symbols('z')



class customLineEdit(QtGui.QLineEdit):
    def __init__(self,parent=None):
        self.parent=parent
        QtGui.QLineEdit.__init__(self)
        #self.text=""
        self.returnPressed.connect(self.sg_returnPressed)

    def sg_returnPressed(self):
        self.parent.mayavi_widget.visualization.mayavi_implicit_3d(str(self.text()))


################################################################################
#The actual visualization6
class Visualization(HasTraits):
    #def __init__(self, parent=None):
    scene = Instance(MlabSceneModel, ())
      # the layout of the dialog screated
      
    def mayavi_implicit_3d(self,str_expr,x_start=-10,x_end=10,no_x_points=100,y_start=-10,y_end=10,no_y_points=100,z_start=-10,z_end=10,no_z_points=100):
      expr = sympify(sympyParsing.symStr(str_expr))
      print(expr)
      expr = simplify(expr)
      print(expr)
      expr = radsimp(expr)
      print(expr)
      num_dum=fraction(expr)
      print(num_dum)
      expr=num_dum[0]
      print(expr)
      #no_x_points=2
      #no_y_points=2
      #no_z_points=2
      #print(sympyParsing.symStr(str_expr))
      no_x_points=complex(0,no_x_points)
      no_y_points=complex(0,no_y_points)
      no_z_points=complex(0,no_z_points)
      points_size=[no_x_points,no_y_points,no_z_points]

      X,Y,Z=np.ogrid[x_start:x_end:no_x_points , y_start:y_end:no_y_points , z_start:z_end:no_z_points]
      #print X
      #print Y
      #print Z
      f = vectorized_lambdify((x,y,z), expr)
      #print(f(0,1.5,10000))
      foo=f(X,Y,Z)
      #print(foo)
      print(foo.shape)
      axis=[]
      s=foo.shape
      doo=foo
      #if len(foo.shape)==3:
          #for i in range(0,len(points_size)):
              #if(s[i]!=points_size[i].imag):
                  #axis.append(i)
          #if s[0]!=no_x_points.imag:
              #axis.append(0)
          #if s[1]!=no_y_points.imag:
              #axis.append(1)
          #if s[2]!=no_z_points.imag:
              #axis.append(2)
          #print(axis)
          #for i in range(0,len(axis)):
      #        doo=np.repeat(doo,points_size[i].imag,axis[i])
      print(doo.shape)
      contour3d=self.scene.mlab.contour3d(doo, contours = [0])
      self.scene.mlab.outline(contour3d, color=(.7, .7, .7))
      self.update_plot()




    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.

        # We can do normal mlab calls on the embedded scene.
        # self.scene.mlab.test_points3d()
        #print(txt)
        #if(txt!=None):
          #self.mayavi_implicit_3d(txt)
          #print(txt)
        #else:
          ##self.mayavi_implicit_3d('x+y+z=1')
        #  self.scene.mlab.test_points3d()
        #x, y, z = np.ogrid[-3:3:100j, -3:3:100j, -3:3:100j]
        #F = x**2/3**2 + y**2/2**2 + z**2/4**2 - 1
        #self.scene.mlab.contour3d(F, contours = [0])
        self.scene.mlab.points3d([0],[0],[0],line_width=0.05,mode='point')
        # self.scene.mlab.axes(color=(.7, .7, .7))
        self.scene.mlab.orientation_axes()
        #self.scene.mlab.outline()
        #xx = yy = zz = np.arange(-10,10,1)
        #xy = xz = yx = yz = zx = zy = np.zeros_like(xx)    
        #self.scene.mlab.plot3d(yx,yy+0.1,yz,line_width=0.01,tube_radius=0.01)
        #self.scene.mlab.plot3d(zx,zy+0.1,zz,line_width=0.01,tube_radius=0.01)
        #self.scene.mlab.plot3d(xx,xy+0.1,xz,line_width=0.01,tube_radius=0.01)


    view = View(Item('scene', editor=SceneEditor(scene_class=Scene),
                     height=250, width=300, show_label=False),
                resizable=True # We need this to resize with the parent widget
                )


    


################################################################################
# The QWidget containing the visualization, this is pure PyQt4 code.
class MayaviQWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.visualization = Visualization()

        # If you want to debug, beware that you need to remove the Qt
        # input hook.
        #QtCore.pyqtRemoveInputHook()
        #import pdb ; pdb.set_trace()
        #QtCore.pyqtRestoreInputHook()

        # The edit_traits call will generate the widget to embed.
        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QVBoxLayout(self.main_widget)
        textbox=customLineEdit(self)
        self.mayavi_widget = MayaviQWidget(self.main_widget)
        l.addWidget(self.mayavi_widget)
        l.addWidget(textbox)
        #self.sc=sc
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()
    def animate(i):
        self.ac.ax.view_init(elev=10., azim=i)

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        # Animate
        print("woo")


if __name__ == "__main__":
    # Don't create a new QApplication, it would unhook the Events
    # set by Traits on the existing QApplication. Simply use the
    # '.instance()' method to retrieve the existing one.
    qApp = QtGui.QApplication.instance()
    aw = ApplicationWindow()
    #aw.setWindowTitle("%s" % progname)
    aw.show()
    #for ii in xrange(0,360,1):
            #aw.sc.ax.view_init(elev=10., azim=ii)
    sys.exit(qApp.exec_())
    qApp.exec_()
