# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slidersd.ui'
#
# Created: Mon Mar 16 20:28:55 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import slider 

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

class SliderShower(QtGui.QWidget):
    def __init__(self,labe,parent = None):
        super(SliderShower,self).__init__(parent)
        self.setupUi(labe)

    def setupUi(self,label):
        ##Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(360, 49)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel()
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QPushButton()
        self.label_3.setFlat(True)
        self.label_3.setMaximumHeight(35)
        self.label_3.setMaximumWidth(45)
        #self.label_3.setSizePolicy(QtGui.QSizePolicy.Ignored,QtGui.QSizePolicy.Fixed)
        #self.label_3.resize(35,35)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalSlider = QtGui.QSlider()
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label_4 = QtGui.QPushButton()
        self.label_4.setFlat(True)
        self.label_4.setMaximumHeight(35)
        self.label_4.setMaximumWidth(45)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)

        self.widget = QtGui.QWidget()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.widget.setLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget)

        self.rangeChanger = slider.SliderRangeEditor(label,self)
        self.verticalLayout.addWidget(self.rangeChanger)
        self.rangeChanger.hide()

        self.setLayout(self.verticalLayout)
        self.minrange = -10
        self.maxrange = 10
        self.step = 1


        self.label_3.clicked.connect(self.onClickHandler)
        self.label_4.clicked.connect(self.onClickHandler)

        self.retranslateUi(label)
        #QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self ,label):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", label+":", None))
        self.label_3.setText(_translate("Form", str(self.minrange), None))
        self.label_4.setText(_translate("Form", str(self.maxrange), None))

    def setMinRange(self,value):
        self.minrange = value
        self.label_3.setText(str(value))

    def setMaxRange(self,value):
        self.maxrange = value
        self.label_4.setText(str(value))


    def setStep(self,value):
        self.step = value

    def onClickHandler(self):
        if(self.rangeChanger.isHidden()):
            self.rangeChanger.show()
            self.widget.hide()
            self.adjustSize()

    def doneClickHandler(self):
        if(self.widget.isHidden()):
            self.widget.show()
            valuel = self.rangeChanger.leftRange.value()
            valuer = self.rangeChanger.rightRange.value()
            stepp = self.rangeChanger.stepValue.value()
            self.setMinRange(valuel)
            self.setMaxRange(valuer)
            self.setStep(stepp)
            self.rangeChanger.hide()
            self.adjustSize()




import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = SliderShower("lo")
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())

