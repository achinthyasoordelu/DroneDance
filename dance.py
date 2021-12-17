# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dance.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.filePathEdit = QtGui.QLineEdit(Form)
        self.filePathEdit.setGeometry(QtCore.QRect(20, 90, 341, 41))
        self.filePathEdit.setObjectName(_fromUtf8("filePathEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.browse = QtGui.QPushButton(Form)
        self.browse.setGeometry(QtCore.QRect(270, 150, 93, 28))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.dance = QtGui.QPushButton(Form)
        self.dance.setGeometry(QtCore.QRect(60, 210, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dance.setFont(font)
        self.dance.setObjectName(_fromUtf8("dance"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Enter WAV Filepath:", None))
        self.browse.setText(_translate("Form", "Browse", None))
        self.dance.setText(_translate("Form", "Dance", None))

