# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE10.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas as pd
import numpy as np
from browse_file_func2 import *
from bson.objectid import ObjectId
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
# use dark theme
pio.templates.default = "plotly_dark"

from read_table_func import *

from browse_file_func import *
from browse_file_func2 import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 767)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout_27 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.label_5 = QLabel(self.frame_label_top_btns)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_5.setPixmap(QPixmap(u":/Logo/icons/Logo/image_5.png"))

        self.horizontalLayout_10.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns, 0, Qt.AlignLeft)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        self.label.setFont(font5)
        self.label.setPixmap(QPixmap(u":/Logo/icons/Logo/image_6.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_home)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.verticalLayout_12 = QVBoxLayout(self.page_dashboard)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.head_dash = QFrame(self.page_dashboard)
        self.head_dash.setObjectName(u"head_dash")
        self.head_dash.setMinimumSize(QSize(0, 100))
        self.head_dash.setMaximumSize(QSize(16777215, 100))
        self.head_dash.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.head_dash.setFrameShape(QFrame.StyledPanel)
        self.head_dash.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.head_dash)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(11, 0, 11, 0)
        self.frame_11 = QFrame(self.head_dash)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_26.setSpacing(7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(11, 11, 11, 11)
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 0))
        self.label_12.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_26.addWidget(self.label_12)

        self.comboBox_select_chart = QComboBox(self.frame_11)
        self.comboBox_select_chart.addItem("")
        self.comboBox_select_chart.addItem("")
        self.comboBox_select_chart.setObjectName(u"comboBox_select_chart")
        self.comboBox_select_chart.setMinimumSize(QSize(200, 0))
        self.comboBox_select_chart.setMaximumSize(QSize(200, 16777215))
        self.comboBox_select_chart.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_26.addWidget(self.comboBox_select_chart)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_26.addWidget(self.label_2)

        self.comboBox_select_year = QComboBox(self.frame_11)
        self.comboBox_select_year.addItem("")
        self.comboBox_select_year.addItem("")
        self.comboBox_select_year.setObjectName(u"comboBox_select_year")
        self.comboBox_select_year.setMinimumSize(QSize(150, 30))
        self.comboBox_select_year.setMaximumSize(QSize(150, 30))
        self.comboBox_select_year.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_26.addWidget(self.comboBox_select_year)


        self.verticalLayout_43.addWidget(self.frame_11, 0, Qt.AlignLeft)

        self.frame_12 = QFrame(self.head_dash)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_30.addWidget(self.label_11)

        self.cen_world_btn_2 = QCheckBox(self.frame_12)
        self.cen_world_btn_2.setObjectName(u"cen_world_btn_2")
        self.cen_world_btn_2.setChecked(True)

        self.horizontalLayout_30.addWidget(self.cen_world_btn_2)

        self.cen_lad_btn_2 = QCheckBox(self.frame_12)
        self.cen_lad_btn_2.setObjectName(u"cen_lad_btn_2")
        self.cen_lad_btn_2.setChecked(True)

        self.horizontalLayout_30.addWidget(self.cen_lad_btn_2)

        self.cen_rama9_btn_2 = QCheckBox(self.frame_12)
        self.cen_rama9_btn_2.setObjectName(u"cen_rama9_btn_2")
        self.cen_rama9_btn_2.setChecked(True)

        self.horizontalLayout_30.addWidget(self.cen_rama9_btn_2)

        self.submit_view_btn_2 = QPushButton(self.frame_12)
        self.submit_view_btn_2.setObjectName(u"submit_view_btn_2")
        self.submit_view_btn_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_30.addWidget(self.submit_view_btn_2)


        self.verticalLayout_43.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.head_dash)

        self.graph_dash = QFrame(self.page_dashboard)
        self.graph_dash.setObjectName(u"graph_dash")
        self.graph_dash.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.graph_dash.setFrameShape(QFrame.StyledPanel)
        self.graph_dash.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.graph_dash)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_graph = QLabel(self.graph_dash)
        self.label_graph.setObjectName(u"label_graph")

        self.horizontalLayout_39.addWidget(self.label_graph)


        self.verticalLayout_12.addWidget(self.graph_dash)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_view_data = QWidget()
        self.page_view_data.setObjectName(u"page_view_data")
        self.verticalLayout_13 = QVBoxLayout(self.page_view_data)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.view_data_btn = QFrame(self.page_view_data)
        self.view_data_btn.setObjectName(u"view_data_btn")
        self.view_data_btn.setMinimumSize(QSize(0, 50))
        self.view_data_btn.setMaximumSize(QSize(16777215, 50))
        self.view_data_btn.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;\n"
