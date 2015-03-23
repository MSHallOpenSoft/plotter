# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'som.ui'
#
# Created: Thu Mar 19 23:33:42 2015
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

class ParameterEquation(QtGui.QWidget):
    def __init__(self,parent = None):
        super(ParameterEquation,self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel()
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel()
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit()
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel()
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit()
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.setLayout(self.verticalLayout)
        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "x(u,v) =", None))
        self.label_2.setText(_translate("Form", "y(u,v) =", None))
        self.label_3.setText(_translate("Form", "z(u,v) =", None))

    def getExpression(self):
        r = []
        r.append("x = "+str(self.lineEdit.text()))
        r.append("y = "+str(self.lineEdit_2.text()))
        r.append("z = "+str(self.lineEdit_3.text()))
        return r




import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ParameterEquation()
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())
