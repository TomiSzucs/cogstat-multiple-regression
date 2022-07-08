# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regression.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(586, 272)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.source_listWidget = QtWidgets.QListWidget(Dialog)
        self.source_listWidget.setMouseTracking(False)
        self.source_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.source_listWidget.setObjectName("source_listWidget")
        self.verticalLayout_3.addWidget(self.source_listWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addPredicted = QtWidgets.QToolButton(Dialog)
        self.addPredicted.setArrowType(QtCore.Qt.RightArrow)
        self.addPredicted.setObjectName("addPredicted")
        self.verticalLayout_2.addWidget(self.addPredicted)
        self.removePredicted = QtWidgets.QToolButton(Dialog)
        self.removePredicted.setArrowType(QtCore.Qt.LeftArrow)
        self.removePredicted.setObjectName("removePredicted")
        self.verticalLayout_2.addWidget(self.removePredicted)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.addPredictor = QtWidgets.QToolButton(Dialog)
        self.addPredictor.setArrowType(QtCore.Qt.RightArrow)
        self.addPredictor.setObjectName("addPredictor")
        self.verticalLayout_2.addWidget(self.addPredictor)
        self.removePredictor = QtWidgets.QToolButton(Dialog)
        self.removePredictor.setArrowType(QtCore.Qt.LeftArrow)
        self.removePredictor.setObjectName("removePredictor")
        self.verticalLayout_2.addWidget(self.removePredictor)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.predicted_listWidget = QtWidgets.QListWidget(Dialog)
        self.predicted_listWidget.setEnabled(True)
        self.predicted_listWidget.setMaximumSize(QtCore.QSize(16777215, 25))
        self.predicted_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.predicted_listWidget.setObjectName("predicted_listWidget")
        self.verticalLayout.addWidget(self.predicted_listWidget)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.predictor_listWidget = QtWidgets.QListWidget(Dialog)
        self.predictor_listWidget.setObjectName("predictor_listWidget")
        self.verticalLayout.addWidget(self.predictor_listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.label.setBuddy(self.source_listWidget)
        self.label_2.setBuddy(self.predicted_listWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.source_listWidget, self.addPredicted)
        Dialog.setTabOrder(self.addPredicted, self.removePredicted)
        Dialog.setTabOrder(self.removePredicted, self.predicted_listWidget)
        Dialog.setTabOrder(self.predicted_listWidget, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Explore relation of variable pairs"))
        self.label.setText(_translate("Dialog", "Available variables"))
        self.pushButton.setText(_translate("Dialog", "O&ptions..."))
        self.addPredictor.setText(_translate("Dialog", "..."))
        self.removePredictor.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "Predicted variable"))
        self.label_3.setText(_translate("Dialog", "Predictor variables"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