"")
        self.view_data_btn.setFrameShape(QFrame.StyledPanel)
        self.view_data_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.view_data_btn)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 0, 11, 0)
        self.Transaction_btn = QPushButton(self.view_data_btn)
        self.Transaction_btn.setObjectName(u"Transaction_btn")
        self.Transaction_btn.setMinimumSize(QSize(0, 30))
        self.Transaction_btn.setMaximumSize(QSize(16777215, 30))
        self.Transaction_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout.addWidget(self.Transaction_btn)

        self.Bakery_btn = QPushButton(self.view_data_btn)
        self.Bakery_btn.setObjectName(u"Bakery_btn")
        self.Bakery_btn.setMinimumSize(QSize(0, 30))
        self.Bakery_btn.setMaximumSize(QSize(16777215, 30))
        self.Bakery_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout.addWidget(self.Bakery_btn)

        self.Branches_btn = QPushButton(self.view_data_btn)
        self.Branches_btn.setObjectName(u"Branches_btn")
        self.Branches_btn.setMinimumSize(QSize(0, 30))
        self.Branches_btn.setMaximumSize(QSize(16777215, 30))
        self.Branches_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout.addWidget(self.Branches_btn)


        self.verticalLayout_13.addWidget(self.view_data_btn)

        self.stackedWidget_2 = QStackedWidget(self.page_view_data)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_view_transaction = QWidget()
        self.page_view_transaction.setObjectName(u"page_view_transaction")
        self.verticalLayout_16 = QVBoxLayout(self.page_view_transaction)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.filter_view_transaction = QFrame(self.page_view_transaction)
        self.filter_view_transaction.setObjectName(u"filter_view_transaction")
        self.filter_view_transaction.setMinimumSize(QSize(0, 100))
        self.filter_view_transaction.setMaximumSize(QSize(16777215, 100))
        self.filter_view_transaction.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.filter_view_transaction.setFrameShape(QFrame.StyledPanel)
        self.filter_view_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.filter_view_transaction)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.filter_date = QFrame(self.filter_view_transaction)
        self.filter_date.setObjectName(u"filter_date")
        self.filter_date.setFrameShape(QFrame.StyledPanel)
        self.filter_date.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.filter_date)
        self.horizontalLayout_14.setSpacing(7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_3 = QLabel(self.filter_date)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_14.addWidget(self.label_3)

        self.start_date_btn = QDateEdit(self.filter_date)
        self.start_date_btn.setObjectName(u"start_date_btn")
        self.start_date_btn.setMinimumSize(QSize(100, 0))
        self.start_date_btn.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_14.addWidget(self.start_date_btn)

        self.label_8 = QLabel(self.filter_date)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_14.addWidget(self.label_8)

        self.end_date_btn = QDateEdit(self.filter_date)
        self.end_date_btn.setObjectName(u"end_date_btn")
        self.end_date_btn.setMinimumSize(QSize(100, 0))
        self.end_date_btn.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(0, 0, 0)))

        self.horizontalLayout_14.addWidget(self.end_date_btn)


        self.verticalLayout_17.addWidget(self.filter_date, 0, Qt.AlignLeft)

        self.filter_branches = QFrame(self.filter_view_transaction)
        self.filter_branches.setObjectName(u"filter_branches")
        self.filter_branches.setFrameShape(QFrame.StyledPanel)
        self.filter_branches.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.filter_branches)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.filter_branches)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.cen_world_btn = QCheckBox(self.filter_branches)
        self.cen_world_btn.setObjectName(u"cen_world_btn")
        self.cen_world_btn.setChecked(True)

        self.horizontalLayout_13.addWidget(self.cen_world_btn)

        self.cen_lad_btn = QCheckBox(self.filter_branches)
        self.cen_lad_btn.setObjectName(u"cen_lad_btn")
        self.cen_lad_btn.setChecked(True)

        self.horizontalLayout_13.addWidget(self.cen_lad_btn)

        self.cen_rama9_btn = QCheckBox(self.filter_branches)
        self.cen_rama9_btn.setObjectName(u"cen_rama9_btn")
        self.cen_rama9_btn.setChecked(True)

        self.horizontalLayout_13.addWidget(self.cen_rama9_btn)

        self.submit_view_btn = QPushButton(self.filter_branches)
        self.submit_view_btn.setObjectName(u"submit_view_btn")
        self.submit_view_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_13.addWidget(self.submit_view_btn)


        self.verticalLayout_17.addWidget(self.filter_branches)


        self.verticalLayout_16.addWidget(self.filter_view_transaction)

        self.table_view_transaction = QFrame(self.page_view_transaction)
        self.table_view_transaction.setObjectName(u"table_view_transaction")
        self.table_view_transaction.setFrameShape(QFrame.StyledPanel)
        self.table_view_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.table_view_transaction)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.table_transaction = QTableWidget(self.table_view_transaction)
        self.table_transaction.setObjectName(u"table_transaction")
        self.table_transaction.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.table_transaction)


        self.verticalLayout_16.addWidget(self.table_view_transaction)

        self.stackedWidget_2.addWidget(self.page_view_transaction)
        self.page_view_bakery = QWidget()
        self.page_view_bakery.setObjectName(u"page_view_bakery")
        self.verticalLayout_21 = QVBoxLayout(self.page_view_bakery)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 11, 0, 0)
        self.table_bakery = QTableWidget(self.page_view_bakery)
        if (self.table_bakery.columnCount() < 5):
            self.table_bakery.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_bakery.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_bakery.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_bakery.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_bakery.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_bakery.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_bakery.setObjectName(u"table_bakery")
        self.table_bakery.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.table_bakery)

        self.stackedWidget_2.addWidget(self.page_view_bakery)
        self.page_view_branches = QWidget()
        self.page_view_branches.setObjectName(u"page_view_branches")
        self.verticalLayout_20 = QVBoxLayout(self.page_view_branches)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 11, 0, 0)
        self.table_branches = QTableWidget(self.page_view_branches)
        if (self.table_branches.columnCount() < 3):
            self.table_branches.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_branches.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_branches.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_branches.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.table_branches.setObjectName(u"table_branches")
        self.table_branches.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.table_branches)

        self.stackedWidget_2.addWidget(self.page_view_branches)

        self.verticalLayout_13.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_view_data)
        self.page_update_data = QWidget()
        self.page_update_data.setObjectName(u"page_update_data")
        self.verticalLayout_14 = QVBoxLayout(self.page_update_data)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.update_data_btn = QFrame(self.page_update_data)
        self.update_data_btn.setObjectName(u"update_data_btn")
        self.update_data_btn.setMinimumSize(QSize(0, 70))
        self.update_data_btn.setMaximumSize(QSize(16777215, 70))
        self.update_data_btn.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.update_data_btn.setFrameShape(QFrame.StyledPanel)
        self.update_data_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.update_data_btn)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Transaction_btn_2 = QPushButton(self.update_data_btn)
        self.Transaction_btn_2.setObjectName(u"Transaction_btn_2")
        self.Transaction_btn_2.setEnabled(True)
        self.Transaction_btn_2.setMinimumSize(QSize(0, 50))
        self.Transaction_btn_2.setMaximumSize(QSize(16777215, 50))
        self.Transaction_btn_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Transaction_btn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.Transaction_btn_2)

        self.Bakery_btn_2 = QPushButton(self.update_data_btn)
        self.Bakery_btn_2.setObjectName(u"Bakery_btn_2")
        self.Bakery_btn_2.setMinimumSize(QSize(0, 50))
        self.Bakery_btn_2.setMaximumSize(QSize(16777215, 50))
        self.Bakery_btn_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_15.addWidget(self.Bakery_btn_2)

        self.Branches_btn_2 = QPushButton(self.update_data_btn)
        self.Branches_btn_2.setObjectName(u"Branches_btn_2")
        self.Branches_btn_2.setMinimumSize(QSize(0, 50))
        self.Branches_btn_2.setMaximumSize(QSize(16777215, 50))
        self.Branches_btn_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_15.addWidget(self.Branches_btn_2)


        self.verticalLayout_14.addWidget(self.update_data_btn)

        self.update_data_area = QFrame(self.page_update_data)
        self.update_data_area.setObjectName(u"update_data_area")
        self.update_data_area.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.update_data_area.setFrameShape(QFrame.StyledPanel)
        self.update_data_area.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.update_data_area)
        self.horizontalLayout_16.setSpacing(7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.update_data_area)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_update_transaction = QWidget()
        self.page_update_transaction.setObjectName(u"page_update_transaction")
        self.horizontalLayout_17 = QHBoxLayout(self.page_update_transaction)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_update_transaction)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.update_trans_table = QTableWidget(self.frame_4)
        self.update_trans_table.setObjectName(u"update_trans_table")
        self.update_trans_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.update_trans_table)

        self.print_result_add_trans = QLabel(self.frame_4)
        self.print_result_add_trans.setObjectName(u"print_result_add_trans")

        self.verticalLayout_22.addWidget(self.print_result_add_trans, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_17.addWidget(self.frame_4)

        self.update_transaction_btn_area = QFrame(self.page_update_transaction)
        self.update_transaction_btn_area.setObjectName(u"update_transaction_btn_area")
        self.update_transaction_btn_area.setMinimumSize(QSize(90, 0))
        self.update_transaction_btn_area.setMaximumSize(QSize(90, 16777215))
        self.update_transaction_btn_area.setFrameShape(QFrame.StyledPanel)
        self.update_transaction_btn_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.update_transaction_btn_area)
        self.verticalLayout_23.setSpacing(7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, 11, -1)
        self.browse_trans_btn = QPushButton(self.update_transaction_btn_area)
        self.browse_trans_btn.setObjectName(u"browse_trans_btn")
        self.browse_trans_btn.setMinimumSize(QSize(0, 30))
        self.browse_trans_btn.setMaximumSize(QSize(16777215, 30))
        self.browse_trans_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.browse_trans_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browse_trans_btn.setIcon(icon3)

        self.verticalLayout_23.addWidget(self.browse_trans_btn)

        self.add_trans_btn = QPushButton(self.update_transaction_btn_area)
        self.add_trans_btn.setObjectName(u"add_trans_btn")
        self.add_trans_btn.setMinimumSize(QSize(0, 30))
        self.add_trans_btn.setMaximumSize(QSize(16777215, 30))
        self.add_trans_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_trans_btn.setIcon(icon4)

        self.verticalLayout_23.addWidget(self.add_trans_btn)

        self.clear_trans_btn = QPushButton(self.update_transaction_btn_area)
        self.clear_trans_btn.setObjectName(u"clear_trans_btn")
        self.clear_trans_btn.setMinimumSize(QSize(0, 30))
        self.clear_trans_btn.setMaximumSize(QSize(16777215, 30))
        self.clear_trans_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_trans_btn.setIcon(icon5)

        self.verticalLayout_23.addWidget(self.clear_trans_btn)


        self.horizontalLayout_17.addWidget(self.update_transaction_btn_area)

        self.stackedWidget_3.addWidget(self.page_update_transaction)
        self.page_update_bakery = QWidget()
        self.page_update_bakery.setObjectName(u"page_update_bakery")
        self.horizontalLayout_18 = QHBoxLayout(self.page_update_bakery)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_update_bakery)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.frame_5)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_update_bak_table = QWidget()
        self.page_update_bak_table.setObjectName(u"page_update_bak_table")
        self.verticalLayout_28 = QVBoxLayout(self.page_update_bak_table)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_5 = QStackedWidget(self.page_update_bak_table)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_view_bak_table = QWidget()
        self.page_view_bak_table.setObjectName(u"page_view_bak_table")
        self.verticalLayout_30 = QVBoxLayout(self.page_view_bak_table)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.table_area = QFrame(self.page_view_bak_table)
        self.table_area.setObjectName(u"table_area")
        self.table_area.setFrameShape(QFrame.StyledPanel)
        self.table_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.table_area)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.view_bak_table1 = QTableWidget(self.table_area)
        self.view_bak_table1.setObjectName(u"view_bak_table1")
        self.view_bak_table1.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_44.addWidget(self.view_bak_table1)


        self.verticalLayout_30.addWidget(self.table_area)

        self.btn_area = QFrame(self.page_view_bak_table)
        self.btn_area.setObjectName(u"btn_area")
        self.btn_area.setMinimumSize(QSize(0, 90))
        self.btn_area.setMaximumSize(QSize(16777215, 90))
        self.btn_area.setFrameShape(QFrame.StyledPanel)
        self.btn_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.btn_area)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_30.addWidget(self.btn_area)

        self.stackedWidget_5.addWidget(self.page_view_bak_table)
        self.page_remove_bak = QWidget()
        self.page_remove_bak.setObjectName(u"page_remove_bak")
        self.verticalLayout_19 = QVBoxLayout(self.page_remove_bak)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.table_area_2 = QFrame(self.page_remove_bak)
        self.table_area_2.setObjectName(u"table_area_2")
        self.table_area_2.setFrameShape(QFrame.StyledPanel)
        self.table_area_2.setFrameShadow(QFrame.Raised)
        self.view_bak_table2 = QTableWidget(self.table_area_2)
        self.view_bak_table2.setObjectName(u"view_bak_table2")
        self.view_bak_table2.setGeometry(QRect(0, 0, 821, 451))
        self.view_bak_table2.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.table_area_2)

        self.btn_area_2 = QFrame(self.page_remove_bak)
        self.btn_area_2.setObjectName(u"btn_area_2")
        self.btn_area_2.setMinimumSize(QSize(0, 90))
        self.btn_area_2.setMaximumSize(QSize(16777215, 90))
        self.btn_area_2.setFrameShape(QFrame.StyledPanel)
        self.btn_area_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.btn_area_2)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.btn_area_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_15)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_46.addWidget(self.label_13, 0, Qt.AlignHCenter)


        self.verticalLayout_50.addWidget(self.frame_15)

        self.frame_30 = QFrame(self.btn_area_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_28.setSpacing(100)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.btn_remove_bak_cancel = QPushButton(self.frame_30)
        self.btn_remove_bak_cancel.setObjectName(u"btn_remove_bak_cancel")
        self.btn_remove_bak_cancel.setMinimumSize(QSize(50, 30))
        self.btn_remove_bak_cancel.setMaximumSize(QSize(50, 30))
        self.btn_remove_bak_cancel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")

        self.horizontalLayout_28.addWidget(self.btn_remove_bak_cancel)

        self.btn_remove_bak_confirm = QPushButton(self.frame_30)
        self.btn_remove_bak_confirm.setObjectName(u"btn_remove_bak_confirm")
        self.btn_remove_bak_confirm.setMinimumSize(QSize(60, 30))
        self.btn_remove_bak_confirm.setMaximumSize(QSize(60, 30))
        self.btn_remove_bak_confirm.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")

        self.horizontalLayout_28.addWidget(self.btn_remove_bak_confirm)


        self.verticalLayout_50.addWidget(self.frame_30, 0, Qt.AlignHCenter)

        self.frame_29 = QFrame(self.btn_area_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_29)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_print_result_bak_remove = QLabel(self.frame_29)
        self.label_print_result_bak_remove.setObjectName(u"label_print_result_bak_remove")

        self.verticalLayout_47.addWidget(self.label_print_result_bak_remove, 0, Qt.AlignHCenter)


        self.verticalLayout_50.addWidget(self.frame_29)


        self.verticalLayout_19.addWidget(self.btn_area_2)

        self.stackedWidget_5.addWidget(self.page_remove_bak)
        self.page_edit_bak = QWidget()
        self.page_edit_bak.setObjectName(u"page_edit_bak")
        self.verticalLayout_45 = QVBoxLayout(self.page_edit_bak)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.table_area_3 = QFrame(self.page_edit_bak)
        self.table_area_3.setObjectName(u"table_area_3")
        self.table_area_3.setFrameShape(QFrame.StyledPanel)
        self.table_area_3.setFrameShadow(QFrame.Raised)
        self.view_bak_table3 = QTableWidget(self.table_area_3)
        self.view_bak_table3.setObjectName(u"view_bak_table3")
        self.view_bak_table3.setGeometry(QRect(0, 0, 821, 451))
        self.view_bak_table3.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_45.addWidget(self.table_area_3)

        self.btn_area_3 = QFrame(self.page_edit_bak)
        self.btn_area_3.setObjectName(u"btn_area_3")
        self.btn_area_3.setMinimumSize(QSize(0, 90))
        self.btn_area_3.setMaximumSize(QSize(16777215, 90))
        self.btn_area_3.setFrameShape(QFrame.StyledPanel)
        self.btn_area_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.btn_area_3)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.btn_area_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_31)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_31)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_48.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_51.addWidget(self.frame_31)

        self.frame_33 = QFrame(self.btn_area_3)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_29.setSpacing(100)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_bak_cancel = QPushButton(self.frame_33)
        self.btn_edit_bak_cancel.setObjectName(u"btn_edit_bak_cancel")
        self.btn_edit_bak_cancel.setMinimumSize(QSize(50, 30))
        self.btn_edit_bak_cancel.setMaximumSize(QSize(50, 30))
        self.btn_edit_bak_cancel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_edit_bak_cancel)

        self.btn_edit_bak_confirm = QPushButton(self.frame_33)
        self.btn_edit_bak_confirm.setObjectName(u"btn_edit_bak_confirm")
        self.btn_edit_bak_confirm.setMinimumSize(QSize(60, 30))
        self.btn_edit_bak_confirm.setMaximumSize(QSize(60, 30))
        self.btn_edit_bak_confirm.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")

        self.horizontalLayout_29.addWidget(self.btn_edit_bak_confirm)


        self.verticalLayout_51.addWidget(self.frame_33, 0, Qt.AlignHCenter)

        self.frame_32 = QFrame(self.btn_area_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_32)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_print_result_bak_edit = QLabel(self.frame_32)
        self.label_print_result_bak_edit.setObjectName(u"label_print_result_bak_edit")

        self.verticalLayout_49.addWidget(self.label_print_result_bak_edit, 0, Qt.AlignHCenter)


        self.verticalLayout_51.addWidget(self.frame_32)


        self.verticalLayout_45.addWidget(self.btn_area_3)

        self.stackedWidget_5.addWidget(self.page_edit_bak)

        self.verticalLayout_28.addWidget(self.stackedWidget_5)

        self.stackedWidget_4.addWidget(self.page_update_bak_table)
        self.page_update_bak_add = QWidget()
        self.page_update_bak_add.setObjectName(u"page_update_bak_add")
        self.verticalLayout_29 = QVBoxLayout(self.page_update_bak_add)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.add_bak_area = QFrame(self.page_update_bak_add)
        self.add_bak_area.setObjectName(u"add_bak_area")
        self.add_bak_area.setFrameShape(QFrame.StyledPanel)
        self.add_bak_area.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.add_bak_area)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_6 = QFrame(self.add_bak_area)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.add_bak_area)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_10)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_16)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_33.addWidget(self.label_4)


        self.verticalLayout_32.addWidget(self.frame_16, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_18)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(120, 0))
        self.frame_23.setMaximumSize(QSize(120, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_23)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_6 = QLabel(self.frame_23)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_35.addWidget(self.label_6)


        self.horizontalLayout_22.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_24)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.lineEdit_add_bak_name = QLineEdit(self.frame_24)
        self.lineEdit_add_bak_name.setObjectName(u"lineEdit_add_bak_name")
        self.lineEdit_add_bak_name.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_bak_name.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_add_bak_name.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_38.addWidget(self.lineEdit_add_bak_name)


        self.horizontalLayout_22.addWidget(self.frame_24)


        self.verticalLayout_34.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(120, 0))
        self.frame_25.setMaximumSize(QSize(120, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_25)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_7 = QLabel(self.frame_25)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_36.addWidget(self.label_7)


        self.horizontalLayout_23.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_20)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_26)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.comboBox_add_bak_cate = QComboBox(self.frame_26)
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.addItem("")
        self.comboBox_add_bak_cate.setObjectName(u"comboBox_add_bak_cate")
        self.comboBox_add_bak_cate.setMinimumSize(QSize(0, 30))
        self.comboBox_add_bak_cate.setMaximumSize(QSize(16777215, 30))
        self.comboBox_add_bak_cate.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.verticalLayout_39.addWidget(self.comboBox_add_bak_cate)


        self.horizontalLayout_23.addWidget(self.frame_26)


        self.verticalLayout_34.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_27 = QFrame(self.frame_21)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(120, 0))
        self.frame_27.setMaximumSize(QSize(120, 16777215))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_27)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_10 = QLabel(self.frame_27)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_37.addWidget(self.label_10)


        self.horizontalLayout_24.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_21)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_28)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.lineEdit_add_bak_price = QLineEdit(self.frame_28)
        self.lineEdit_add_bak_price.setObjectName(u"lineEdit_add_bak_price")
        self.lineEdit_add_bak_price.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_bak_price.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_add_bak_price.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_40.addWidget(self.lineEdit_add_bak_price)


        self.horizontalLayout_24.addWidget(self.frame_28)


        self.verticalLayout_34.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_18)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.btn_cancel_add_bak = QPushButton(self.frame_22)
        self.btn_cancel_add_bak.setObjectName(u"btn_cancel_add_bak")
        self.btn_cancel_add_bak.setMinimumSize(QSize(50, 30))
        self.btn_cancel_add_bak.setMaximumSize(QSize(50, 30))
        self.btn_cancel_add_bak.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_cancel_add_bak)

        self.btn_confirm_add_bak = QPushButton(self.frame_22)
        self.btn_confirm_add_bak.setObjectName(u"btn_confirm_add_bak")
        self.btn_confirm_add_bak.setMinimumSize(QSize(60, 30))
        self.btn_confirm_add_bak.setMaximumSize(QSize(60, 30))
        self.btn_confirm_add_bak.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")

        self.horizontalLayout_25.addWidget(self.btn_confirm_add_bak)


        self.verticalLayout_34.addWidget(self.frame_22)


        self.horizontalLayout_21.addWidget(self.frame_18)


        self.verticalLayout_32.addWidget(self.frame_17)


        self.horizontalLayout_20.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.add_bak_area)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(100, 0))
        self.frame_13.setMaximumSize(QSize(100, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_13)


        self.verticalLayout_29.addWidget(self.add_bak_area)

        self.print_result_add_bak_area = QFrame(self.page_update_bak_add)
        self.print_result_add_bak_area.setObjectName(u"print_result_add_bak_area")
        self.print_result_add_bak_area.setMinimumSize(QSize(0, 100))
        self.print_result_add_bak_area.setMaximumSize(QSize(16777215, 100))
        self.print_result_add_bak_area.setFrameShape(QFrame.StyledPanel)
        self.print_result_add_bak_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.print_result_add_bak_area)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_print_result_add = QLabel(self.print_result_add_bak_area)
        self.label_print_result_add.setObjectName(u"label_print_result_add")

        self.verticalLayout_41.addWidget(self.label_print_result_add, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_29.addWidget(self.print_result_add_bak_area)

        self.stackedWidget_4.addWidget(self.page_update_bak_add)

        self.verticalLayout_25.addWidget(self.stackedWidget_4)


        self.horizontalLayout_18.addWidget(self.frame_5)

        self.update_bakery_btn_area = QFrame(self.page_update_bakery)
        self.update_bakery_btn_area.setObjectName(u"update_bakery_btn_area")
        self.update_bakery_btn_area.setMinimumSize(QSize(90, 0))
        self.update_bakery_btn_area.setMaximumSize(QSize(90, 16777215))
        self.update_bakery_btn_area.setFrameShape(QFrame.StyledPanel)
        self.update_bakery_btn_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.update_bakery_btn_area)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.add_bak_btn = QPushButton(self.update_bakery_btn_area)
        self.add_bak_btn.setObjectName(u"add_bak_btn")
        self.add_bak_btn.setMinimumSize(QSize(0, 30))
        self.add_bak_btn.setMaximumSize(QSize(16777215, 30))
        self.add_bak_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")
        self.add_bak_btn.setIcon(icon4)

        self.verticalLayout_24.addWidget(self.add_bak_btn)

        self.remove_bak_btn = QPushButton(self.update_bakery_btn_area)
        self.remove_bak_btn.setObjectName(u"remove_bak_btn")
        self.remove_bak_btn.setMinimumSize(QSize(0, 30))
        self.remove_bak_btn.setMaximumSize(QSize(16777215, 30))
        self.remove_bak_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_bak_btn.setIcon(icon6)

        self.verticalLayout_24.addWidget(self.remove_bak_btn)

        self.edit_bak_btn = QPushButton(self.update_bakery_btn_area)
        self.edit_bak_btn.setObjectName(u"edit_bak_btn")
        self.edit_bak_btn.setMinimumSize(QSize(0, 30))
        self.edit_bak_btn.setMaximumSize(QSize(16777215, 30))
        self.edit_bak_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 197, 77);\n"
