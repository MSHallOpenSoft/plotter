from __future__ import unicode_literals
import sympyParsing
import sys
import sympy
import time
import os
import random
import sympyPlot_implicit
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

class customLineEdit(QtGui.QLineEdit):
    def __init__(self,parent=None):
        self.parent=parent
        QtGui.QLineEdit.__init__(self)
        #self.text=""
        self.returnPressed.connect(self.sg_returnPressed)

    def sg_returnPressed(self):
        print("wooooo")
        print(self.text())
        #self.parent.
        txt=sympyParsing.exprLatex(str(self.text()))
        #self.parent.sc.fig.suptitle('$'+txt+'$', x=0.0, y=0.5,  horizontalalignment='left', verticalalignment='center')
        #self.parent.sc.update_figure()
        #x_arr,y_arr=sympyParsing.exprParseSolve(str(self.text()),1,5)
        #print(y_arr)
        #y_arr=[i[0] for i in y_arr]
        changed=sympyParsing.symStr(str(self.text()))
        print(changed)
        foo=sympy.sympify(changed)
        sympy_p1 = sympyPlot_implicit.plot_implicit(foo,show=False,ax=self.parent.sc.ax)
        print(self.parent.sc.ax.get_children())
        sympy_p1.plotNow()
        print(self.parent.sc.ax.get_children())
        #print(sympy_p1._backend)
        #self.parent.sc.ax.add_collection(sympy_p1._backend.ax.get_children()[2])
        #self.parent.sc.ax.plot(x_arr,y_arr,'r')
        self.parent.sc.update_figure()


class MplPlot3dCanvas_2(FigureCanvas):
  def __init__(self,parent=None):
      self.surfs = [] # [{"xx":,"yy:","val:"}]
      self.fig= plt.figure()
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
  def update_figure(self):
      #print(time.localtime())
      #self.ax.dist+=1
      #self.ax.azim=(self.ax.azim+5)%360
      self.draw()
  def zoom_factory(self,base_scale = 2.):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        print(cur_xlim,cur_ylim)
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
            print event.button
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
#      for plt in self.plots:
              ## del plt
          #self.ax.collections.remove(plt)
          #self.plots = []
          #for surf in self.surfs:
              #plt = self.ax.plot_surface(surf["xx"], surf["yy"], surf["val"], rstride=5, cstride=5, cmap=cm.jet, linewidth=1, antialiased=True)
      #        self.plots.append(plt)
          #self.draw()


#class MplPlot3dView(QWidget):
    #def __init__(self, parent = None):
       #super(MplPlot3dView, self).__init__(parent)
       #self.canvas = MplPlot3dCanvas()
       #self.toolbar = NavigationToolbar(self.canvas, self.canvas)
       #self.vbox = QVBoxLayout()
       #self.vbox.addWidget(self.canvas)
       #self.vbox.addWidget(self.toolbar)
       #self.setLayout(self.vbox)
#       self.to_update = False

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
        sc = MplPlot3dCanvas_2(self.main_widget)
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
