# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Thu Nov  4 17:34:29 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Properties(object):
    def setupUi(self, Properties):
        Properties.setObjectName(_fromUtf8("Properties"))
        Properties.resize(242, 184)
        self.verticalLayout = QtGui.QVBoxLayout(Properties)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Properties)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.accountTab = QtGui.QWidget()
        self.accountTab.setObjectName(_fromUtf8("accountTab"))
        self.formLayout = QtGui.QFormLayout(self.accountTab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.accountTab)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)
        self.label_2 = QtGui.QLabel(self.accountTab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_2)
        self.passwordLine = QtGui.QLineEdit(self.accountTab)
        self.passwordLine.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLine.setObjectName(_fromUtf8("passwordLine"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.passwordLine)
        self.rememberCheckBox = QtGui.QCheckBox(self.accountTab)
        self.rememberCheckBox.setChecked(True)
        self.rememberCheckBox.setObjectName(_fromUtf8("rememberCheckBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.rememberCheckBox)
        self.usernameLine = QtGui.QLineEdit(self.accountTab)
        self.usernameLine.setObjectName(_fromUtf8("usernameLine"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.usernameLine)
        self.tabWidget.addTab(self.accountTab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout_2 = QtGui.QFormLayout(self.tab)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_3)
        self.fileListItems = QtGui.QSpinBox(self.tab)
        self.fileListItems.setMinimum(5)
        self.fileListItems.setMaximum(15)
        self.fileListItems.setObjectName(_fromUtf8("fileListItems"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.fileListItems)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_4)
        self.clipboardCheckBox = QtGui.QCheckBox(self.tab)
        self.clipboardCheckBox.setText(_fromUtf8(""))
        self.clipboardCheckBox.setChecked(True)
        self.clipboardCheckBox.setObjectName(_fromUtf8("clipboardCheckBox"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.clipboardCheckBox)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_5)
        self.notificationCheckBox = QtGui.QCheckBox(self.tab)
        self.notificationCheckBox.setText(_fromUtf8(""))
        self.notificationCheckBox.setObjectName(_fromUtf8("notificationCheckBox"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.notificationCheckBox)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(Properties)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog-ok.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.okButton.setIcon(icon)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(Properties)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog-cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Properties)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Properties.close)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Properties.close)
        QtCore.QMetaObject.connectSlotsByName(Properties)

    def retranslateUi(self, Properties):
        Properties.setWindowTitle(QtGui.QApplication.translate("Properties", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Properties", "UserName", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Properties", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.rememberCheckBox.setText(QtGui.QApplication.translate("Properties", "Remember Me", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accountTab), QtGui.QApplication.translate("Properties", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Properties", "Number of items in filelist", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Properties", "Auto-copy short URL to clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Properties", "Notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Properties", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("Properties", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Properties", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc