# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'der.ui'
#
# Created: Mon Mar 16 14:47:03 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import example
import AccodionMain

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


class DockContents(QtGui.QWidget):

    def __init__(self,parent = None):
		super(DockContents,self).__init__(parent)
		self.parent = parent
		self.setupUI()

    def setupUI(self):
        self.resize(400,700)
        self.setMinimumWidth(360)
        self.vertical = QtGui.QVBoxLayout()

        self.addNewPlotButton = QtGui.QPushButton("Add a new plot")

        self.vertical.addWidget(self.addNewPlotButton)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))

        self.widget = QtGui.QWidget()
        self.vertical2 = QtGui.QFormLayout()
        #self.vertical2.setHorizontalSpacing(0)
        self.widget.setLayout(self.vertical2)
        self.vertical2.setSpacing(0)
        self.vertical2.setContentsMargins(0,0,0,0)
        self.vertical2.setMargin(0)
        self.scrollArea.setWidget(self.widget)



        self.vertical.addWidget(self.scrollArea)

        self.horizontal = QtGui.QHBoxLayout()

        self.horizontal.addLayout(self.vertical)
        self.setLayout(self.horizontal)

        self.addNewPlotButton.clicked.connect(self.addNewEquation)
        self.noOfEquations = 0
        self.eqList = []

    def addNewEquation(self):
        self.noOfEquations = self.noOfEquations + 1
        frame = AccodionMain.AccordionMain(self,"Plot_"+str(self.noOfEquations),example.MainFrameR(self))
        frame.frame.show()
        self.eqList.append(frame)
        self.vertical2.addWidget(frame)

	

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = DockContents()
    #for i in range(10):
       # ex.addParameter("kas")
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())




