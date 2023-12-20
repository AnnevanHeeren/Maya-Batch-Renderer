from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BatchRenderer(object):
    def setupUi(self, BatchRenderer):
        if not BatchRenderer.objectName():
            BatchRenderer.setObjectName(u"BatchRenderer")
        BatchRenderer.resize(621, 883)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatchRenderer.sizePolicy().hasHeightForWidth())
        BatchRenderer.setSizePolicy(sizePolicy)
        BatchRenderer.setContextMenuPolicy(Qt.NoContextMenu)
        BatchRenderer.setInputMethodHints(Qt.ImhNone)
        BatchRenderer.setSizeGripEnabled(False)
        BatchRenderer.setModal(False)
        self.verticalLayoutWidget = QWidget(BatchRenderer)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 30, 523, 816))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.chbox_subdir = QCheckBox(self.verticalLayoutWidget)
        self.chbox_subdir.setObjectName(u"chbox_subdir")
        self.chbox_subdir.setChecked(True)

        self.verticalLayout.addWidget(self.chbox_subdir)

        self.btn_select_dir = QPushButton(self.verticalLayoutWidget)
        self.btn_select_dir.setObjectName(u"btn_select_dir")
        self.btn_select_dir.setEnabled(True)
        self.btn_select_dir.setAcceptDrops(False)

        self.verticalLayout.addWidget(self.btn_select_dir)

        self.lbl_selected_dir = QLabel(self.verticalLayoutWidget)
        self.lbl_selected_dir.setObjectName(u"lbl_selected_dir")

        self.verticalLayout.addWidget(self.lbl_selected_dir)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.lbl_active_files = QLabel(self.verticalLayoutWidget)
        self.lbl_active_files.setObjectName(u"lbl_active_files")
        self.lbl_active_files.setMinimumSize(QSize(0, 16))

        self.horizontalLayout_5.addWidget(self.lbl_active_files)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.lst_active = QListWidget(self.verticalLayoutWidget)
        self.lst_active.setObjectName(u"lst_active")
        self.lst_active.setSelectionMode(QAbstractItemView.MultiSelection)
        self.lst_active.setSortingEnabled(True)

        self.horizontalLayout.addWidget(self.lst_active)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.chbox_mb = QCheckBox(self.verticalLayoutWidget)
        self.chbox_mb.setObjectName(u"chbox_mb")
        self.chbox_mb.setChecked(True)

        self.gridLayout_2.addWidget(self.chbox_mb, 3, 1, 1, 1)

        self.chbox_obj = QCheckBox(self.verticalLayoutWidget)
        self.chbox_obj.setObjectName(u"chbox_obj")
        self.chbox_obj.setChecked(True)

        self.gridLayout_2.addWidget(self.chbox_obj, 3, 0, 1, 1)

        self.chbox_fbx = QCheckBox(self.verticalLayoutWidget)
        self.chbox_fbx.setObjectName(u"chbox_fbx")
        self.chbox_fbx.setChecked(True)

        self.gridLayout_2.addWidget(self.chbox_fbx, 2, 0, 1, 1)

        self.chbox_ma = QCheckBox(self.verticalLayoutWidget)
        self.chbox_ma.setObjectName(u"chbox_ma")
        self.chbox_ma.setChecked(True)

        self.gridLayout_2.addWidget(self.chbox_ma, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.buttonBox_2 = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.NoButton)
        self.buttonBox_2.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_select_files = QPushButton(self.verticalLayoutWidget)
        self.btn_select_files.setObjectName(u"btn_select_files")

        self.horizontalLayout_3.addWidget(self.btn_select_files)

        self.btn_delete_files = QPushButton(self.verticalLayoutWidget)
        self.btn_delete_files.setObjectName(u"btn_delete_files")

        self.horizontalLayout_3.addWidget(self.btn_delete_files)

        self.btn_clear_list = QPushButton(self.verticalLayoutWidget)
        self.btn_clear_list.setObjectName(u"btn_clear_list")

        self.horizontalLayout_3.addWidget(self.btn_clear_list)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.btn_output_dir = QPushButton(self.verticalLayoutWidget)
        self.btn_output_dir.setObjectName(u"btn_output_dir")

        self.verticalLayout.addWidget(self.btn_output_dir)

        self.lbl_output_dir = QLabel(self.verticalLayoutWidget)
        self.lbl_output_dir.setObjectName(u"lbl_output_dir")

        self.verticalLayout.addWidget(self.lbl_output_dir)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_5)

        self.lbl_render_settings = QLabel(self.verticalLayoutWidget)
        self.lbl_render_settings.setObjectName(u"lbl_render_settings")

        self.verticalLayout.addWidget(self.lbl_render_settings)

        self.cmb_output_type = QComboBox(self.verticalLayoutWidget)
        self.cmb_output_type.addItem("")
        self.cmb_output_type.addItem("")
        self.cmb_output_type.addItem("")
        self.cmb_output_type.setObjectName(u"cmb_output_type")

        self.verticalLayout.addWidget(self.cmb_output_type)

        self.cmb_output_size = QComboBox(self.verticalLayoutWidget)
        self.cmb_output_size.addItem("")
        self.cmb_output_size.addItem("")
        self.cmb_output_size.setObjectName(u"cmb_output_size")

        self.verticalLayout.addWidget(self.cmb_output_size)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_close = QPushButton(self.verticalLayoutWidget)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_6.addWidget(self.btn_close)

        self.btn_render = QPushButton(self.verticalLayoutWidget)
        self.btn_render.setObjectName(u"btn_render")

        self.horizontalLayout_6.addWidget(self.btn_render)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        QWidget.setTabOrder(self.btn_select_dir, self.btn_output_dir)
        QWidget.setTabOrder(self.btn_output_dir, self.cmb_output_type)
        QWidget.setTabOrder(self.cmb_output_type, self.cmb_output_size)

        self.retranslateUi(BatchRenderer)

        QMetaObject.connectSlotsByName(BatchRenderer)
    # setupUi

    def retranslateUi(self, BatchRenderer):
        BatchRenderer.setWindowTitle(QCoreApplication.translate("BatchRenderer", u"Batch Render Menu", None))