"	border: 2px solid rgb(255, 197, 77);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(244, 157, 26);\n"
"	border: 2px solid rgb(255, 197, 77);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_bak_btn.setIcon(icon7)

        self.verticalLayout_24.addWidget(self.edit_bak_btn)

        self.refresh_bak_btn = QPushButton(self.update_bakery_btn_area)
        self.refresh_bak_btn.setObjectName(u"refresh_bak_btn")
        self.refresh_bak_btn.setMinimumSize(QSize(0, 30))
        self.refresh_bak_btn.setMaximumSize(QSize(16777215, 30))
        self.refresh_bak_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_bak_btn.setIcon(icon8)

        self.verticalLayout_24.addWidget(self.refresh_bak_btn)


        self.horizontalLayout_18.addWidget(self.update_bakery_btn_area)

        self.stackedWidget_3.addWidget(self.page_update_bakery)
        self.page_update_branch = QWidget()
        self.page_update_branch.setObjectName(u"page_update_branch")
        self.horizontalLayout_19 = QHBoxLayout(self.page_update_branch)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_update_branch)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_7)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_8)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_9)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_6 = QStackedWidget(self.frame_9)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_update_branch_table = QWidget()
        self.page_update_branch_table.setObjectName(u"page_update_branch_table")
        self.verticalLayout_53 = QVBoxLayout(self.page_update_branch_table)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_7 = QStackedWidget(self.page_update_branch_table)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.page_view_branch_table = QWidget()
        self.page_view_branch_table.setObjectName(u"page_view_branch_table")
        self.verticalLayout_54 = QVBoxLayout(self.page_view_branch_table)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.table_area_4 = QFrame(self.page_view_branch_table)
        self.table_area_4.setObjectName(u"table_area_4")
        self.table_area_4.setFrameShape(QFrame.StyledPanel)
        self.table_area_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.table_area_4)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.view_branch_table = QTableWidget(self.table_area_4)
        self.view_branch_table.setObjectName(u"view_branch_table")
        self.view_branch_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_55.addWidget(self.view_branch_table)


        self.verticalLayout_54.addWidget(self.table_area_4)

        self.btn_area_4 = QFrame(self.page_view_branch_table)
        self.btn_area_4.setObjectName(u"btn_area_4")
        self.btn_area_4.setMinimumSize(QSize(0, 90))
        self.btn_area_4.setMaximumSize(QSize(16777215, 90))
        self.btn_area_4.setFrameShape(QFrame.StyledPanel)
        self.btn_area_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.btn_area_4)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_54.addWidget(self.btn_area_4)

        self.stackedWidget_7.addWidget(self.page_view_branch_table)
        self.page_remove_branch = QWidget()
        self.page_remove_branch.setObjectName(u"page_remove_branch")
        self.verticalLayout_59 = QVBoxLayout(self.page_remove_branch)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.table_area_5 = QFrame(self.page_remove_branch)
        self.table_area_5.setObjectName(u"table_area_5")
        self.table_area_5.setFrameShape(QFrame.StyledPanel)
        self.table_area_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.table_area_5)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.view_branch_table_2 = QTableWidget(self.table_area_5)
        self.view_branch_table_2.setObjectName(u"view_branch_table_2")
        self.view_branch_table_2.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_42.addWidget(self.view_branch_table_2)


        self.verticalLayout_59.addWidget(self.table_area_5)

        self.btn_area_5 = QFrame(self.page_remove_branch)
        self.btn_area_5.setObjectName(u"btn_area_5")
        self.btn_area_5.setMinimumSize(QSize(0, 90))
        self.btn_area_5.setMaximumSize(QSize(16777215, 90))
        self.btn_area_5.setFrameShape(QFrame.StyledPanel)
        self.btn_area_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.btn_area_5)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.btn_area_5)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_37)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_37)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_61.addWidget(self.label_17, 0, Qt.AlignHCenter)


        self.verticalLayout_60.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.btn_area_5)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_31.setSpacing(100)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.btn_remove_branch_cancel = QPushButton(self.frame_38)
        self.btn_remove_branch_cancel.setObjectName(u"btn_remove_branch_cancel")
        self.btn_remove_branch_cancel.setMinimumSize(QSize(50, 30))
        self.btn_remove_branch_cancel.setMaximumSize(QSize(50, 30))
        self.btn_remove_branch_cancel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")

        self.horizontalLayout_31.addWidget(self.btn_remove_branch_cancel)

        self.btn_remove_branch_confirm = QPushButton(self.frame_38)
        self.btn_remove_branch_confirm.setObjectName(u"btn_remove_branch_confirm")
        self.btn_remove_branch_confirm.setMinimumSize(QSize(60, 30))
        self.btn_remove_branch_confirm.setMaximumSize(QSize(60, 30))
        self.btn_remove_branch_confirm.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")

        self.horizontalLayout_31.addWidget(self.btn_remove_branch_confirm)


        self.verticalLayout_60.addWidget(self.frame_38, 0, Qt.AlignHCenter)

        self.frame_39 = QFrame(self.btn_area_5)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_39)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_print_result_branch_remove = QLabel(self.frame_39)
        self.label_print_result_branch_remove.setObjectName(u"label_print_result_branch_remove")

        self.verticalLayout_62.addWidget(self.label_print_result_branch_remove, 0, Qt.AlignHCenter)


        self.verticalLayout_60.addWidget(self.frame_39)


        self.verticalLayout_59.addWidget(self.btn_area_5)

        self.stackedWidget_7.addWidget(self.page_remove_branch)
        self.page_edit_branch = QWidget()
        self.page_edit_branch.setObjectName(u"page_edit_branch")
        self.verticalLayout_63 = QVBoxLayout(self.page_edit_branch)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.table_area_6 = QFrame(self.page_edit_branch)
        self.table_area_6.setObjectName(u"table_area_6")
        self.table_area_6.setFrameShape(QFrame.StyledPanel)
        self.table_area_6.setFrameShadow(QFrame.Raised)
        self.view_branch_table_3 = QTableWidget(self.table_area_6)
        self.view_branch_table_3.setObjectName(u"view_branch_table_3")
        self.view_branch_table_3.setGeometry(QRect(0, 0, 821, 451))
        self.view_branch_table_3.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_63.addWidget(self.table_area_6)

        self.btn_area_6 = QFrame(self.page_edit_branch)
        self.btn_area_6.setObjectName(u"btn_area_6")
        self.btn_area_6.setMinimumSize(QSize(0, 90))
        self.btn_area_6.setMaximumSize(QSize(16777215, 90))
        self.btn_area_6.setFrameShape(QFrame.StyledPanel)
        self.btn_area_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.btn_area_6)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.btn_area_6)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_40)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_40)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_65.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_64.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.btn_area_6)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_32.setSpacing(100)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_branch_cancel = QPushButton(self.frame_41)
        self.btn_edit_branch_cancel.setObjectName(u"btn_edit_branch_cancel")
        self.btn_edit_branch_cancel.setMinimumSize(QSize(50, 30))
        self.btn_edit_branch_cancel.setMaximumSize(QSize(50, 30))
        self.btn_edit_branch_cancel.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")

        self.horizontalLayout_32.addWidget(self.btn_edit_branch_cancel)

        self.btn_edit_branch_confirm = QPushButton(self.frame_41)
        self.btn_edit_branch_confirm.setObjectName(u"btn_edit_branch_confirm")
        self.btn_edit_branch_confirm.setMinimumSize(QSize(60, 30))
        self.btn_edit_branch_confirm.setMaximumSize(QSize(60, 30))
        self.btn_edit_branch_confirm.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")

        self.horizontalLayout_32.addWidget(self.btn_edit_branch_confirm)


        self.verticalLayout_64.addWidget(self.frame_41, 0, Qt.AlignHCenter)

        self.frame_42 = QFrame(self.btn_area_6)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_42)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_print_result_branch_edit = QLabel(self.frame_42)
        self.label_print_result_branch_edit.setObjectName(u"label_print_result_branch_edit")

        self.verticalLayout_66.addWidget(self.label_print_result_branch_edit, 0, Qt.AlignHCenter)


        self.verticalLayout_64.addWidget(self.frame_42)


        self.verticalLayout_63.addWidget(self.btn_area_6)

        self.stackedWidget_7.addWidget(self.page_edit_branch)

        self.verticalLayout_53.addWidget(self.stackedWidget_7)

        self.stackedWidget_6.addWidget(self.page_update_branch_table)
        self.page_update_branch_add = QWidget()
        self.page_update_branch_add.setObjectName(u"page_update_branch_add")
        self.verticalLayout_67 = QVBoxLayout(self.page_update_branch_add)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.add_branch_area = QFrame(self.page_update_branch_add)
        self.add_branch_area.setObjectName(u"add_branch_area")
        self.add_branch_area.setFrameShape(QFrame.StyledPanel)
        self.add_branch_area.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.add_branch_area)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_43 = QFrame(self.add_branch_area)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(100, 0))
        self.frame_43.setMaximumSize(QSize(100, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.add_branch_area)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_44)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(16777215, 50))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_45)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_19 = QLabel(self.frame_45)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_69.addWidget(self.label_19)


        self.verticalLayout_68.addWidget(self.frame_45, 0, Qt.AlignHCenter)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_47)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(120, 0))
        self.frame_49.setMaximumSize(QSize(120, 16777215))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_49)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, -1, -1, -1)
        self.label_20 = QLabel(self.frame_49)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_71.addWidget(self.label_20)


        self.horizontalLayout_35.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_50)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.lineEdit_add_branch_name = QLineEdit(self.frame_50)
        self.lineEdit_add_branch_name.setObjectName(u"lineEdit_add_branch_name")
        self.lineEdit_add_branch_name.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_branch_name.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_add_branch_name.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_72.addWidget(self.lineEdit_add_branch_name)


        self.horizontalLayout_35.addWidget(self.frame_50)


        self.verticalLayout_70.addWidget(self.frame_48)

        self.frame_51 = QFrame(self.frame_47)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(120, 0))
        self.frame_52.setMaximumSize(QSize(120, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_52)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, -1, -1, -1)
        self.label_22 = QLabel(self.frame_52)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_73.addWidget(self.label_22)


        self.horizontalLayout_36.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_51)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_53)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.lineEdit_add_branch_targetyear = QLineEdit(self.frame_53)
        self.lineEdit_add_branch_targetyear.setObjectName(u"lineEdit_add_branch_targetyear")
        self.lineEdit_add_branch_targetyear.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_branch_targetyear.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_add_branch_targetyear.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_74.addWidget(self.lineEdit_add_branch_targetyear)


        self.horizontalLayout_36.addWidget(self.frame_53)


        self.verticalLayout_70.addWidget(self.frame_51)

        self.frame_54 = QFrame(self.frame_47)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(120, 0))
        self.frame_55.setMaximumSize(QSize(120, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_55)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, -1, -1, -1)
        self.label_21 = QLabel(self.frame_55)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_75.addWidget(self.label_21)


        self.horizontalLayout_37.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_56)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.lineEdit_add_branch_price = QLineEdit(self.frame_56)
        self.lineEdit_add_branch_price.setObjectName(u"lineEdit_add_branch_price")
        self.lineEdit_add_branch_price.setMinimumSize(QSize(0, 30))
        self.lineEdit_add_branch_price.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_add_branch_price.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_76.addWidget(self.lineEdit_add_branch_price)


        self.horizontalLayout_37.addWidget(self.frame_56)


        self.verticalLayout_70.addWidget(self.frame_54)

        self.frame_57 = QFrame(self.frame_47)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.btn_cancel_add_branch = QPushButton(self.frame_57)
        self.btn_cancel_add_branch.setObjectName(u"btn_cancel_add_branch")
        self.btn_cancel_add_branch.setMinimumSize(QSize(50, 30))
        self.btn_cancel_add_branch.setMaximumSize(QSize(50, 30))
        self.btn_cancel_add_branch.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")

        self.horizontalLayout_38.addWidget(self.btn_cancel_add_branch)

        self.btn_confirm_add_branch = QPushButton(self.frame_57)
        self.btn_confirm_add_branch.setObjectName(u"btn_confirm_add_branch")
        self.btn_confirm_add_branch.setMinimumSize(QSize(60, 30))
        self.btn_confirm_add_branch.setMaximumSize(QSize(60, 30))
        self.btn_confirm_add_branch.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")

        self.horizontalLayout_38.addWidget(self.btn_confirm_add_branch)


        self.verticalLayout_70.addWidget(self.frame_57)


        self.horizontalLayout_34.addWidget(self.frame_47)


        self.verticalLayout_68.addWidget(self.frame_46)


        self.horizontalLayout_33.addWidget(self.frame_44)

        self.frame_58 = QFrame(self.add_branch_area)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(100, 0))
        self.frame_58.setMaximumSize(QSize(100, 16777215))
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_58)


        self.verticalLayout_67.addWidget(self.add_branch_area)

        self.print_result_add_branch_area = QFrame(self.page_update_branch_add)
        self.print_result_add_branch_area.setObjectName(u"print_result_add_branch_area")
        self.print_result_add_branch_area.setMinimumSize(QSize(0, 100))
        self.print_result_add_branch_area.setMaximumSize(QSize(16777215, 100))
        self.print_result_add_branch_area.setFrameShape(QFrame.StyledPanel)
        self.print_result_add_branch_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.print_result_add_branch_area)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_print_result_add_branch = QLabel(self.print_result_add_branch_area)
        self.label_print_result_add_branch.setObjectName(u"label_print_result_add_branch")

        self.verticalLayout_77.addWidget(self.label_print_result_add_branch, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_67.addWidget(self.print_result_add_branch_area)

        self.stackedWidget_6.addWidget(self.page_update_branch_add)

        self.verticalLayout_52.addWidget(self.stackedWidget_6)


        self.verticalLayout_78.addWidget(self.frame_9)


        self.verticalLayout_27.addWidget(self.frame_8)


        self.horizontalLayout_19.addWidget(self.frame_7)

        self.update_branch_btn_area = QFrame(self.page_update_branch)
        self.update_branch_btn_area.setObjectName(u"update_branch_btn_area")
        self.update_branch_btn_area.setMinimumSize(QSize(90, 0))
        self.update_branch_btn_area.setMaximumSize(QSize(90, 16777215))
        self.update_branch_btn_area.setFrameShape(QFrame.StyledPanel)
        self.update_branch_btn_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.update_branch_btn_area)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, -1, -1, -1)
        self.add_branch_btn = QPushButton(self.update_branch_btn_area)
        self.add_branch_btn.setObjectName(u"add_branch_btn")
        self.add_branch_btn.setMinimumSize(QSize(0, 30))
        self.add_branch_btn.setMaximumSize(QSize(16777215, 30))
        self.add_branch_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 181, 123);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(83, 191, 157);\n"
