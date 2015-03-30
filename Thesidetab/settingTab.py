#!/user/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue Mar 17 23:25:54 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import colorButton
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


class SettingTab(QtGui.QWidget):

    def __init__(self,parent = None):
        super(SettingTab,self).__init__(parent)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
       
        #.resize(350,300)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        #self.groupBox_2.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(_fromUtf8(""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox()
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.horizontalSlider = QtGui.QSlider(self.groupBox)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setStyleSheet(_fromUtf8(""))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_8.addWidget(self.horizontalSlider)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_9.addWidget(self.label_2)
        self.label_3 = colorButton.QColorButton(self.groupBox)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(20, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_9.addWidget(self.label_3)

        self.label_Y = colorButton.QColorButton(self.groupBox)
        
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_Y.setSizePolicy(sizePolicy)
        self.label_Y.setMinimumSize(QtCore.QSize(20, 20))
        self.label_Y.setObjectName(_fromUtf8("label_3"))
        self.label_Y.setColor("#00ff00")
        self.horizontalLayout_9.addWidget(self.label_Y)

        self.label_Z = colorButton.QColorButton(self.groupBox)
        
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        ##sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_Z.setSizePolicy(sizePolicy)
        self.label_Z.setMinimumSize(QtCore.QSize(20, 20))
        self.label_Z.setObjectName(_fromUtf8("label_3"))
        self.label_Z.setColor("#0000ff")
        self.horizontalLayout_9.addWidget(self.label_Z)

        self.label_Y.hide()
        self.label_Z.hide()


        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_9.addWidget(self.radioButton)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_9.addWidget(self.radioButton_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.comboBox_4)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_10.addWidget(self.label_6)
        self.horizontalSlider_2 = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalLayout_10.addWidget(self.horizontalSlider_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_11.addWidget(self.label_7)
        self.horizontalSlider_3 = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.horizontalLayout_11.addWidget(self.horizontalSlider_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.groupBox)
        self.spacerItem1 = QtGui.QSpacerItem(1, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)
        self.setLayout(self.verticalLayout)
        self.radioButton.setChecked(True)

        self.colorAxis = ["#ff0000","#00ff00","#0000ff"]

        self.radioButton.clicked.connect(lambda: self.changedAxis(0))
        self.radioButton_2.clicked.connect(lambda: self.changedAxis(2))
        self.radioButton_3.clicked.connect(lambda: self.changedAxis(1))
        i = 0
        paren = self.parent
        self.comboBox_2.currentIndexChanged.connect(lambda :paren.typeSelector(self.comboBox_2))
        self.comboBox.currentIndexChanged.connect(lambda :paren.dimensionSelector(self.comboBox))


        self.retranslateUi()
       # QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self ):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_2.setTitle(_translate("Form", "Graph", None))
        self.comboBox.setItemText(0, _translate("Form", "3D", None))
        self.comboBox.setItemText(1, _translate("Form", "2D", None))
        self.comboBox_2.setItemText(0, _translate("Form", "Regular", None))
        self.comboBox_2.setItemText(1, _translate("Form", "Implicit", None))
        self.comboBox_2.setItemText(2, _translate("Form", "Parametric", None))
        self.comboBox_2.setItemText(3, _translate("Form", "Table", None))
        self.groupBox.setTitle(_translate("Form", "Appearance", None))
        self.label.setText(_translate("Form", "Resolution", None))
        self.label_2.setText(_translate("Form", "Color:", None))
        #self.label_3.setText(_translate("Form", "color", None))
        self.label_4.setText(_translate("Form", "Along", None))
        self.radioButton.setText(_translate("Form", "X", None))
        self.radioButton_3.setText(_translate("Form", "Y", None))
        self.radioButton_2.setText(_translate("Form", "Z", None))
        self.label_5.setText(_translate("Form", "Draw", None))
        self.comboBox_4.setItemText(0, _translate("Form", "Points", None))
        self.comboBox_4.setItemText(1, _translate("Form", "Surface", None))
        self.comboBox_4.setItemText(2, _translate("Form", "Contour", None))
        self.comboBox_4.setItemText(3, _translate("Form", "Lines", None))
        self.comboBox_4.setItemText(4, _translate("Form", "S+L", None))
        self.label_6.setText(_translate("Form", "Thickness", None))
        self.label_7.setText(_translate("Form", "Transparency", None))

    def changedAxis(self,id):
        self.label_3.hide()
        self.label_Z.hide()
        self.label_Y.hide()

        if(id == 0):
            self.label_3.show()
        elif(id == 1):
            self.label_Y.show()
        else:
            self.label_Z.show()


        




import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = SettingTab()
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())
