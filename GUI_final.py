# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_final.ui'
#
# Created: Thu Mar 19 22:03:17 2015
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
        MainWindow.setStyleSheet(_fromUtf8("QFrame{\n"
"border:none;\n"
"}\n"
"QStatusBar{ \n"
"background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.33, stop:0 rgba(255, 255, 255, 255), stop:0.125 rgba(155, 174, 198, 255), stop:0.318182 rgba(104, 117, 133, 255), stop:0.534091 rgba(65, 73, 83, 255), stop:0.875 rgba(42, 47, 54, 255)); }\n"
" QMainWindow{\n"
" background-image: url(:/img/Icons/rsz_back1.jpg); border:none;\n"
" background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
" text-align: center; }\n"
" QGroupBox{ \n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); }\n"
" QTabWidget{\n"
" background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); }\n"
" QDockWidget{\n"
" background-color:#737373;\n"
" border:none;\n"
" padding:0px; \n"
"}\n"
" QSlider::groove:horizontal {\n"
" background:red;\n"
" height: 15px;\n"
" position: absolute; \n"
"left: 4px; \n"
"right: 4px; }\n"
" QSlider::handle:horizontal {\n"
" height:20px;\n"
" width: 10px; \n"
"background: qlineargradient(spread:pad, x1:0, y1:0.477, x2:0, y2:0, stop:0.125 rgba(42, 47, 54, 255), stop:0.465909 rgba(65, 73, 83, 255), stop:0.681818 rgba(104, 117, 133, 255), stop:0.875 rgba(155, 174, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
" margin: -4px; }\n"
" QSlider::handle:hover:horizontal { \n"
"height:20px;\n"
" width: 10px;\n"
" background:qlineargradient(spread:pad, x1:0, y1:0.477, x2:0, y2:0, stop:0.125 rgba(91, 95, 100, 255), stop:0.465909 rgba(122, 132, 146, 255), stop:0.681818 rgba(141, 153, 167, 255), stop:0.875 rgba(181, 195, 212, 255), stop:1 rgba(255, 255, 255, 255));\n"
" margin: -4px;\n"
" }\n"
" QSlider::add-page:horizontal { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255));\n"
" }\n"
" QSlider::sub-page:horizontal { \n"
"background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)) ;\n"
" }\n"
" QToolButton{ \n"
"position: relative;\n"
" border: none; \n"
"outline:none;\n"
" color: black;\n"
" padding: 0px;\n"
" border-radius: 2px;\n"
" font-size: 22px;\n"
" }\n"
" QToolButton:hover:!pressed{ \n"
"position: relative;\n"
" border: none; \n"
"outline:none; \n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255));\n"
" color: white;\n"
" padding: 0px;\n"
" border-radius: 2px;\n"
" font-size: 22px; \n"
"}\n"
" QPushButton{ \n"
"position: relative;\n"
" border:none;\n"
" outline:none; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color: white;\n"
" padding: 6px 20px; \n"
"border-radius: 2px;\n"
" font-size: 20px;\n"
" }\n"
" QPushButton:hover:!pressed{ \n"
"position: relative;\n"
" border: none; \n"
"outline:none;\n"
" background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255));\n"
" color: white; \n"
"padding: 6px 20px; \n"
"border-radius: 2px;\n"
" font-size:20px; \n"
"} \n"
"QComboBox { \n"
"border: none; \n"
"padding: 1px 18px 1px 3px; \n"
"min-width: 6em;\n"
" }\n"
" QComboBox, QComboBox:drop-down \n"
"{\n"
" background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" }\n"
" QComboBox:on, QComboBox:drop-down:on { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255)); \n"
"}\n"
" QComboBox:on {\n"
" padding-top: 3px;\n"
" padding-left: 4px; \n"
"} \n"
"QComboBox::drop-down{\n"
" subcontrol-origin: padding; \n"
"subcontrol-position: top right;\n"
" width: 15px; \n"
"border-left-width: 1px; \n"
"border-left-color: darkgray; \n"
"border-left-style: solid;\n"
" }\n"
" QComboBox::down-arrow { \n"
"image:url(:/arrow/Icons/arrow-new.png);\n"
" } \n"
"QComboBox::down-arrow:on {\n"
" top: 1px;\n"
" left: 1px;\n"
" }\n"
" QMenu {\n"
" background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.483136, y2:0.466, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255)); \n"
"border: none; \n"
"}\n"
" QMenu::item {\n"
" background-color: transparent;\n"
" }\n"
" QMenu::item:selected {\n"
" background-color:rgb(120, 255, 13);\n"
" }\n"
" QMenuBar { \n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)) } QMenuBar::item {\n"
" spacing: 3px;\n"
" padding: 1px 4px; \n"
"background: transparent; \n"
"border-radius: 2px;\n"
" }\n"
" QMenuBar::item:selected {\n"
" background:#737373;\n"
" }\n"
" QMenuBar::item:pressed \n"
"{ background: #414953; \n"
"} \n"
"QTableWidget{ \n"
"background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255));\n"
" border:1px solid rgb(171, 173, 179);\n"
" }\n"
" QTextEdit{ \n"
"background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #DBDBDB, stop:1 rgba(255, 255, 255, 255)); \n"
"}\n"
" QScrollBar:horizontal {\n"
" border: none; background: #DBDBDB; height: 15px; margin: 0px 20px 0 20px; \n"
"}\n"
" QScrollBar::handle:horizontal { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" min-width: 20px;\n"
" }\n"
" QScrollBar::handle:horizontal:hover { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255));\n"
" min-width: 20px;\n"
" } \n"
"QScrollBar::add-line:horizontal {\n"
" border: none;\n"
" background:#DBDBDB; \n"
"width: 20px;\n"
" subcontrol-position: right;\n"
" subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:horizontal {\n"
" border:none; \n"
"background:#DBDBDB; \n"
"width: 20px;\n"
" subcontrol-position: left;\n"
" subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::add-line:horizontal:hover:!pressed { \n"
"border: none;\n"
" background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255)); \n"
"width: 20px;\n"
" subcontrol-position: right; \n"
"subcontrol-origin: margin; \n"
"}\n"
" QScrollBar::sub-line:horizontal:hover:!pressed { \n"
"border:none;\n"
" background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" width: 20px; \n"
"subcontrol-position: left;\n"
" subcontrol-origin: margin; \n"
"}\n"
" QScrollBar::left-arrow:horizontal{\n"
" image: url(:/arrow/Icons/left-arrow.png);\n"
" }\n"
" QScrollBar::right-arrow:horizontal{\n"
" image: url(:/arrow/Icons/right-arrow.png);\n"
" }\n"
" QScrollBar:vertical {\n"
" border: none;\n"
" background: #DBDBDB;\n"
" width: 15px; \n"
"margin: 0px 20px 0 20px; \n"
"} \n"
"QScrollBar::handle:vertical { background:qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" min-height: 20px; }\n"
" QScrollBar::handle:vertical:hover { background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0802727, stop:0 rgba(255, 255, 255, 255), stop:0.0397727 rgba(222, 255, 196, 255), stop:0.176136 rgba(168, 255, 99, 255), stop:0.642045 rgba(127, 200, 70, 255));\n"
" min-height: 15px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
" border: none;\n"
" background:#DBDBDB; \n"
"height: 20px;\n"
" subcontrol-position: bottom; \n"
"subcontrol-origin: margin; \n"
"}\n"
" QScrollBar::sub-line:vertical {\n"
" border:none; \n"
"background:#DBDBDB; \n"
"height: 20px;\n"
" subcontrol-position: top;\n"
" subcontrol-origin: margin;\n"
" } \n"
"QScrollBar::add-line:vertical:hover:!pressed { \n"
"border: none; \n"
"background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" height: 20px;\n"
" subcontrol-position:bottom; \n"
"subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical:hover:!pressed { b\n"
"order:none; \n"
"background: qlineargradient(spread:pad, x1:0, y1:0.664, x2:0, y2:0, stop:0.357955 rgba(89, 189, 9, 255), stop:0.801136 rgba(120, 255, 13, 255), stop:0.9375 rgba(175, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
" height: 20px; \n"
"subcontrol-position:top;\n"
" subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical{ \n"
"image: url(:/arrow/Icons/up-arrow.png); \n"
"} \n"
"QScrollBar::down-arrow:vertical{\n"
" image: url(:/arrow/Icons/down-arrow.png);\n"
" }"))
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
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/arrow/Icons/double-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(320, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
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
        self.toolButton_7 = QtGui.QToolButton(self.frame)
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
        self.toolButton_9 = QtGui.QToolButton(self.frame)
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
        self.toolButton_8 = QtGui.QToolButton(self.frame)
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
        self.toolButton_5 = QtGui.QToolButton(self.frame)
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
        self.tableWidget = QtGui.QTableWidget(self.frame)
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
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton_21 = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_3.addWidget(self.pushButton_21)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setStyleSheet(_fromUtf8(""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_6.addWidget(self.widget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 21))
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
        self.dockWidget.setMinimumSize(QtCore.QSize(320, 91))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_5 = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.comboBox_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.dockWidget_2.setMinimumSize(QtCore.QSize(427, 324))
        self.dockWidget_2.setStyleSheet(_fromUtf8(""))
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
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setFrame(True)
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
        self.tabWidget_2.setStyleSheet(_fromUtf8(""))
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
        self.horizontalLayout_8.amenuddWidget(self.label)
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
        self.tabWidget_3.setStyleSheet(_fromUtf8(""))
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(489, 70))
        self.dockWidget_3.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_17 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_17.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_17.setStyleSheet(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Item-New-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon5)
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setObjectName(_fromUtf8("toolButton_17"))
        self.horizontalLayout.addWidget(self.toolButton_17)
        self.toolButton_10 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_10.setStyleSheet(_fromUtf8(""))
        self.toolButton_10.setIcon(icon3)
        self.toolButton_10.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.horizontalLayout.addWidget(self.toolButton_10)
        self.toolButton_20 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_20.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_20.setStyleSheet(_fromUtf8(""))
        self.toolButton_20.setIcon(icon4)
        self.toolButton_20.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_20.setObjectName(_fromUtf8("toolButton_20"))
        self.horizontalLayout.addWidget(self.toolButton_20)
        self.toolButton_18 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_18.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_18.setStyleSheet(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Open-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_18.setIcon(icon6)
        self.toolButton_18.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_18.setObjectName(_fromUtf8("toolButton_18"))
        self.horizontalLayout.addWidget(self.toolButton_18)
        self.line_4 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.toolButton_4 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_4.setStyleSheet(_fromUtf8(""))
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton_3 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet(_fromUtf8(""))
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.line_5 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.checkBox = QtGui.QCheckBox(self.dockWidgetContents_3)
        self.checkBox.setMaximumSize(QtCore.QSize(20, 25))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.Example = QtGui.QToolButton(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Example.sizePolicy().hasHeightForWidth())
        self.Example.setSizePolicy(sizePolicy)
        self.Example.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Example.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Example.setStyleSheet(_fromUtf8("QToolButton{\n"
"font-size: 15px;\n"
"color:rgb(255, 255, 255);\n"
"}"))
        self.Example.setIconSize(QtCore.QSize(24, 24))
        self.Example.setObjectName(_fromUtf8("Example"))
        self.horizontalLayout.addWidget(self.Example)
        self.line_6 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Board-Pin-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon7)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_25 = QtGui.QToolButton(self.dockWidgetContents_3)
        self.toolButton_25.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_25.setStyleSheet(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Table-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_25.setIcon(icon8)
        self.toolButton_25.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_25.setObjectName(_fromUtf8("toolButton_25"))
        self.horizontalLayout.addWidget(self.toolButton_25)
        self.line_8 = QtGui.QFrame(self.dockWidgetContents_3)
        self.line_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout.addWidget(self.line_8)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_4.sizePolicy().hasHeightForWidth())
        self.dockWidget_4.setSizePolicy(sizePolicy)
        self.dockWidget_4.setMinimumSize(QtCore.QSize(624, 70))
        self.dockWidget_4.setMaximumSize(QtCore.QSize(524287, 70))
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.line_7 = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_2.addWidget(self.line_7)
        self.toolButton_19 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_19.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_19.setStyleSheet(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Keyboard-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_19.setIcon(icon9)
        self.toolButton_19.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_19.setObjectName(_fromUtf8("toolButton_19"))
        self.horizontalLayout_2.addWidget(self.toolButton_19)
        self.toolButton_23 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_23.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_23.setStyleSheet(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Printer-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_23.setIcon(icon10)
        self.toolButton_23.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_23.setObjectName(_fromUtf8("toolButton_23"))
        self.horizontalLayout_2.addWidget(self.toolButton_23)
        self.toolButton_2 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setIcon(icon4)
        self.toolButton_2.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.toolButton_24 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_24.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_24.setStyleSheet(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Camera-02-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_24.setIcon(icon11)
        self.toolButton_24.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_24.setObjectName(_fromUtf8("toolButton_24"))
        self.horizontalLayout_2.addWidget(self.toolButton_24)
        self.toolButton_22 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_22.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_22.setStyleSheet(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Facebook-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_22.setIcon(icon12)
        self.toolButton_22.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_22.setObjectName(_fromUtf8("toolButton_22"))
        self.horizontalLayout_2.addWidget(self.toolButton_22)
        self.line_3 = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_2.addWidget(self.line_3)
        self.toolButton_21 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_21.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_21.setStyleSheet(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Media-Play-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_21.setIcon(icon13)
        self.toolButton_21.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_21.setObjectName(_fromUtf8("toolButton_21"))
        self.horizontalLayout_2.addWidget(self.toolButton_21)
        self.toolButton_16 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_16.setStyleSheet(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Stop-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_16.setIcon(icon14)
        self.toolButton_16.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_16.setObjectName(_fromUtf8("toolButton_16"))
        self.horizontalLayout_2.addWidget(self.toolButton_16)
        self.line_2 = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.toolButton_15 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_15.setStyleSheet(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Column-Selection-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon15)
        self.toolButton_15.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_15.setObjectName(_fromUtf8("toolButton_15"))
        self.horizontalLayout_2.addWidget(self.toolButton_15)
        self.toolButton_14 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_14.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_14.setStyleSheet(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Slash-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon16)
        self.toolButton_14.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_14.setObjectName(_fromUtf8("toolButton_14"))
        self.horizontalLayout_2.addWidget(self.toolButton_14)
        self.line = QtGui.QFrame(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.toolButton_13 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_13.setStyleSheet(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Magnifying-Glass-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon17)
        self.toolButton_13.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_13.setObjectName(_fromUtf8("toolButton_13"))
        self.horizontalLayout_2.addWidget(self.toolButton_13)
        self.toolButton_12 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_12.setStyleSheet(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-In-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon18)
        self.toolButton_12.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_12.setObjectName(_fromUtf8("toolButton_12"))
        self.horizontalLayout_2.addWidget(self.toolButton_12)
        self.toolButton_11 = QtGui.QToolButton(self.dockWidgetContents_4)
        self.toolButton_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.toolButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_11.setAutoFillBackground(False)
        self.toolButton_11.setStyleSheet(_fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Zoom-Out-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon19)
        self.toolButton_11.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_11.setObjectName(_fromUtf8("toolButton_11"))
        self.horizontalLayout_2.addWidget(self.toolButton_11)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_4)
        self.dockWidget_5 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_5.setObjectName(_fromUtf8("dockWidget_5"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents_5)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_5)
        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
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
        self.toolButton.setToolTip(_translate("MainWindow", "Always on Top", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.toolButton_25.setToolTip(_translate("MainWindow", "Show/Hide Table", None))
        self.toolButton_25.setText(_translate("MainWindow", "...", None))
        self.toolButton_19.setToolTip(_translate("MainWindow", "Keyboard", None))
        self.toolButton_19.setText(_translate("MainWindow", "...", None))
        self.toolButton_23.setToolTip(_translate("MainWindow", "Print graph", None))
        self.toolButton_23.setText(_translate("MainWindow", "...", None))
        self.toolButton_2.setToolTip(_translate("MainWindow", "Save Graph", None))
        self.toolButton_2.setText(_translate("MainWindow", "...", None))
        self.toolButton_24.setToolTip(_translate("MainWindow", "Take a screenshot", None))
        self.toolButton_24.setText(_translate("MainWindow", "...", None))
        self.toolButton_22.setToolTip(_translate("MainWindow", "Go to our FaceBook page", None))
        self.toolButton_22.setText(_translate("MainWindow", "...", None))
        self.toolButton_21.setToolTip(_translate("MainWindow", "Play", None))
        self.toolButton_21.setText(_translate("MainWindow", "...", None))
        self.toolButton_16.setToolTip(_translate("MainWindow", "Stop", None))
        self.toolButton_16.setText(_translate("MainWindow", "...", None))
        self.toolButton_15.setToolTip(_translate("MainWindow", "Disable Anti-Aliasing", None))
        self.toolButton_15.setText(_translate("MainWindow", "...", None))
        self.toolButton_14.setToolTip(_translate("MainWindow", "Enable Anti-Aliasing", None))
        self.toolButton_14.setText(_translate("MainWindow", "...", None))
        self.toolButton_13.setToolTip(_translate("MainWindow", "Zoom All", None))
        self.toolButton_13.setText(_translate("MainWindow", "...", None))
        self.toolButton_12.setToolTip(_translate("MainWindow", "Zoom in", None))
        self.toolButton_12.setText(_translate("MainWindow", "...", None))
        self.toolButton_11.setToolTip(_translate("MainWindow", "Zoom out", None))
        self.toolButton_11.setText(_translate("MainWindow", "...", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
