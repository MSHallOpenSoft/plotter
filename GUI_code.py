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
        MainWindow.setStyleSheet(_fromUtf8("QFrame{\n"
"border:none;\n"
"}\n"
"QStatusBar{ background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.33, stop:0 rgba(255, 255, 255, 255), stop:0.125 rgba(155, 174, 198, 255), stop:0.318182 rgba(104, 117, 133, 255), stop:0.534091 rgba(65, 73, 83, 255), stop:0.875 rgba(42, 47, 54, 255)); } QMainWindow{ background-image: url(:/img/Icons/rsz_back1.jpg); border:none; background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); text-align: center; } QGroupBox{ background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); } QTabWidget{ background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); } QDockWidget{ background-color:#737373; border:none; padding:0px; } QSlider::groove:horizontal { background:red; height: 15px; position: absolute; left: 4px; right: 4px; } QSlider::handle:horizontal { height:20px; width: 10px; background: qlineargradient(spread:pad, x1:0, y1:0.477, x2:0, y2:0, stop:0.125 rgba(42, 47, 54, 255), stop:0.465909 rgba(65, 73, 83, 255), stop:0.681818 rgba(104, 117, 133, 255), stop:0.875 rgba(155, 174, 198, 255), stop:1 rgba(255, 255, 255, 255)); margin: -4px; } QSlider::handle:hover:horizontal { height:20px; width: 10px; background:qlineargradient(spread:pad, x1:0, y1:0.477, x2:0, y2:0, stop:0.125 rgba(91, 95, 100, 255), stop:0.465909 rgba(122, 132, 146, 255), stop:0.681818 rgba(141, 153, 167, 255), stop:0.875 rgba(181, 195, 212, 255), stop:1 rgba(255, 255, 255, 255)); margin: -4px; } QSlider::add-page:horizontal { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); } QSlider::sub-page:horizontal { background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)) ; } QToolButton{ position: relative; border: none; outline:none; color: black; padding: 0px; border-radius: 2px; font-size: 22px; } QToolButton:hover:!pressed{ position: relative; border: none; outline:none; background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); color: white; padding: 0px; border-radius: 2px; font-size: 22px; } QPushButton{ position: relative; border:none; outline:none; background-color: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); color: white; padding: 6px 20px; border-radius: 2px; font-size: 20px; } QPushButton:hover:!pressed{ position: relative; border: none; outline:none; background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); color: white; padding: 6px 20px; border-radius: 2px; font-size:20px; } QComboBox { border: none; padding: 1px 18px 1px 3px; min-width: 6em; } QComboBox, QComboBox:drop-down { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); } QComboBox:on, QComboBox:drop-down:on { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); } QComboBox:on { padding-top: 3px; padding-left: 4px; } QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 15px; border-left-width: 1px; border-left-color: darkgray; border-left-style: solid; } QComboBox::down-arrow { image:url(:/arrow/Icons/arrow-new.png); } QComboBox::down-arrow:on { top: 1px; left: 1px; } QMenu { background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); border: none; } QMenu::item { background-color: transparent; } QMenu::item:selected { background-color:rgb(120, 255, 13); } QMenuBar { background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)) } QMenuBar::item { spacing: 3px; padding: 1px 4px; background: transparent; border-radius: 2px; } QMenuBar::item:selected { background:#737373; } QMenuBar::item:pressed { background: #414953; } QTableWidget{ background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)); border:1px solid rgb(171, 173, 179); } QTextEdit{ background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)); } QScrollBar:horizontal { border: none; background: #DBDBDB; height: 15px; margin: 0px 20px 0 20px; } QScrollBar::handle:horizontal { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); min-width: 20px; } QScrollBar::handle:horizontal:hover { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); min-width: 20px; } QScrollBar::add-line:horizontal { border: none; background:#DBDBDB; width: 20px; subcontrol-position: right; subcontrol-origin: margin; } QScrollBar::sub-line:horizontal { border:none; background:#DBDBDB; width: 20px; subcontrol-position: left; subcontrol-origin: margin; } QScrollBar::add-line:horizontal:hover:!pressed { border: none; background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); width: 20px; subcontrol-position: right; subcontrol-origin: margin; } QScrollBar::sub-line:horizontal:hover:!pressed { border:none; background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); width: 20px; subcontrol-position: left; subcontrol-origin: margin; } QScrollBar::left-arrow:horizontal{ image: url(:/arrow/Icons/left-arrow.png); } QScrollBar::right-arrow:horizontal{ image: url(:/arrow/Icons/right-arrow.png); } QScrollBar:vertical { border: none; background: #DBDBDB; width: 15px; margin: 0px 20px 0 20px; } QScrollBar::handle:vertical { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); min-height: 20px; } QScrollBar::handle:vertical:hover { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); min-height: 15px; } QScrollBar::add-line:vertical { border: none; background:#DBDBDB; height: 20px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::sub-line:vertical { border:none; background:#DBDBDB; height: 20px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover:!pressed { border: none; background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); height: 20px; subcontrol-position:bottom; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover:!pressed { border:none; background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); height: 20px; subcontrol-position:top; subcontrol-origin: margin; } QScrollBar::up-arrow:vertical{ image: url(:/arrow/Icons/up-arrow.png); } QScrollBar::down-arrow:vertical{ image: url(:/arrow/Icons/down-arrow.png); }"))
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
        contents_2=QtGui.QWidget(self.tabWidget)
        layout_2= QtGui.QVBoxLayout(contents_2)
        widget_2 = QtGui.QWidget(self)
        sc_2=MplPlot3dCanvas_2(widget_2)
        layout_2.addWidget(sc_2)
        self.tabWidget.addTab(contents_2, "2D Graph")
        contents = QtGui.QWidget(self.tabWidget)
        layout = QtGui.QVBoxLayout(contents)
        widget_1 = QtGui.QWidget(self)
        self.mayavi_widget = mayaviPlot.MayaviQWidget(widget_1)
        layout.addWidget(self.mayavi_widget)
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
        self.tabWidget.addTab(contents, "3D Graph")
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
        

      

        self.dockWidgetContents = mainFrame.DockContents(self)

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
        self.toolButton_8.clicked.connect(self.showFileChooser)
        self.toolButton_7.clicked.connect(self.addRowDataPoint)
        self.toolButton_9.clicked.connect(self.removeRowDataPoint)
        self.toolButton_5.clicked.connect(self.saveDataValuesToFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))

    def getTabName(self):
        return self.t.getProjectName();