#if QT_CONFIG(whatsthis)
        BatchRenderer.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.chbox_subdir.setText(QCoreApplication.translate("BatchRenderer", u"Include Subdirectories", None))
        self.btn_select_dir.setText(QCoreApplication.translate("BatchRenderer", u"Select Directory", None))
        self.lbl_selected_dir.setText(QCoreApplication.translate("BatchRenderer", u"Selected Directory...", None))
        self.lbl_active_files.setText(QCoreApplication.translate("BatchRenderer", u"Files to Render", None))
        self.chbox_mb.setText(QCoreApplication.translate("BatchRenderer", u"MB", None))
        self.chbox_obj.setText(QCoreApplication.translate("BatchRenderer", u"OBJ", None))
        self.chbox_fbx.setText(QCoreApplication.translate("BatchRenderer", u"FBX", None))
        self.chbox_ma.setText(QCoreApplication.translate("BatchRenderer", u"MA", None))
        self.btn_select_files.setText(QCoreApplication.translate("BatchRenderer", u"Add Item", None))
        self.btn_delete_files.setText(QCoreApplication.translate("BatchRenderer", u"Delete Item", None))
        self.btn_clear_list.setText(QCoreApplication.translate("BatchRenderer", u"Clear All", None))
        self.btn_output_dir.setText(QCoreApplication.translate("BatchRenderer", u"Output Directory", None))
        self.lbl_output_dir.setText(QCoreApplication.translate("BatchRenderer", u"Selected Output Directory...", None))
        self.lbl_render_settings.setText(QCoreApplication.translate("BatchRenderer", u"Render Settings", None))
        self.cmb_output_type.setItemText(0, QCoreApplication.translate("BatchRenderer", u"PNG", None))
        self.cmb_output_type.setItemText(1, QCoreApplication.translate("BatchRenderer", u"JPG", None))
        self.cmb_output_type.setItemText(2, QCoreApplication.translate("BatchRenderer", u"EXR", None))

        self.cmb_output_size.setItemText(0, QCoreApplication.translate("BatchRenderer", u"1920x1080", None))
        self.cmb_output_size.setItemText(1, QCoreApplication.translate("BatchRenderer", u"960x540", None))

        self.btn_close.setText(QCoreApplication.translate("BatchRenderer", u"Close", None))
        self.btn_render.setText(QCoreApplication.translate("BatchRenderer", u"Render", None))
    # retranslateUi

