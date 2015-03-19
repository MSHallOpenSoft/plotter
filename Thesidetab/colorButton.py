from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal


class QColorButton(QtGui.QPushButton):
    '''
    Custom Qt Widget to show a chosen color.

    Left-clicking the button shows the color-chooser, while
    right-clicking resets the color to None (no-color).    
    '''

    colorChanged = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QColorButton, self).__init__(*args, **kwargs)

        self._color = '#FF0000' 
        self.setMaximumWidth(32)
        self.pressed.connect(self.onColorPicker)
        self.setStyleSheet("background-color: %s;" % self._color)
        #self.setFlat(True)

    def setColor(self, color):
        if color != self._color:
            self._color = color
            #self.colorChanged.emit()

        
            self.setStyleSheet("background-color: %s;" % self._color)
        

    def color(self):
        return self._color

    def onColorPicker(self):
        '''
        Show color-picker dialog to select color.

        Qt will use the native dialog by default.

        '''
        dlg = QtGui.QColorDialog()
        if self._color:
            dlg.setCurrentColor(QtGui.QColor(self._color))

        if dlg.exec_():
            print dlg.currentColor().name()
            self.setColor(dlg.currentColor().name())

    def mousePressEvent(self, e):
        ##if e.button() == QtGui.RightButton:
            #self.setColor(None)

        return super(QColorButton, self).mousePressEvent(e)