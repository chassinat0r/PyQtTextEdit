# Form implementation generated from reading ui file 'ui_output.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setObjectName("menubar")
        self.filemenu = self.menubar.addMenu("File")
        self.helpmenu = self.menubar.addMenu("Help")
        self.verticalLayout.addWidget(self.menubar)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.addTabButton = QtWidgets.QToolButton(Form)
        self.addTabButton.setObjectName("addTabButton")
        self.horizontalLayout.addWidget(self.addTabButton)

        self.closeTabButton = QtWidgets.QToolButton(Form)
        self.closeTabButton.setObjectName("closeTabButton")
        self.horizontalLayout.addWidget(self.closeTabButton)

        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyQtTextEdit"))
        self.addTabButton.setText(_translate("Form", "+"))
        self.closeTabButton.setText(_translate("Form", "x"))