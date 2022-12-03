# def browse_csv():
#     import pandas as pd
#     import sys
#     from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
#     # from GUI_BASE4 import *

#     app = QApplication(sys.argv)
#     widget = QWidget()

#     # open file dialog
#     fname = QFileDialog.getOpenFileName(widget, 'Open file', 'c:\\', "CSV files (*.csv)")

#     # read csv file to dataframe
#     df_browse = pd.read_csv(fname[0])
#     return df_browse
    
    # show dataframe in update_trans_table widget

def browse_csv(self):
    import pandas as pd
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
    # from GUI_BASE4 import *

    app = QApplication(sys.argv)
    widget = QWidget()

    # open file dialog
    fname = QFileDialog.getOpenFileName(widget, 'Open file', 'c:\\', "CSV files (*.csv)")

    # read csv file to dataframe
    # df_browse = pd.read_csv(fname[0])
    # return df_browse

    # read location of csv file
    self.csv_file = fname[0]
    print(self.csv_file)
    # dont turn off the window
    self.show()






    


