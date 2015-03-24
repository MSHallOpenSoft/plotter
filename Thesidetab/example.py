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
import som
import som2
import tableCon
import AccodionMain


class MainFrameR(QtGui.QWidget):
    def __init__(self,parent):
        super(MainFrameR,self).__init__(parent)
        self.parent = parent
        self.table = self.parent.parent.frame
        self.tableContents = []
        self.hideTable = self.parent.parent.frame_2
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

        self.tableValue = QtGui.QTableWidget()

        self.vertical.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        
        self.widget = range5.RangeTab(self)
        self.rangeTab = accordion.Accordion(self,"Range",self.widget)
        #self.widget.setGeometry(QtCore.QRect(40, 30, 301, 91))
        #self.widget.setObjectName(_fromUtf8("widget"))
        
        self.widget_2 = settingTab.SettingTab(self)
        self.settingTab = accordion.Accordion(self,"Settings",self.widget_2)

        self.widget_3 = sliderTop.ParamList([],self)
        self.sliderTab = accordion.Accordion(self,"Parameters",self.widget_3)

        self.widget_4 = QtGui.QLineEdit(self)
        self.equationTab = accordion.Accordion(self,"Expression",self.widget_4)

        self.widget_41 = som.ExplicitEquation(self)
        self.equationTabExplicit = accordion.Accordion(self,"Expression",self.widget_41)

        self.widget_42 = som2.ParameterEquation(self)
        self.equationTabParameter = accordion.Accordion(self,"Expression",self.widget_42)









        self.sliderTab.hide()

        self.widget_43 = QtGui.QLineEdit(self)
        self.equationTable = accordion.Accordion(self,"Expression",self.widget_43)

        
        self.equationTable.frame.setText("[Table]")
        self.equationTable.frame.setReadOnly(True)
        self.equationTable.hide()
      
        self.vertical.addRow(self.equationTab)
        self.vertical.addRow(self.equationTabParameter)
        self.vertical.addRow(self.equationTabExplicit)
        self.vertical.addRow(self.equationTable)
        self.vertical.addRow(self.rangeTab)
        self.vertical.addRow(self.settingTab)
        self.vertical.addRow(self.sliderTab)

        self.equationTab.hide()
        self.equationTabParameter.hide()

        self.equationTabExplicit.frame.show()
        self.equationTabExplicit.iconButton.setIcon(self.equationTabExplicit.icon2)


        

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


    def typeSelector(self,combob):
        if(combob.currentIndex() == 0):
            self.equationTab.hide()
            self.equationTabParameter.hide()
            self.equationTabExplicit.show()
            self.equationTabExplicit.frame.show()
            self.equationTable.hide()
            self.table.hide()
            self.hideTable.hide()
        elif(combob.currentIndex() == 1):
            self.equationTab.show()
            self.equationTab.frame.show()
            self.equationTabParameter.hide()
            self.equationTabExplicit.hide()
            self.equationTable.hide()
            self.table.hide()
            self.hideTable.hide()
        elif(combob.currentIndex() == 2):
            self.equationTab.hide()
            self.equationTabParameter.show()
            self.equationTabParameter.frame.show()
            self.equationTabExplicit.hide()
            self.equationTable.hide()
            self.table.hide()
            self.hideTable.hide()
        elif(combob.currentIndex() == 3):
            self.equationTab.hide()
            self.equationTabParameter.hide()
            self.equationTabExplicit.hide()
            self.equationTable.show()
            self.equationTable.frame.show()
            #self.table.show()
            #self.hideTable.hide()
            #add listener to dispaly in table
            

            #self.saveThetableContents()
            #self.table.setData(self.tableContents)
            ##temp = self.parent.eqList[-1]
            #self.table.setPlotName(temp.label)


            #print "here"


        self.adjustSize()


    def saveThetableContents(self):
        layf = self.parent.eqList

        for i in range(len(layf)):
            print type(layf[i])
            if(layf[i].label == self.table.getPlotName()):
                layf[i].tableContents = self.table.data


    def dimensionSelector(self,combob):
        if(combob.currentIndex() == 0):   # 0 is 3D
            self.equationTabParameter.frame.label_3.show()
            self.equationTabParameter.frame.lineEdit_3.show()
            self.equationTabExplicit.frame.setfor3D()
            self.rangeTab.frame.setupfor3D()
        elif(combob.currentIndex() == 1): 
            self.equationTabExplicit.frame.setfor2D()
            self.equationTabParameter.frame.label_3.hide()
            self.equationTabParameter.frame.lineEdit_3.hide()
            self.equationTabParameter.frame.adjustSize()
            self.rangeTab.frame.setupfor2D()
        self.adjustSize()

    def getExpression(self):
        listr = []
        if(not self.equationTab.isHidden()):
            listr.append(self.equationTab.frame.text())
        elif(not self.equationTabExplicit.isHidden()):
            listr.append(self.equationTabExplicit.frame.getExpre())
        elif(not self.equationTabParameter.isHidden()):
            listr = self.equationTabParameter.frame.getExpression()
        elif(not self.equationTable.isHidden()):
            listr = self.tableContents

        return listr








    

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = MainFrameR(None)
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())

