import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *
from browse_file_func import *
from browse_file_func2 import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        ########################################################################
        # START - WINDOW ATTRIBUTES
        ########################################################################

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        # SET ==> WINDOW TITLE
        self.setWindowTitle('Bakery House Data Magement')
        UIFunctions.labelTitle(self, 'Bakery House')
        UIFunctions.labelDescription(self, 'Data Magement')
        ## ==> END ##

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        # ==> CREATE MENUS
        ########################################################################

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        # PAGES
        ########################################################################

        ### Update Branch Page ###
        # 1) Brach Botton - update branch
        self.ui.Branches_btn_2.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_update_branch_table))
        # 2) Add Button - update branch
        self.ui.add_branch_btn.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_update_branch_add))
        # 3) Remove Button - update branch
        self.ui.remove_branch_btn.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_remove_branch))
        # 4) Edit Button - update branch
        self.ui.edit_branch_btn.clicked.connect(lambda: self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_edit_branch))
        # 5) Refresh Button - update branch
        self.ui.refresh_branch_btn.clicked.connect(lambda: self.ui.stackedWidget_6.setCurrentWidget(self.ui.page_update_branch_table))

        ### Update Bakery Page ###
        # 1) Bakery Botton - update bakery
        self.ui.Bakery_btn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_update_bakery))
        self.ui.Bakery_btn_2.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_view_bak_table))
        # 2) Add Button - update bakery
        self.ui.add_bak_btn.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_update_bak_add))
        # 3) Remove Button - update bakery
        self.ui.remove_bak_btn.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_remove_bak))
        # 4) Edit Button - update bakery
        self.ui.edit_bak_btn.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_edit_bak))
        # 5) Refresh Button - update bakery
        self.ui.refresh_bak_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_update_bakery))
        self.ui.refresh_bak_btn.clicked.connect(lambda: self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_view_bak_table))

        ### brows Page ###
        # when click on browse_trans_btn call browse_csv function
        # self.ui.browse_trans_btn.clicked.connect(lambda: browse_csv(self))





        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home",
                               "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Data Visualization", "btn_dashboard",
                               "url(:/16x16/icons/16x16/cil-chart.png)", True)
        UIFunctions.addNewMenu(self, "View Data", "btn_view_data",
                               "url(:/16x16/icons/16x16/cil-view-quilt.png)", True)
        UIFunctions.addNewMenu(self, "Update Data", "btn_update_data",
                               "url(:/16x16/icons/16x16/cil-loop-circular.png)", True)
        # UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets",
        #                        "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        # USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "BH", "", True)
        ## ==> END ##


        # ==> Browse Data
        ########################################################################
        # def browse_transaction_func():
        #     df_browse = browse_csv()

        #     # return df_browse

        #     #show df_browse in update_trans_table
        #     self.ui.update_trans_table.setRowCount(len(df_browse))
        #     self.ui.update_trans_table.setColumnCount(len(df_browse.columns))

        #     for i in range(len(df_browse)):
        #         for j in range(len(df_browse.columns)):
        #             self.ui.update_trans_table.setItem(i, j, QTableWidgetItem(str(df_browse.iloc[i, j])))
        #     self.ui.update_trans_table.setHorizontalHeaderLabels(df_browse.columns)
        #     self.ui.update_trans_table.resizeColumnsToContents()
        #     self.ui.update_trans_table.resizeRowsToContents()
        #     self.ui.update_trans_table.setSortingEnabled(True)


        # self.ui.browse_trans_btn.clicked.connect(lambda: browse_csv2(self))
        # self.ui.browse_trans_btn.clicked.connect(lambda: print("click: browse_trans_btn"))





        # ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        # ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        # END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        # ==> QTableWidget RARAMETERS
        ########################################################################
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
        #     QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        

    ########################################################################
    # MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE Home
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE Dashboard
        if btnWidget.objectName() == "btn_dashboard":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
            UIFunctions.resetStyle(self, "btn_dashboard")
            UIFunctions.labelPage(self, "Data Visualization")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE View_Data
        if btnWidget.objectName() == "btn_view_data":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_view_data)
            UIFunctions.resetStyle(self, "btn_view_data")
            UIFunctions.labelPage(self, "View Data")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE Update_data
        if btnWidget.objectName() == "btn_update_data":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_update_data)
            UIFunctions.resetStyle(self, "btn_update_data")
            UIFunctions.labelPage(self, "Update Data")
            btnWidget.setStyleSheet(
                UIFunctions.selectMenu(btnWidget.styleSheet()))



    ## ==> END ##




    ########################################################################
    # START ==> APP EVENTS
    ########################################################################

    # EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    # EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    # EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) +
              ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    # EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) +
              ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    # END ==> APP EVENTS
    ############################## ---/--/--- ##############################



if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())

# if __name__ == "__main__":
    # use a new QApplication instance in the same time