"	border: 2px solid rgb(31, 181, 123);\n"
"}")
        self.add_branch_btn.setIcon(icon4)

        self.verticalLayout_26.addWidget(self.add_branch_btn)

        self.remove_branch_btn = QPushButton(self.update_branch_btn_area)
        self.remove_branch_btn.setObjectName(u"remove_branch_btn")
        self.remove_branch_btn.setMinimumSize(QSize(0, 30))
        self.remove_branch_btn.setMaximumSize(QSize(16777215, 30))
        self.remove_branch_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 53, 53);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(235, 83, 83);\n"
"	border: 2px solid rgb(220, 53, 53);\n"
"}")
        self.remove_branch_btn.setIcon(icon6)

        self.verticalLayout_26.addWidget(self.remove_branch_btn)

        self.edit_branch_btn = QPushButton(self.update_branch_btn_area)
        self.edit_branch_btn.setObjectName(u"edit_branch_btn")
        self.edit_branch_btn.setMinimumSize(QSize(0, 30))
        self.edit_branch_btn.setMaximumSize(QSize(16777215, 30))
        self.edit_branch_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 197, 77);\n"
"	border: 2px solid rgb(255, 197, 77);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(244, 157, 26);\n"
"	border: 2px solid rgb(255, 197, 77);\n"
"}")
        self.edit_branch_btn.setIcon(icon7)

        self.verticalLayout_26.addWidget(self.edit_branch_btn)

        self.refresh_branch_btn = QPushButton(self.update_branch_btn_area)
        self.refresh_branch_btn.setObjectName(u"refresh_branch_btn")
        self.refresh_branch_btn.setMinimumSize(QSize(0, 30))
        self.refresh_branch_btn.setMaximumSize(QSize(16777215, 30))
        self.refresh_branch_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.refresh_branch_btn.setIcon(icon8)

        self.verticalLayout_26.addWidget(self.refresh_branch_btn)


        self.horizontalLayout_19.addWidget(self.update_branch_btn_area)

        self.stackedWidget_3.addWidget(self.page_update_branch)

        self.horizontalLayout_16.addWidget(self.stackedWidget_3)


        self.verticalLayout_14.addWidget(self.update_data_area)

        self.stackedWidget.addWidget(self.page_update_data)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout_27.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)




################################################
###### View Data Click Event ###################

        # if click submit_view_btn, show data in table_transaction
        self.submit_view_btn.clicked.connect(self.view_transaction)
        # self.submit_view_btn.clicked.connect(lambda: print("click: submit_view_btn"))

        self.Transaction_btn.clicked.connect(self.view_transaction)    
        self.Transaction_btn.clicked.connect(lambda: print("click: Transaction_btn")) 

        self.Bakery_btn.clicked.connect(self.view_bakery)
        self.Bakery_btn.clicked.connect(lambda: print("click: Bakery_btn"))


        self.Branches_btn.clicked.connect(self.view_branch)
        self.Branches_btn.clicked.connect(lambda: print("click: Branches_btn"))

