# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Sun Mar 15 00:12:39 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!



'''
Please Note : All the developers are requested to kindly specify or atleast mention the unique features being added by them 
              so as to keep track of them and such that these don't go unattended, when writing the documentation about unique features of our plotter

unique (not-so-common) features of MS Hall Opensoft Plotter Software :

### till 18th March 2015 :

allowing for keyboard shortcuts for adding TabPages - by Ravi
accounting for file inputs not in proper csv format and specifying the delimiters for the same- by Varun




Please point out any further feautures that can be included in our plotter, or even mention any basic required functionality not included yet:

### Basic Functionality:
    
    Naming the new Project as soon as a new TabPage project is created ( instead of naming it as Project 1....etc.)
    (The project will be saved by the same name in the saved plots folder)

### Additional Features :

    Adding a Tutorial flipPage at the very first use (describing all the keyboard shortcuts etc.)


## Please keep adding more as you come to think of any !!!
'''


import mayaviPlot
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *

#from plottingEquation_3d_explicit import MplPlot3dCanvas
from imp_plottingEquation import MplPlot3dCanvas_2
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
    totalTabs=0
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        QtGui.QShortcut(QtGui.QKeySequence("Esc"), self, self.showAll)
        self.expression_list=[]
        self.tabIdentifier=Ui_MainWindow.totalTabs
        Ui_MainWindow.totalTabs+=1

    def addNewEquationEditor(self,layout,spacer):
        n = layout.count()
        layout.removeItem(layout.itemAt(n-1))
        dockWidgetContents = Exp_Form(self)
        self.expression_list.append(dockWidgetContents)
        layout.addWidget(dockWidgetContents)
        layout.addItem(spacer)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1396, 727)
        MainWindow.setStyleSheet(_fromUtf8("QFrame{\n"
"border:none;\n"
"}\n"
"QStatusBar{ \n"
"background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.33, stop:0 rgba(255, 255, 255, 255), stop:0.125 rgba(155, 174, 198, 255), stop:0.318182 rgba(104, 117, 133, 255), stop:0.534091 rgba(65, 73, 83, 255), stop:0.875 rgba(42, 47, 54, 255)); }\n"
" QMainWindow{\n"
" background-image: url(Icons/rsz_back1.jpg); border:none; background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); text-align: center; }\n"
" QGroupBox{ \n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); }\n"
" QTabWidget{\n"
" background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); } \n"
"QDockWidget{ background-color:#737373; border:none; padding:0px; } QSlider::groove:horizontal { background:red; height: 15px; position: absolute; left: 4px; right: 4px; } \n"
"QSlider::handle:horizontal {\n"
" height:20px; width: 10px; background: qlineargradient(spread:pad, x1:0, y1:0.477, x2:0, y2:0, stop:0.125 rgba(42, 47, 54, 255), stop:0.465909 rgba(65, 73, 83, 255), stop:0.681818 rgba(104, 117, 133, 255), stop:0.875 rgba(155, 174, 198, 255), stop:1 rgba(255, 255, 255, 255)); margin: -4px; } \n"
"QSlider::handle:hover:horizontal { height:20px; width: 10px; background:qlineargradient(spread:pad, x1:0, y1:0.477, x2:0, y2:0, stop:0.125 rgba(91, 95, 100, 255), stop:0.465909 rgba(122, 132, 146, 255), stop:0.681818 rgba(141, 153, 167, 255), stop:0.875 rgba(181, 195, 212, 255), stop:1 rgba(255, 255, 255, 255)); margin: -4px; }\n"
" QSlider::add-page:horizontal { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.278, stop:0 rgba(200, 239, 217, 255), stop:0.0852273 rgba(126, 201, 157, 255), stop:0.448864 rgba(59, 180, 109, 255), stop:0.75 rgba(43, 151, 88, 255)); }\n"
" QSlider::sub-page:horizontal { background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)) ; }\n"
" QToolButton{ position: relative; border: none; outline:none; color: black; padding: 0px; border-radius: 2px; font-size: 22px; }\n"
" QToolButton:hover:!pressed{ position: relative; border: none; outline:none; background-color:qlineargradient(spread:pad, x1:0, y1:0.71, x2:0, y2:0, stop:0 rgba(198, 198, 198, 255), stop:0.471591 rgba(207, 207, 207, 255), stop:1 rgba(255, 255, 255, 255)); color: white; padding: 4px; border-radius: 2px; font-size: 22px; }\n"
" QPushButton{ position: relative; border:none; outline:none; background-color:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); color: white; padding: 6px 20px; border-radius: 2px; font-size: 20px; } QPushButton:hover:!pressed{ position: relative; border: none; outline:none; background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.278, stop:0 rgba(200, 239, 217, 255), stop:0.0852273 rgba(126, 201, 157, 255), stop:0.448864 rgba(59, 180, 109, 255), stop:0.75 rgba(43, 151, 88, 255)); color: white; padding: 6px 20px; border-radius: 2px; font-size:20px; } \n"
"QComboBox { border: none; padding: 1px 18px 1px 3px; min-width: 6em; } QComboBox, QComboBox:drop-down { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); } QComboBox:on, QComboBox:drop-down:on { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.278, stop:0 rgba(200, 239, 217, 255), stop:0.0852273 rgba(126, 201, 157, 255), stop:0.448864 rgba(59, 180, 109, 255), stop:0.75 rgba(43, 151, 88, 255)); }\n"
" QComboBox:on { padding-top: 3px; padding-left: 4px; } \n"
"QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 15px; border-left-width: 1px; border-left-color: darkgray; border-left-style: solid; }\n"
" QComboBox::down-arrow { image:url(Icons/arrow-new.png); } QComboBox::down-arrow:on { top: 1px; left: 1px; }\n"
" QMenu { background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); border: none; } \n"
"QMenu::item { background-color: transparent; }\n"
" QMenu::item:selected { background-color:rgb(24, 164, 82); } \n"
"QMenuBar { background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)) }\n"
" QMenuBar::item { spacing: 3px; padding: 1px 4px; background: transparent; border-radius: 2px; } \n"
"QMenuBar::item:selected { background:#737373; } \n"
"QMenuBar::item:pressed { background: #414953; }\n"
" QTableWidget{ background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)); border:1px solid rgb(171, 173, 179); } \n"
"QTextEdit{ background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)); } \n"
"QScrollBar:horizontal { border: none; background: #DBDBDB; height: 15px; margin: 0px 20px 0px 20px; } \n"
"QScrollBar::handle:horizontal { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); min-width: 20px; } QScrollBar::handle:horizontal:hover { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.278, stop:0 rgba(200, 239, 217, 255), stop:0.0852273 rgba(126, 201, 157, 255), stop:0.448864 rgba(59, 180, 109, 255), stop:0.75 rgba(43, 151, 88, 255)); min-width: 20px; }\n"
" QScrollBar::add-line:horizontal { border: none; background:#DBDBDB; width: 20px; subcontrol-position: right; subcontrol-origin: margin; }\n"
" QScrollBar::sub-line:horizontal { border:none; background:#DBDBDB; width: 20px; subcontrol-position: left; subcontrol-origin: margin; } \n"
"QScrollBar::add-line:horizontal:hover:!pressed { border: none; background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); width: 20px; subcontrol-position: right; subcontrol-origin: margin; } \n"
"QScrollBar::sub-line:horizontal:hover:!pressed { border:none; background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); width: 20px; subcontrol-position: left; subcontrol-origin: margin; } \n"
"QScrollBar::left-arrow:horizontal{ image: url(Icons/left-arrow.png); } QScrollBar::right-arrow:horizontal{ image: url(Icons/right-arrow.png); } \n"
"QScrollBar:vertical { border: none; background: #DBDBDB; width: 15px; margin: 20px 0px 20px 0px; } \n"
"QScrollBar::handle:vertical { background:qlineargradient(spread:pad, x1:0.659545, y1:0, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); min-height: 20px; } QScrollBar::handle:vertical:hover { background:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 239, 217, 255), stop:0.0852273 rgba(126, 201, 157, 255), stop:0.448864 rgba(59, 180, 109, 255), stop:0.75 rgba(43, 151, 88, 255)); min-height: 15px; } QScrollBar::add-line:vertical { border: none; background:#DBDBDB; height: 20px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::sub-line:vertical { border:none; background:#DBDBDB; height: 20px; subcontrol-position: top; subcontrol-origin: margin; } \n"
"QScrollBar::add-line:vertical:hover:!pressed { border: none; background: qlineargradient(spread:pad, x1:0.659545, y1:0, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); height: 20px; subcontrol-position:bottom; subcontrol-origin: margin; }\n"
" QScrollBar::sub-line:vertical:hover:!pressed { border:none; background: qlineargradient(spread:pad, x1:0.659545, y1:0, x2:0, y2:0, stop:0.25 rgba(17, 118, 59, 255), stop:0.551136 rgba(20, 138, 69, 255), stop:0.914773 rgba(114, 189, 145, 255), stop:1 rgba(132, 221, 169, 255)); height: 20px; subcontrol-position:top; subcontrol-origin: margin; } \n"
"QScrollBar::up-arrow:vertical{ image: url(Icons/up-arrow.png); } QScrollBar::down-arrow:vertical{ image: url(Icons/down-arrow.png); }"))
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
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/double-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(320, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.toolButton_7 = QtGui.QToolButton(self.frame)
        self.toolButton_7.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_7.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_7.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Add-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon1)
        self.toolButton_7.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_5.addWidget(self.toolButton_7)
        self.toolButton_9 = QtGui.QToolButton(self.frame)
        self.toolButton_9.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_9.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_9.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Minus-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon2)
        self.toolButton_9.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.horizontalLayout_5.addWidget(self.toolButton_9)
        self.toolButton_8 = QtGui.QToolButton(self.frame)
        self.toolButton_8.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_8.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_8.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Folder-Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon3)
        self.toolButton_8.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_5.addWidget(self.toolButton_8)
        self.toolButton_5 = QtGui.QToolButton(self.frame)
        self.toolButton_5.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_5.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Save-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtGui.QTableWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setStyleSheet(_fromUtf8(""))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.header=self.tableWidget.horizontalHeader();
        self.header.setResizeMode(QHeaderView.Stretch);
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton_21 = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_3.addWidget(self.pushButton_21)
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
        contents_2=QtGui.QWidget(self.tabWidget)
        layout_2= QtGui.QVBoxLayout(contents_2)
        sc_2=MplPlot3dCanvas_2(self)
        widget_2=QtGui.QWidget(self)
        layout_2.addWidget(sc_2)
        self.tabWidget.addTab(contents_2, "2D Graph")
        contents = QtGui.QWidget(self.tabWidget)
        layout = QtGui.QVBoxLayout(contents)
        widget_1 = QtGui.QWidget(self)
        self.mayavi_widget = mayaviPlot.MayaviQWidget()
        layout.addWidget(self.mayavi_widget)
        self.tabWidget.addTab(contents, "3D Graph")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 21))
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
        

      

        self.dockWidgetContents = mainFrame.DockContents(self)

        self.dockWidget.setWidget(self.dockWidgetContents)

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)






        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(489, 70))
        self.dockWidget_3.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(0)
        self.toolButton_17 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_17.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_17.setStyleSheet(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Item-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon5)
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setObjectName(_fromUtf8("toolButton_17"))
        self.horizontalLayout.addWidget(self.toolButton_17)
        self.toolButton_10 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_10.setStyleSheet(_fromUtf8(""))
        self.toolButton_10.setIcon(icon3)
        self.toolButton_10.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.horizontalLayout.addWidget(self.toolButton_10)
        self.toolButton_20 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_20.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_20.setStyleSheet(_fromUtf8(""))
        self.toolButton_20.setIcon(icon4)
        self.toolButton_20.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_20.setObjectName(_fromUtf8("toolButton_20"))
        self.horizontalLayout.addWidget(self.toolButton_20)
        self.toolButton_18 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_18.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_18.setStyleSheet(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_18.setIcon(icon6)
        self.toolButton_18.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_18.setObjectName(_fromUtf8("toolButton_18"))
        self.horizontalLayout.addWidget(self.toolButton_18)
        self.line_4 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.toolButton_4 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet(_fromUtf8(""))
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton_3 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet(_fromUtf8(""))
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.line_5 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.checkBox = QtGui.QCheckBox(self.dockWidgetContents_3)
        self.checkBox.setMaximumSize(QtCore.QSize(20, 25))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.Example = QtGui.QToolButton(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Example.sizePolicy().hasHeightForWidth())
        self.Example.setSizePolicy(sizePolicy)
        self.Example.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Example.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Example.setStyleSheet(_fromUtf8("QToolButton{\n"
"font-size: 15px;\n"
"color:rgb(255, 255, 255);\n"
"}"))
        self.Example.setIconSize(QtCore.QSize(24, 24))
        self.Example.setObjectName(_fromUtf8("Example"))
        self.horizontalLayout.addWidget(self.Example)
        self.line_6 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Board-Pin-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon7)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_25 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_25.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_25.setStyleSheet(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Table-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_25.setIcon(icon8)
        self.toolButton_25.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_25.setObjectName(_fromUtf8("toolButton_25"))
        self.horizontalLayout.addWidget(self.toolButton_25)
        self.line_8 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout.addWidget(self.line_8)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_4.sizePolicy().hasHeightForWidth())
        self.dockWidget_4.setSizePolicy(sizePolicy)
        self.dockWidget_4.setMinimumSize(QtCore.QSize(624, 70))
        self.dockWidget_4.setMaximumSize(QtCore.QSize(524287, 70))
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(0)
        self.line_7 = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_2.addWidget(self.line_7)
        self.toolButton_19 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_19.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_19.setStyleSheet(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Keyboard-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_19.setIcon(icon9)
        self.toolButton_19.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_19.setObjectName(_fromUtf8("toolButton_19"))
        self.horizontalLayout_2.addWidget(self.toolButton_19)
        self.toolButton_23 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_23.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_23.setStyleSheet(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Printer-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_23.setIcon(icon10)
        self.toolButton_23.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_23.setObjectName(_fromUtf8("toolButton_23"))
        self.horizontalLayout_2.addWidget(self.toolButton_23)
        self.toolButton_2 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.toolButton_24 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_24.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_24.setStyleSheet(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Camera-02-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_24.setIcon(icon11)
        self.toolButton_24.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_24.setObjectName(_fromUtf8("toolButton_24"))
        self.horizontalLayout_2.addWidget(self.toolButton_24)
        self.toolButton_22 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_22.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_22.setStyleSheet(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Facebook-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_22.setIcon(icon12)
        self.toolButton_22.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_22.setObjectName(_fromUtf8("toolButton_22"))
        self.horizontalLayout_2.addWidget(self.toolButton_22)
        self.line_3 = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_2.addWidget(self.line_3)
        self.toolButton_21 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_21.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_21.setStyleSheet(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Media-Play-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_21.setIcon(icon13)
        self.toolButton_21.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_21.setObjectName(_fromUtf8("toolButton_21"))
        self.horizontalLayout_2.addWidget(self.toolButton_21)
        self.toolButton_16 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_16.setStyleSheet(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Stop-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon14)
        self.toolButton_16.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_16.setObjectName(_fromUtf8("toolButton_16"))
        self.horizontalLayout_2.addWidget(self.toolButton_16)
        self.line_2 = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.toolButton_15 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_15.setStyleSheet(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Column-Selection-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon15)
        self.toolButton_15.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_15.setObjectName(_fromUtf8("toolButton_15"))
        self.horizontalLayout_2.addWidget(self.toolButton_15)
        self.toolButton_14 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_14.setStyleSheet(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Slash-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon16)
        self.toolButton_14.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_14.setObjectName(_fromUtf8("toolButton_14"))
        self.horizontalLayout_2.addWidget(self.toolButton_14)
        self.line = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.toolButton_13 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_13.setStyleSheet(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Magnifying-Glass-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon17)
        self.toolButton_13.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        self.horizontalLayout_2.addWidget(self.toolButton_13)
        self.toolButton_12 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_12.setStyleSheet(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-In-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon18)
        self.toolButton_12.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.horizontalLayout_2.addWidget(self.toolButton_12)
        self.toolButton_11 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_11.setAutoFillBackground(False)
        self.toolButton_11.setStyleSheet(_fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-Out-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon19)
        self.toolButton_11.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.horizontalLayout_2.addWidget(self.toolButton_11)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_4)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)   
        
        self.pushButton_3.clicked.connect(self.hide_2)
        self.pushButton.setVisible(False)
        self.frame_2.setVisible(False)
        self.pushButton.clicked.connect(self.show_2)
        self.toolButton_19.clicked.connect(self.show_1)
        self.toolButton_8.clicked.connect(self.showFileChooser)
        self.toolButton_7.clicked.connect(self.addRowDataPoint)
        self.toolButton_9.clicked.connect(self.removeRowDataPoint)
        self.toolButton_5.clicked.connect(self.saveDataValuesToFile)
        self.toolButton_15.clicked.connect(self.hideAll)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def hideAll(self):
        self.dockWidget.hide()
        self.dockWidget_4.hide()
        self.dockWidget_3.hide()
        self.frame.hide()

    def showAll(self):
        self.dockWidget.show()
        self.dockWidget_4.show()
        self.dockWidget_3.show()
        self.frame.show()

    def saveDataValuesToFile(self):
        pname = ex.getTabName()
        import csv
        #savFile = open(pname+'.csv','w')
        with open(pname+".csv",'w') as output:
            writeHead = csv.writer(output,delimiter=',',lineterminator='\n')
            for i in range (0,self.tableWidget.rowCount()):
                row = list()

                for j in range (0,3):
                    try :
                        item = self.tableWidget.item(i,j).text()
                    except Exception,e:
                        continue
                    #toInt = int(item)
                    print item
                    row.append(item)

                #print row
                writeHead.writerow(row)

        #savFile.close()

    def addRowDataPoint(self):
        rowC = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowC)

    def removeRowDataPoint(self):
        if(self.tableWidget.currentRow()==-1):
            self.errorRemoveDataPoint()
        else:
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            self.tableWidget.setCurrentCell(-1,-1)

    def errorRemoveDataPoint(self):
        Dialog = QtGui.QDialog()
        u = Ui_Dialog_2("Please select the data point to remove")
        u.setupUi(Dialog)
        Dialog.exec_()

    # For Hand Cursor
    def hand_cursor(self,widget):
        widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def showFileChooser(self):
        fname = QtGui.QFileDialog.getOpenFileName(self,'Select File')
        self.delimit=','
        import csv
        f=open(fname,'rt')
        try:
            reader = csv.reader(f)
            num_rows = 0
            for row in reader:
                num_rows=num_rows+1

            with open(fname,'r') as fil :
               text = fil.read()

            count_comma=0
            for char in text:
               if char==',':
                  count_comma=count_comma+1

            if count_comma != (num_rows * 2) : # i.e. it is NOT a csv file
                self.showSelectDelimiter()

            self.tableWidget.setRowCount(num_rows)
            ## create items in all added 
            rowno_=0
            f=open(fname,'rt')
            reader=csv.reader(f,delimiter=self.delimit)
            try:   
                for row in reader:
                    for col in range (0,3):
                        float(row[col])
                        item = QtGui.QTableWidgetItem(row[col])
                        self.tableWidget.setItem(rowno_,col,item)
                    rowno_=rowno_+1        

                self.tableWidget.setRowCount(rowno_)
                
            except Exception, e:
                self.showU=self.showInvalidValueError()
                self.tableWidget.setRowCount(0)                    

        finally:
            f.close()                                  
                

    def showInvalidValueError(self):
        Dialog = QtGui.QDialog()
        u = Ui_Dialog_2('Cannnot import values ! Data Invalid !')
        u.setupUi(Dialog)
        Dialog.exec_()

    def showSelectDelimiter(self):
      Dialog = QtGui.QDialog()
      u = Ui_Dialog()
      u.setupUi(Dialog)
      dialg = StartDialog()
      if dialg.exec_():
        self.delimit = dialg.getDelim()
      #self.showFileChooser()

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
            at.setTarget(self.dockWidgetContents.eqList[0].frame.widget_4)
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
        self.pushButton_3.setText(_translate("MainWindow", "Hide", None))
        self.toolButton_7.setToolTip(_translate("MainWindow", "Add", None))
        self.toolButton_7.setText(_translate("MainWindow", "...", None))
        self.toolButton_9.setToolTip(_translate("MainWindow", "Remove", None))
        self.toolButton_9.setText(_translate("MainWindow", "...", None))
        self.toolButton_8.setToolTip(_translate("MainWindow", "Import Coordinates", None))
        self.toolButton_8.setText(_translate("MainWindow", "...", None))
        self.toolButton_5.setToolTip(_translate("MainWindow", "Export Coordinates", None))
        self.toolButton_5.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z", None))
        self.pushButton_21.setText(_translate("MainWindow", "Redraw", None))
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
        self.toolButton.setToolTip(_translate("MainWindow", "Always on Top", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_25.setToolTip(_translate("MainWindow", "Show/Hide Table", None))
        self.toolButton_25.setText(_translate("MainWindow", "...", None))
        self.toolButton_19.setToolTip(_translate("MainWindow", "Keyboard", None))
        self.toolButton_19.setText(_translate("MainWindow", "...", None))
        self.toolButton_23.setToolTip(_translate("MainWindow", "Print graph", None))
        self.toolButton_23.setText(_translate("MainWindow", "...", None))
        self.toolButton_2.setToolTip(_translate("MainWindow", "Save Graph", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.toolButton_24.setToolTip(_translate("MainWindow", "Take a screenshot", None))
        self.toolButton_24.setText(_translate("MainWindow", "...", None))
        self.toolButton_22.setToolTip(_translate("MainWindow", "Go to our FaceBook page", None))
        self.toolButton_22.setText(_translate("MainWindow", "...", None))
        self.toolButton_21.setToolTip(_translate("MainWindow", "Play", None))
        self.toolButton_21.setText(_translate("MainWindow", "...", None))
        self.toolButton_16.setToolTip(_translate("MainWindow", "Stop", None))
        self.toolButton_16.setText(_translate("MainWindow", "...", None))
        self.toolButton_15.setToolTip(_translate("MainWindow", "Disable Anti-Aliasing", None))
        self.toolButton_15.setText(_translate("MainWindow", "...", None))
        self.toolButton_14.setToolTip(_translate("MainWindow", "Enable Anti-Aliasing", None))
        self.toolButton_14.setText(_translate("MainWindow", "...", None))
        self.toolButton_13.setToolTip(_translate("MainWindow", "Zoom All", None))
        self.toolButton_13.setText(_translate("MainWindow", "...", None))
        self.toolButton_12.setToolTip(_translate("MainWindow", "Zoom in", None))
        self.toolButton_12.setText(_translate("MainWindow", "...", None))
        self.toolButton_11.setToolTip(_translate("MainWindow", "Zoom out", None))
        self.toolButton_11.setText(_translate("MainWindow", "...", None))
        #self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))


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

  def getProjectName(self):
        return 'Project %s' % len(self.pages)

class Ui_MainWindow_2(QtGui.QMainWindow):
    delimit = ','
    #t=TabContainer()
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
        self.t=TabContainer()
        self.vbox.addWidget(self.t)
        self.vbox.setMargin(0)
        self.vbox.setSpacing(0)
        #self.vbox.setContentsMargins(0,0,0,0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

    def getTabName(self):
        return self.t.getProjectName();



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(456, 339)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 110, 211, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 110, 141, 32))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(False)
        self.widget.setGeometry(QtCore.QRect(50, 200, 311, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)   
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.widget.setPalette(palette)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 291, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(60, 20, 361, 71))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_6 = QtGui.QLabel(self.widget_2)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 281, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.widget_2)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 331, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(240, 160, 83, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(320, 160, 41, 31))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(lambda:self.storeDelim)
        self.comboBox.activated.connect(self.storeDelim)
        self.textEdit.textChanged.connect(self.storeDelim)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Choose Delimiter", None))
        self.label.setText(_translate("Dialog", "Please specify delimiter :", None))
        self.comboBox.setItemText(0, _translate("Dialog", "\',\' (comma)", None))
        self.comboBox.setItemText(1, _translate("Dialog", "\' \' (space)", None))
        self.comboBox.setItemText(2, _translate("Dialog", "\';\' (semicolon)", None))
        self.comboBox.setItemText(3, _translate("Dialog", "\'-\' (dash)", None))
        self.comboBox.setItemText(4, _translate("Dialog", "\':\' (colon)", None))
        self.comboBox.setItemText(5, _translate("Dialog", "Specify other", None))
        self.label_2.setText(_translate("Dialog", "The Plotter retrieves values ", None))
        self.label_3.setText(_translate("Dialog", "separated by the chosen delimiter", None))
        self.label_6.setText(_translate("Dialog", "The Plotter has detected that the", None))
        self.label_7.setText(_translate("Dialog", "selected file is NOT in proper csv format", None))
        self.label_4.setText(_translate("Dialog", "Specify :", None))    

    def storeDelim(self):
        if self.comboBox.currentIndex()==0:
            self.ch = ','
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==1:
            self.ch = ' '
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==2:
            self.ch = ';'
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==3:
            self.ch = '-'
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==4:
            self.ch = ':'
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==5:
            self.label_4.setEnabled(True)
            self.textEdit.setEnabled(True)
            self.ch=str(self.textEdit.toPlainText())

    def getDelim(self):
        return self.ch

class StartDialog(QtGui.QDialog, Ui_Dialog): 
    def __init__(self,parent=None): 
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)
class Ui_Dialog_2(object):    ## class for error Dialog Box
    mssg = 'error message'

    def __init__(self,string):
        self.mssg = string

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 126)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 70, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 400, 22))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", self.mssg, None))

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow_2()
    ex.showMaximized()
    at=Ui_DockWidget(None)
    sys.exit(app.exec_())
