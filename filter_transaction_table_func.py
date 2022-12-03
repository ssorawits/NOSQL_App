# def read_transactions_table() and filter data
def filter_transaction_data(self):
    import read_table_func
    import GUI_BASE2_3
    import pandas as pd

    df = read_table_func.read_transactions_table()

    # convert start_date_btn and end_date_btn to date
    start_date = GUI_BASE2_3.start_date_btn.date().toPyDate()
    start_date = pd.to_datetime(start_date)
    end_date = GUI_BASE2_3.end_date_btn.date().toPyDate()
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

    self.table_transaction.setRowCount(len(df))
    self.table_transaction.setColumnCount(len(df.columns))

    for i in range(len(df)):
        for j in range(len(df.columns)):
            self.table_transaction.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(df.iloc[i, j])))
    self.table_transaction.setHorizontalHeaderLabels(df.columns)