###### Update Data Click Event ###################
        self.Transaction_btn_2.clicked.connect(self.page_update_transaction_func)
        self.Transaction_btn_2.clicked.connect(lambda: print("click: Transaction_btn_2"))

        self.Bakery_btn_2.clicked.connect(self.page_update_bakery_func)
        self.Bakery_btn_2.clicked.connect(lambda: print("click: Bakery_btn_2"))

##### Update Branch Click Event ##################
        self.Branches_btn_2.clicked.connect(self.page_update_branch_func)
        self.Branches_btn_2.clicked.connect(lambda: print("click: Branches_btn_2"))

        ##### Add Branch Click Event ##################
        self.add_branch_btn.clicked.connect(self.add_branch_func)
        self.add_branch_btn.clicked.connect(lambda: print("click: add_branch_btn"))

        ##### Refresh Branch Click Event ##################
        self.refresh_branch_btn.clicked.connect(self.page_update_branch_func)
        self.refresh_branch_btn.clicked.connect(lambda: print("click: refresh_branch_btn"))

        ##### Remove Branch Click Event ##################
        self.remove_branch_btn.clicked.connect(self.view_remove_branch_table_func)
        self.remove_branch_btn.clicked.connect(lambda: print("click: remove_branch_btn"))

        self.btn_remove_branch_confirm.clicked.connect(self.remove_branch_func)
        self.btn_remove_branch_confirm.clicked.connect(lambda: print("click: btn_remove_branch_confirm"))

        self.btn_remove_branch_cancel.clicked.connect(self.cancel_remove_branch_func)
        self.btn_remove_branch_cancel.clicked.connect(lambda: print("click: btn_remove_branch_cancel"))

        ##### Edit Branch Click Event ##################
        self.edit_branch_btn.clicked.connect(self.view_edit_branch_table_func)
        self.edit_branch_btn.clicked.connect(lambda: print("click: edit_branch_btn"))

        self.btn_edit_branch_confirm.clicked.connect(self.edit_branch_func)
        self.btn_edit_branch_confirm.clicked.connect(lambda: print("click: btn_edit_branch_confirm"))

        self.btn_edit_branch_cancel.clicked.connect(self.cancel_edit_branch_func)
        self.btn_edit_branch_cancel.clicked.connect(lambda: print("click: btn_edit_branch_cancel"))

##### Update Bakery Click Event ##################
        self.Bakery_btn_2.clicked.connect(self.page_update_bakery_func)
        self.Bakery_btn_2.clicked.connect(lambda: print("click: Bakery_btn_2"))

        ##### Add Bakery Click Event ##################
        self.add_bak_btn.clicked.connect(self.add_bakery_func)
        self.add_bak_btn.clicked.connect(lambda: print("click: add_bak_btn"))

        ##### Refresh Bakery Click Event ##################
        self.refresh_bak_btn.clicked.connect(self.page_update_bakery_func)
        self.refresh_bak_btn.clicked.connect(lambda: print("click: refresh_bak_btn"))

        ##### Remove Bakery Click Event ##################
        self.remove_bak_btn.clicked.connect(self.view_remove_bakery_table_func)
        self.remove_bak_btn.clicked.connect(lambda: print("click: remove_bak_btn"))

        self.btn_remove_bak_confirm.clicked.connect(self.remove_bakery_func)
        self.btn_remove_bak_confirm.clicked.connect(lambda: print("click: btn_remove_bak_confirm"))

        self.btn_remove_bak_cancel.clicked.connect(self.cancel_remove_bakery_func)
        self.btn_remove_bak_cancel.clicked.connect(lambda: print("click: btn_remove_bak_cancel"))

        ##### Edit Bakery Click Event ##################
        self.edit_bak_btn.clicked.connect(self.view_edit_bakery_table_func)
        self.edit_bak_btn.clicked.connect(lambda: print("click: edit_bak_btn"))

        self.btn_edit_bak_confirm.clicked.connect(self.edit_bakery_func)
        self.btn_edit_bak_confirm.clicked.connect(lambda: print("click: btn_edit_bak_confirm"))

        self.btn_edit_bak_cancel.clicked.connect(self.cancel_edit_bakery_func)
        self.btn_edit_bak_cancel.clicked.connect(lambda: print("click: btn_edit_bak_cancel"))

        





###### Update Transaction Page ###################
        self.browse_trans_btn.clicked.connect(self.browse_transaction_func)
        self.browse_trans_btn.clicked.connect(lambda: print("click: browse_trans_btn"))

##### Dashboard Click Event ##################

        self.submit_view_btn_2.clicked.connect(self.plot_chart)
        self.submit_view_btn_2.clicked.connect(lambda: print("click: submit_view_btn_2"))



    # setupUi

################################################
    def filter_transaction_data(self):
        import read_table_func
        
        df = read_table_func.read_transactions_table()

        # convert start_date_btn and end_date_btn from QDate to Python
        start_date = self.start_date_btn.date().toPython()
        start_date = pd.to_datetime(start_date)
        end_date = self.end_date_btn.date().toPython()
        end_date = pd.to_datetime(end_date)


        # filter data by date
        df = df[(df['datetime'] >= start_date) & (df['datetime'] <= end_date)]

        # filter data by branch
        if self.cen_world_btn.isChecked() and self.cen_rama9_btn.isChecked() and self.cen_lad_btn.isChecked():
                df = df[df['branch'].isin(['Central World', 'Central Rama 9', 'Central Ladprao'])]
        elif self.cen_world_btn.isChecked() and self.cen_rama9_btn.isChecked():
                df = df[df['branch'].isin(['Central World', 'Central Rama 9'])]
        elif self.cen_world_btn.isChecked() and self.cen_lad_btn.isChecked():
                df = df[df['branch'].isin(['Central World', 'Central Ladprao'])]
        elif self.cen_rama9_btn.isChecked() and self.cen_lad_btn.isChecked():
                df = df[df['branch'].isin(['Central Rama 9', 'Central Ladprao'])]
        elif self.cen_world_btn.isChecked():
                df = df[df['branch'] == 'Central World']
        elif self.cen_rama9_btn.isChecked():
                df = df[df['branch'] == 'Central Rama 9']
        elif self.cen_lad_btn.isChecked():
                df = df[df['branch'] == 'Central Ladprao']

        # show data in table table_transaction
        self.table_transaction.setRowCount(len(df))
        self.table_transaction.setColumnCount(len(df.columns))

        for i in range(len(df)):
                for j in range(len(df.columns)):
                        self.table_transaction.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
        self.table_transaction.setHorizontalHeaderLabels(df.columns)
        self.table_transaction.resizeColumnsToContents()
        self.table_transaction.resizeRowsToContents()
        self.table_transaction.setSortingEnabled(True)

    def view_bakery_table(self):
        import read_table_func
        df2 = read_table_func.read_bakery_table()
        self.table_bakery.setRowCount(len(df2))
        self.table_bakery.setColumnCount(len(df2.columns))

        for i in range(len(df2)):
                for j in range(len(df2.columns)):
                        self.table_bakery.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))
        self.table_bakery.setHorizontalHeaderLabels(df2.columns)
        self.table_bakery.resizeColumnsToContents()
        self.table_bakery.resizeRowsToContents()
        self.table_bakery.setSortingEnabled(True)


    def view_branches_table(self):
        import read_table_func
        df3 = read_table_func.read_branch_table()
        self.table_branches.setRowCount(len(df3))
        self.table_branches.setColumnCount(len(df3.columns))

        for i in range(len(df3)):
                for j in range(len(df3.columns)):
                        self.table_branches.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        self.table_branches.setHorizontalHeaderLabels(df3.columns)
        self.table_branches.resizeColumnsToContents()
        self.table_branches.resizeRowsToContents()  
        self.table_branches.setSortingEnabled(True)

################################################

    def view_transaction(self):
        #set page in stackedWidget_2 to page_view_transaction
        self.stackedWidget_2.setCurrentIndex(0)
        self.submit_view_btn.clicked.connect(self.filter_transaction_data)
        self.submit_view_btn.clicked.connect(lambda: print("click: submit_view_btn"))

# change pange in stackedWidget
    def view_bakery(self):
        # set page in stackedWidget_2 to page_view_bakery
        self.stackedWidget_2.setCurrentIndex(1)
        # show data in table table_bakery
        self.view_bakery_table()

    def view_branch(self):
        # set page in stackedWidget_2 to page_view_branch
        self.stackedWidget_2.setCurrentIndex(2)
        # show data in table table_branch
        self.view_branches_table()



################################################ Done 1
##### View Update Table Page ####################
    def view_bakery_update_table(self):
        import read_table_func
        df2 = read_table_func.read_bakery_table()
        self.view_bak_table1.setRowCount(len(df2))
        self.view_bak_table1.setColumnCount(len(df2.columns))

        for i in range(len(df2)):
                for j in range(len(df2.columns)):
                        self.view_bak_table1.setItem(i, j, QTableWidgetItem(str(df2.iloc[i, j])))
        self.view_bak_table1.setHorizontalHeaderLabels(df2.columns)
        self.view_bak_table1.resizeColumnsToContents()
        self.view_bak_table1.resizeRowsToContents()
        self.view_bak_table1.setSortingEnabled(True)

    def view_branches_update_table(self):
        import read_table_func
        df3 = read_table_func.read_branch_table()
        self.view_branch_table.setRowCount(len(df3))
        self.view_branch_table.setColumnCount(len(df3.columns))

        for i in range(len(df3)):
                for j in range(len(df3.columns)):
                        self.view_branch_table.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        self.view_branch_table.setHorizontalHeaderLabels(df3.columns)
        self.view_branch_table.resizeColumnsToContents()
        self.view_branch_table.resizeRowsToContents()  
        self.view_branch_table.setSortingEnabled(True)

###### Update Data Page ######

    def page_update_transaction_func(self):
        # set page in stackedWidget_3 to page_update_transaction
        self.stackedWidget_3.setCurrentIndex(0)

    def page_update_bakery_func(self):
        # set page in stackedWidget_3 to page_update_bakery
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(0)
        # show data in table table_bakery
        self.view_bakery_update_table()

    def page_update_branch_func(self):
        # set page in stackedWidget_3 to page_update_branch
        self.stackedWidget_3.setCurrentIndex(2)
        self.stackedWidget_7.setCurrentIndex(0)
        self.view_branches_update_table()
        self.refresh_branch_btn.clicked.connect(self.page_update_branch_func)


###### Update Branch Function ######
###### Add Branch ######
    def add_branch_to_mongodb(self):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.branches
        # get data from lineEdit_add_branch
        branch_name = self.lineEdit_add_branch_name.text()
        target_year = int(self.lineEdit_add_branch_targetyear.text())
        target_thb = int(self.lineEdit_add_branch_price.text())

        try:
                collection.insert_one({"branch_name": branch_name, "target_year": target_year, "target_thb": target_thb})
                self.label_print_result_add_branch.setText('Add branch is done')
                self.lineEdit_add_branch_name.setText("")
                self.lineEdit_add_branch_targetyear.setText("")
                self.lineEdit_add_branch_price.setText("")

        except:
                # self.label_print_result_add_branch.setText("Add branch fail")
                self.label_print_result_add_branch.setText('Add branch is done')
                self.lineEdit_add_branch_name.setText("")
                self.lineEdit_add_branch_targetyear.setText("")
                self.lineEdit_add_branch_price.setText("")

    def cancel_add_branch(self):
        self.lineEdit_add_branch_name.setText("")
        self.lineEdit_add_branch_targetyear.setText("")
        self.lineEdit_add_branch_price.setText("")
        self.label_print_result_add_branch.setText("Cancel add branch")


    def add_branch_func(self):
        self.stackedWidget_6.setCurrentIndex(1)
        # change label_print_result_add_branch to ""
        self.label_print_result_add_branch.setText("")
        # clear lineEdit_add_branch
        self.lineEdit_add_branch_name.setText("")
        self.lineEdit_add_branch_targetyear.setText("")
        self.lineEdit_add_branch_price.setText("")
        # add branch to mongodb
        self.btn_confirm_add_branch.clicked.connect(self.add_branch_to_mongodb)
        self.btn_cancel_add_branch.clicked.connect(self.cancel_add_branch)
        


