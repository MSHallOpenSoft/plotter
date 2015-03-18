# -*- coding: utf-8 -*-

#  implementation generated from reading ui file 'sliderCh.ui'
#
# Created: Mon Mar 16 20:15:20 2015
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

class SliderRangeEditor(QtGui.QWidget):
    def __init__(self,parent = None):
        super(SliderRangeEditor,self).__init__()
        self.parent = parent
        self.label = "a"
        self.setupUi()
        

    def setupUi(self):
       # .setObjectName(_fromUtf8(""))
       # .resize(365, 49)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout99 = QtGui.QHBoxLayout()
        self.horizontalLayout99.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout99.setObjectName(_fromUtf8("horizontalLayout99"))
        self.leftRange = QtGui.QDoubleSpinBox()
        self.leftRange.setSingleStep(0.1)
        self.leftRange.setObjectName(_fromUtf8("leftRange"))
        self.horizontalLayout99.addWidget(self.leftRange)
        self.placeHolder = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeHolder.sizePolicy().hasHeightForWidth())
        self.placeHolder.setSizePolicy(sizePolicy)
        self.placeHolder.setObjectName(_fromUtf8("placeHolder"))
        self.horizontalLayout99.addWidget(self.placeHolder)
        self.rightRange = QtGui.QDoubleSpinBox()
        self.rightRange.setObjectName(_fromUtf8("rightRange"))
        self.horizontalLayout99.addWidget(self.rightRange)
        self.stepLabel = QtGui.QLabel()
        self.stepLabel.setObjectName(_fromUtf8("stepLabel"))
        self.horizontalLayout99.addWidget(self.stepLabel)
        self.stepValue = QtGui.QDoubleSpinBox()
        self.stepValue.setObjectName(_fromUtf8("stepValue"))
        self.horizontalLayout99.addWidget(self.stepValue)
        self.confirmButton = QtGui.QPushButton()
        self.confirmButton.setMinimumSize(QtCore.QSize(50, 0))
        self.confirmButton.setObjectName(_fromUtf8("confirmButton"))
        self.horizontalLayout99.addWidget(self.confirmButton)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout99.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout99)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.setLayout(self.horizontalLayout_2)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self ):
        #.setWindowTitle(_translate("", "", None))
        self.placeHolder.setText(_translate( "form",u'\u2264' +" "+self.label+" "+u'\u2264', None))
        self.stepLabel.setText(_translate( "","Step:", None))
        self.confirmButton.setText(_translate( "","Done", None))

    def getConfirmButton():
        return self.confirmButton

    def setLabel(self,label):
        self.label = label
        self.placeHolder.setText(u'\u2264' +" "+self.label+" "+u'\u2264')


import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = SliderRangeEditor()
    ex.setLabel("gte")
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())

