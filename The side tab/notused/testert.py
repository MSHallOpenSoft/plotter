# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'der.ui'
#
# Created: Mon Mar 16 14:47:03 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import accordion
import settingTab
import range
import sliderTop
from AccodionMain import AccordionMain

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


class MainFrameR(QtGui.QWidget):

	def __init__(self):
		super(MainFrameR,self).__init__()
		self.parent = parent
		self.componentLabels = ["Expression","Range","Parameters","Settings"]
        self.setupUI(self)

	def setupUI(self,Form):
		Form.resize(400,150)

		self.verticalLayout = QtGui.QVBoxLayout()

		#self.exprEdit = QtGui.QPushButton("hjtu")
		#self.expressionEdit = AccordionMain(self,self.componentLabels[0],self.exprEdit)
        self.pushButton=QtGui.QPushButton("kdkd")
        self.verticalLayout.addWidget(self.pushButton)



	def see(self):
		print "haha"


import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = MainFrameR()
    #for i in range(10):
       # ex.addParameter("kas")
    ex.show()
    #ex.see()
    #ex.showMaximized()
    sys.exit(app.exec_())
