
from PyQt4 import QtCore, QtGui
from function_2 import Ui_DockWidget

class at(Ui_DockWidget):
    def __init__(self, parent=None, name=None, fl=0):
        Ui_DockWidget.__init__(self)

if __name__ == "__main__":
    import sys
    a = QtGui.QApplication(sys.argv)
    #QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w=at()
    w.show()
    a.exec_loop()