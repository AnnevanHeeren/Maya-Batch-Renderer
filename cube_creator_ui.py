# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createblockrnXpbw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import maya.OpenMayaUI as omui
import pymel.core as pm
from shiboken2 import wrapInstance  # Used to access internal information about Maya

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
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 40, 281, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.createBox = QPushButton(self.verticalLayoutWidget)
        self.createBox.setObjectName(u"createBox")

        self.verticalLayout.addWidget(self.createBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.createBox.setText(QCoreApplication.translate("Dialog", u"Create Box", None))
    # retranslateUi


class CreateCubeWindow(Ui_Dialog):
    def __init__(self, parent=maya_main_window()):
        super(Ui_Dialog, self).__init__(parent)

        self.show(Ui_Dialog)