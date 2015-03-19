from PyQt4 import QtCore
from PyQt4 import QtGui


import sys, random
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

class ColorPicker(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setFixedSize(500,100)
		self.move(250,250)
		self.setWindowTitle("Color Picker")

		self.button = QtGui.QPushButton("Open Color Picker",self)
		self.button.move(25,25)
		self.button.clicked.connect(self.OpenColorPicker)

	def OpenColorPicker(self):
		self.window=QtGui.QColorDialog()
		cp=self.window.getColor(options = QtGui.QColorDialog.ShowAlphaChannel)
		print (str(cp.red()) + "." + str(cp.green()) + "." +str(cp.blue()))
		#tu = QtGui.QColorDialog.customCount()
		#print tu
app = QtGui.QApplication(sys.argv)

cp = ColorPicker()
cp.show()

sys.exit(app.exec_())