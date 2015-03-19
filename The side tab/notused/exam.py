from PySide.QtGui import *
from PySide.QtCore import *

class ClickableLabel(QLabel):
    """
        A Label that emits a signal when clicked.
    """

    def __init__(self, *args):
        super(ClickableLabel,self).__init__(*args)

    def mousePressEvent(self, event):
        self.action.triggered.emit()

# example

class clickedButton(QPushButton):
	
	 def had(self):
		if(self.isHidden()):
			self.show()
		else:
			self.hide()
	
	
	
app = QApplication([])
window = QWidget()
layout = QVBoxLayout(window)
labelA = ClickableLabel('Click on me for more.')
#labelA.setMaximumSize(QSize(16777215, 30))
layout.addWidget(labelA)
labelB = clickedButton('Here I am.')
layout.addWidget(labelB)
labelB.hide()
labelc = ClickableLabel('Click on me for knoe more.')
layout.addWidget(labelc)

labeld = clickedButton('Here I am.HAHA')
layout.addWidget(labeld)
labeld.hide()

action = QAction('Action', labelA)
labelA.action = action
action.triggered.connect(labelB.had)


action2 = QAction('Action', labeld)
labelc.action = action2
action2.triggered.connect(labeld.had)

window.show()
app.exec_()
