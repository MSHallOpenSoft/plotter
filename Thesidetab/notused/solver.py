# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acods.ui'
#
# Created: Sun Mar 15 19:05:35 2015
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
        

class ClickableLabel(QtGui.QLabel):
    """
        A Label that emits a signal when clicked.
    """

    def __init__(self):
        super(ClickableLabel,self).__init__()

    def mousePressEvent(self, event):
        self.action.triggered.emit()
        
        
class clickedFrame(QtGui.QFrame):
	
	 def had(self):
		if(self.isHidden()):
			self.show()
		else:
			self.hide()

class ExpressionShower(QtGui.QWidget):


    def __init__(self):
		super(ExpressionShower,self).__init__()
		self.setupUI()
	
    def setupUI(self):
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = ClickableLabel()
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(5)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.frame = clickedFrame(self)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.verticalLayout)

        

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        self.label.setText("test")
	def SetName(n):
		self.nameh = n



import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = ExpressionShower()
    w.show()
    sys.exit(app.exec_())
		
		