from __future__ import unicode_literals
import sympyParsing
import sys
import sympy
import copy
import time
import os
import random
import sympyPlot_implicit
import sympyPlot
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends import qt4_compat
use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

progname = os.path.basename(sys.argv[0])
progversion = "0.1"
x = sympy.symbols('x')
y = sympy.symbols('y')
u = sympy.symbols('u')
v = sympy.symbols('v')

class customLineEdit(QtGui.QLineEdit):
    """
    A simple, custom input taking class to test when this module is run.
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
        print("wooooo")
        print(self.text())
        #self.parent.
        #txt=sympyParsing.exprLatex(str(self.text()))
        #self.parent.sc.fig.suptitle('$'+txt+'$', x=0.0, y=0.5,  horizontalalignment='left', verticalalignment='center')
        #self.parent.sc.update_figure()
        #x_arr,y_arr=sympyParsing.exprParseSolve(str(self.text()),1,5)
        #print(y_arr)
        #y_arr=[i[0] for i in y_arr]
        sympy_p1 = self.parent.sc.plot_2d_implicit(str(self.text()))
        #print(self.parent.sc.ax.get_children())


class MplPlot2dCanvas(FigureCanvas):
  def __init__(self,parent=None):
      self.parent=parent
      self.dic_plot={} #storing contour
      self.dic_parameter={} #storing parameters
      self.dic_calculated={} #storing calculated values
      self.dic_index={} #storing calculated values
      self.count=0
      self.plotobj={}
      self.surfs = [] # [{"xx":,"yy:","val:"}]
      self.fig= plt.figure()
      self.plotted=0
      #self.fig = Figure()
      self.fig.suptitle("this is  the  figure  title",  fontsize=12)
      FigureCanvas.__init__(self, self.fig)
      FigureCanvas.setSizePolicy(self,
          QtGui.QSizePolicy.Expanding,
          QtGui.QSizePolicy.Expanding)
      FigureCanvas.updateGeometry(self)
      #self.toolbar = NavigationToolbar(self, parent)
      #self.ax = AxesDD(self.fig) # Canvas figure must be created for mouse rotation
      self.ax = self.fig.add_subplot(111)
      #self.ax2 = self.fig.add_subplot(111)
      self.ax.set_xlabel('row (m CCD)')
      self.ax.set_ylabel('col (m CCD)')
      #self.ax.set_zlabel('Phi (m)')
      self.format_coord_org = self.ax.format_coord
      self.ax.format_coord = self.report_pixel
      f=self.zoom_factory(1.2)
      #self.ax.view_init(elev=45,azim=45)
      #self.ax.dist=20
        # Clear figure
      #self.fig.clear()
        # Set figure title
      #self.fig.suptitle('$\\int \\sqrt{\\frac{1}{x}}\\, dx$', x=0.0, y=0.5,  horizontalalignment='left', verticalalignment='center')

      #timer = QtCore.QTimer(self)
      #timer.timeout.connect(self.update_figure)
      #timer.start(100)
  def remove_from_3d(self,keystr):
      if keystr in self.parent.mayavi_widget.visualization.dic_contour:
        self.parent.mayavi_widget.visualization.dic_contour[keystr].remove()
        self.parent.mayavi_widget.visualization.dic_outline[keystr].remove()
        #self.parent.mayavi_widget.visualization.update_plot()
        self.parent.mayavi_widget.visualization.dic_parameter.pop(keystr,None)
        self.parent.mayavi_widget.visualization.dic_contour.pop(keystr,None)
        self.parent.mayavi_widget.visualization.dic_calculated.pop(keystr,None)
        self.parent.mayavi_widget.visualization.dic_outline.pop(keystr,None)
        print(self.parent.mayavi_widget)

  def plot_2d_parametric(self,curTab=0,curPlot=1,**kwargs):
      len_arguments=len(kwargs)
      print(kwargs)
      keystr='plt'+str(curPlot)
      self.remove_from_3d('tab'+str(curTab)+keystr)
      u_start=kwargs.get('u_start',(-5))
      eqn=kwargs.get('eqn',('x=u','y=u'))
      color=kwargs.get('color',(0.5,0.8,0.5))
      print(eqn)
      keystr='plt'+str(curPlot)
      eqn1=eqn[0]
      eqn2=eqn[1]
      line_width=kwargs.get('line_width',0.2)
      u_end=kwargs.get('u_end', 5)
      v_start=kwargs.get('v_start',-5)
      v_end=kwargs.get('v_end',5)
      expr1 = sympy.sympify((eqn1[4:]))
      expr1 = sympy.simplify(expr1)
      expr1 = sympy.radsimp(expr1)
      num_dum=sympy.fraction(expr1)
      expr1=num_dum[0]

      expr2 = sympy.sympify((eqn2[4:]))
      expr2 = sympy.simplify(expr2)
      expr2 = sympy.radsimp(expr2)
      num_dum=sympy.fraction(expr2)
      expr2=num_dum[0]
      print(expr1,expr2)
      color=kwargs.get('color',(0.5,0.8,0.5))
      if(keystr in self.dic_parameter):
        shared_items = set(kwargs.items()) & set(self.dic_parameter[keystr].items())
        print(shared_items)
        len_shared = len(shared_items)
        if len_shared == len_arguments:
            print("no change")
            return
      self.ax.cla()
      sympy_p1 = sympyPlot.plot_parametric(expr1,expr2,(u,u_start,u_end),(v,v_start,v_end),ax=self.ax,fig=self.fig,show=False,line_color=color)
      if(len(self.dic_plot)==0):
        self.plotobj=sympy_p1
      else:
        print("goooiiiooooooooooooooo")
        if keystr in self.dic_index:
          print("hooooiioooooooooooo")
          self.plotobj._series.pop(self.dic_index[keystr])
        self.plotobj.extend(sympy_p1)

      self.dic_plot[keystr]=sympy_p1
      self.dic_index[keystr]=len(self.plotobj._series)-1
      self.dic_parameter[keystr]=kwargs
      #print(self.plotobj._series)
      self.plotobj.plotNow()
      self.update_figure()

  def plot_2d_implicit(self,curTab=0,curPlot=1,**kwargs):
      """
        Using the same logic as ``plot_implicit_3d`` for plotting multiple graphs efficiently.
        We are using two dictionaries, ``dic_index`` and ``dic_parameter`` to store the position
        of a particular plot in the ``_series`` attribute of the plot returned by ``plot_implicit``.
        The dictionaries are indexed by ``keystr`` which is of the form ``plt1``. If the key already exists,
        we check if there is any change in the parameters using ``dic_parameter``.
        If there is a change we remove the plot from the ``_series`` and put the new plot and update the ``dic_index``.
        ``dic_index`` stores an index of a plot in the ``_series`` list.
      """
      len_arguments=len(kwargs)
      print(kwargs)
      keystr='plt'+str(curPlot)
      self.remove_from_3d('tab'+str(curTab)+keystr)
      color=kwargs.get('color',(0.5,0.8,0.5))
      x_start=kwargs.get('x_start',(-5))
      eqn=kwargs.get('eqn',"x+y=0")
      line_width=kwargs.get('line_width',0.2)
      x_end=kwargs.get('x_end', 5)
      y_start=kwargs.get('y_start',-5)
      y_end=kwargs.get('y_end',5)
      expr = sympy.sympify(sympyParsing.symStr(eqn))
      expr = sympy.simplify(expr)
      expr = sympy.radsimp(expr)
      num_dum=sympy.fraction(expr)
      expr=num_dum[0]
      shared_items=[]
      if(keystr in self.dic_parameter):
        shared_items = set(kwargs.items()) & set(self.dic_parameter[keystr].items())
        print(shared_items)
        len_shared = len(shared_items)
        if len_shared == len_arguments:
            print("no change")
            return
      self.ax.cla()
      print("adsflasdfasdf")
      print(expr)
      sympy_p1 = sympyPlot_implicit.plot_implicit(expr,show=False,ax=self.ax,fig=self.fig,x_var=(x,x_start,x_end),y_var=(y,y_start,y_end),line_color=color,linewidth=line_width)
      if(len(self.dic_plot)==0):
        self.plotobj=sympy_p1
      else:
        print("goooiiiooooooooooooooo")
        if keystr in self.dic_index:
          print("hooooiioooooooooooo")
          self.plotobj._series.pop(self.dic_index[keystr])
        self.plotobj.extend(sympy_p1)

      self.dic_plot[keystr]=sympy_p1
      self.dic_index[keystr]=len(self.plotobj._series)-1
      self.dic_parameter[keystr]=kwargs
      #print(self.plotobj._series)
      self.plotobj.plotNow()
      self.update_figure()
      
  def update_figure(self):
      self.draw()

  def zoom_factory(self,base_scale = 2.):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        #print(cur_xlim,cur_ylim)
        xdata = event.xdata # get event x location
        ydata = event.ydata # get event y location
        x_left = xdata - cur_xlim[0]
        x_right = cur_xlim[1] - xdata
        y_top = ydata - cur_ylim[0]
        y_bottom = cur_ylim[1] - ydata
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            #print event.button
        # set new limits
        self.ax.set_xlim([xdata - x_left*scale_factor, xdata + x_right*scale_factor])
        self.ax.set_ylim([ydata - y_top*scale_factor, ydata + y_bottom*scale_factor])
        #self.ax.set_xlim([xdata - cur_xrange*scale_factor,
                     #xdata + cur_xrange*scale_factor])
        #self.ax.set_ylim([ydata - cur_yrange*scale_factor,
        #             ydata + cur_yrange*scale_factor])
        #plt.draw() # force re-draw
        self.update_figure()

    #self.fig = ax.get_figure() # get the figure of interest
    # attach the call back
    self.fig.canvas.mpl_connect('scroll_event',zoom_fun)

    #return the function
    return zoom_fun


  def report_pixel(self, xd, yd):
      s = self.format_coord_org(xd, yd)
      s = s.replace(",", " ")
      return s

  def update_view(self):
      print("boo")
      self.draw()


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
        sc = MplPlot2dCanvas(self.main_widget)
        l.addWidget(sc)
        l.addWidget(textbox)
        self.sc=sc
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
        #self.sc.update_view()
        #QtGui.QMessageBox.about(self, "About",
#"""embedding_in_qt4.py example
#Copyright 2005 Florent Rougon, 2006 Darren Dale

#This program is a simple example of a Qt4 application embedding matplotlib
#canvases.

#It may be used and modified with no restriction; raw copies as well as
#modified versions may be distributed without limitation."""
#)

if __name__=='__main__':
  qApp = QtGui.QApplication(sys.argv)
  aw = ApplicationWindow()
  aw.setWindowTitle("%s" % progname)
  aw.show()
	#for ii in xrange(0,360,1):
		#aw.sc.ax.view_init(elev=10., azim=ii)
  sys.exit(qApp.exec_())
  qApp.exec_()
