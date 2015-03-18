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


class AccordionMain(QtGui.QWidget):

    def __init__(self,parent,label,frame):
        super(AccordionMain,self).__init__()
        self.frame = frame
        self.label = label
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        ##Form.setWindowModality(QtCore.Qt.WindowModal)
        #Form.resize(350, 130)
        
        self.verticalLayout = QtGui.QVBoxLayout()
        self.resize(350,130)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton()
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.drawButton = QtGui.QPushButton("Draw")
        self.drawButton.setMaximumSize(60,30)
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.addWidget(self.pushButton)
        self.horizontalLayout2.addWidget(self.drawButton)

        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setContentsMargins(0,0,0,0)
        self.horizontalLayout2.setMargin(0)

        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setMargin(0)


        self.verticalLayout.addLayout(self.horizontalLayout2)
        #self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtGui.QFrame.Raised)
        #self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)

        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.setLayout(self.verticalLayout)



        self.frame.hide()

        self.pushButton.clicked.connect(self.accord)
        

        self.retranslateUi()
        

    def retranslateUi(self):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", self.label, None))

    def accord(self):
        if(self.frame.isHidden()):
            
            self.frame.show()
        else:
            
            self.frame.hide()

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QPushButton("lao")
    ex = AccordionMain(None,"lol",w)
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())