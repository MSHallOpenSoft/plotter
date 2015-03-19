# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'range.ui'
#
# Created: Tue Mar 17 23:44:07 2015
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

class RangeTab(QtGui.QWidget):
    def __init__(self,parent = None):
        super(RangeTab,self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        #Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(368, 129)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.XLeft = QtGui.QDoubleSpinBox()
        self.XLeft.setObjectName(_fromUtf8("Xleft"))
        self.XLeft.setMinimum(-99999)
        self.horizontalLayout.addWidget(self.XLeft)
        self.label_2 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.XRight = QtGui.QDoubleSpinBox()
        self.XRight.setObjectName(_fromUtf8("XRight"))
        self.XRight.setMinimum(-99999)
        self.horizontalLayout.addWidget(self.XRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.YLeft = QtGui.QDoubleSpinBox()
        self.YLeft.setObjectName(_fromUtf8("YLeft"))
        self.YLeft.setMinimum(-99999)
        self.horizontalLayout_2.addWidget(self.YLeft)
        self.label_4 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.YRight = QtGui.QDoubleSpinBox()
        self.YRight.setObjectName(_fromUtf8("YRight"))
        self.YRight.setMinimum(-99999)
        self.horizontalLayout_2.addWidget(self.YRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(20, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.ZLeft = QtGui.QDoubleSpinBox()
        self.ZLeft.setObjectName(_fromUtf8("ZLeft"))
        self.ZLeft.setMinimum(-99999)
        self.horizontalLayout_3.addWidget(self.ZLeft)
        self.label_6 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(20, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.ZRight = QtGui.QDoubleSpinBox()
        self.ZRight.setObjectName(_fromUtf8("ZRight"))
        self.ZRight.setMinimum(-99999)
        self.horizontalLayout_3.addWidget(self.ZRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.spacerItem1 = QtGui.QSpacerItem(1, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)

        self.setLayout(self.verticalLayout)
        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
       # Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "X : ", None))
        self.label_2.setText(_translate("Form", "to", None))
        self.label_3.setText(_translate("Form", "Y:", None))
        self.label_4.setText(_translate("Form", "to", None))
        self.label_5.setText(_translate("Form", "Z:", None))
        self.label_6.setText(_translate("Form", "to", None))
        self.XRight.setValue(10)
        self.XLeft.setValue(-10)
        self.YRight.setValue(10)
        self.YLeft.setValue(-10)
        self.ZRight.setValue(10)
        self.ZLeft.setValue(-10)



import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = RangeTab()
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())

