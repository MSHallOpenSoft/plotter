# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'functions.ui'
#
# Created: Sun Mar 15 20:35:30 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_DockWidget_2(QtGui.QDockWidget):
    def __init__(self,parent,target_area):
        super(Ui_DockWidget_2, self).__init__(parent)
        self.setupUi(self)
        self.target=target_area
        self.hide()
        self.setFloating(True)

    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(293, 250)
        DockWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        '''DockWidget.setStyleSheet("\n"
            " QPushButton{ \n"
"position: relative;\n"
" border:none;\n"
" outline:none; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color: white;\n"
" padding: 6px 20px; \n"
"border-radius: 2px;\n"
" font-size: 15px;\n"
" }\n"
" QPushButton:hover:!pressed{ \n"
"position: relative;\n"
" border: none; \n"
"outline:none;\n"
" background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255));\n"
" color: white; \n"
"padding: 6px 20px; \n"
"border-radius: 2px;\n"
" font-size:15px; \n"
"} \n"
" QTabWidget{\n"
" background-color:#737373;\n"
" border:none;\n"
" padding:0px; \n"
" }\n")'''
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(275, 16777215))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.tab)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        '''self.pushButton_10 = QtGui.QPushButton(self.tab)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 5, 0, 1, 1)'''
        '''self.pushButton_9 = QtGui.QPushButton(self.tab)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 1)'''
        '''self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)'''
        '''self.pushButton_8 = QtGui.QPushButton(self.tab)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)'''
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        '''self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)'''
        self.pushButton_11 = QtGui.QPushButton(self.tab)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)
        '''self.pushButton_12 = QtGui.QPushButton(self.tab)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout.addWidget(self.pushButton_12, 3, 1, 1, 1)'''
        '''self.pushButton_13 = QtGui.QPushButton(self.tab)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout.addWidget(self.pushButton_13, 2, 2, 1, 1)'''
        '''self.pushButton_14 = QtGui.QPushButton(self.tab)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout.addWidget(self.pushButton_14, 3, 2, 1, 1)'''
        '''self.pushButton_15 = QtGui.QPushButton(self.tab)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout.addWidget(self.pushButton_15, 4, 1, 1, 1)'''
        '''self.pushButton_16 = QtGui.QPushButton(self.tab)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout.addWidget(self.pushButton_16, 4, 2, 1, 1)'''
        '''self.pushButton_17 = QtGui.QPushButton(self.tab)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout.addWidget(self.pushButton_17, 5, 1, 1, 1)'''
        '''self.pushButton_18 = QtGui.QPushButton(self.tab)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.gridLayout.addWidget(self.pushButton_18, 5, 2, 1, 1)'''
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        '''self.pushButton_33 = QtGui.QPushButton(self.tab_2)
        self.pushButton_33.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.gridLayout_2.addWidget(self.pushButton_33, 4, 1, 1, 1)'''
        '''self.pushButton_20 = QtGui.QPushButton(self.tab_2)
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.gridLayout_2.addWidget(self.pushButton_20, 1, 1, 1, 1)'''
        '''self.pushButton_32 = QtGui.QPushButton(self.tab_2)
        self.pushButton_32.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.gridLayout_2.addWidget(self.pushButton_32, 3, 2, 1, 1)'''
        self.pushButton_28 = QtGui.QPushButton(self.tab_2)
        self.pushButton_28.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.gridLayout_2.addWidget(self.pushButton_28, 0, 0, 1, 1)
        self.pushButton_29 = QtGui.QPushButton(self.tab_2)
        self.pushButton_29.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.gridLayout_2.addWidget(self.pushButton_29, 0, 1, 1, 1)
        '''self.pushButton_30 = QtGui.QPushButton(self.tab_2)
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.gridLayout_2.addWidget(self.pushButton_30, 3, 1, 1, 1)'''
        '''self.pushButton_26 = QtGui.QPushButton(self.tab_2)
        self.pushButton_26.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.gridLayout_2.addWidget(self.pushButton_26, 3, 0, 1, 1)'''
        '''self.pushButton_27 = QtGui.QPushButton(self.tab_2)
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.gridLayout_2.addWidget(self.pushButton_27, 0, 1, 1, 1)'''
        self.pushButton_19 = QtGui.QPushButton(self.tab_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.gridLayout_2.addWidget(self.pushButton_19, 1, 0, 1, 1)
        self.pushButton_24 = QtGui.QPushButton(self.tab_2)
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.gridLayout_2.addWidget(self.pushButton_24, 4, 0, 1, 1)
        self.pushButton_25 = QtGui.QPushButton(self.tab_2)
        self.pushButton_25.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.gridLayout_2.addWidget(self.pushButton_25, 4, 1, 1, 1)
        '''self.pushButton_21 = QtGui.QPushButton(self.tab_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.gridLayout_2.addWidget(self.pushButton_21, 0, 0, 1, 1)'''
        self.pushButton_31 = QtGui.QPushButton(self.tab_2)
        self.pushButton_31.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.gridLayout_2.addWidget(self.pushButton_31, 1, 1, 1, 1)
        '''self.pushButton_22 = QtGui.QPushButton(self.tab_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.gridLayout_2.addWidget(self.pushButton_22, 2, 0, 1, 1)'''
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_37 = QtGui.QPushButton(self.tab_3)
        self.pushButton_37.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.gridLayout_3.addWidget(self.pushButton_37, 1, 0, 1, 1)
        self.pushButton_38 = QtGui.QPushButton(self.tab_3)
        self.pushButton_38.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.gridLayout_3.addWidget(self.pushButton_38, 1, 1, 1, 1)
        '''self.pushButton_39 = QtGui.QPushButton(self.tab_3)
        self.pushButton_39.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.gridLayout_3.addWidget(self.pushButton_39, 0, 0, 1, 1)'''
        self.pushButton_40 = QtGui.QPushButton(self.tab_3)
        self.pushButton_40.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_40.setObjectName(_fromUtf8("pushButton_40"))
        self.gridLayout_3.addWidget(self.pushButton_40, 2, 0, 1, 1)
        '''self.pushButton_41 = QtGui.QPushButton(self.tab_3)
        self.pushButton_41.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_41.setObjectName(_fromUtf8("pushButton_41"))
        self.gridLayout_3.addWidget(self.pushButton_41, 5, 0, 1, 1)'''
        self.pushButton_42 = QtGui.QPushButton(self.tab_3)
        self.pushButton_42.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TlwgTypewriter"))
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setObjectName(_fromUtf8("pushButton_42"))
        self.gridLayout_3.addWidget(self.pushButton_42, 2, 1, 1, 1)
        self.pushButton_43 = QtGui.QPushButton(self.tab_3)
        self.pushButton_43.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_43.setObjectName(_fromUtf8("pushButton_43"))
        self.gridLayout_3.addWidget(self.pushButton_43, 1, 2, 1, 1)
        self.pushButton_44 = QtGui.QPushButton(self.tab_3)
        self.pushButton_44.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_44.setObjectName(_fromUtf8("pushButton_44"))
        self.gridLayout_3.addWidget(self.pushButton_44, 3, 0, 1, 1)
        '''self.pushButton_45 = QtGui.QPushButton(self.tab_3)
        self.pushButton_45.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_45.setObjectName(_fromUtf8("pushButton_45"))
        self.gridLayout_3.addWidget(self.pushButton_45, 0, 1, 1, 1)'''
        '''self.pushButton_46 = QtGui.QPushButton(self.tab_3)
        self.pushButton_46.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_46.setObjectName(_fromUtf8("pushButton_46"))
        self.gridLayout_3.addWidget(self.pushButton_46, 0, 2, 1, 1)'''
        '''self.pushButton_47 = QtGui.QPushButton(self.tab_3)
        self.pushButton_47.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_47.setObjectName(_fromUtf8("pushButton_47"))
        self.gridLayout_3.addWidget(self.pushButton_47, 2, 1, 1, 1)'''
        self.pushButton_48 = QtGui.QPushButton(self.tab_3)
        self.pushButton_48.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_48.setObjectName(_fromUtf8("pushButton_48"))
        self.gridLayout_3.addWidget(self.pushButton_48, 3, 1, 1, 1)
        '''self.pushButton_49 = QtGui.QPushButton(self.tab_3)
        self.pushButton_49.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_49.setObjectName(_fromUtf8("pushButton_49"))
        self.gridLayout_3.addWidget(self.pushButton_49, 2, 2, 1, 1)'''
        self.pushButton_50 = QtGui.QPushButton(self.tab_3)
        self.pushButton_50.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TlwgTypewriter"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setObjectName(_fromUtf8("pushButton_50"))
        self.gridLayout_3.addWidget(self.pushButton_50, 3, 2, 1, 1)
        self.pushButton_51 = QtGui.QPushButton(self.tab_3)
        self.pushButton_51.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_51.setObjectName(_fromUtf8("pushButton_51"))
        self.gridLayout_3.addWidget(self.pushButton_51, 2, 2, 1, 1)
        '''self.pushButton_52 = QtGui.QPushButton(self.tab_3)
        self.pushButton_52.setMinimumSize(QtCore.QSize(0, 40))'''
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        '''self.pushButton_52.setFont(font)
        self.pushButton_52.setObjectName(_fromUtf8("pushButton_52"))
        self.gridLayout_3.addWidget(self.pushButton_52, 4, 2, 1, 1)'''
        '''self.pushButton_53 = QtGui.QPushButton(self.tab_3)
        self.pushButton_53.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_53.setObjectName(_fromUtf8("pushButton_53"))
        self.gridLayout_3.addWidget(self.pushButton_53, 5, 1, 1, 1)'''
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setPointSize(15)
        font.setBold(False)
        #self.pushButton_41.setFont(font)
        self.pushButton_42.setFont(font)
        self.pushButton_44.setFont(font)
        self.pushButton_51.setFont(font)
        #self.pushButton_53.setFont(font)

        DockWidget.setWidget(self.dockWidgetContents)
        self.pushButton.clicked.connect(lambda:self.function_1("cos()"))
        self.pushButton_4.clicked.connect(lambda:self.function_1("arccos()"))
        self.pushButton_2.clicked.connect(lambda:self.function_1("sin()"))
        self.pushButton_7.clicked.connect(lambda:self.function_1("tan()"))
        #self.pushButton_10.clicked.connect(lambda:self.function_1("cot()"))
        #self.pushButton_9.clicked.connect(lambda:self.function_1("sec()"))
        #self.pushButton_6.clicked.connect(lambda:self.function_1("cosh()"))
        #self.pushButton_8.clicked.connect(lambda:self.function_1("csc()"))
        self.pushButton_3.clicked.connect(lambda:self.function_1("arcsin()"))
        #self.pushButton_5.clicked.connect(lambda:self.function_1("sinh()"))
        self.pushButton_11.clicked.connect(lambda:self.function_1("arctan()"))
        #self.pushButton_12.clicked.connect(lambda:self.function_1("arccsc()"))
        #self.pushButton_13.clicked.connect(lambda:self.function_1("tanh()"))
        #self.pushButton_14.clicked.connect(lambda:self.function_1("csch()"))
        #self.pushButton_15.clicked.connect(lambda:self.function_1("arcsec()"))
        #self.pushButton_16.clicked.connect(lambda:self.function_1("sech()"))
        #self.pushButton_17.clicked.connect(lambda:self.function_1("arccot()"))
        #self.pushButton_18.clicked.connect(lambda:self.function_1("coth()"))
        #self.pushButton_33.clicked.connect(lambda:self.function_2("~"))
        #self.pushButton_20.clicked.connect(lambda:self.function_3("quantile(,)"))
        #self.pushButton_32.clicked.connect(lambda:self.function_3("nPr(,)"))
        self.pushButton_28.clicked.connect(lambda:self.function_1("mean()"))
        self.pushButton_29.clicked.connect(lambda:self.function_1("var()"))
        #self.pushButton_30.clicked.connect(lambda:self.function_3("nCr(,)"))
        #self.pushButton_26.clicked.connect(lambda:self.function_3("corr(,)"))
        #self.pushButton_27.clicked.connect(lambda:self.function_1("length()"))
        self.pushButton_19.clicked.connect(lambda:self.function_1("median()"))
        self.pushButton_24.clicked.connect(lambda:self.function_1("factorial()"))
        self.pushButton_25.clicked.connect(lambda:self.function_1("std()"))
        #self.pushButton_21.clicked.connect(lambda:self.function_1("total()"))
        self.pushButton_31.clicked.connect(lambda:self.function_3("cov(,)"))
        #self.pushButton_22.clicked.connect(lambda:self.function_1("stdevp()"))
        self.pushButton_37.clicked.connect(lambda:self.function_1("ceil()"))
        self.pushButton_38.clicked.connect(lambda:self.function_1("floor()"))
        #self.pushButton_39.clicked.connect(lambda:self.function_3("lcm(,)"))
        self.pushButton_40.clicked.connect(lambda:self.function_1("abs()"))
        #self.pushButton_41.setText(_translate("DockWidget", u'\u2211', None))
        self.pushButton_42.clicked.connect(lambda:self.function_1("log10()"))
        self.pushButton_43.clicked.connect(lambda:self.function_1("around()"))
        self.pushButton_44.clicked.connect(lambda:self.function_5("()**(1/3)"))
        #self.pushButton_45.clicked.connect(lambda:self.function_3("gcd(,)"))
        #self.pushButton_46.clicked.connect(lambda:self.function_3("mod(,)"))
        #self.pushButton_47.clicked.connect(lambda:self.function_3("min(,)"))
        self.pushButton_48.clicked.connect(lambda:self.function_1("exp()"))
        #self.pushButton_49.clicked.connect(lambda:self.function_3("max(,)"))
        self.pushButton_50.clicked.connect(lambda:self.function_1("log()"))
        self.pushButton_51.clicked.connect(lambda:self.function_3("log(,)"))
        #self.pushButton_52.clicked.connect(lambda:self.function_2("d/dx"))
        #self.pushButton_53.setText(_translate("DockWidget", u'\u220F', None))
        self.retranslateUi(DockWidget)  
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def setTarget(self,target_area):
        self.target=target_area
    def function_1(self,str_num):
        self.target.insert(str_num)
        self.target.setCursorPosition(self.target.cursorPosition()-1)
    def function_2(self,str_num):
        self.target.insert(str_num)
    def function_3(self,str_num):
        self.target.insert(str_num)
        self.target.setCursorPosition(self.target.cursorPosition()-2)
    def function_4(self,str_num):
        self.target.insert(str_num)
        self.target.setCursorPosition(self.target.cursorPosition()-3)
    def function_5(self,str_num):
        self.target.insert(str_num)
        self.target.setCursorPosition(self.target.cursorPosition()-8)
    def function_6(self,str_num):
        self.target.insert(str_num)
        self.target.setCursorPosition(self.target.cursorPosition()-4)
    def retranslateUi(self, DockWidget):
        DockWidget.setToolTip(_translate("DockWidget", "Functions", None))
        #DockWidget.setWindowTitle(_translate("DockWidget", "Functions", None))
        self.pushButton.setText(_translate("DockWidget", "cos", None))
        self.pushButton_4.setText(_translate("DockWidget", "arccos", None))
        self.pushButton_2.setText(_translate("DockWidget", "sin", None))
        self.pushButton_7.setText(_translate("DockWidget", "tan", None))
        #self.pushButton_10.setText(_translate("DockWidget", "cot", None))
        #self.pushButton_9.setText(_translate("DockWidget", "sec", None))
        #self.pushButton_6.setText(_translate("DockWidget", "cosh", None))
        #self.pushButton_8.setText(_translate("DockWidget", "csc", None))
        self.pushButton_3.setText(_translate("DockWidget", "arcsin", None))
        #self.pushButton_5.setText(_translate("DockWidget", "sinh", None))
        self.pushButton_11.setText(_translate("DockWidget", "arctan", None))
        #self.pushButton_12.setText(_translate("DockWidget", "arcsc", None))
        #self.pushButton_13.setText(_translate("DockWidget", "tanh", None))
        #self.pushButton_14.setText(_translate("DockWidget", "csch", None))
        #self.pushButton_15.setText(_translate("DockWidget", "arcsec", None))
        #self.pushButton_16.setText(_translate("DockWidget", "sech", None))
        #self.pushButton_17.setText(_translate("DockWidget", "arccot", None))
        #self.pushButton_18.setText(_translate("DockWidget", "coth", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DockWidget", "trig", None))
        #self.pushButton_33.setText(_translate("DockWidget", "~", None))
        #self.pushButton_20.setText(_translate("DockWidget", "quantile", None))
        #self.pushButton_32.setText(_translate("DockWidget", "nPr", None))
        self.pushButton_28.setText(_translate("DockWidget", "mean", None))
        self.pushButton_29.setText(_translate("DockWidget", "var", None))
        #self.pushButton_30.setText(_translate("DockWidget", "nCr", None))
        #self.pushButton_26.setText(_translate("DockWidget", "corr", None))
        #self.pushButton_27.setText(_translate("DockWidget", "length", None))
        self.pushButton_19.setText(_translate("DockWidget", "median", None))
        self.pushButton_24.setText(_translate("DockWidget", "n!", None))
        self.pushButton_25.setText(_translate("DockWidget", "stdev", None))
        #self.pushButton_21.setText(_translate("DockWidget", "total", None))
        self.pushButton_31.setText(_translate("DockWidget", "cov", None))
        #self.pushButton_22.setText(_translate("DockWidget", "stdevp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DockWidget", "stats", None))
        self.pushButton_37.setText(_translate("DockWidget", "ceil", None))
        self.pushButton_38.setText(_translate("DockWidget", "floor", None))
        #self.pushButton_39.setText(_translate("DockWidget", "lcm", None))
        self.pushButton_40.setText(_translate("DockWidget", "abs", None))
        #self.pushButton_41.setText(_translate("DockWidget", u'\u2211', None))
        self.pushButton_42.setText(_translate("DockWidget", u'\u33D2', None))
        self.pushButton_43.setText(_translate("DockWidget", "round", None))
        self.pushButton_44.setText(_translate("DockWidget", u'\u221B', None))
        #self.pushButton_45.setText(_translate("DockWidget", "gcd", None))
        #self.pushButton_46.setText(_translate("DockWidget", "mod", None))
        #self.pushButton_47.setText(_translate("DockWidget", "min", None))
        self.pushButton_48.setText(_translate("DockWidget", "exp", None))
        #self.pushButton_49.setText(_translate("DockWidget", "max", None))
        self.pushButton_50.setText(_translate("DockWidget", "ln", None))
        self.pushButton_51.setText(_translate("DockWidget", u'\u33D2\u2090', None))
        #self.pushButton_52.setText(_translate("DockWidget", "d/dx", None))
        #self.pushButton_53.setText(_translate("DockWidget", u'\u220F', None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DockWidget", "misc", None))

if __name__ == "__main__":
    import sys
    a = QtGui.QApplication(sys.argv)
    w=Ui_DockWidget_2(None,None)
    #w.setFloating(True)
    w.show()
    sys.exit(a.exec_())