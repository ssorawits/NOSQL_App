#browse_csv() file using Pysiide2
def browse_csv2():
    import sys
    from PySide2.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
    import pandas as pd

    app = QApplication(sys.argv)
    widget = QWidget()

    # open file dialog
    fname = QFileDialog.getOpenFileName(widget, 'Open file', 'c:\\', "CSV files (*.csv)")

    # get file name
    df_browse2 = pd.read_csv(fname[0])

    return df_browse2