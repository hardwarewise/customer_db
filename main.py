import sys
import database
import qdarkstyle
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog
from PySide6 import QtCore, QtGui
from PySide6.QtGui import QIcon, QPixmap
from ui_mainwindow import Ui_MainWindow
from pathlib import Path
import rc_resources


class MainPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.EDIT_MODE = 0  # 0 = New record 1 = Update Record
        self.idx = 0
        self.path = ""
        self.setupUi(self)
        self.setWindowTitle("Customer Database")
        
        appIcon = QIcon(QPixmap(":/icons/database"))
        self.setWindowIcon(appIcon)
        searcIcon = QIcon(QPixmap(":/icons/search"))
        self.searchBtn.setIcon(searcIcon)
        browseIcon = QIcon(QPixmap(":/icons/browse"))
        self.browseBtn.setIcon(browseIcon)
        clearIcon = QIcon(QPixmap(":/icons/clear"))
        self.clearFilterBtn.setIcon(clearIcon)
        resetIcon = QIcon(QPixmap(":/icons/reset"))
        self.resetBtn.setIcon(resetIcon)
        saveIcon = QIcon(QPixmap(":/icons/save"))
        self.saveBtn.setIcon(saveIcon)
        deleteIcon = QIcon(QPixmap(":/icons/delete"))
        self.deleteSelectedRecordBtn.setIcon(deleteIcon)
        
        
        self.saveBtn.setDisabled(True)
        self.deleteSelectedRecordBtn.setDisabled(True)
        self.tableWidget.itemClicked.connect(lambda: self.deleteSelectedRecordBtn.setDisabled(False))
        self.customerIdLineEdit.textChanged.connect(
            lambda: self.saveBtn.setEnabled(self.customerIdLineEdit.text() != ""))
        self.saveBtn.clicked.connect(self.addCustomer)
        self.resetBtn.clicked.connect(self.clearLines)
        self.searchBtn.clicked.connect(self.searchCustomer)
        self.tableWidget.itemDoubleClicked.connect(self.takeRecord)
        self.clearFilterBtn.clicked.connect(self.listCustomers)
        self.browseBtn.clicked.connect(self.browse_photo)
        self.deleteSelectedRecordBtn.clicked.connect(self.deleteCustomer)
        self.tableWidget.selectionModel().selectionChanged.connect(
            self.onSelectionChanged)

        self.listCustomers()

    @QtCore.Slot()
    def onSelectionChanged(self):
        self.deleteSelectedRecordBtn.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
        )
    
    def browse_photo(self):
#         
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a Photo", 
            "photos/", 
            "Images (*.png *.jpg)")
        if filename:
            self.path = str(Path(filename)).replace("\\", "/")
            self.photoFrame.setStyleSheet(f"border-image: url('{self.path}');")
           
                
    def deleteCustomer(self):
        self.tableWidget.showColumn(0)
        selected_record = self.tableWidget.selectedItems()[0].text()
        database.delete_customer(database.connect(), (selected_record,))
        self.tableWidget.hideColumn(0)
        self.clearLines()
        self.listCustomers()

    def takeRecord(self):
        self.clearLines()
        self.tableWidget.showColumn(0)
        self.tableWidget.showColumn(7)
        self.current_rows = []
        for idx in self.tableWidget.selectedIndexes():
            self.current_rows.append(str(self.tableWidget.item(self.tableWidget.currentRow(), idx.column()).text()))
        self.idx = int(self.current_rows[0])
        self.customerIdLineEdit.setText(self.current_rows[1])
        self.nameLineEdit.setText(self.current_rows[2])
        self.surnameLineEdit.setText(self.current_rows[3])
        self.phoneNumberLineEdit.setText(self.current_rows[4])
        self.emailLineEdit.setText(self.current_rows[5])
        self.addressTextEdit.setText(self.current_rows[6])
        photo = self.current_rows[7]
        photo = photo.replace("\\", "/")
        self.photoFrame.setStyleSheet(f"border-image: url('{photo}');")
        self.tableWidget.hideColumn(0)
        self.tableWidget.hideColumn(7)
        self.EDIT_MODE = 1
        self.saveBtn.setText("Update")

    def searchCustomer(self):
        searchstr = self.searchLineEdit.text()
        rows = database.get_customers_by_any(connection, searchstr)
        self.tableWidget.setRowCount(len(rows))
        for rowIndex, rowData in enumerate(rows):
            for colIndex, colData in enumerate(rowData):
                self.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(colData)))

        if self.tableWidget.rowCount() > 0:
            self.searchFoundTotalLabel.setStyleSheet("color : green;")
            self.searchFoundTotalLabel.setText(f"{int(rowIndex) + 1} record found.")
        else:
            self.searchFoundTotalLabel.setStyleSheet("color : red;")
            self.searchFoundTotalLabel.setText("No record found.")
        self.tableWidget.hideColumn(0)

    def addCustomer(self):
        customerId = self.customerIdLineEdit.text()
        name = self.nameLineEdit.text()
        surname = self.surnameLineEdit.text()
        address = self.addressTextEdit.toPlainText()
        email = self.emailLineEdit.text()
        phoneNumber = self.phoneNumberLineEdit.text()
        photo_path = str(self.path)
        if self.EDIT_MODE == 0:
            database.add_customers(connection, customerId, name, surname, phoneNumber, email, address, photo_path)
        elif self.EDIT_MODE == 1:
            database.update_customer(connection, customerId, name, surname, phoneNumber, email,
             address, photo_path, self.idx)
        self.listCustomers()
        self.clearLines()

    def clearLines(self):
        self.EDIT_MODE = 0
        self.saveBtn.setText("Save")
        self.customerIdLineEdit.setText('')
        self.nameLineEdit.setText('')
        self.surnameLineEdit.setText('')
        self.addressTextEdit.setText('')
        self.emailLineEdit.setText('')
        self.phoneNumberLineEdit.setText('')
        self.photoFrame.setStyleSheet("border-image : None;")
        self.path = ""

    def listCustomers(self):
        self.searchFoundTotalLabel.setText('')
        self.searchLineEdit.setText('')
        rows = database.get_all_customers(database.connect())
        self.tableWidget.setRowCount(len(rows))
        for rowIndex, rowData in enumerate(rows):
            for colIndex, colData in enumerate(rowData):
                self.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(colData)))
        self.tableWidget.hideColumn(0)
        self.tableWidget.hideColumn(7)


if __name__ == '__main__':
    connection = database.connect()
    database.create_tables(connection)
    app = QApplication(sys.argv)
    window = MainPage()
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window.show()
    app.exec()
