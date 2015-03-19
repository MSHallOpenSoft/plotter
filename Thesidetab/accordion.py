# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'der.ui'
#
# Created: Mon Mar 16 14:47:03 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


class Accordion(QtGui.QWidget):

    def __init__(self,parent,label,frame):
        super(Accordion,self).__init__(parent)
        self.frame = frame
        self.label = label
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        #Form.setObjectName(_fromUtf8("Form"))
        #Form.setWindowModality(QtCore.Qt.WindowModal)
        #Form.resize(350, 130)
        self.verticalLayout = QtGui.QFormLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton()
        self.pushButton.setFlat(True)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 0))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setMargin(0)

        self.iconButton = QtGui.QPushButton()

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Add-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        

        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Minus-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.iconButton.setIcon(self.icon)
        self.iconButton.setFlat(True)
        self.iconButton.setMaximumSize(30,30)
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.addWidget(self.iconButton)
        self.horizontalLayout2.addWidget(self.pushButton)

        #self.horispacer = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        ##self.horizontalLayout2.addItem(self.horispacer)
        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setContentsMargins(0,0,0,0)
        self.horizontalLayout2.setMargin(0)

        self.verticalLayout.addRow(self.horizontalLayout2)
        #self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtGui.QFrame.Raised)
        #self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addRow(self.frame)

        #spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        #self.verticalLayout.addItem(spacerItem)
        

        self.setLayout(self.verticalLayout)
        self.frame.hide()

        self.pushButton.clicked.connect(self.accord)
        self.iconButton.clicked.connect(self.accord)

        self.retranslateUi()
        

    def retranslateUi(self):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", self.label, None))

    def accord(self):
        if(self.frame.isHidden()):
            self.iconButton.setIcon(self.icon2)
            self.frame.show()
        else:
            self.iconButton.setIcon(self.icon)
            self.frame.hide()
            self.adjustSize()
            self.parent.adjustSize()

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QPushButton("lao")
    ex = Accordion(None,"lol",w)
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())