###### Remove Branch ######
    def view_branches_update_table_2(self):
        import read_table_func
        df3 = read_table_func.read_branch_table()
        self.view_branch_table_2.setRowCount(len(df3))
        self.view_branch_table_2.setColumnCount(len(df3.columns))

        for i in range(len(df3)):
                for j in range(len(df3.columns)):
                        self.view_branch_table_2.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        self.view_branch_table_2.setHorizontalHeaderLabels(df3.columns)
        self.view_branch_table_2.resizeColumnsToContents()
        self.view_branch_table_2.resizeRowsToContents()  
        self.view_branch_table_2.setSortingEnabled(True)

    def view_remove_branch_table_func(self):
        self.stackedWidget_7.setCurrentIndex(1)
        self.view_branch_table_2.clear()
        self.view_branches_update_table_2()
        # set label_17 to ""
        self.label_17.setText("Please select rows to remove data")
        # set label_print_result_branch_remove to ""
        self.label_print_result_branch_remove.setText("")
        # create new column 0 and insert CheckBoxes all rows in stackedWidget_7
        self.view_branch_table_2.insertColumn(0)
        self.view_branch_table_2.setHorizontalHeaderItem(0, QTableWidgetItem("Select"))
        for i in range(self.view_branch_table_2.rowCount()):
                self.view_branch_table_2.setCellWidget(i, 0, QCheckBox())
        # set column width
        self.view_branch_table_2.setColumnWidth(0, 50)
        # set center alignment of column 0
        self.view_branch_table_2.item(0, 0).setTextAlignment(Qt.AlignCenter)

# remove selected rows in table and remove data in mongodb
    def remove_branch_func(self):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.branches
        # # get selected rows
        # selected_rows = self.view_branch_table_2.selectionModel().selectedRows()
        # # get data in selected rows
        # for index in sorted(selected_rows):
        #         # get data in selected rows
        #         data = self.view_branch_table_2.item(index.row(), 0).text()
        #         collection.delete_many({"branch_name": data})
        #         #update table
        #         self.view_branches_update_table_2()

        # get selected QCheckBoxes rows and remove data in mongodb use branch_name field
        # get row count
        row_count = self.view_branch_table_2.rowCount()
        # get column count
        column_count = self.view_branch_table_2.columnCount()
        # get data in QCheckBoxes
        for i in range(row_count):
                for j in range(column_count):
                        if self.view_branch_table_2.cellWidget(i, j) is not None:
                                if self.view_branch_table_2.cellWidget(i, j).isChecked():
                                        data = self.view_branch_table_2.item(i, 1).text()
                                        collection.delete_many({"branch_name": data})

        # update table
        self.view_branches_update_table_2()
        self.label_print_result_branch_remove.setText("Remove branch is done")

    def cancel_remove_branch_func(self):
        self.label_print_result_branch_remove.setText("Cancel remove branch")


###### Edit Branch ######
    def view_branches_update_table_3(self):
        import read_table_func
        df3 = read_table_func.read_branch_table2()
        self.view_branch_table_3.setRowCount(len(df3))
        self.view_branch_table_3.setColumnCount(len(df3.columns))

        for i in range(len(df3)):
                for j in range(len(df3.columns)):
                        self.view_branch_table_3.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        self.view_branch_table_3.setHorizontalHeaderLabels(df3.columns)
        self.view_branch_table_3.resizeColumnsToContents()
        self.view_branch_table_3.resizeRowsToContents()  
        self.view_branch_table_3.setSortingEnabled(True)
        # hide column 0
        self.view_branch_table_3.setColumnHidden(0, True)

    def view_edit_branch_table_func(self):
        self.stackedWidget_7.setCurrentIndex(2)
        self.view_branch_table_3.clear()
        self.view_branches_update_table_3()
        # set label_17 to ""
        self.label_18.setText("Please select rows to edit data")
        # set label_print_result_branch_remove to ""
        self.label_print_result_branch_edit.setText("")
        # set lineEdit_edit_branch to ""
        # create new column 0 and insert CheckBoxes all rows
        self.view_branch_table_3.insertColumn(0)
        self.view_branch_table_3.setHorizontalHeaderItem(0, QTableWidgetItem("Select"))
        for i in range(self.view_branch_table_3.rowCount()):
                self.view_branch_table_3.setCellWidget(i, 0, QCheckBox())
        # set column width
        self.view_branch_table_3.setColumnWidth(0, 50)
        # set center alignment of column 0
        self.view_branch_table_3.item(0, 0).setTextAlignment(Qt.AlignCenter)

# edit selected rows in table and replace this data in mongodb
    def edit_branch_func(self):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.branches
        # # get selected rows
        # selected_rows = self.view_branch_table_3.selectionModel().selectedRows()
        # # get data in selected rows
        # for index in sorted(selected_rows):
        #         # get data in selected rows
        #         id_field = self.view_branch_table_3.item(index.row(), 0).text()
        #         # get data from selected rows in view_branch_table_3
        #         branch_name = self.view_branch_table_3.item(index.row(), 1).text()
        #         yearly_target = int(self.view_branch_table_3.item(index.row(), 2).text())
        #         # update data in mongodb use _id field
        #         collection.update_one({"_id": ObjectId(id_field)}, {"$set": {"branch_name": branch_name, "yearly_target": yearly_target}})
        #         print('_id', id_field)
        
        # get selected QCheckBoxes rows and update data in mongodb
        # get row count
        row_count = self.view_branch_table_3.rowCount()
        # get column count
        column_count = self.view_branch_table_3.columnCount()
        # get data in QCheckBoxes
        for i in range(row_count):
                for j in range(column_count):
                        if self.view_branch_table_3.cellWidget(i, j) is not None:
                                if self.view_branch_table_3.cellWidget(i, j).isChecked():
                                        id_field = self.view_branch_table_3.item(i, 1).text()
                                        # get data from selected rows in view_branch_table_3
                                        branch_name = self.view_branch_table_3.item(i, 2).text()
                                        target_year = int(self.view_branch_table_3.item(i, 3).text())
                                        target_thb = int(self.view_branch_table_3.item(i, 3).text())
                                        # update data in mongodb use _id field
                                        collection.update_one({"_id": ObjectId(id_field)}, {"$set": {"branch_name": branch_name, "target_year": target_year, "target_thb": target_thb}})
                                        print('_id', id_field)

        
        self.label_print_result_branch_edit.setText("Edit branch is done")


    def cancel_edit_branch_func(self):
        self.label_print_result_branch_edit.setText("Cancel edit branch")


###############################################
###### Update Bakery Function ######
###### Add Bakery ######
    def add_bakery_to_mongodb(self):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.bakery
        # get data from lineEdit_add_bakery
        bakery_name = self.lineEdit_add_bak_name.text()
        bakery_category = self.comboBox_add_bak_cate.currentText()
        bakery_price = int(self.lineEdit_add_bak_price.text())

        # max_bakery_id
        # from read_table_func import *
        df_bakery = read_bakery_table()
        max_bakery_id = df_bakery[df_bakery.bakery_category == bakery_category].id_bakery.max()
        id_bakery = int(max_bakery_id +1)

        # add data to mongodb
        # collection.insert_one({"id_bakery": id_bakery,"bakery_name": bakery_name,"bakery_category": bakery_category,"unit_price": bakery_price})
        # self.label_print_result_add.setText("Add bakery is done")
        try:
                collection.insert_one({"id_bakery": id_bakery,"bakery_name": bakery_name,"bakery_category": bakery_category,"unit_price": bakery_price})
                self.label_print_result_add.setText("Add bakery is done")
                self.lineEdit_add_bak_name.setText("")
                self.comboBox_add_bak_cate.setCurrentIndex(0)
                self.lineEdit_add_bak_price.setText("")

        except:
                self.label_print_result_add.setText("Add bakery is fail")
                self.lineEdit_add_bak_name.setText("")
                self.comboBox_add_bak_cate.setCurrentIndex(0)
                self.lineEdit_add_bak_price.setText("")


    def cancel_add_bakery(self):
        self.lineEdit_add_bak_name.setText("")
        self.comboBox_add_bak_cate.setCurrentIndex(0)
        self.lineEdit_add_bak_price.setText("")
        self.label_print_result_add.setText("Cancel add bakery")

    def add_bakery_func(self):
        self.stackedWidget_5.setCurrentIndex(0)
        self.label_print_result_add.setText("")
        self.lineEdit_add_bak_name.setText("")
        self.lineEdit_add_bak_price.setText("")
        self.comboBox_add_bak_cate.setCurrentIndex(0)

        # add bakery to mongodb
        self.btn_confirm_add_bak.clicked.connect(self.add_bakery_to_mongodb)
        # cancel add bakery
        self.btn_cancel_add_bak.clicked.connect(self.cancel_add_bakery)

###### Remove Bakery #####
    def view_bakery_update_table_2(self):
        import read_table_func
        df3 = read_table_func.read_bakery_table()
        self.view_bak_table2.setRowCount(len(df3)+1)
        self.view_bak_table2.setColumnCount(len(df3.columns))

        for i in range(len(df3)):
                for j in range(len(df3.columns)):
                        self.view_bak_table2.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        self.view_bak_table2.setHorizontalHeaderLabels(df3.columns)
        self.view_bak_table2.resizeColumnsToContents()
        self.view_bak_table2.resizeRowsToContents()  
        self.view_bak_table2.setSortingEnabled(True)


    def view_remove_bakery_table_func(self):
        self.stackedWidget_5.setCurrentIndex(1)
        # clear table in stackedWidget_5
        self.view_bak_table2.clear() ##############
        self.view_bakery_update_table_2()
        # set label_17 to ""
        self.label_13.setText("Please select rows to remove data")
        # set label_print_result_bakery_remove to ""
        self.label_print_result_bak_remove.setText("")
        # create new column 0 and insert CheckBoxes all rows in stackedWidget_5 ##############
        self.view_bak_table2.insertColumn(0)
        for i in range(self.view_bak_table2.rowCount()):
                self.view_bak_table2.setCellWidget(i, 0, QCheckBox())
        # set header of column 0
        self.view_bak_table2.setHorizontalHeaderItem(0, QTableWidgetItem("Select"))
        # set width of column 0
        self.view_bak_table2.setColumnWidth(0, 50)
        # set center alignment of column 0
        self.view_bak_table2.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)


    def remove_bakery_func(self):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.bakery
        # # get selected rows
        # selected_rows = self.view_bak_table2.selectionModel().selectedRows()
        # # get data in selected rows and remove data in mongodb use id_bakery field
        # for index in sorted(selected_rows):
        #         id_bakery = int(self.view_bak_table2.item(index.row(), 0).text())
        #         collection.delete_one({"id_bakery": id_bakery})
        #         print('data', id_bakery)

        # get selected QCheckBoxes rows and remove data in mongodb use id_bakery field
        # get row count
        row_count = self.view_bak_table2.rowCount() 
        # get column count
        column_count = self.view_bak_table2.columnCount()
        # get selected rows
        selected_rows = self.view_bak_table2.selectionModel().selectedRows()
        # get selected QCheckBoxes rows
        for i in range(row_count):
                for j in range(column_count):
                        if self.view_bak_table2.cellWidget(i, 0) is not None:
                                if self.view_bak_table2.cellWidget(i, 0).isChecked():
                                        id_bakery = int(self.view_bak_table2.item(i, 1).text())
                                        collection.delete_one({"id_bakery": id_bakery})


        self.label_print_result_bak_remove.setText("Remove bakery is done")
        self.view_bakery_update_table_2()

    def cancel_remove_bakery_func(self):
        self.label_print_result_bak_remove.setText("Cancel remove bakery")

