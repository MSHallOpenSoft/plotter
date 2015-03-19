# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sun Mar 15 00:12:39 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

#import mayaviPlot
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
#from plottingEquation_3d_explicit import MplPlot3dCanvas
#from imp_plottingEquation import MplPlot3dCanvas_2
from PyQt4.QtCore import Qt, SIGNAL
from function_2 import Ui_DockWidget
import numpy as np
#import matplotlib.pyplot as plotter
i=1
import sys, random  
from Thesidetab import mainFrame
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.expression_list=[]

    def addNewEquationEditor(self,layout,spacer):
        n = layout.count()
        layout.removeItem(layout.itemAt(n-1))
        dockWidgetContents = Exp_Form(self)
        self.expression_list.append(dockWidgetContents)
        layout.addWidget(dockWidgetContents)
        layout.addItem(spacer)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1160, 600)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"  text-align: center; \n"
"  \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
" QSlider::groove:horizontal {\n"
"     background: red;\n"
"     height: 15px;\n"
"     position: absolute; \n"
"     left: 4px; right: 4px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     height:20px;\n"
"     width: 10px;\n"
"     background: green;\n"
"     margin: -4px; \n"
" }\n"
"\n"
" QSlider::add-page:horizontal {\n"
"     background:rgb(255, 255, 127)\n"
" }\n"
"\n"
" QSlider::sub-page:horizontal {\n"
"     background: rgb(255, 170, 0);\n"
" }\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n" 
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QPushButton{\n"
"  position: relative;\n"
"  border:none;\n"
"  outline:none;\n"
"  background: #89669b;\n"
"  color: white;\n"
"  border-radius: 2px;\n"
"  padding: 6px 20px;\n"
"  font-size: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #745385;\n"
"  color: white;\n"
"  border-radius: 2px;\n"
"  font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #9d74b2;\n"
"  color: white;\n"
"  border-radius: 2px;\n"
"  font-size: 20px;\n"  
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_2.setStyleSheet(_fromUtf8("QFrame, QLabel, QToolTip {\n"
"    border: 0px solid green;\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 20, 121))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.toolButton_7 = QtGui.QToolButton(self.frame)
        self.toolButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.toolButton_7.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Add-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_5.addWidget(self.toolButton_7)
        self.toolButton_9 = QtGui.QToolButton(self.frame)
        self.toolButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.toolButton_9.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Minus-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon1)
        self.toolButton_9.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_5.addWidget(self.toolButton_9)
        self.toolButton_8 = QtGui.QToolButton(self.frame)
        self.toolButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.toolButton_8.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Folder-Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon2)
        self.toolButton_8.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_5.addWidget(self.toolButton_8)
        self.toolButton_6 = QtGui.QToolButton(self.frame)
        self.toolButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.toolButton_6.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon3)
        self.toolButton_6.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_5.addWidget(self.toolButton_6)
        self.toolButton_5 = QtGui.QToolButton(self.frame)
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.toolButton_5.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Save-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtGui.QTableWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #self.tableWidget.setResizeMode()
        self.header=self.tableWidget.horizontalHeader();
        self.header.setResizeMode(QHeaderView.Stretch);
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.pushButton_21 = QtGui.QPushButton(self.frame)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_5.addWidget(self.pushButton_21)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        '''self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, "2D Graph")
        self.tab.setVisible(False)'''
        #self.tab_2 = QtGui.QWidget()
        #self.tab_2.setObjectName(_fromUtf8("tab_2"))
        '''contents_2=QtGui.QWidget(self.tabWidget)
        layout_2= QtGui.QVBoxLayout(contents_2)
        widget_2 = QtGui.QWidget(self)
        sc_2=MplPlot3dCanvas_2(widget_2)
        layout_2.addWidget(sc_2)
        self.tabWidget.addTab(contents_2, "2D Graph")
        contents = QtGui.QWidget(self.tabWidget)
        layout = QtGui.QVBoxLayout(contents)
        widget_1 = QtGui.QWidget(self)
        self.mayavi_widget = MayaviQWidget(widget_1)
        layout.addWidget(self.mayavi_widget)'''
        self.tableWidget.setStyleSheet(_fromUtf8(".button {\n"
"  background: orange;\n"
"  outline: none;\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 0.25em;\n"
"  padding: 0.75em 2em;\n"
"  line-height: 1;\n"
"  box-shadow: 0 0 0.25em rgba(0,0,0,0.5);\n"
"  text-shadow: 0 0 0.25em rgba(0,0,0,0.5);\n"
"  font-size: 1.5rem;\n"
"}\n"
".button-white {\n"
"  background: white;\n"
"  color: orange;\n"
"}\n"
".button-round {\n"
"  border-radius: 100%;\n"
"  padding: 0.75em;\n"
"  width: 3em;\n"
"  height: 3em;\n"
"}\n"
".button-ripple {\n"
"  position: relative;\n"
"  overflow: hidden;\n"
"  transform: translate(0);\n"
"}\n"
".button-ripple_content {\n"
"  position: relative;\n"
"  z-index: 1;\n"
"}\n"
".button-ripple_ripples {\n"
"  position: absolute;\n"
"  top: 0;\n"
"  left: 0;\n"
"}\n"
".button-ripple_ripple{\n"
"  display: block;\n"
"  position: absolute;\n"
"  border-radius: 100%;\n"
"  width: 1em;\n"
"  height: 1em;\n"
"  margin: -0.5em 0 0 -0.5em;\n"
"  transform: scale(0);\n"
"\n"
"  top: 0;\n"
"  left: 0;\n"
"\n"
"  animation: ripple-animation 2s;\n"
"}\n"
"\n"
"@keyframes ripple-animation {\n"
"    from {\n"
"      transform: scale3d(1,1,1);\n"
"      opacity: 0.8;\n"
"    }\n"
"    to {\n"
"      transform: scale3d(100,100,1);\n"
"      opacity: 0;\n"
"    }\n"
"}\n"
"\n"
"/* Make things perty */\n"
"html {  height: 100%;}\n"
"body { font-family: \'Source Sans Pro\', Helvetica, Arial, sans-serif; background: url(http://www.jmchristensendesign.com/wp-content/themes/jmcdsn/images/intro_default-background.jpg); color: #fff; height: 100%; padding-top: 2em; text-align: center;}\n"
"h1, h2{ margin: 0; text-transform: uppercase;text-shadow: 0 0 0.5em black;}\n"
"h2 { font-weight: 300}\n"
"input { border: 1px solid #666; background: #333; color: #fff; padding: 0.5em; box-shadow: none; outline: none !important; margin: 1em  auto; text-align: center;}\n"
"a { color: orange; text-decoration: none; transition: color 250ms ease-in-out;}\n"
"a:hover { color: yellow;}\n"
".container { display:block; margin: 2em 0;}"))
        #self.tabWidget.addTab(contents, "3D Graph")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
       
        #self.dockWidgetContents.SetName("plot1")

        #self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        #self.dockWidget.setGeometry
        

      

        self.dockWidgetContents = mainFrame.DockContents()

        self.dockWidget.setWidget(self.dockWidgetContents)

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_17 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_17.setObjectName(_fromUtf8("toolButton_17"))
        self.toolButton_17.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Item-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon5)
        self.toolButton_17.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton_17)
        self.toolButton_10 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.toolButton_10.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n""  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        self.toolButton_10.setIcon(icon2)
        self.toolButton_10.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton_10)
        self.toolButton_20 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_20.setObjectName(_fromUtf8("toolButton_20"))
        self.toolButton_20.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        self.toolButton_20.setIcon(icon4)
        self.toolButton_20.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton_20)
        self.toolButton_18 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_18.setObjectName(_fromUtf8("toolButton_18"))
        self.toolButton_18.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        self.toolButton_18.setIcon(icon3)
        self.toolButton_18.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton_18)
        self.toolButton_4 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_4.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton_3 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_3.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_2 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.line_5 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.checkBox = QtGui.QCheckBox(self.dockWidgetContents_3)
        self.checkBox.setMaximumSize(QtCore.QSize(20, 16777215))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.Example = QtGui.QToolButton(self.dockWidgetContents_3)
        self.Example.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Example.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        self.Example.setIconSize(QtCore.QSize(48, 48))
        self.Example.setObjectName(_fromUtf8("Example"))
        self.horizontalLayout.addWidget(self.Example)
        self.line_6 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Board-Pin-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon6)
        self.toolButton.setIconSize(QtCore.QSize(48, 48))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.toolButton_25 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_25.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Table-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_25.setIcon(icon7)
        self.toolButton_25.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_25.setObjectName(_fromUtf8("toolButton_25"))
        self.horizontalLayout.addWidget(self.toolButton_25)
        self.line_8 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout.addWidget(self.line_8)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.line_7 = QtGui.QFrame(self.dockWidgetContents_4)
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_4.addWidget(self.line_7)
        self.toolButton_19 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_19.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Briefcase-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_19.setIcon(icon8)
        self.toolButton_19.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_19.setObjectName(_fromUtf8("toolButton_19"))
        self.horizontalLayout_4.addWidget(self.toolButton_19)
        self.toolButton_23 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_23.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Printer-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_23.setIcon(icon9)
        self.toolButton_23.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_23.setObjectName(_fromUtf8("toolButton_23"))
        self.horizontalLayout_4.addWidget(self.toolButton_23)
        self.toolButton_24 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_24.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Camera-02-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_24.setIcon(icon10)
        self.toolButton_24.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_24.setObjectName(_fromUtf8("toolButton_24"))
        self.horizontalLayout_4.addWidget(self.toolButton_24)
        self.toolButton_22 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_22.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Facebook-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_22.setIcon(icon11)
        self.toolButton_22.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_22.setObjectName(_fromUtf8("toolButton_22"))
        self.horizontalLayout_4.addWidget(self.toolButton_22)
        self.line_3 = QtGui.QFrame(self.dockWidgetContents_4)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_4.addWidget(self.line_3)
        self.toolButton_21 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_21.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Media-Play-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_21.setIcon(icon12)
        self.toolButton_21.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_21.setObjectName(_fromUtf8("toolButton_21"))
        self.horizontalLayout_4.addWidget(self.toolButton_21)
        self.toolButton_16 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_16.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Stop-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon13)
        self.toolButton_16.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_16.setObjectName(_fromUtf8("toolButton_16"))
        self.horizontalLayout_4.addWidget(self.toolButton_16)
        self.line_2 = QtGui.QFrame(self.dockWidgetContents_4)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_4.addWidget(self.line_2)
        self.toolButton_15 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_15.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Column-Selection-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon14)
        self.toolButton_15.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_15.setObjectName(_fromUtf8("toolButton_15"))
        self.horizontalLayout_4.addWidget(self.toolButton_15)
        self.toolButton_14 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_14.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Slash-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon15)
        self.toolButton_14.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_14.setObjectName(_fromUtf8("toolButton_14"))
        self.horizontalLayout_4.addWidget(self.toolButton_14)
        self.line = QtGui.QFrame(self.dockWidgetContents_4)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_4.addWidget(self.line)
        self.toolButton_13 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_13.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Magnifying-Glass-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon16)
        self.toolButton_13.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        self.horizontalLayout_4.addWidget(self.toolButton_13)
        self.toolButton_12 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_12.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-In-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon17)
        self.toolButton_12.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.horizontalLayout_4.addWidget(self.toolButton_12)
        self.toolButton_11 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_11.setAutoFillBackground(False)
        self.toolButton_11.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"}"))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-Out-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon18)
        self.toolButton_11.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.horizontalLayout_4.addWidget(self.toolButton_11)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_4)
        self.actionNew_Project = QtGui.QAction(MainWindow)
        self.actionNew_Project.setObjectName(_fromUtf8("actionNew_Project"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)   
        
        self.pushButton_3.clicked.connect(self.hide_2)
        self.pushButton.setVisible(False)
        self.frame_2.setVisible(False)
        self.pushButton.clicked.connect(self.show_2)
        self.toolButton_19.clicked.connect(self.show_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # For Hand Cursor
    def hand_cursor(self,widget):
        widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    
    def hide_2(self):
        self.frame.hide()
        self.frame_2.show()
        self.pushButton.show()
    def show_2(self):
        self.frame.show()
        self.frame_2.hide()
        self.pushButton.hide()
    
    def show_1(self):
        if at.isVisible()==False:
            at.move(1920-911,1080-296)
            at.show()
            at.set
        else:
            at.hide()

    def add_page(self):
        #self.pages.append(self.create_page(self.create_new_page_button(),self.create_new_page_button_2()))
        contents = QtGui.QWidget(self.tabWidget)
        layout = QtGui.QVBoxLayout(contents)
        # add other widgets to the contents layout here
        # i.e. layout.addWidget(widget), etc
        widget_1 = QtGui.QWidget(self)
        #l = QtGui.QVBoxLayout(widget_1)
        #textbox=customLineEdit(self)
        sc = MayaviQWidget(widget_1)
        #l.addWidget(sc)
        #l.addWidget(textbox)
        layout.addWidget(sc)
        #layout.addWidget(self.create_new_page_button(),1,Qt.AlignTop)
        #layout.addWidget(self.create_new_page_button_2(),15,Qt.AlignTop)
        global i
        i+=1
        self.tabWidget.addTab( contents , 'Untitled'+str(i))        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "T\n"
"a\n"
"b\n"
"l\n"
"e\n"
"", None))
        self.pushButton_3.setText(_translate("MainWindow","Hide", None))
        self.toolButton_7.setText(_translate("MainWindow", "...", None))
        self.toolButton_9.setText(_translate("MainWindow", "...", None))
        self.toolButton_8.setText(_translate("MainWindow", "...", None))
        self.toolButton_6.setText(_translate("MainWindow", "...", None))
        self.toolButton_5.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z", None))
        self.pushButton_21.setText(_translate("MainWindow", "Redraw", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2D Graph", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3D Graph", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        
        self.toolButton_17.setToolTip(_translate("MainWindow", "Create New", None))
        self.toolButton_17.setText(_translate("MainWindow", "...", None))
        self.toolButton_10.setToolTip(_translate("MainWindow", "Open Existing", None))
        self.toolButton_10.setText(_translate("MainWindow", "...", None))
        self.toolButton_20.setToolTip(_translate("MainWindow", "Save to Drive", None))
        self.toolButton_20.setText(_translate("MainWindow", "...", None))
        self.toolButton_18.setToolTip(_translate("MainWindow", "Load New", None))
        self.toolButton_18.setText(_translate("MainWindow", "...", None))
        self.toolButton_4.setToolTip(_translate("MainWindow", "Add new Equation", None))
        self.toolButton_4.setText(_translate("MainWindow", "...", None))
        self.toolButton_3.setToolTip(_translate("MainWindow", "Remove this Equation", None))
        self.toolButton_3.setText(_translate("MainWindow", "...", None))
        self.checkBox.setToolTip(_translate("MainWindow", "Show on Graph", None))
        self.Example.setToolTip(_translate("MainWindow", "Illustrate with an Example", None))
        self.Example.setWhatsThis(_translate("MainWindow", "Example", None))
        self.Example.setText(_translate("MainWindow", "Example", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_25.setText(_translate("MainWindow", "...", None))
        self.toolButton_19.setText(_translate("MainWindow", "...", None))
        self.toolButton_23.setToolTip(_translate("MainWindow", "Print graph", None))
        self.toolButton_23.setText(_translate("MainWindow", "...", None))
        self.toolButton_24.setToolTip(_translate("MainWindow", "Take a screenshot", None))
        self.toolButton_24.setText(_translate("MainWindow", "...", None))
        self.toolButton_22.setToolTip(_translate("MainWindow", "Go to our FaceBook page", None))
        self.toolButton_22.setText(_translate("MainWindow", "...", None))
        self.toolButton_21.setToolTip(_translate("MainWindow", "Play", None))
        self.toolButton_21.setText(_translate("MainWindow", "...", None))
        self.toolButton_16.setToolTip(_translate("MainWindow", "Stop", None))
        self.toolButton_16.setText(_translate("MainWindow", "...", None))
        self.toolButton_15.setText(_translate("MainWindow", "...", None))
        self.toolButton_14.setText(_translate("MainWindow", "...", None))
        self.toolButton_13.setToolTip(_translate("MainWindow", "Zoom", None))
        self.toolButton_13.setText(_translate("MainWindow", "...", None))
        self.toolButton_12.setToolTip(_translate("MainWindow", "Zoom in", None))
        self.toolButton_12.setText(_translate("MainWindow", "...", None))
        self.toolButton_11.setToolTip(_translate("MainWindow", "Zoom out", None))
        self.toolButton_11.setText(_translate("MainWindow", "...", None))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_10.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_20.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_18.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_4.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_3.setIconSize(QtCore.QSize(30, 30))
        self.Example.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_25.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))


class TabContainer(QtGui.QWidget):
  def __init__(self):
    super(TabContainer, self).__init__()
    self.initUI()
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+T"), self, self.add_page)
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, self.closeTab_1)
    

  def initUI(self):
    #self.setGeometry( 150, 150, 650, 350)
    self.tabWidget = QtGui.QTabWidget(self)
    self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
   # self.tabwidget.setTabShape(QtGui.QTabWidget.Triangular)
    #QtCore.QObject.connect(self, QtCore.SIGNAL('tabCloseRequested(int)'), self.closeTab)
    self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested (int)'),self.closeTab)
    self.tabWidget.setTabsClosable(True)
    #self.tabwidget.removeTab(1)
    self.tabWidget.setAutoFillBackground(False)
    self.tabWidget.setMovable(True)
    #self.tabwidget.setTabShape(QtGui.QTabWidget.Rounded)
    vbox = QtGui.QVBoxLayout()
    self.tabWidget.setDocumentMode(True)
    vbox.addWidget(self.tabWidget)
    self.tabButton = QtGui.QToolButton(self)
    self.tabButton.setText(' + ')
    font = self.tabButton.font()
    font.setBold(True)
    self.tabButton.setFont(font)
    self.tabWidget.setCornerWidget(self.tabButton)
    self.tabButton.clicked.connect(self.add_page)
    self.setLayout(vbox)
    self.pages = []
    self.add_page()
    self.show()
    
  def closeTab(self, index):
      
      #self.tabWidget.widget(index).close()
      if self.tabWidget.count()== 1:
          self.close()
      #self.pages.remove(self.tabwidget.currentWidget())
      self.tabWidget.removeTab(index)
      
      self.tabWidget.destroy(index)
      print len(self.pages)
        
  def closeTab_1(self):
      
      print"hello"
      index=self.tabWidget.currentIndex()
      if self.tabWidget.count()== 1:
          self.close()
      
      self.pages.remove(self.tabWidget.currentWidget())
      self.tabWidget.destroy(index)
      self.tabWidget.removeTab(index)
      print len(self.pages)
        

  def create_page(self, *contents):
    print("creating new page")
    page = QtGui.QWidget()
    vbox = QtGui.QVBoxLayout()
    
    for c in contents:
        vbox.addWidget(c)

    page.setLayout(vbox)
    return page

  def add_page(self):
    #self.pages.append( self.create_page( MainWindow() ) )
    print("adding page")
    self.pages.append(Ui_MainWindow())
    self.tabWidget.addTab( self.pages[-1] , 'Project %s' % len(self.pages) )
    self.tabWidget.setCurrentIndex( len(self.pages)-1 )

class Ui_MainWindow_2(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.vbox=QtGui.QVBoxLayout(self.centralwidget)
        self.vbox.addWidget(TabContainer())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow_2()
    ex.showMaximized()
    at=Ui_DockWidget()
    sys.exit(app.exec_())