class Ui_Dialog(object):
    ch=','

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(456, 284)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 240, 341, 32))
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
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(False)
        self.widget.setGeometry(QtCore.QRect(70, 160, 311, 71))
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

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(lambda:self.storeDelim)
        self.comboBox.activated.connect(self.storeDelim)

    def storeDelim(self):
        if self.comboBox.currentIndex()==0:
            self.ch = ','
        elif self.comboBox.currentIndex()==1:
            self.ch = ' '
        elif self.comboBox.currentIndex()==2:
            self.ch = ';'
        elif self.comboBox.currentIndex()==3:
            self.ch = '-'
        elif self.comboBox.currentIndex()==4:
            self.ch = ':'

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Choose Delimiter", None))
        self.label.setText(_translate("Dialog", "Please specify delimiter :", None))
        self.comboBox.setItemText(0, _translate("Dialog", "\',\' (comma)", None))
        self.comboBox.setItemText(1, _translate("Dialog", "\' \' (space)", None))
        self.comboBox.setItemText(2, _translate("Dialog", "\';\' (semicolon)", None))
        self.comboBox.setItemText(3, _translate("Dialog", "\'-\' (dash)", None))
        self.comboBox.setItemText(4, _translate("Dialog", "\':\' (colon)", None))
        self.label_2.setText(_translate("Dialog", "The Plotter retrieves values ", None))
        self.label_3.setText(_translate("Dialog", "separated by the chosen delimiter", None))
        self.label_6.setText(_translate("Dialog", "The Plotter has detected that the", None))
        self.label_7.setText(_translate("Dialog", "selected file is NOT in proper csv format", None))

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
    at=Ui_DockWidget()
    sys.exit(app.exec_())
