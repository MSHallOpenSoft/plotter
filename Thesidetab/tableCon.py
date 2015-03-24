# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'der.ui'
#
# Created: Mon Mar 16 14:47:03 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
''''
@Varun : Need to check the close delimeter choose action properly execute and check



'''


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


class TableContents(QtGui.QFrame):

    def __init__(self,parent = None):
        super(TableContents,self).__init__(parent)
        self.parent = parent
        self.setupUI()

    def setupUI(self):
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(320, 16777215))
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Raised)
        self.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.toolButton_7 = QtGui.QToolButton(self)
        self.toolButton_7.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_7.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_7.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Add-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon1)
        self.toolButton_7.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_5.addWidget(self.toolButton_7)
        self.toolButton_9 = QtGui.QToolButton(self)
        self.toolButton_9.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_9.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_9.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Minus-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon2)
        self.toolButton_9.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.horizontalLayout_5.addWidget(self.toolButton_9)
        self.toolButton_8 = QtGui.QToolButton(self)
        self.toolButton_8.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_8.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_8.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Folder-Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon3)
        self.toolButton_8.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_5.addWidget(self.toolButton_8)
        self.toolButton_5 = QtGui.QToolButton(self)
        self.toolButton_5.setMinimumSize(QtCore.QSize(10, 0))
        self.toolButton_5.setMaximumSize(QtCore.QSize(35, 16777215))
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Save-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(40, 30))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtGui.QTableWidget(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setStyleSheet(_fromUtf8(""))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.header=self.tableWidget.horizontalHeader();
        self.header.setResizeMode(QtGui.QHeaderView.Stretch);
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton_21 = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_3.addWidget(self.pushButton_21)
        #self.horizontalLayout_3.addWidget(self)
        self.toolButton_8.clicked.connect(self.showFileChooser)
        self.toolButton_7.clicked.connect(self.addRowDataPoint)
        self.toolButton_9.clicked.connect(self.removeRowDataPoint)
        self.toolButton_5.clicked.connect(self.saveDataValuesToFile)

        self.retranslateUI()

    def retranslateUI(self):
        self.pushButton_3.setText(_translate("MainWindow", "Hide", None))
        self.toolButton_7.setToolTip(_translate("MainWindow", "Add", None))
        self.toolButton_7.setText(_translate("MainWindow", "...", None))
        self.toolButton_9.setToolTip(_translate("MainWindow", "Remove", None))
        self.toolButton_9.setText(_translate("MainWindow", "...", None))
        self.toolButton_8.setToolTip(_translate("MainWindow", "Import Coordinates", None))
        self.toolButton_8.setText(_translate("MainWindow", "...", None))
        self.toolButton_5.setToolTip(_translate("MainWindow", "Export Coordinates", None))
        self.toolButton_5.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z", None))
        self.pushButton_21.setText(_translate("MainWindow", "Redraw", None))

    def saveDataValuesToFile(self):
        #EDIT : here add the filename to be stored as
        #pname = ex.getTabName()
        import csv
        #savFile = open(pname+'.csv','w')
        fpname = QtGui.QFileDialog.getSaveFileName(self,'Select Save File')
        with open(fpname + ".csv",'w') as output:
            writeHead = csv.writer(output,delimiter=',',lineterminator='\n')
            for i in range (0,self.tableWidget.rowCount()):
                row = list()

                for j in range (0,self.tableWidget.columnCount()):
                    try :
                        item = self.tableWidget.item(i,j).text()
                    except Exception,e:
                        continue
                    #toInt = int(item)
                    print item
                    row.append(item)

                #print row
                writeHead.writerow(row)

        #savFile.close()

    def addRowDataPoint(self):
        rowC = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowC)

    def removeRowDataPoint(self):
        if(self.tableWidget.currentRow()==-1):
            self.errorRemoveDataPoint()
        else:
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            self.tableWidget.setCurrentCell(-1,-1)

    def errorRemoveDataPoint(self):
        # Dialog = QtGui.QDialog()
        # u = Ui_Dialog_2("Please select the data point to remove")
        # u.setupUi(Dialog)
        # Dialog.exec_()
        errorDialog = QtGui.QErrorMessage()
        #print "here"
        errorDialog.showMessage("Please select the data point to remove","error")
        #print "here"
        errorDialog.exec_()

    def showFileChooser(self):
        fname = QtGui.QFileDialog.getOpenFileName(self,'Select File to Open')
        self.delimit=','
        import csv
        f = open('_.csv','w')
        try:
            f=open(fname,'rt')
            reader = csv.reader(f)
            num_rows = 0
            for row in reader:
                num_rows=num_rows+1

            with open(fname,'r') as fil :
               text = fil.read()

            count_comma=0
            for char in text:
               if char==',':
                  count_comma=count_comma+1

            if ((count_comma !=num_rows * 2) and (count_comma != num_rows)) : # i.e. it is NOT a csv file
                self.showSelectDelimiter()

            self.tableWidget.setRowCount(num_rows)
            ## create items in all added 
            rowno_=0
            f=open(fname,'rt')
            reader=csv.reader(f,delimiter=self.delimit)
            if(count_comma == num_rows):        # i.e. values correspond to a 2D graph
                col_count = 2
                self.tableWidget.setColumnHidden(2,True)
                print "123"
            elif (count_comma == (num_rows*2)):
                col_count = 3
                self.tableWidget.setColumnHidden(2,False)
                print "456"

            try:   
                for row in reader:
                    for col in range (0,col_count):
                        float(row[col])
                        item = QtGui.QTableWidgetItem(row[col])
                        self.tableWidget.setItem(rowno_,col,item)
                    rowno_=rowno_+1        

                self.tableWidget.setRowCount(rowno_)
                
            except Exception, e:
                self.showU=self.showInvalidValueError()
                self.tableWidget.setRowCount(0)   
            except Exception, e: 
                print""

        finally:
            f.close()                                  
                

    def showInvalidValueError(self):
        errorDialog = QtGui.QErrorMessage()
        #print "here"
        errorDialog.showMessage("Cannot Import Values!! Data Invalid","error")
        #print "here"
        errorDialog.exec_()

    def showSelectDelimiter(self):
      Dialog = QtGui.QDialog()
      u = Ui_Dialog()
      u.setupUi(Dialog)
      dialg = StartDialog()
      if dialg.exec_():
        self.delimit = dialg.getDelim()
      #self.showFileChooser()

        


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        #Dialog.resize(500,468)
        self.ch = " "
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 110, 211, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 110, 141, 32))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(False)
        self.widget.setGeometry(QtCore.QRect(50, 200, 311, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)   
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.widget.setPalette(palette)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 291, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(60, 20, 361, 71))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_6 = QtGui.QLabel(self.widget_2)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 281, 22))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.widget_2)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 331, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(240, 160, 83, 22))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(320, 160, 41, 31))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(lambda:self.storeDelim)
        self.comboBox.activated.connect(self.storeDelim)
        self.textEdit.textChanged.connect(self.storeDelim)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Choose Delimiter", None))
        self.label.setText(_translate("Dialog", "Please specify delimiter :", None))
        self.comboBox.setItemText(0, _translate("Dialog", "\',\' (comma)", None))
        self.comboBox.setItemText(1, _translate("Dialog", "\' \' (space)", None))
        self.comboBox.setItemText(2, _translate("Dialog", "\';\' (semicolon)", None))
        self.comboBox.setItemText(3, _translate("Dialog", "\'-\' (dash)", None))
        self.comboBox.setItemText(4, _translate("Dialog", "\':\' (colon)", None))
        self.comboBox.setItemText(5, _translate("Dialog", "Specify other", None))
        self.label_2.setText(_translate("Dialog", "The Plotter retrieves values ", None))
        self.label_3.setText(_translate("Dialog", "separated by the chosen delimiter", None))
        self.label_6.setText(_translate("Dialog", "The Plotter has detected that the", None))
        self.label_7.setText(_translate("Dialog", "selected file is NOT in proper csv format", None))
        self.label_4.setText(_translate("Dialog", "Specify :", None))    

    def storeDelim(self):
        if self.comboBox.currentIndex()==0:
            self.ch = ','
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==1:
            self.ch = ' '
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==2:
            self.ch = ';'
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==3:
            self.ch = '-'
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==4:
            self.ch = ':'
            self.label_4.setEnabled(False)
            self.textEdit.setEnabled(False)
        elif self.comboBox.currentIndex()==5:
            self.label_4.setEnabled(True)
            self.textEdit.setEnabled(True)
            self.ch=str(self.textEdit.toPlainText())

    def getDelim(self):
        return self.ch

class StartDialog(QtGui.QDialog, Ui_Dialog): 
    def __init__(self,parent=None): 
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)
import sys
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = TableContents(None)
    #for i in range(10):
       # ex.addParameter("kas")
    ex.show()
    #ex.showMaximized()
    sys.exit(app.exec_())