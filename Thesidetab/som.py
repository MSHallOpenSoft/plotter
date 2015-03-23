# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'som.ui'
#
# Created: Thu Mar 19 21:53:16 2015
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

class ExplicitEquation(QtGui.QWidget):
    def __init__(self,parent = None):
        super(ExplicitEquation,self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setContentsMargins(5,5,5,5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox()
        self.comboBox.setMinimumSize(50, 30)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        #rm.setWindowTitle(_translate("Form", "Form", None))
        self.comboBox.setItemText(1, _translate("Form", "x = ", None))
        self.comboBox.setItemText(0, _translate("Form", "y = ", None))
        self.comboBox.setItemText(2, _translate("Form", "z = ", None))
        self.comboBox.setItemText(3, _translate("Form", "x > ", None))
        self.comboBox.setItemText(4, _translate("Form", "y >", None))
        self.comboBox.setItemText(5, _translate("Form", "z >", None))
        self.comboBox.setItemText(6, _translate("Form", "x <", None))
        self.comboBox.setItemText(7, _translate("Form", "y < ", None))
        self.comboBox.setItemText(8, _translate("Form", "z <", None))
        self.comboBox.setItemText(9, _translate("Form", "x "+u"\u2264", None))
        self.comboBox.setItemText(10, _translate("Form", "y "+u"\u2264", None))
        self.comboBox.setItemText(11, _translate("Form", "z "+u"\u2264", None))
        self.comboBox.setItemText(12, _translate("Form", "x "+u"\u2265", None))
        self.comboBox.setItemText(13, _translate("Form", "y "+u"\u2265", None))
        self.comboBox.setItemText(14, _translate("Form", "z "+u"\u2265", None))
        self.comboBox.setCurrentIndex(2)

    def getExpre(self):
        st = self.comboBox.currentText() + self.lineEdit.text()
        return st

    def setfor2D(self):
        self.comboBox.setCurrentIndex(0)

    def setfor3D(self):
        self.comboBox.setCurrentIndex(2)


import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ExplicitEquation()
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())

