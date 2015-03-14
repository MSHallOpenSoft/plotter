# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Tue Mar 10 19:35:39 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, SIGNAL
i=1
import sys, random
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
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+T"), self, self.add_page)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, self.closeTab_1)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1160, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.toolButton_7 = QtGui.QToolButton(self.frame)
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_5.addWidget(self.toolButton_7)
        self.toolButton_9 = QtGui.QToolButton(self.frame)
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.horizontalLayout_5.addWidget(self.toolButton_9)
        self.toolButton_8 = QtGui.QToolButton(self.frame)
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_5.addWidget(self.toolButton_8)
        self.toolButton_6 = QtGui.QToolButton(self.frame)
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.horizontalLayout_5.addWidget(self.toolButton_6)
        self.toolButton_5 = QtGui.QToolButton(self.frame)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtGui.QTableWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.pushButton_21 = QtGui.QPushButton(self.frame)
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_5.addWidget(self.pushButton_21)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabButton = QtGui.QToolButton(self)
        self.tabButton.setText('+')
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tabWidget.setCornerWidget(self.tabButton)
        self.tabButton.clicked.connect(self.add_page)
        self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested (int)'),self.closeTab)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setDocumentMode(True)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        #self.tab_2 = QtGui.QWidget()
        #self.tab_2.setObjectName(_fromUtf8("tab_2"))
        #self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
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
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_17 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_17.setObjectName(_fromUtf8("toolButton_17"))
        self.horizontalLayout.addWidget(self.toolButton_17)
        self.toolButton_10 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.horizontalLayout.addWidget(self.toolButton_10)
        self.toolButton_20 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_20.setObjectName(_fromUtf8("toolButton_20"))
        self.horizontalLayout.addWidget(self.toolButton_20)
        self.toolButton_18 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_18.setObjectName(_fromUtf8("toolButton_18"))
        self.horizontalLayout.addWidget(self.toolButton_18)
        self.toolButton_4 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton_3 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_2 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.toolButton_19 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_19.setObjectName(_fromUtf8("toolButton_19"))
        self.horizontalLayout_4.addWidget(self.toolButton_19)
        self.toolButton_23 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_23.setObjectName(_fromUtf8("toolButton_23"))
        self.horizontalLayout_4.addWidget(self.toolButton_23)
        self.toolButton_24 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_24.setObjectName(_fromUtf8("toolButton_24"))
        self.horizontalLayout_4.addWidget(self.toolButton_24)
        self.toolButton_22 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_22.setObjectName(_fromUtf8("toolButton_22"))
        self.horizontalLayout_4.addWidget(self.toolButton_22)
        self.toolButton_21 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_21.setObjectName(_fromUtf8("toolButton_21"))
        self.horizontalLayout_4.addWidget(self.toolButton_21)
        self.toolButton_16 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_16.setObjectName(_fromUtf8("toolButton_16"))
        self.horizontalLayout_4.addWidget(self.toolButton_16)
        self.toolButton_15 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_15.setObjectName(_fromUtf8("toolButton_15"))
        self.horizontalLayout_4.addWidget(self.toolButton_15)
        self.toolButton_14 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_14.setObjectName(_fromUtf8("toolButton_14"))
        self.horizontalLayout_4.addWidget(self.toolButton_14)
        self.toolButton_13 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        self.horizontalLayout_4.addWidget(self.toolButton_13)
        self.toolButton_12 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.horizontalLayout_4.addWidget(self.toolButton_12)
        self.toolButton_11 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.horizontalLayout_4.addWidget(self.toolButton_11)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
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
        self.pushButton_3.clicked.connect(lambda:self.hide_2())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # For Hand Cursor
    def hand_cursor(self,widget):
        widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def hide_2(self):
        self.frame.hide()
    def closeTab(self, index):
        if self.tabWidget.count()== 1:
            self.close()
        self.tabWidget.removeTab(index)
      
        self.tabWidget.destroy(index)
    def closeTab_1(self):
      
        index=self.tabWidget.currentIndex()
        if self.tabWidget.count()== 1:
            self.close()
        #self.pages.remove(self.tabWidget.currentWidget())
        self.tabWidget.destroy(index)
        self.tabWidget.removeTab(index)
    def create_new_page_button(self):
        radioButton = QtGui.QRadioButton('2D Graph')
        radioButton.setGeometry(QtCore.QRect(0, 0, 116, 22))
        #radioButton.clicked.connect(self.add_pagex)
        return radioButton
  
    def create_new_page_button_2(self):
        radioButton_2 = QtGui.QRadioButton('3D Graph')
        radioButton_2.setGeometry(QtCore.QRect(0, 0, 116, 22))
        #radioButton_2.clicked.connect(self.add_pagex)
        return radioButton_2
  
    def create_new_page_button_3(self):
        btn = QtGui.QPushButton('Change the title of the page!')
        btn.clicked.connect(self.change_title)
        return btn
    
    def create_page(self, *contents):
        page = QtGui.QWidget()
        num = 0 
        hbox = QtGui.QHBoxLayout() 
        vbox = QtGui.QVBoxLayout()  
        hbox.addStretch(1) 
        for c in contents[0:2]: 
            hbox.addWidget(c)
        #hbox.addWidget(contents[3])
        vbox.addLayout(hbox)
        vbox.insertStretch(-1,1) 
        page.setLayout(vbox)
        return page 
    
    def add_page(self):
        #self.pages.append(self.create_page(self.create_new_page_button(),self.create_new_page_button_2()))
        contents = QtGui.QWidget(self.tabWidget)
        layout = QtGui.QVBoxLayout(contents)
        # add other widgets to the contents layout here
        # i.e. layout.addWidget(widget), etc
        #layout.addWidget(self.create_new_page_button(),1)
        layout.addWidget(self.create_new_page_button(),1,Qt.AlignTop)
        layout.addWidget(self.create_new_page_button_2(),15,Qt.AlignTop)
        global i
        i+=1
        self.tabWidget.addTab( contents , 'Untitled'+str(i))        
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_3.setText(_translate("MainWindow", "Hide", None))
        self.toolButton_7.setText(_translate("MainWindow", "...", None))
        self.toolButton_9.setText(_translate("MainWindow", "...", None))
        self.toolButton_8.setText(_translate("MainWindow", "...", None))
        self.toolButton_6.setText(_translate("MainWindow", "...", None))
        self.toolButton_5.setText(_translate("MainWindow", "...", None))
        self.pushButton_21.setText(_translate("MainWindow", "Redraw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Untitled1", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.toolButton_17.setText(_translate("MainWindow", "...", None))
        self.toolButton_10.setText(_translate("MainWindow", "...", None))
        self.toolButton_20.setText(_translate("MainWindow", "...", None))
        self.toolButton_18.setText(_translate("MainWindow", "...", None))
        self.toolButton_4.setText(_translate("MainWindow", "...", None))
        self.toolButton_3.setText(_translate("MainWindow", "...", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_19.setText(_translate("MainWindow", "...", None))
        self.toolButton_23.setText(_translate("MainWindow", "...", None))
        self.toolButton_24.setText(_translate("MainWindow", "...", None))
        self.toolButton_22.setText(_translate("MainWindow", "...", None))
        self.toolButton_21.setText(_translate("MainWindow", "...", None))
        self.toolButton_16.setText(_translate("MainWindow", "...", None))
        self.toolButton_15.setText(_translate("MainWindow", "...", None))
        self.toolButton_14.setText(_translate("MainWindow", "...", None))
        self.toolButton_13.setText(_translate("MainWindow", "...", None))
        self.toolButton_12.setText(_translate("MainWindow", "...", None))
        self.toolButton_11.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z", None))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.setStyleSheet('''
QMainWindow::separator {
     background: yellow;
     width: 10px; /* when vertical */
     height: 10px; /* when horizontal */
 }

 QMainWindow::separator:hover {
     background: red;
 }
QPushButton {
    
    background-color:#79bbff;
    border-radius:6px;
    border:1px solid #84bbf3;
    color:#ffffff;
    font-family:arial;
    font-size:15px;
    font-weight:bold;
    padding:6px 24px;
    text-decoration:none;
    outline:none;

}

QPushButton:hover {
    background-color:#378de5;
}
QPushButton:active {
    position:relative;
    top:1px;
}
QTabWidget::pane { /* The tab widget frame */
     border-top: 2px solid #C2C7CB;
     position: absolute;
     top: -0.5em;
 }

 QTabWidget::tab-bar {
     alignment: center;
 }

 /* Style the tab using the tab sub-control. Note that
     it reads QTabBar _not_ QTabWidget */
 QTabBar::tab {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
     border: 2px solid #C4C4C3;
     border-bottom-color: #C2C7CB; /* same as the pane color */
     border-top-left-radius: 4px;
     border-top-right-radius: 4px;
     min-width: 8ex;
     padding: 2px;
 }

 QTabBar::tab:selected, QTabBar::tab:hover {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
 }

 QTabBar::tab:selected {
     border-color: #9B9B9B;
     border-bottom-color: #C2C7CB; /* same as pane color */
 }
  QTabBar::tear {
     image: url(tear_indicator.png);
 }

 QTabBar::scroller { /* the width of the scroll buttons */
     width: 20px;
 }

 QTabBar QToolButton { /* the scroll buttons are tool buttons */
     border-image: url(scrollbutton.png) 2;
     border-width: 2px;
 }

 QTabBar QToolButton::right-arrow { /* the arrow mark in the tool buttons */
     image: url(rightarrow.png);
 }

 QTabBar QToolButton::left-arrow {
     image: url(leftarrow.png);
 }
 QTabBar::close-button {
     image: url(close.png)
     subcontrol-position: left;
 }
 QTabBar::close-button:hover {
     image: url(close-hover.png)
 }
 QTableView {
     selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,
                                 stop: 0 #FF92BB, stop: 1 white);
 }

''')
    ex.show()
    sys.exit(app.exec_())