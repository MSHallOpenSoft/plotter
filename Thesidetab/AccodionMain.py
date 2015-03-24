# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'der.ui'
#
# Created: Mon Mar 16 14:47:03 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from customThreading import MyThread
import tableCon

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


class AccordionMain(QtGui.QWidget):
    def __init__(self,parent,label,frame):
        super(AccordionMain,self).__init__()
        self.frame = frame
        self.label = label
        self.parent = parent
        self.setupUi()
        self.plotThread = MyThread(self)
        self.connect(self.plotThread,QtCore.SIGNAL('finished'),self.finishedPlotting)
        self.plottingNow=False

    def finishedPlotting(self):
      print("finished plotting")

    def plot3d_spawn_thread(self,**kwargs):
      self.plotThread.plot3d(**kwargs)
      print("foooooooooo")
      return

    def setupUi(self):
        ##Form.setWindowModality(QtCore.Qt.WindowModal)
        #Form.resize(350, 130)
        
        self.verticalLayout = QtGui.QVBoxLayout()
        self.resize(350,130)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton()
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"  font-size: 14px;\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  background:white;\n"
"  color: black;\n"
"  padding: 3px 10px;\n"
"  border-radius: 2px;\n"
"}"))


        self.iconButton = QtGui.QPushButton()

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/closeButton.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconButton.setIcon(self.icon)
        self.iconButton.setFlat(True)
        self.iconButton.setMaximumSize(40,40)

        self.drawButton = QtGui.QPushButton("Draw")
        self.drawButton.setMaximumSize(60,30)
        self.drawButton.clicked.connect(self.plot)
        self.drawButton.setStyleSheet("QPushButton{font-size:13px; padding:2px;}")
        self.iconButton.setStyleSheet("QPushButton{ padding:1px;}")
        self.horizontalLayout2 = QtGui.QHBoxLayout()
        self.horizontalLayout2.addWidget(self.iconButton)
        self.horizontalLayout2.addWidget(self.pushButton)
        self.horizontalLayout2.addWidget(self.drawButton)

        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setContentsMargins(0,0,0,0)
        self.horizontalLayout2.setMargin(0)

        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setMargin(0)


        self.verticalLayout.addLayout(self.horizontalLayout2)
        #self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtGui.QFrame.Raised)
        #self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.setLayout(self.verticalLayout)
        self.iconButton.clicked.connect(self.closeHandler)
        self.frame.hide()
        self.pushButton.clicked.connect(self.accord)
        self.retranslateUi()

    def plot(self):
      #print(str(self.frame.widget_4.text()))
      curTab=self.parent.parent.tabIdentifier
      curPlot=int(self.label[5:])
      print(curTab,curPlot)
      print(self.parent.parent.tabIdentifier)
      #print(self.plottingIdentifier)
      print("fooooooooooooooooooooooooooooooooo")
      print(self.frame.rangeTab.frame.XRight)
      print(self.frame.rangeTab.frame.XLeft)
      print(self.frame.settingTab.frame.comboBox.currentText())
      #self.frame.settingTab.label_3.
      color= self.frame.settingTab.frame.label_3.color()
      print(color)
      print(QtGui.QColor(color).red())
      #colorr=QtGui.QColor(color).red()
      #colorb=QtGui.QColor(color).blue()
      #colorg=QtGui.QColor(color).green()
      color=QtGui.QColor(color).getRgbF()[0:-1]
      print(color)
      currentDim=self.frame.settingTab.frame.comboBox.currentText()
      transparency=self.frame.settingTab.frame.horizontalSlider_3.value()
      thickness=self.frame.settingTab.frame.horizontalSlider_2.value()
      resolution=self.frame.settingTab.frame.horizontalSlider.value()
      print(resolution)
      print(thickness)
      print(transparency)
      transparency=transparency/100.0
      print(transparency)
      opacity=1-transparency
      print(opacity)
      print(currentDim)

      expr=self.frame.getExpression()
      print(expr)
      eqn=""
      if len(expr)==1:
        eqn=expr[0]
      
      x_start=self.frame.rangeTab.frame.XLeft.value()
      x_end=self.frame.rangeTab.frame.XRight.value()
      y_start=self.frame.rangeTab.frame.YLeft.value()
      y_end=self.frame.rangeTab.frame.YRight.value()
      z_start=self.frame.rangeTab.frame.ZRight.value()
      z_end=self.frame.rangeTab.frame.ZLeft.value()
      if(currentDim=="3D"):
        self.plot3d_spawn_thread(curTab=curTab
          ,curPlot=curPlot,eqn=eqn,color=color,line_width=thickness,opacity=opacity,x_start=x_start,x_end=x_end,no_x_points=10
          ,y_start=y_start,y_end=y_end,no_y_points=10,z_start=z_start,z_end=z_end,no_z_points=10)
      else:
        print("plot 2d")
      #print( self.parent.parent.mayavi_widget.visualization)
        

    def retranslateUi(self):
        #Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", self.label, None))

    def accord(self):
        if(self.frame.isHidden()):
            
            self.frame.show()
            print "here"
            print type(self.parent.parent)
            print type(self.frame.tableValue)
            hlayout = self.parent.parent.horizontalLayout_3
            print hlayout.count()
            j = 1;
            for i in range(hlayout.count()):
              if(type(hlayout.itemAt(i)) == tableCon.TableContents):
                frem = hlayout.itemAt(i)
                j = i

            hlayout.takeAt(i)



            
            hlayout.insertWidget(i,self.frame.table)
            
            self.parent.parent.adjustSize()
            
        else:
          j = 1;
          hlayout = self.parent.parent.horizontalLayout_3
          for i in range(hlayout.count()):
            if(type(hlayout.itemAt(i)) == tableCon.TableContents):
              frem = hlayout.itemAt(i)
              j = i
          self.parent.parent.horizontalLayout_3.takeAt(j)
          self.frame.hide()

    def closeHandler(self):
        if(self):
            self.deleteLater()

    def getMainFrame(self):
      return parent

    

import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QPushButton("lao")
    ex = AccordionMain(None,"lol",w)
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())
