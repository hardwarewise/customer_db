# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 599)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(-1, -1, 20, -1)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.surnameLineEdit = QLineEdit(self.groupBox)
        self.surnameLineEdit.setObjectName(u"surnameLineEdit")

        self.gridLayout.addWidget(self.surnameLineEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.customerIdLineEdit = QLineEdit(self.groupBox)
        self.customerIdLineEdit.setObjectName(u"customerIdLineEdit")

        self.gridLayout.addWidget(self.customerIdLineEdit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.emailLineEdit = QLineEdit(self.groupBox)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.emailLineEdit, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, Qt.AlignTop)

        self.phoneNumberLineEdit = QLineEdit(self.groupBox)
        self.phoneNumberLineEdit.setObjectName(u"phoneNumberLineEdit")
        self.phoneNumberLineEdit.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.phoneNumberLineEdit, 5, 1, 1, 1)

        self.photoFrame = QFrame(self.groupBox)
        self.photoFrame.setObjectName(u"photoFrame")
        self.photoFrame.setMinimumSize(QSize(100, 130))
        self.photoFrame.setMaximumSize(QSize(100, 130))
        self.photoFrame.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"border-radius: 20px;")
        self.photoFrame.setFrameShape(QFrame.StyledPanel)
        self.photoFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.photoFrame, 1, 2, 3, 1)

        self.nameLineEdit = QLineEdit(self.groupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 1, 1, 1, 1)

        self.addressTextEdit = QTextEdit(self.groupBox)
        self.addressTextEdit.setObjectName(u"addressTextEdit")
        self.addressTextEdit.setMaximumSize(QSize(16777215, 80))

        self.gridLayout.addWidget(self.addressTextEdit, 3, 1, 1, 1)

        self.browseBtn = QPushButton(self.groupBox)
        self.browseBtn.setObjectName(u"browseBtn")

        self.gridLayout.addWidget(self.browseBtn, 4, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(self.groupBox)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)

        self.resetBtn = QPushButton(self.groupBox)
        self.resetBtn.setObjectName(u"resetBtn")

        self.horizontalLayout.addWidget(self.resetBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.deleteSelectedRecordBtn = QPushButton(self.groupBox_2)
        self.deleteSelectedRecordBtn.setObjectName(u"deleteSelectedRecordBtn")

        self.horizontalLayout_3.addWidget(self.deleteSelectedRecordBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.searchLineEdit = QLineEdit(self.groupBox_2)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout_3.addWidget(self.searchLineEdit)

        self.searchBtn = QPushButton(self.groupBox_2)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_3.addWidget(self.searchBtn)

        self.clearFilterBtn = QPushButton(self.groupBox_2)
        self.clearFilterBtn.setObjectName(u"clearFilterBtn")

        self.horizontalLayout_3.addWidget(self.clearFilterBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.searchFoundTotalLabel = QLabel(self.groupBox_2)
        self.searchFoundTotalLabel.setObjectName(u"searchFoundTotalLabel")
        self.searchFoundTotalLabel.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.verticalLayout_2.addWidget(self.searchFoundTotalLabel)

        self.tableWidget = QTableWidget(self.groupBox_2)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 744, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Customer ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Customer ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Surname:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.phoneNumberLineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"(000) 000 00 00", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Customer List", None))
        self.deleteSelectedRecordBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Record", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.clearFilterBtn.setText(QCoreApplication.translate("MainWindow", u"Clear Filter", None))
        self.searchFoundTotalLabel.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Customer Id", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Surname", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Photo", None));
    # retranslateUi

