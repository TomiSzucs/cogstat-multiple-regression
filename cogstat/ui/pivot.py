# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pivot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 350)
        Dialog.setMinimumSize(QtCore.QSize(360, 350))
        Dialog.setMaximumSize(QtCore.QSize(360, 350))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 310, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.function = QtWidgets.QComboBox(Dialog)
        self.function.setGeometry(QtCore.QRect(210, 270, 141, 24))
        self.function.setObjectName("function")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.function.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 130, 55, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 70, 55, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 55, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 200, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 250, 55, 13))
        self.label_6.setObjectName("label_6")
        self.removeRows = QtWidgets.QPushButton(Dialog)
        self.removeRows.setGeometry(QtCore.QRect(180, 170, 21, 21))
        self.removeRows.setObjectName("removeRows")
        self.addRows = QtWidgets.QPushButton(Dialog)
        self.addRows.setGeometry(QtCore.QRect(180, 150, 21, 21))
        self.addRows.setObjectName("addRows")
        self.addColumns = QtWidgets.QPushButton(Dialog)
        self.addColumns.setGeometry(QtCore.QRect(180, 90, 21, 21))
        self.addColumns.setObjectName("addColumns")
        self.removeColumns = QtWidgets.QPushButton(Dialog)
        self.removeColumns.setGeometry(QtCore.QRect(180, 110, 21, 21))
        self.removeColumns.setObjectName("removeColumns")
        self.addPages = QtWidgets.QPushButton(Dialog)
        self.addPages.setGeometry(QtCore.QRect(180, 30, 21, 21))
        self.addPages.setObjectName("addPages")
        self.removePages = QtWidgets.QPushButton(Dialog)
        self.removePages.setGeometry(QtCore.QRect(180, 50, 21, 21))
        self.removePages.setObjectName("removePages")
        self.addDependent = QtWidgets.QPushButton(Dialog)
        self.addDependent.setGeometry(QtCore.QRect(180, 220, 21, 21))
        self.addDependent.setObjectName("addDependent")
        self.removeDependent = QtWidgets.QPushButton(Dialog)
        self.removeDependent.setGeometry(QtCore.QRect(180, 240, 21, 21))
        self.removeDependent.setObjectName("removeDependent")
        self.sourceListWidget = QtWidgets.QListWidget(Dialog)
        self.sourceListWidget.setGeometry(QtCore.QRect(10, 30, 150, 230))
        self.sourceListWidget.setMinimumSize(QtCore.QSize(150, 230))
        self.sourceListWidget.setMaximumSize(QtCore.QSize(150, 230))
        self.sourceListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.sourceListWidget.setObjectName("sourceListWidget")
        self.rowsListWidget = QtWidgets.QListWidget(Dialog)
        self.rowsListWidget.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.rowsListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rowsListWidget.setObjectName("rowsListWidget")
        self.columnsListWidget = QtWidgets.QListWidget(Dialog)
        self.columnsListWidget.setGeometry(QtCore.QRect(210, 90, 141, 31))
        self.columnsListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.columnsListWidget.setObjectName("columnsListWidget")
        self.pagesListWidget = QtWidgets.QListWidget(Dialog)
        self.pagesListWidget.setGeometry(QtCore.QRect(210, 30, 141, 31))
        self.pagesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pagesListWidget.setObjectName("pagesListWidget")
        self.dependentListWidget = QtWidgets.QListWidget(Dialog)
        self.dependentListWidget.setGeometry(QtCore.QRect(210, 220, 141, 21))
        self.dependentListWidget.setObjectName("dependentListWidget")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pivot table"))
        self.label.setText(_translate("Dialog", "Available variables"))
        self.function.setItemText(0, _translate("Dialog", "N"))
        self.function.setItemText(1, _translate("Dialog", "Sum"))
        self.function.setItemText(2, _translate("Dialog", "Mean"))
        self.function.setItemText(3, _translate("Dialog", "Median"))
        self.function.setItemText(4, _translate("Dialog", "Lower quartile"))
        self.function.setItemText(5, _translate("Dialog", "Upper quartile"))
        self.function.setItemText(6, _translate("Dialog", "Standard deviation"))
        self.function.setItemText(7, _translate("Dialog", "Variance"))
        self.label_2.setText(_translate("Dialog", "Rows"))
        self.label_3.setText(_translate("Dialog", "Columns"))
        self.label_4.setText(_translate("Dialog", "Pages"))
        self.label_5.setText(_translate("Dialog", "Dependent variable"))
        self.label_6.setText(_translate("Dialog", "Function"))
        self.removeRows.setText(_translate("Dialog", "<="))
        self.addRows.setText(_translate("Dialog", "=>"))
        self.addColumns.setText(_translate("Dialog", "=>"))
        self.removeColumns.setText(_translate("Dialog", "<="))
        self.addPages.setText(_translate("Dialog", "=>"))
        self.removePages.setText(_translate("Dialog", "<="))
        self.addDependent.setText(_translate("Dialog", "=>"))
        self.removeDependent.setText(_translate("Dialog", "<="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