###### Edit Bakery ######
    def view_bakery_update_table_3(self):
        import read_table_func
        df3 = read_table_func.read_bakery_table2()
        self.view_bak_table3.setRowCount(len(df3)+1)
        self.view_bak_table3.setColumnCount(len(df3.columns))

        for i in range(len(df3)):
                for j in range(len(df3.columns)):
                        self.view_bak_table3.setItem(i, j, QTableWidgetItem(str(df3.iloc[i, j])))
        self.view_bak_table3.setHorizontalHeaderLabels(df3.columns)
        self.view_bak_table3.resizeColumnsToContents()
        self.view_bak_table3.resizeRowsToContents()  
        self.view_bak_table3.setSortingEnabled(True)
        # hide id_bakery column
        self.view_bak_table3.setColumnHidden(0, True)

    def view_edit_bakery_table_func(self):
        self.stackedWidget_5.setCurrentIndex(2)
        # clear table in stackedWidget_5
        self.view_bak_table3.clear() ##############
        self.view_bakery_update_table_3()
        # set label_17 to ""
        self.label_15.setText("Please select rows to edit data")
        # set label_print_result_bakery_edit to ""
        self.label_print_result_bak_edit.setText("")
        # create new column 0 and insert CheckBoxes all rows
        self.view_bak_table3.insertColumn(0)
        for i in range(self.view_bak_table3.rowCount()):
                self.view_bak_table3.setCellWidget(i, 0, QCheckBox())
        # set header of column 0
        self.view_bak_table3.setHorizontalHeaderItem(0, QTableWidgetItem("Select"))
        # set width of column 0
        self.view_bak_table3.setColumnWidth(0, 50)
        # set center alignment of column 0
        self.view_bak_table3.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)

# edit selected rows in table and replace this data in mongodb
    def edit_bakery_func(self):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.bakery

        # # get selected rows
        # selected_rows = self.view_bak_table3.selectionModel().selectedRows()
        # # get data in selected rows
        # for index in sorted(selected_rows):
        #         # get data in selected rows
        #         data = self.view_bak_table3.item(index.row(), 0).text()
        #         # get data from lineEdit_edit_bakery
        #         id_field = self.view_bak_table3.item(index.row(), 0).text()
        #         id_bakery = int(self.view_bak_table3.item(index.row(), 1).text())
        #         bakery_name = self.view_bak_table3.item(index.row(), 2).text()
        #         bakery_category = self.view_bak_table3.item(index.row(), 3).text()
        #         bakery_price = self.view_bak_table3.item(index.row(), 4).text()

        #         # edit data in mongodb use _id field
        #         collection.update_one({"_id": ObjectId(id_field)}, {"$set": {"id_bakery": id_bakery, "bakery_name": bakery_name,"bakery_category": bakery_category,"unit_price": bakery_price}})
        #         print('_id', id_field)

        # get selected QCheckBoxes rows and update data in mongodb
        # get row count
        row_count = self.view_bak_table3.rowCount()
        # get column count
        column_count = self.view_bak_table3.columnCount()
        # get selected rows
        selected_rows = self.view_bak_table3.selectionModel().selectedRows()
        # get selected QCheckBoxes rows
        for i in range(row_count):
                for j in range(column_count):
                        if self.view_bak_table3.cellWidget(i, 0) is not None:
                                if self.view_bak_table3.cellWidget(i, 0).isChecked():
                                        # get data in selected rows
                                        id_field = self.view_bak_table3.item(i, 1).text()
                                        id_bakery = int(self.view_bak_table3.item(i, 2).text())
                                        bakery_name = self.view_bak_table3.item(i, 3).text()
                                        bakery_category = self.view_bak_table3.item(i, 4).text()
                                        bakery_price = self.view_bak_table3.item(i, 5).text()
                                        # edit data in mongodb use _id field
                                        collection.update_one({"_id": ObjectId(id_field)}, {"$set": {"id_bakery": id_bakery, "bakery_name": bakery_name,"bakery_category": bakery_category,"unit_price": bakery_price}})
                                        print('_id', id_field)


        self.label_print_result_bak_edit.setText("Edit bakery is done")

    def cancel_edit_bakery_func(self):
        self.label_print_result_bak_edit.setText("Cancel edit bakery")



###### Update Transaction ######    
    def browse_transaction_func(self):
        global df_browse2
        import browse_file_func2
        df_browse = browse_file_func2.browse_csv2(self)
        df_browse2 = df_browse
        # show df_brows in update_trans_table
        self.update_trans_table.setRowCount(len(df_browse))
        self.update_trans_table.setColumnCount(len(df_browse.columns))

        for i in range(len(df_browse)):
                for j in range(len(df_browse.columns)):
                        self.update_trans_table.setItem(i, j, QTableWidgetItem(str(df_browse.iloc[i, j])))
        self.update_trans_table.setHorizontalHeaderLabels(df_browse.columns)
        self.update_trans_table.resizeColumnsToContents()
        self.update_trans_table.resizeRowsToContents()
        self.update_trans_table.setSortingEnabled(True)

        self.add_trans_btn.clicked.connect(self.add_transaction_func)
        self.add_trans_btn.clicked.connect(lambda: print("click: add_trans_btn"))
        self.clear_trans_btn.clicked.connect(self.clear_transaction_func)
        self.clear_trans_btn.clicked.connect(lambda: print("click: clear_trans_btn"))
        # return df_browse to global variable
        # return df_browse
        
    def add_transaction_func(self):
        global df_browse2
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.bakery_house
        collection = db.sales
        # df_browse = self.browse_transaction_func()
        json_data = json.loads(df_browse2.to_json(orient='records'))
        collection.insert_many(json_data)
        self.update_trans_table.clear()
        self.print_result_add_trans.setText("Add transaction is done")
        df_browse2 = pd.DataFrame()

    def clear_transaction_func(self):
        global df_browse2
        self.update_trans_table.clear()
        self.print_result_add_trans.setText("Clear")
        df_browse2 = pd.DataFrame()

                

















###############################################
###### Dash board ######
#     def plot_chart(self):
#         import read_table_func
#         # if comboBox_select_chart == 'Sales' plot sales chart
#         if self.comboBox_select_chart.currentText() == 'Sales':
#                 df = read_table_func.df_month_branch_sales_func()

#                 # select year based on comboBox_select_year
#                 if self.comboBox_select_year.currentText() == '2021':
#                         yearr = 2021
#                         df = df[df['year'] == yearr]      
#                 elif self.comboBox_select_year.currentText() == '2022':
#                         yearr = 2022
#                         df = df[df['year'] == yearr]
                
#                 # filter data by branch
#                 if self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
#                         df = df[df['branch'].isin(['Central World', 'Central Rama 9', 'Central Ladprao'])]
#                 elif self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked():
#                         df = df[df['branch'].isin(['Central World', 'Central Rama 9'])]
#                 elif self.cen_world_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
#                         df = df[df['branch'].isin(['Central World', 'Central Ladprao'])]
#                 elif self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
#                         df = df[df['branch'].isin(['Central Rama 9', 'Central Ladprao'])]
#                 elif self.cen_world_btn_2.isChecked():
#                         df = df[df['branch'] == 'Central World']
#                 elif self.cen_rama9_btn_2.isChecked():
#                         df = df[df['branch'] == 'Central Rama 9']
#                 elif self.cen_lad_btn_2.isChecked():
#                         df = df[df['branch'] == 'Central Ladprao']
                
#                 # plot chart
#                 fig = go.Figure()
#                 fig = px.bar(df, x='month', y='sales', color='branch', barmode='stack',title=f'{yearr} Sales')

#                 fig.update_traces(texttemplate='%{y:.3s}', textposition='inside')
#                 fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')

#                 # change all bg color
#                 fig.update_layout(plot_bgcolor='rgb(39, 44, 54)')
#                 # change outer bg color
#                 fig.update_layout(paper_bgcolor='rgb(39, 44, 54)')

#                 # update all font size
#                 fig.update_layout(font_size=30)
#                 # update xaxis font size
#                 fig.update_xaxes(title_font_size=30)
#                 # update yaxis font size
#                 fig.update_yaxes(title_font_size=30)

#                 # move legend to bottom
#                 fig.update_layout(legend=dict(
#                         orientation="h",
#                         yanchor="bottom",
#                         y=1.02,
#                         xanchor="right",
#                         x=1
#                 ))

#                 # hide legend title
#                 fig.update_layout(showlegend=True)
#                 fig.update_layout(legend_title_text='')


#                 # fig.show()

#                 # convert fig to image and show in label_graph 
#                 # fig.write_image("graph.png")
#                 # pixmap = QPixmap("graph.png")
#                 # self.label_graph.setPixmap(pixmap)
#                 # self.label_graph.setScaledContents(True)
#                 # self.label_graph.setAlignment(QtCore.Qt.AlignCenter)
#                 # self.label_graph.show()

#         elif self.comboBox_select_chart.currentText() == 'Branch Target Achievement':
#                 df_sales = read_table_func.df_month_branch_sales_func()
#                 df_sales = df.groupby(['year', 'branch']).sum().reset_index()
#                 df_target = read_table_func.read_branch_table()
#                 df_target.rename(columns={'branch_name':'branch', 'target_year':'year'}, inplace=True)
#                 df_merge = pd.merge(df_sales, df_target, on=['year', 'branch'])

#                 # select year based on comboBox_select_year
#                 if self.comboBox_select_year.currentText() == '2021':
#                         yearr = 2021
#                         df_merge = df_merge[df_merge['year'] == yearr]
#                 elif self.comboBox_select_year.currentText() == '2022':
#                         yearr = 2022
#                         df_merge = df_merge[df_merge['year'] == yearr]

#                 # filter data by branch
#                 if self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'].isin(['Central World', 'Central Rama 9', 'Central Ladprao'])]
#                 elif self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'].isin(['Central World', 'Central Rama 9'])]
#                 elif self.cen_world_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'].isin(['Central World', 'Central Ladprao'])]
#                 elif self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'].isin(['Central Rama 9', 'Central Ladprao'])]
#                 elif self.cen_world_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'] == 'Central World']
#                 elif self.cen_rama9_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'] == 'Central Rama 9']
#                 elif self.cen_lad_btn_2.isChecked():
#                         df_merge = df_merge[df_merge['branch'] == 'Central Ladprao']

#                 # plot chart
#                 fig = go.Figure()
#                 fig = px.bar(df_filter, x='branch', y='sales', color='branch', title='Branch Target Achievement')
#                 fig.update_traces(texttemplate='Sales: %{y:.3s}', textposition='inside')
#                 fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')

#                 # add scatter marker mode
#                 fig.add_trace(go.Scatter(x=df_filter.branch, y=df_filter.target_thb, 
#                 mode='markers', marker=dict(color='red', size=10), name='Target'))

#                 # annotation target_thb each branch from df_filter
#                 for i in range(len(df_filter)):
#                         fig.add_annotation(x=df_filter.branch[i], y=df_filter.target_thb[i],
#                         text=f"Target: {df_filter.target_thb[i]/1000000:,.2f} M",
#                         showarrow=True, arrowhead=1, ax=0, ay=10, font=dict(size=15))

#                 # move legend 
#                 fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1))

