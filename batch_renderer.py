# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batchrender.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import re

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

import pymel.core as pm
import maya.OpenMayaUI as omui

def maya_main_window():
    """
    Provides a way for PySide2/Python to interact with the maya main window, which is Qt based(C++)

    Retrieves the pointer to the main maya window
    The pointer is converted into an int
    The shiboken wrapInstance wraps the integer pointer as a PySide2 QWidget
    :return: Maya main window pointer
    :rtype: QtWidgets.QWidget
    """
    main_window_pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_pointer), QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(632, 879)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 591, 841))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_select_dir = QPushButton(self.verticalLayoutWidget)
        self.btn_select_dir.setObjectName(u"btn_select_dir")
        self.btn_select_dir.setEnabled(True)
        self.btn_select_dir.setAcceptDrops(False)

        self.verticalLayout.addWidget(self.btn_select_dir)

        self.lbl_selected_dir = QLabel(self.verticalLayoutWidget)
        self.lbl_selected_dir.setObjectName(u"lbl_selected_dir")

        self.verticalLayout.addWidget(self.lbl_selected_dir)

        self.chbox_subdir = QCheckBox(self.verticalLayoutWidget)
        self.chbox_subdir.setObjectName(u"chbox_subdir")
        self.chbox_subdir.setChecked(True)

        self.verticalLayout.addWidget(self.chbox_subdir)

        self.chbox_latest_versions = QCheckBox(self.verticalLayoutWidget)
        self.chbox_latest_versions.setObjectName(u"chbox_latest_versions")
        self.chbox_latest_versions.setChecked(True)

        self.verticalLayout.addWidget(self.chbox_latest_versions)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.chbox_fbx = QCheckBox(self.verticalLayoutWidget)
        self.chbox_fbx.setObjectName(u"chbox_fbx")

        self.gridLayout_3.addWidget(self.chbox_fbx, 0, 0, 1, 1)

        self.chbox_obj = QCheckBox(self.verticalLayoutWidget)
        self.chbox_obj.setObjectName(u"chbox_obj")

        self.gridLayout_3.addWidget(self.chbox_obj, 1, 0, 1, 1)

        self.chbox_mb = QCheckBox(self.verticalLayoutWidget)
        self.chbox_mb.setObjectName(u"chbox_mb")

        self.gridLayout_3.addWidget(self.chbox_mb, 1, 1, 1, 1)

        self.chbox_ma = QCheckBox(self.verticalLayoutWidget)
        self.chbox_ma.setObjectName(u"chbox_ma")

        self.gridLayout_3.addWidget(self.chbox_ma, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.buttonBox_2 = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.NoButton)
        self.buttonBox_2.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox_2)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 10))
        self.scrollArea.setMaximumSize(QSize(16777215, 160))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 587, 85))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply | QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.btn_select_dir, self.chbox_subdir)
        QWidget.setTabOrder(self.chbox_subdir, self.chbox_latest_versions)
        QWidget.setTabOrder(self.chbox_latest_versions, self.chbox_fbx)
        QWidget.setTabOrder(self.chbox_fbx, self.chbox_obj)
        QWidget.setTabOrder(self.chbox_obj, self.chbox_ma)
        QWidget.setTabOrder(self.chbox_ma, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.chbox_mb)
        QWidget.setTabOrder(self.chbox_mb, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, parent=maya_main_window()):
        # super(Dialog, self).__init__(parent)
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Batch Render Menu", None))
        # if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.btn_select_dir.setText(QCoreApplication.translate("Dialog", u"Select Directory", None))
        self.lbl_selected_dir.setText(QCoreApplication.translate("Dialog", u"Selected Directory...", None))
        self.chbox_subdir.setText(QCoreApplication.translate("Dialog", u"Include Subdirectories", None))
        self.chbox_latest_versions.setText(QCoreApplication.translate("Dialog", u"Latest Versions Only", None))
        self.chbox_fbx.setText(QCoreApplication.translate("Dialog", u"FBX", None))
        self.chbox_obj.setText(QCoreApplication.translate("Dialog", u"OBJ", None))
        self.chbox_mb.setText(QCoreApplication.translate("Dialog", u"MB", None))
        self.chbox_ma.setText(QCoreApplication.translate("Dialog", u"MA", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Add Item to List", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Clear List", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Output Directory", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Selected Output Directory", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"JPG", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"EXR", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"PNG", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"1920x1080", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"New Item", None))

    # retranslateUi

class ImportFiles():

