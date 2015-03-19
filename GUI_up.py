# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Mon Mar 16 22:24:12 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1396, 727)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"  text-align: center; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
" QSlider::groove:horizontal {\n"
"     background: red;\n"
"     height: 15px;\n"
"     position: absolute; \n"
"     left: 4px; right: 4px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     height:20px;\n"
"     width: 10px;\n"
"     background: green;\n"
"     margin: -4px; \n"
" }\n"
"\n"
" QSlider::add-page:horizontal {\n"
"     background:rgb(255, 255, 127)\n"
" }\n"
"\n"
" QSlider::sub-page:horizontal {\n"
"     background: rgb(255, 170, 0);\n"
" }\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QPushButton{\n"
"  position: relative;\n"
"  border:none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #89669b;\n"
"  color: white;\n"
"  padding: 6px 20px;\n"
"  border-radius: 2px;\n"
"  font-size: 20px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QPushButton:hover{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #745385;\n"
"  color: white;\n"
"  padding: 6px 20px;\n"
"  border-radius: 2px;\n"
"  font-size:20px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QPushButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #9d74b2;\n"
"  color: white;\n"
"  padding: 6px 20px;\n"
"  border-radius: 2px;\n"
"  font-size: 20px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_2.setStyleSheet(_fromUtf8("QFrame, QLabel, QToolTip {\n"
"    border: 0px solid green;\n"
"}"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 20, 121))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{\n"
"border_bottom_style:outset;\n"
"border_bottom_width:3px;\n"
"border_bottom_color:qlineargradient(spread:pad, x1:0, y1:0.494, x2:0.284, y2:0.489318, stop:0 rgba(0, 0, 0, 255), stop:0.664773 rgba(255, 255, 255, 255))\n"
"}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.toolButton_7 = QtGui.QToolButton(self.frame)
        self.toolButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_7.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Add-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.horizontalLayout_5.addWidget(self.toolButton_7)
        self.toolButton_9 = QtGui.QToolButton(self.frame)
        self.toolButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_9.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Minus-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon1)
        self.toolButton_9.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_9.setObjectName(_fromUtf8("toolButton_9"))
        self.horizontalLayout_5.addWidget(self.toolButton_9)
        self.toolButton_8 = QtGui.QToolButton(self.frame)
        self.toolButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_8.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Folder-Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon2)
        self.toolButton_8.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.horizontalLayout_5.addWidget(self.toolButton_8)
        self.toolButton_6 = QtGui.QToolButton(self.frame)
        self.toolButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_6.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon3)
        self.toolButton_6.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.horizontalLayout_5.addWidget(self.toolButton_6)
        self.toolButton_5 = QtGui.QToolButton(self.frame)
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet(_fromUtf8("QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"background:rgb(66, 204, 225);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Save-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtGui.QTableWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setStyleSheet(_fromUtf8(".button {\n"
"  background: orange;\n"
"  outline: none;\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 0.25em;\n"
"  padding: 0.75em 2em;\n"
"  line-height: 1;\n"
"  box-shadow: 0 0 0.25em rgba(0,0,0,0.5);\n"
"  text-shadow: 0 0 0.25em rgba(0,0,0,0.5);\n"
"  font-size: 1.5rem;\n"
"}\n"
".button-white {\n"
"  background: white;\n"
"  color: orange;\n"
"}\n"
".button-round {\n"
"  border-radius: 100%;\n"
"  padding: 0.75em;\n"
"  width: 3em;\n"
"  height: 3em;\n"
"}\n"
".button-ripple {\n"
"  position: relative;\n"
"  overflow: hidden;\n"
"  transform: translate(0);\n"
"}\n"
".button-ripple_content {\n"
"  position: relative;\n"
"  z-index: 1;\n"
"}\n"
".button-ripple_ripples {\n"
"  position: absolute;\n"
"  top: 0;\n"
"  left: 0;\n"
"}\n"
".button-ripple_ripple{\n"
"  display: block;\n"
"  position: absolute;\n"
"  border-radius: 100%;\n"
"  width: 1em;\n"
"  height: 1em;\n"
"  margin: -0.5em 0 0 -0.5em;\n"
"  transform: scale(0);\n"
"\n"
"  top: 0;\n"
"  left: 0;\n"
"\n"
"  animation: ripple-animation 2s;\n"
"}\n"
"\n"
"@keyframes ripple-animation {\n"
"    from {\n"
"      transform: scale3d(1,1,1);\n"
"      opacity: 0.8;\n"
"    }\n"
"    to {\n"
"      transform: scale3d(100,100,1);\n"
"      opacity: 0;\n"
"    }\n"
"}\n"
"\n"
"/* Make things perty */\n"
"html {  height: 100%;}\n"
"body { font-family: \'Source Sans Pro\', Helvetica, Arial, sans-serif; background: url(http://www.jmchristensendesign.com/wp-content/themes/jmcdsn/images/intro_default-background.jpg); color: #fff; height: 100%; padding-top: 2em; text-align: center;}\n"
"h1, h2{ margin: 0; text-transform: uppercase;text-shadow: 0 0 0.5em black;}\n"
"h2 { font-weight: 300}\n"
"input { border: 1px solid #666; background: #333; color: #fff; padding: 0.5em; box-shadow: none; outline: none !important; margin: 1em  auto; text-align: center;}\n"
"a { color: orange; text-decoration: none; transition: color 250ms ease-in-out;}\n"
"a:hover { color: yellow;}\n"
".container { display:block; margin: 2em 0;}"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.pushButton_21 = QtGui.QPushButton(self.frame)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_5.addWidget(self.pushButton_21)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_6.addWidget(self.widget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_5 = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_5, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_6, 1, 0, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 20))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setStyleSheet(_fromUtf8("QDockWidget{\n"
"    background-color: rgb(11, 170, 165);\n"
"    color:rgb(56, 252, 255);\n"
"}\n"
""))
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(_fromUtf8(""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox_3)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget_2 = QtGui.QTabWidget(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(310, 0))
        self.tabWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setStyleSheet(_fromUtf8("QTabWidget{\n"
"background_color: rgb(56, 252, 255);\n"
"color: rgb(56, 252, 255);\n"
"}"))
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_2.setIconSize(QtCore.QSize(16, 25))
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.horizontalSlider = QtGui.QSlider(self.groupBox)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setStyleSheet(_fromUtf8(""))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_8.addWidget(self.horizontalSlider)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_9.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(20, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_9.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_9.addWidget(self.radioButton)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_9.addWidget(self.radioButton_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.horizontalLayout_10.addWidget(self.comboBox_4)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_10.addWidget(self.label_6)
        self.horizontalSlider_2 = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalLayout_10.addWidget(self.horizontalSlider_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_11.addWidget(self.label_7)
        self.horizontalSlider_3 = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.horizontalLayout_11.addWidget(self.horizontalSlider_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_4)
        self.tabWidget_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget_3.setStyleSheet(_fromUtf8("QTabBar::tab{\n"
"height : 40px;\n"
"width : 156px;\n"
"}"))
        self.tabWidget_3.setUsesScrollButtons(False)
        self.tabWidget_3.setMovable(True)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget_3.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget_3.addTab(self.tab_6, _fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.tabWidget_3)
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_17 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_17.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Item-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon5)
        self.toolButton_17.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_17.setObjectName(_fromUtf8("toolButton_17"))
        self.horizontalLayout.addWidget(self.toolButton_17)
        self.toolButton_10 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_10.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        self.toolButton_10.setIcon(icon2)
        self.toolButton_10.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.horizontalLayout.addWidget(self.toolButton_10)
        self.toolButton_20 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_20.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        self.toolButton_20.setIcon(icon4)
        self.toolButton_20.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_20.setObjectName(_fromUtf8("toolButton_20"))
        self.horizontalLayout.addWidget(self.toolButton_20)
        self.toolButton_18 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_18.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        self.toolButton_18.setIcon(icon3)
        self.toolButton_18.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_18.setObjectName(_fromUtf8("toolButton_18"))
        self.horizontalLayout.addWidget(self.toolButton_18)
        self.line_4 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.toolButton_4 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton_3 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.line_5 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.checkBox = QtGui.QCheckBox(self.dockWidgetContents_3)
        self.checkBox.setMaximumSize(QtCore.QSize(20, 16777215))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.Example = QtGui.QToolButton(self.dockWidgetContents_3)
        self.Example.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Example.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        self.Example.setIconSize(QtCore.QSize(48, 48))
        self.Example.setObjectName(_fromUtf8("Example"))
        self.horizontalLayout.addWidget(self.Example)
        self.line_6 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Board-Pin-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon6)
        self.toolButton.setIconSize(QtCore.QSize(48, 48))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_25 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_25.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Table-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_25.setIcon(icon7)
        self.toolButton_25.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_25.setObjectName(_fromUtf8("toolButton_25"))
        self.horizontalLayout.addWidget(self.toolButton_25)
        self.line_8 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout.addWidget(self.line_8)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.line_7 = QtGui.QFrame(self.dockWidgetContents_4)
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_4.addWidget(self.line_7)
        self.toolButton_19 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_19.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Briefcase-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_19.setIcon(icon8)
        self.toolButton_19.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_19.setObjectName(_fromUtf8("toolButton_19"))
        self.horizontalLayout_4.addWidget(self.toolButton_19)
        self.toolButton_23 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_23.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Printer-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_23.setIcon(icon9)
        self.toolButton_23.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_23.setObjectName(_fromUtf8("toolButton_23"))
        self.horizontalLayout_4.addWidget(self.toolButton_23)
        self.toolButton_24 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_24.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Camera-02-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_24.setIcon(icon10)
        self.toolButton_24.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_24.setObjectName(_fromUtf8("toolButton_24"))
        self.horizontalLayout_4.addWidget(self.toolButton_24)
        self.toolButton_22 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_22.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Facebook-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_22.setIcon(icon11)
        self.toolButton_22.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_22.setObjectName(_fromUtf8("toolButton_22"))
        self.horizontalLayout_4.addWidget(self.toolButton_22)
        self.line_3 = QtGui.QFrame(self.dockWidgetContents_4)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_4.addWidget(self.line_3)
        self.toolButton_21 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_21.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Media-Play-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_21.setIcon(icon12)
        self.toolButton_21.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_21.setObjectName(_fromUtf8("toolButton_21"))
        self.horizontalLayout_4.addWidget(self.toolButton_21)
        self.toolButton_16 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_16.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Stop-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon13)
        self.toolButton_16.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_16.setObjectName(_fromUtf8("toolButton_16"))
        self.horizontalLayout_4.addWidget(self.toolButton_16)
        self.line_2 = QtGui.QFrame(self.dockWidgetContents_4)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_4.addWidget(self.line_2)
        self.toolButton_15 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_15.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Column-Selection-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon14)
        self.toolButton_15.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_15.setObjectName(_fromUtf8("toolButton_15"))
        self.horizontalLayout_4.addWidget(self.toolButton_15)
        self.toolButton_14 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_14.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Slash-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon15)
        self.toolButton_14.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_14.setObjectName(_fromUtf8("toolButton_14"))
        self.horizontalLayout_4.addWidget(self.toolButton_14)
        self.line = QtGui.QFrame(self.dockWidgetContents_4)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_4.addWidget(self.line)
        self.toolButton_13 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_13.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Magnifying-Glass-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon16)
        self.toolButton_13.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        self.horizontalLayout_4.addWidget(self.toolButton_13)
        self.toolButton_12 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_12.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-In-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon17)
        self.toolButton_12.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.horizontalLayout_4.addWidget(self.toolButton_12)
        self.toolButton_11 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_11.setAutoFillBackground(False)
        self.toolButton_11.setStyleSheet(_fromUtf8("\n"
"QToolButton{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}\n"
"QToolButton:hover:!pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: #fbd334;\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"    border-image: url(c:/Data/navArrowsSelected.png);\n"
"}\n"
"QToolButton:focus\n"
" {\n"
" border-image: url();\n"
"} \n"
"QToolButton:pressed{\n"
"  position: relative;\n"
"  border: none;\n"
"  outline:none;\n"
"  cursor:pointer;\n"
"  cursor: hand;\n"
"  background: rgb(57, 255, 146);\n"
"  color: white;\n"
"  padding: 2px 2px;\n"
"  border-radius: 2px;\n"
"  font-size: 22px;\n"
"  -webkit-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   -moz-box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"   box-shadow: 0 0 4px rgba(0,0,0, .75);\n"
"}"))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-Out-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon18)
        self.toolButton_11.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.horizontalLayout_4.addWidget(self.toolButton_11)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_4)
        self.dockWidget_5 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_5.setObjectName(_fromUtf8("dockWidget_5"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents_5)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_5)
        self.actionNew_Project = QtGui.QAction(MainWindow)
        self.actionNew_Project.setObjectName(_fromUtf8("actionNew_Project"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "T\n"
"a\n"
"b\n"
"l\n"
"e\n"
"", None))
        self.pushButton_3.setText(_translate("MainWindow", "Hide", None))
        self.toolButton_7.setToolTip(_translate("MainWindow", "Add", None))
        self.toolButton_7.setText(_translate("MainWindow", "...", None))
        self.toolButton_9.setToolTip(_translate("MainWindow", "Remove", None))
        self.toolButton_9.setText(_translate("MainWindow", "...", None))
        self.toolButton_8.setText(_translate("MainWindow", "...", None))
        self.toolButton_6.setText(_translate("MainWindow", "...", None))
        self.toolButton_5.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z", None))
        self.pushButton_21.setText(_translate("MainWindow", "Redraw", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "x", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "y", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "z", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "x", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "y", None))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "z", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "3D", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "2D", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Cartesian", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Cylindrical", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Spherical", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Regular", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Implicit", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Parametric", None))
        self.groupBox.setTitle(_translate("MainWindow", "Appearance", None))
        self.label.setText(_translate("MainWindow", "Resolution", None))
        self.label_2.setText(_translate("MainWindow", "Color:", None))
        self.label_3.setText(_translate("MainWindow", "color", None))
        self.label_4.setText(_translate("MainWindow", "Along", None))
        self.radioButton.setText(_translate("MainWindow", "X", None))
        self.radioButton_3.setText(_translate("MainWindow", "Z", None))
        self.radioButton_2.setText(_translate("MainWindow", "Y", None))
        self.label_5.setText(_translate("MainWindow", "Draw", None))
        self.label_6.setText(_translate("MainWindow", "Thickness", None))
        self.label_7.setText(_translate("MainWindow", "Transparency", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Appear", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Tab 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Axis Settings", None))
        self.toolButton_17.setToolTip(_translate("MainWindow", "Create New", None))
        self.toolButton_17.setText(_translate("MainWindow", "...", None))
        self.toolButton_10.setToolTip(_translate("MainWindow", "Open Existing", None))
        self.toolButton_10.setText(_translate("MainWindow", "...", None))
        self.toolButton_20.setToolTip(_translate("MainWindow", "Save to Drive", None))
        self.toolButton_20.setText(_translate("MainWindow", "...", None))
        self.toolButton_18.setToolTip(_translate("MainWindow", "Load New", None))
        self.toolButton_18.setText(_translate("MainWindow", "...", None))
        self.toolButton_4.setToolTip(_translate("MainWindow", "Add new Equation", None))
        self.toolButton_4.setText(_translate("MainWindow", "...", None))
        self.toolButton_3.setToolTip(_translate("MainWindow", "Remove this Equation", None))
        self.toolButton_3.setText(_translate("MainWindow", "...", None))
        self.checkBox.setToolTip(_translate("MainWindow", "Show on Graph", None))
        self.Example.setToolTip(_translate("MainWindow", "Illustrate with an Example", None))
        self.Example.setWhatsThis(_translate("MainWindow", "Example", None))
        self.Example.setText(_translate("MainWindow", "Example", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_25.setText(_translate("MainWindow", "...", None))
        self.toolButton_19.setText(_translate("MainWindow", "...", None))
        self.toolButton_23.setToolTip(_translate("MainWindow", "Print graph", None))
        self.toolButton_23.setText(_translate("MainWindow", "...", None))
        self.toolButton_24.setToolTip(_translate("MainWindow", "Take a screenshot", None))
        self.toolButton_24.setText(_translate("MainWindow", "...", None))
        self.toolButton_22.setToolTip(_translate("MainWindow", "Go to our FaceBook page", None))
        self.toolButton_22.setText(_translate("MainWindow", "...", None))
        self.toolButton_21.setToolTip(_translate("MainWindow", "Play", None))
        self.toolButton_21.setText(_translate("MainWindow", "...", None))
        self.toolButton_16.setToolTip(_translate("MainWindow", "Stop", None))
        self.toolButton_16.setText(_translate("MainWindow", "...", None))
        self.toolButton_15.setText(_translate("MainWindow", "...", None))
        self.toolButton_14.setText(_translate("MainWindow", "...", None))
        self.toolButton_13.setToolTip(_translate("MainWindow", "Zoom", None))
        self.toolButton_13.setText(_translate("MainWindow", "...", None))
        self.toolButton_12.setToolTip(_translate("MainWindow", "Zoom in", None))
        self.toolButton_12.setText(_translate("MainWindow", "...", None))
        self.toolButton_11.setToolTip(_translate("MainWindow", "Zoom out", None))
        self.toolButton_11.setText(_translate("MainWindow", "...", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))