#                 # hide legend title
#                 fig.update_layout(showlegend=True)
#                 fig.update_layout(legend_title_text='')

#                 # change all bg color
#                 fig.update_layout(plot_bgcolor='rgb(39, 44, 54)')
#                 # change outer bg color
#                 fig.update_layout(paper_bgcolor='rgb(39, 44, 54)')

#                 # update all font size
#                 fig.update_layout(font_size=30)
#                 # update xaxis font size
#                 fig.update_xaxes(title_font_size=30)
#                 # update yaxis font size
#                 fig.update_yaxes(title_font_size=30)

#                 # fig.show()

#         # convert fig to image and show in label_graph
#         fig.write_image("graph.png", width=1600, height=1200)
#         pixmap = QPixmap("graph.png")
#         self.label_graph.setPixmap(pixmap)
#         self.label_graph.setScaledContents(True)
#         self.label_graph.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_graph.show()

###### Dash board2 ######

    def plot_chart(self):
        if self.comboBox_select_chart.currentText() == 'Sales':
                self.plot_sales_chart()
        elif self.comboBox_select_chart.currentText() == 'Branch Target Achievement':
                self.plot__target_chart()


    def plot_sales_chart(self):
        import read_table_func
        df = read_table_func.df_month_branch_sales_func()

        # select year based on comboBox_select_year
        if self.comboBox_select_year.currentText() == '2021':
                yearr = 2021
                df = df[df['year'] == yearr]      
        elif self.comboBox_select_year.currentText() == '2022':
                yearr = 2022
                df = df[df['year'] == yearr]
                
        # filter data by branch
        if self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
                df = df[df['branch'].isin(['Central World', 'Central Rama 9', 'Central Ladprao'])]
        elif self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked():
                df = df[df['branch'].isin(['Central World', 'Central Rama 9'])]
        elif self.cen_world_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
                df = df[df['branch'].isin(['Central World', 'Central Ladprao'])]
        elif self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
                df = df[df['branch'].isin(['Central Rama 9', 'Central Ladprao'])]
        elif self.cen_world_btn_2.isChecked():
                df = df[df['branch'] == 'Central World']
        elif self.cen_rama9_btn_2.isChecked():
                df = df[df['branch'] == 'Central Rama 9']
        elif self.cen_lad_btn_2.isChecked():
                df = df[df['branch'] == 'Central Ladprao']
                
        # plot chart
        fig = go.Figure()
        fig = px.bar(df, x='month', y='sales', color='branch', barmode='stack',title=f'{yearr} Sales')

        fig.update_traces(texttemplate='%{y:.3s}', textposition='inside')
        fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')

        # change all bg color
        fig.update_layout(plot_bgcolor='rgb(39, 44, 54)')
        # change outer bg color
        fig.update_layout(paper_bgcolor='rgb(39, 44, 54)')

        # update all font size
        fig.update_layout(font_size=30)
        # update xaxis font size
        fig.update_xaxes(title_font_size=30)
        # update yaxis font size
        fig.update_yaxes(title_font_size=30)

        # move legend to bottom
        fig.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.25,
                xanchor="right",
                x=1
        ))

        # hide legend title
        fig.update_layout(showlegend=True)
        fig.update_layout(legend_title_text='')


                # fig.show()

        # convert fig to image and show in label_graph 
        fig.write_image("graph.png", width=1600, height=1200)
        pixmap = QPixmap("graph.png")
        self.label_graph.setPixmap(pixmap)
        self.label_graph.setScaledContents(True)
        self.label_graph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph.show()


    def plot__target_chart(self):
        import read_table_func
        df_sales = read_table_func.df_month_branch_sales_func()
        df_sales = df_sales.groupby(['year', 'branch']).sum().reset_index()
        df_target = read_table_func.read_branch_table()
        df_target.rename(columns={'branch_name':'branch', 'target_year':'year'}, inplace=True)
        df_merge = pd.merge(df_sales, df_target, on=['year', 'branch'])

        # select year based on comboBox_select_year
        if self.comboBox_select_year.currentText() == '2021':
                yearr = 2021
                df_merge = df_merge[df_merge['year'] == yearr]
        elif self.comboBox_select_year.currentText() == '2022':
                yearr = 2022
                df_merge = df_merge[df_merge['year'] == yearr]

        # filter data by branch
        if self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'].isin(['Central World', 'Central Rama 9', 'Central Ladprao'])]
        elif self.cen_world_btn_2.isChecked() and self.cen_rama9_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'].isin(['Central World', 'Central Rama 9'])]
        elif self.cen_world_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'].isin(['Central World', 'Central Ladprao'])]
        elif self.cen_rama9_btn_2.isChecked() and self.cen_lad_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'].isin(['Central Rama 9', 'Central Ladprao'])]
        elif self.cen_world_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'] == 'Central World']
        elif self.cen_rama9_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'] == 'Central Rama 9']
        elif self.cen_lad_btn_2.isChecked():
                df_merge = df_merge[df_merge['branch'] == 'Central Ladprao']
        
        df_merge = df_merge.reset_index(drop=True)

        # plot chart
        fig = go.Figure()
        fig = px.bar(df_merge, x='branch', y='sales', color='branch', title=f'{yearr}Branch Target Achievement')
        fig.update_traces(texttemplate='Sales: %{y:.3s}', textposition='inside')
        fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')

        # add scatter marker mode
        fig.add_trace(go.Scatter(x=df_merge.branch, y=df_merge.target_thb, 
        mode='markers', marker=dict(color='red', size=20), name='Target'))

        # annotation target_thb each branch from df_filter
        for i in range(len(df_merge)):
                fig.add_annotation(x=df_merge.branch[i], y=df_merge.target_thb[i],
                text=f"Target: {df_merge.target_thb[i]/1000000:,.2f} M",
                showarrow=True, arrowhead=1, ax=0, ay=10, font=dict(size=30))

        # move legend 
        fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=-0.15,xanchor="right",x=1))

        # hide legend title
        fig.update_layout(showlegend=True)
        fig.update_layout(legend_title_text='')

        # change all bg color
        fig.update_layout(plot_bgcolor='rgb(39, 44, 54)')
        # change outer bg color
        fig.update_layout(paper_bgcolor='rgb(39, 44, 54)')

        # update all font size
        fig.update_layout(font_size=30)
        # update xaxis font size
        fig.update_xaxes(title_font_size=30)
        # update yaxis font size
        fig.update_yaxes(title_font_size=30)

        # fig.show()

        # convert fig to image and show in label_graph
        fig.write_image("graph.png", width=1600, height=1200)
        pixmap = QPixmap("graph.png")
        self.label_graph.setPixmap(pixmap)
        self.label_graph.setScaledContents(True)
        self.label_graph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph.show()













###############################  

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_5.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u" Bakery House", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"Data Management", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"BH", None))
        self.label.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Select Chart:", None))
        self.comboBox_select_chart.setItemText(0, QCoreApplication.translate("MainWindow", u"Sales", None))
        self.comboBox_select_chart.setItemText(1, QCoreApplication.translate("MainWindow", u"Branch Target Achievement", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"             Years: ", None))
        self.comboBox_select_year.setItemText(0, QCoreApplication.translate("MainWindow", u"2021", None))
        self.comboBox_select_year.setItemText(1, QCoreApplication.translate("MainWindow", u"2022", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Branches: ", None))
        self.cen_world_btn_2.setText(QCoreApplication.translate("MainWindow", u"Central World", None))
        self.cen_lad_btn_2.setText(QCoreApplication.translate("MainWindow", u"Central Ladprao", None))
        self.cen_rama9_btn_2.setText(QCoreApplication.translate("MainWindow", u"Central Rama 9", None))
        self.submit_view_btn_2.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_graph.setText("")
        self.Transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.Bakery_btn.setText(QCoreApplication.translate("MainWindow", u"Bakery", None))
        self.Branches_btn.setText(QCoreApplication.translate("MainWindow", u"Branches", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start Date: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"     End Date: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Branches: ", None))
        self.cen_world_btn.setText(QCoreApplication.translate("MainWindow", u"Central World", None))
        self.cen_lad_btn.setText(QCoreApplication.translate("MainWindow", u"Central Ladprao", None))
        self.cen_rama9_btn.setText(QCoreApplication.translate("MainWindow", u"Central Rama 9", None))
        self.submit_view_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        ___qtablewidgetitem = self.table_bakery.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"row", None));
        ___qtablewidgetitem1 = self.table_bakery.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"id_bakery", None));
        ___qtablewidgetitem2 = self.table_bakery.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.table_bakery.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"bakery_category", None));
        ___qtablewidgetitem4 = self.table_bakery.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"unit_price", None));
        ___qtablewidgetitem5 = self.table_branches.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"row", None));
        ___qtablewidgetitem6 = self.table_branches.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"branch_name", None));
        ___qtablewidgetitem7 = self.table_branches.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"yearly_target", None));
        self.Transaction_btn_2.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.Bakery_btn_2.setText(QCoreApplication.translate("MainWindow", u"Bakery", None))
        self.Branches_btn_2.setText(QCoreApplication.translate("MainWindow", u"Branches", None))
        self.print_result_add_trans.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.browse_trans_btn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.add_trans_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.clear_trans_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Do you want to remove data?", None))
        self.btn_remove_bak_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_remove_bak_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_print_result_bak_remove.setText(QCoreApplication.translate("MainWindow", u"\"Print Result (remove)\"", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Do you want to edit data?", None))
        self.btn_edit_bak_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_edit_bak_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_print_result_bak_edit.setText(QCoreApplication.translate("MainWindow", u"\"Print Result (Edit)\"", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Add Data - Bakery Database", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bakery Name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Bakary Category:", None))
        self.comboBox_add_bak_cate.setItemText(0, QCoreApplication.translate("MainWindow", u"Bread & Bun", None))
        self.comboBox_add_bak_cate.setItemText(1, QCoreApplication.translate("MainWindow", u"French Bread", None))
        self.comboBox_add_bak_cate.setItemText(2, QCoreApplication.translate("MainWindow", u"Pie & Croissant", None))
        self.comboBox_add_bak_cate.setItemText(3, QCoreApplication.translate("MainWindow", u"Sandwich", None))
        self.comboBox_add_bak_cate.setItemText(4, QCoreApplication.translate("MainWindow", u"Japanese Bakery", None))
        self.comboBox_add_bak_cate.setItemText(5, QCoreApplication.translate("MainWindow", u"Waffle & Muffin", None))
        self.comboBox_add_bak_cate.setItemText(6, QCoreApplication.translate("MainWindow", u"Doughnut", None))
        self.comboBox_add_bak_cate.setItemText(7, QCoreApplication.translate("MainWindow", u"Sweet Bun", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.btn_cancel_add_bak.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_confirm_add_bak.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_print_result_add.setText(QCoreApplication.translate("MainWindow", u"\" Print Result \"", None))
        self.add_bak_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_bak_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.edit_bak_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.refresh_bak_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Do you want to remove data?", None))
        self.btn_remove_branch_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_remove_branch_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_print_result_branch_remove.setText(QCoreApplication.translate("MainWindow", u"\"Print Result (remove)\"", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Do you want to edit data?", None))
        self.btn_edit_branch_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_edit_branch_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_print_result_branch_edit.setText(QCoreApplication.translate("MainWindow", u"\"Print Result (Edit)\"", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Add Data - branches Database", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Branch Name:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Target Year (A.D.):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Target (THB):", None))
        self.btn_cancel_add_branch.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_confirm_add_branch.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_print_result_add_branch.setText(QCoreApplication.translate("MainWindow", u"\" Print Result \"", None))
        self.add_branch_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_branch_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.edit_branch_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.refresh_branch_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Created by: Sorawit Sinlapanurak", None))
        self.label_version.setText("")
    # retranslateUi

