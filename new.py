# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 437)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.mubansheet_textEdit = QtWidgets.QTextEdit(Form)
        self.mubansheet_textEdit.setGeometry(QtCore.QRect(480, 40, 111, 40))
        self.mubansheet_textEdit.setObjectName("mubansheet_textEdit")
        self.mubansheet_label = QtWidgets.QLabel(Form)
        self.mubansheet_label.setGeometry(QtCore.QRect(480, 10, 141, 21))
        self.mubansheet_label.setObjectName("mubansheet_label")
        self.mubanwenjian_textEdit = QtWidgets.QTextEdit(Form)
        self.mubanwenjian_textEdit.setGeometry(QtCore.QRect(30, 40, 441, 40))
        self.mubanwenjian_textEdit.setObjectName("mubanwenjian_textEdit")
        self.muban_label = QtWidgets.QLabel(Form)
        self.muban_label.setGeometry(QtCore.QRect(30, 10, 371, 21))
        self.muban_label.setObjectName("muban_label")
        self.zonshuju_textEdit = QtWidgets.QTextEdit(Form)
        self.zonshuju_textEdit.setGeometry(QtCore.QRect(30, 140, 441, 40))
        self.zonshuju_textEdit.setObjectName("zonshuju_textEdit")
        self.zonshuju_label = QtWidgets.QLabel(Form)
        self.zonshuju_label.setGeometry(QtCore.QRect(30, 110, 371, 21))
        self.zonshuju_label.setObjectName("zonshuju_label")
        self.zonshujusheet_textEdit = QtWidgets.QTextEdit(Form)
        self.zonshujusheet_textEdit.setGeometry(QtCore.QRect(480, 140, 111, 40))
        self.zonshujusheet_textEdit.setObjectName("zonshujusheet_textEdit")
        self.zonshujusheet_label = QtWidgets.QLabel(Form)
        self.zonshujusheet_label.setGeometry(QtCore.QRect(480, 110, 111, 21))
        self.zonshujusheet_label.setObjectName("zonshujusheet_label")
        self.confirm_Button = QtWidgets.QPushButton(Form)
        self.confirm_Button.setGeometry(QtCore.QRect(510, 310, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe Fan Heiti Std")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.confirm_Button.setFont(font)
        self.confirm_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.confirm_Button.setObjectName("confirm_Button")
        self.mubandakai_pushButton = QtWidgets.QPushButton(Form)
        self.mubandakai_pushButton.setGeometry(QtCore.QRect(610, 40, 81, 41))
        self.mubandakai_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.mubandakai_pushButton.setObjectName("mubandakai_pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 140, 81, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setGeometry(QtCore.QRect(30, 280, 291, 31))
        self.date_label.setObjectName("date_label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 310, 150, 40))
        self.textEdit.setObjectName("textEdit")
        self.type_ComboBox = QtWidgets.QComboBox(Form)
        self.type_ComboBox.setGeometry(QtCore.QRect(320, 310, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.type_ComboBox.setFont(font)
        self.type_ComboBox.setObjectName("type_ComboBox")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.qunianfile_textEdit = QtWidgets.QTextEdit(Form)
        self.qunianfile_textEdit.setGeometry(QtCore.QRect(30, 235, 500, 40))
        self.qunianfile_textEdit.setObjectName("qunianfile_textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 195, 261, 41))
        self.label.setObjectName("label")
        self.quniansheet_textEdit = QtWidgets.QTextEdit(Form)
        self.quniansheet_textEdit.setGeometry(QtCore.QRect(550, 235, 111, 40))
        self.quniansheet_textEdit.setObjectName("quniansheet_textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 200, 251, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 280, 121, 31))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(30, 380, 681, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mubansheet_label.setText(_translate("Form", "模板sheet"))
        self.muban_label.setText(_translate("Form", "模板文件路径,支持拖文件/手动选择文件"))
        self.zonshuju_label.setText(_translate("Form", "总数据文件路径，支持拖文件/手动选择文件"))
        self.zonshujusheet_label.setText(_translate("Form", "总数据sheet"))
        self.confirm_Button.setText(_translate("Form", "开始"))
        self.mubandakai_pushButton.setText(_translate("Form", "打开文件"))
        self.pushButton_2.setText(_translate("Form", "打开文件"))
        self.date_label.setText(_translate("Form", "指定年份，如果是今年,可以不填写"))
        self.type_ComboBox.setItemText(0, _translate("Form", "sku"))
        self.type_ComboBox.setItemText(1, _translate("Form", "品系"))
        self.type_ComboBox.setItemText(2, _translate("Form", "业态品类"))
        self.label.setText(_translate("Form", "过去数据文件路径"))
        self.label_2.setText(_translate("Form", "过去数据Sheet"))
        self.label_3.setText(_translate("Form", "数据处理类型"))
