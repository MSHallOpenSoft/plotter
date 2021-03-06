# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acods.ui'
#
# Created: Mon Mar 16 01:07:14 2015
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


class ClickableLabel(QtGui.QPushButton):
    """
        A Label that emits a signal when clicked.
    """

    def __init__(self,*args):
        super(ClickableLabel,self).__init__(*args)

    # def mousePressEvent(self, event):
    #      self.action.triggered(1).emit()
        
        
class clickedFrame(QtGui.QFrame):
    
     def had(self):
        if(self.isHidden()):
            self.show()
        else:
            self.hide()

class Ui_Form(QtGui.QWidget):
    
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(400, 130)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = ClickableLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
       # self.label.setAlignment(QtCore.Qt.AlignCenter)
       # self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.frame = clickedFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label.clicked.connect(self.frame.had)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Add new Plot", None))

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Ui_Form()
    w.show()
    sys.exit(app.exec_())

