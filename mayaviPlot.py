# First, and before importing any Enthought packages, set the ETS_TOOLKIT
# environment variable to qt4, to tell Traits that we will use Qt.
import os
os.environ['ETS_TOOLKIT'] = 'qt4'
# By default, the PySide binding will be used. If you want the PyQt bindings
# to be used, you need to set the QT_API environment variable to 'pyqt'
os.environ['QT_API'] = 'pyqt'

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
    """A simple, custom input taking class to test when this module is run.
    The input is taken from an object of this to give it to mayavi and test.
    This is not used in the actual GUI. Used to just test this module separately
    by running this file. The graph is plotted when the enter key is pressed in
    this input box. It calls the ``mayavi_implicit_3d`` method from the ``Visualization``
    class to draw the plot.
    """
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
    """Mayavi visualization class."""
    #def __init__(self, parent=None):
    scene = Instance(MlabSceneModel, ())
    dic_contour={} #storing contour
    dic_parameter={} #storing parameters
    dic_calculated={} #storing calculated values
    dic_outline={} #storing outline
    # the layout of the dialog screated
      
    def mayavi_implicit_3d(self,curTab=0,curPlot=1,**kwargs):
      """
      The main 3d plotting method. Uses sympy's ``simplify`` and ``rationalise`` methods
      to obtain the numerator and then plot it. This is done to avoid ``division by zero`` error. The behaviour
      with respect to asymptotes is as expected.
      Maintaining separate dictionaries ``dic_contour``,``dic_parameter``,``dic_calculated``,``dic_outline`` to store the
      ``contours``(plotted 3d object) , ``parameters``, ``outline`` respectively. Using key strings of the form ``tab1plt1`` with the
      use of the respective tab and plot identifiers for the dictionaries. When for the same plot a new input is
      given, we check the difference between the new and the currently plotted parameters, and if we needed the ``contour``
      is cacluclated again using ``numpy's ogrid`` method. This way for complex graphs, if parameters are changed which do not
      affect the actual plot (not characteristics like ``colour``, ``transparency`` etc. ), there is no recalculation taking place.

      If the dimension of the output given by ``numpy's ogrid`` method is not of the form (t,t,t) we manually change the numpy
      array using ``numpy's repeat`` method. This is used to plot 2d equations like ``x+y=0``,``x+z=0``,``z=0`` etc in 3d form.
      """
      donot_calculate=False
      len_arguments=len(kwargs)
      len_shared=0

      x_start=kwargs.get('x_start',(-5))
      eqn=kwargs.get('eqn',"x+y+z=0")
      line_width=kwargs.get('line_width',0.2)
      opacity=kwargs.get('opacity',1)
      x_end=kwargs.get('x_end', 5)
      y_start=kwargs.get('y_start',-5)
      y_end=kwargs.get('y_end',5)
      z_start=kwargs.get('z_start',-5)
      z_end=kwargs.get('z_end',5)

      no_x_points=kwargs.get('no_x_points',10)
      no_y_points=kwargs.get('no_y_points',10)
      no_z_points=kwargs.get('no_z_points',10)
      color=kwargs.get('color',(0.5,0.8,0.5))
      #print(self.dic_parameter)
      keystr="tab"+str(curTab)+"plt"+str(curPlot)
      shared_items=[]
      print("hooooo")
      if(keystr in self.dic_parameter):
          if self.dic_parameter[keystr]['eqn'] == kwargs['eqn']:
            print(kwargs)
            print(self.dic_parameter)
            shared_items = set(kwargs.items()) & set(self.dic_parameter[keystr].items())
            print(shared_items)
            len_shared = len(shared_items)
            if len_shared == len_arguments:
                print("no change")
                return
            donot_calculate = len_shared == len_arguments-1 and self.dic_parameter[keystr]['color'] != kwargs['color']

      self.dic_parameter[keystr]=kwargs
      print("shaaaaaaaaaare",len_shared)
      if(donot_calculate):
          doo=self.dic_calculated[keystr]
          print("not calculating")
      else:
          expr = sympify(sympyParsing.symStr(eqn))
          expr = simplify(expr)
          expr = radsimp(expr)
          num_dum=fraction(expr)
          expr=num_dum[0]
          no_x_points=complex(0,no_x_points)
          no_y_points=complex(0,no_y_points)
          no_z_points=complex(0,no_z_points)
          points_size=[no_x_points,no_y_points,no_z_points]
          X,Y,Z=np.ogrid[x_start:x_end:no_x_points , y_start:y_end:no_y_points , z_start:z_end:no_z_points]
          f = vectorized_lambdify((x,y,z), expr)
          foo=f(X,Y,Z)
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
          self.dic_calculated[keystr]=doo

      if(keystr in self.dic_contour):
          self.dic_contour[keystr].remove()

      if(keystr in self.dic_outline):
          self.dic_outline[keystr].remove()
      self.dic_contour[keystr]=self.scene.mlab.contour3d(doo,color=color,line_width=line_width,opacity=opacity, contours = [0])
      self.dic_outline[keystr]=self.scene.mlab.outline(self.dic_contour[keystr], color=(.7, .7, .7))
      self.update_plot()
      #self.started=0

    @on_trait_change('scene.activated')
    def update_plot(self):
        """
         This function is called when the view is opened. We don't
         populate the scene when the view is not yet open, as some
         VTK features require a GLContext.
         We can do normal mlab calls on the embedded scene.
        """
        self.scene.mlab.points3d([0],[0],[0],line_width=0.05,mode='point')
        self.scene.mlab.orientation_axes()
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
class MayaviQWidget(QtGui.QWidget):
    """
        The QWidget containing the visualization, this is pure PyQt4 code.
    """ 
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
    """
      This class is used just to test this module by running this file. This is the Application
      window which is created when this file is run.
    """
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
