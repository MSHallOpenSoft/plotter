# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Mar 17 22:49:40 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import copy
import slidersd

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


class LabelButton(QtGui.QPushButton):

    def __init__(self,labelName,parent = None):
        super(LabelButton,self).__init__(parent)
        self.parent = parent
        self.setMaximumSize(30,30)
        self.setText(labelName)
        self.name = labelName

    mySignal = QtCore.pyqtSignal(QtGui.QWidget)
    def mousePressEvent(self, *args, **kwargs):
        self.mySignal.emit(self)

class ParamList(QtGui.QWidget):

    def __init__(self,labelsP,parent=None):
        super(ParamList,self).__init__(parent)
        self.labels = copy.deepcopy(labelsP)
        self.buttonList = []
        self.setupUi()


    def setupUi(self):
        #Form.setObjectName(_fromUtf8("Form"))
        #Form.resize(360, 40)
        #Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(72, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 50))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 76, 40))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.hlayout = QtGui.QHBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.hlayout)
        spacerItem2 = QtGui.QSpacerItem(10, 1, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.pushButton = QtGui.QPushButton()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(10, 1, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        #spacerItem1 = QtGui.QSpacerItem(1, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        #self.verticalLayout.addItem(spacerItem1)
        self.sliderList = []
        self.setLayout(self.verticalLayout)

        self.verticalLayout.setMargin(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
       # Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Add Slider:", None))
        self.pushButton.setText(_translate("Form", "all", None))
        #print "here"
        if(len(self.labels) <= 1):
            self.pushButton.hide()

        for i in range(len(self.labels)): 
            self.buttonList.append(LabelButton(self.labels[i]))
            self.buttonList[i].mySignal.connect(self.onClickHandler)
            self.hlayout.addWidget(self.buttonList[-1])
        spacerItem2 = QtGui.QSpacerItem(10, 1, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlayout.addSpacerItem(spacerItem2)
        

    def addParameter(self,name):
        self.labels.append(name)
        self.but = LabelButton(name)
        self.buttonList.append(self.but)
        #print "here"
        i = self.hlayout.count() - 1
        self.but.mySignal.connect(self.onClickHandler)
        self.hlayout.insertWidget(i,self.but)

    def onClickHandler(self,ref):
        #print "here"
        i = self.hlayout.indexOf(ref)
       # print i
        f = slidersd.SliderShower(ref.name)
        self.sliderList.append(f)
        self.hlayout.removeWidget(ref)
       # print self.hlayout.count()
        if(self.hlayout.count() <= 2):
            self.pushButton.hide()

        if(self.hlayout.count() == 1):

            #print "here"
            self.verticalLayout.removeItem(self.horizontalLayout_2)
            self.deleteLayout(self.horizontalLayout_2)

        ref.deleteLater()
        self.verticalLayout.addWidget(f)
        self.scrollAreaWidgetContents.adjustSize()

    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            #sip.delete(layout)


import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ParamList(["g","k"])
    ex.addParameter("d")
    #for i in range(10):
       # ex.addParameter("kas")
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())