# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created: Wed Mar 18 13:46:41 2015
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


import settingTab
import range5
import accordion
import sliderTop


class MainFrameR(QtGui.QWidget):
    def __init__(self,parent = None):
        super(MainFrameR,self).__init__(parent)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        #Form.setObjectName(_fromUtf8("Form"))
        self.resize(400, 10)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.vertical = QtGui.QFormLayout()

        self.vertical.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        
        self.widget = range5.RangeTab()
        self.rangeTab = accordion.Accordion(self,"Range",self.widget)
        #self.widget.setGeometry(QtCore.QRect(40, 30, 301, 91))
        #self.widget.setObjectName(_fromUtf8("widget"))
        
        self.widget_2 = settingTab.SettingTab()
        self.settingTab = accordion.Accordion(self,"Settings",self.widget_2)

        self.widget_3 = sliderTop.ParamList([])
        self.sliderTab = accordion.Accordion(self,"Parameters",self.widget_3)

        self.widget_4 = QtGui.QLineEdit()
        self.equationTab = accordion.Accordion(self,"Expression",self.widget_4)


        self.sliderTab.hide()

        self.equationTab.frame.show()
      
        self.vertical.addRow(self.equationTab)
        self.vertical.addRow(self.rangeTab)
        self.vertical.addRow(self.settingTab)
        self.vertical.addRow(self.sliderTab)

        self.vertical.setSpacing(0)
        self.vertical.setContentsMargins(0,0,0,0)
        self.vertical.setMargin(0)

        ##spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
       # self.vertical.addItem(spacerItem)

        #self.horizontal = QtGui.QHBoxLayout()
        #self.horizontal.addLayout(self.vertical)
        self.setLayout(self.vertical)
        #self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = MainFrameR()
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())

