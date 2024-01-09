import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import maya.OpenMayaUI as omui
import maya.mel as mel
import pymel.core as pm
import mtoa.utils as mutils
from shiboken2 import wrapInstance


class Ui_BatchRenderer(object):
    def setupUi(self, BatchRenderer):
        if not BatchRenderer.objectName():
            BatchRenderer.setObjectName(u"BatchRenderer")
        self.object_name = BatchRenderer.objectName()
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
        self.lbl_selected_dir.setEnabled(False)

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
        self.cmb_output_type.setItemText(0, QCoreApplication.translate("BatchRenderer", u"png", None))
        self.cmb_output_type.setItemText(1, QCoreApplication.translate("BatchRenderer", u"jpeg", None))
        self.cmb_output_type.setItemText(2, QCoreApplication.translate("BatchRenderer", u"exr", None))

        self.cmb_output_size.setItemText(0, QCoreApplication.translate("BatchRenderer", u"1920x1080", None))
        self.cmb_output_size.setItemText(1, QCoreApplication.translate("BatchRenderer", u"960x540", None))

        self.btn_close.setText(QCoreApplication.translate("BatchRenderer", u"Close", None))
        self.btn_render.setText(QCoreApplication.translate("BatchRenderer", u"Render", None))
    # retranslateUi


def maya_main_window():
    """
    Provides a way for PySide2/Python to interact with the maya main window,
    which is Qt based(C++)

    Retrieves the pointer to the main maya window
    The pointer is converted into an int
    The shiboken wrapInstance wraps the integer pointer as a PySide2 QWidget
    :return: Maya main window pointer
    :rtype: QtWidgets.QWidget
    """
    main_window_pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_pointer), QWidget)


class BatchRenderer(QDialog):
    def __init__(self, parent=maya_main_window()):
        super(BatchRenderer, self).__init__(parent)
        self.ui = Ui_BatchRenderer()
        self.ui.setupUi(self)
        self.create_connections()
        self.setup_scene()

        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            # if the name of the dialog already exists as another dialog,
            # close it
            if widget.objectName() == self.ui.object_name:
                widget.close()

        self.file_list = {}
        self.original_file_list = {}
        self.file_type_list = ['fbx', 'obj', 'ma', 'mb']

        self.render_cam

        self.START_FRAME = 1001
        self.END_FRAME = 1021

        self.output_dir = "" 

    def create_connections(self):
        # Calls methods on button press
        self.ui.btn_select_dir.clicked.connect(self.get_directory)
        self.ui.btn_render.clicked.connect(self.render_clicked)
        self.ui.btn_close.clicked.connect(self.close)

        # When a file type checkbox is pressed, the update method is called.
        # stateChanged.connect() returns a state, lambda gets the state and
        # passes it to the update checkbox function.
        self.ui.chbox_fbx.stateChanged.connect(lambda state:
                                               self.update_checkbox_filetype('fbx', state))
        self.ui.chbox_obj.stateChanged.connect(lambda state:
                                               self.update_checkbox_filetype('obj', state))
        self.ui.chbox_ma.stateChanged.connect(lambda state:
                                              self.update_checkbox_filetype('ma', state))
        self.ui.chbox_mb.stateChanged.connect(lambda state:
                                              self.update_checkbox_filetype('mb', state))

        self.ui.btn_select_files.clicked.connect(self.add_files)
        self.ui.btn_delete_files.clicked.connect(self.delete_files)
        self.ui.btn_clear_list.clicked.connect(self.clear_file_list)

        self.ui.btn_output_dir.clicked.connect(self.set_output_directory)

        print('create connections')

    def setup_scene(self):
        """
        Creates a three-point light setup, a camera, an infinity background
        and a box to scale objects to
        """
        bounding_box = pm.polyCube(n='bounds', d=1.5, w=1.5)
        pm.setAttr(bounding_box[0].translateY, 0.5)
        pm.scale(bounding_box[0], 0.2, 0.2, 0.2)
        pm.hide(bounding_box[0])

        key_light = mutils.createLocator("aiAreaLight", asLight=True)
        transform_node = pm.listRelatives(key_light[1], parent=True)
        pm.rename(transform_node, 'key_light_br')
        pm.setAttr("key_light_br.translateX", 4)
        pm.setAttr("key_light_br.translateZ", 3)
        pm.setAttr("key_light_br.translateY", 2.4)
        pm.setAttr("key_light_br.rotateX", -24)
        pm.setAttr("key_light_br.rotateY", 50)
        pm.setAttr("key_light_br.exposure", 7.6)

        fill_light = mutils.createLocator("aiAreaLight", asLight=True)
        transform_node = pm.listRelatives(fill_light[1], parent=True)
        pm.rename(transform_node, 'fill_light_br')
        pm.setAttr("fill_light_br.translateX", 3)
        pm.setAttr("fill_light_br.translateZ", -4)
        pm.setAttr("fill_light_br.translateY", 1.6)
        pm.setAttr("fill_light_br.rotateX", -20)
        pm.setAttr("fill_light_br.rotateY", 140)
        pm.setAttr("fill_light_br.exposure", 6)

        rim_light = mutils.createLocator("aiAreaLight", asLight=True)
        transform_node = pm.listRelatives(rim_light[1], parent=True)
        pm.rename(transform_node, 'rim_light_br')
        pm.setAttr("rim_light_br.translateX", -4)
        pm.setAttr("rim_light_br.translateY", 2.6)
        pm.setAttr("rim_light_br.rotateX", -8)
        pm.setAttr("rim_light_br.rotateY", -90)
        pm.setAttr("rim_light_br.exposure", 6)

        pm.polyPlane(n='background', sw=1, sh=1, h=20, w=8)
        pm.polyExtrudeEdge('background.e[1]', ty=10)
        pm.polyBevel3('background.e[1]', f=0.4, sg=6, oaf=True)
        pm.move(-2, 0, 0)
        pm.polySoftEdge(a=180)

        self.render_cam = pm.camera(n='render_cam')
        pm.setAttr(self.render_cam[0].rotateY, 90)
        pm.setAttr(self.render_cam[0].translateX, 4)
        pm.setAttr(self.render_cam[0].translateY, 1)
        pm.setAttr(self.render_cam[0].rotateZ, 6)
        pm.setAttr(self.render_cam[0].translate, lock=True)
        pm.setAttr(self.render_cam[0].rotate, lock=True)

    def get_directory(self, *args):
        """
        Opens file navigator and lets user choose a directory to
        gather files from
        Shows the chosen directory in the UI
        """
        self.file_list.clear()
        self.folder_dir = QFileDialog().getExistingDirectory(self,
                                                             "Select Directory")

        # Changes the directory label to the selected dir
        self.ui.lbl_selected_dir.setEnabled(True)
        self.ui.lbl_selected_dir.setText(self.folder_dir)
        self.file_list.clear()
        self.get_files()
        # print(self.file_list)
        self.list_files()

    def update_checkbox_filetype(self, checkbox, state):
        """
        Updates the list of accepted file types when checkbox is pressed
        :param checkbox: the checkbox that was pressed
        :param state: the state the checkbox changed to
        """

        # state 2 means checkbox is checked
        if state == 2:
            self.file_type_list.append(checkbox)
        # state 0 means checkbox is unchecked
        elif state == 0:
            self.file_type_list.remove(checkbox)

        # A dict of new filtered files is assigned to old file dict
        self.file_list = self.filter_files()
        self.list_files()
        print(self.file_type_list)
        print(self.file_list)

    def get_files(self):
        """
        Creates a dictionary of all files found in the given directory,
        and also goes through subdirectories if that checkbox is checked
        """
        if self.ui.chbox_subdir.isChecked():
            for (path, dirs, files) in os.walk(self.folder_dir):
                for file in files:
                    file_type = file.split('.')[-1]
                    if file_type in self.file_type_list:
                        self.file_list[f'{path}/{file}'] = file
        else:
            for item in os.listdir(self.folder_dir):
                if os.path.isfile(f'{self.folder_dir}/{item}'):
                    file_type = item.split('.')[-1]
                    if file_type in self.file_type_list:
                        self.file_list[f'{self.folder_dir}/{item}'] = item

        # In order for the filters to work correctly,
        # there needs to be an original and current file dict/list
        self.original_file_list = self.file_list

    def list_files(self):
        """
        Lists all files from the file dict in the list widget
        In order to update correctly, the widget is cleared first
        """
        self.ui.lst_active.clear()
        for file in self.file_list:
            self.ui.lst_active.addItem(file)

    def filter_files(self):
        """
        Is called in the update checkbox method
        Creates a temporary dict with only the checked filetypes
        :returns: a dict with only checked file types
        """
        filtered_file_list = {}
        for full_path, file in self.original_file_list.items():
            file_type = self.original_file_list[full_path].split('.')[-1]
            if file_type in self.file_type_list:
                filtered_file_list[full_path] = file
        return filtered_file_list

    def add_files(self):
        """
        Opens a dialog to select files from
        Dialog returns a tuple
        Then filters them according to the file types selected
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.Detail)
        file_names, file_type = dialog.getOpenFileNames(self, caption="Select Files to Add")
        for full_path in file_names:
            if full_path not in self.original_file_list:
                file = full_path.split('/')[-1]
                self.original_file_list[full_path] = file
                self.file_list[full_path] = file
        # print(self.file_list)
        self.file_list = self.filter_files()
        self.list_files()

    def delete_files(self):
        """
        Deletes all files that are selected in the list widget
        Gets all selected items as list from widget
        Converts each item from pointer to text that matches file dict key
        Creates a list of selected files and removes each item from file dict
        """
        selected_files = [file.text() for file in self.ui.lst_active.selectedItems()]

        for file in selected_files:
            self.original_file_list.pop(file, None)
            self.file_list.pop(file, None)
        self.list_files()
        print(self.file_list)

    def clear_file_list(self):
        self.file_list.clear()
        self.list_files()

    def rotate_object(self, geo):
        # Rotates object 360* from start till end of frame range
        pm.setKeyframe(geo, attribute='rotateY', time=self.START_FRAME, value=0)
        pm.setKeyframe(geo, attribute='rotateY', time=self.END_FRAME, value=360)

    def set_output_directory(self):
        """
        Opens file dialog for the user to select an output directory
        Changes the output dir label
        """
        self.output_dir = QFileDialog().getExistingDirectory(self,
                                                        "Select Directory")
        self.ui.lbl_output_dir.setEnabled(True)
        self.ui.lbl_output_dir.setText(self.output_dir)

        self.output_dir = self.output_dir.replace('/', '\\')

        print(self.output_dir)

    def scale_obj(self, geo):
        """
        Scales imported object to the reference object
        """
        pm.xform(geo, centerPivots=True)
        pm.makeIdentity(geo, apply=True, translate=True, rotate=True, scale=True)
        pm.matchTransform(geo, 'bounds')

    def render(self):
        """
        Sets render settings
        Renders each object that is in the file dict and stores rendered frame
        in output directory
        """
        # Render settings independent of user input and objects
        pm.setAttr('defaultRenderGlobals.animation', 1)
        pm.setAttr('defaultRenderGlobals.extensionPadding', 4)
        pm.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
        pm.setAttr('defaultRenderGlobals.startFrame', self.START_FRAME)
        pm.setAttr('defaultRenderGlobals.endFrame', self.END_FRAME)
        pm.setAttr(self.render_cam[0].renderable, True)
        pm.setAttr('persp.renderable', False)

        # Render settings dependent of user input
        if self.ui.cmb_output_size.currentText() == '1920x1080':
            pm.setAttr('defaultResolution.width', 1920)
            pm.setAttr('defaultResolution.height', 1080)
        else:
            pm.setAttr('defaultResolution.width', 960)
            pm.setAttr('defaultResolution.height', 540)

        pm.setAttr('defaultArnoldDriver.ai_translator',
                   self.ui.cmb_output_type.currentText(), type='string')

        # Runs over all objects the user wants to render
        for full_path, file in self.file_list.items():
            geo = file.split('.')[0]
            pm.setAttr('defaultRenderGlobals.imageFilePrefix',
                       f'{self.output_dir}\\{geo}/{geo}',
                       type='string')
            imported = pm.importFile(full_path, i=True, returnNewNodes=True)
            self.scale_obj(imported)
            self.rotate_object(imported)
            # Only way to batch render sequentially with Arnold in Maya
            mel.eval('arnoldRender -b;')
            pm.delete(imported)

    def render_clicked(self):
        """
        Checks if dict of files is empty, and renders or gives warning to user when empty
        """
        if not self.file_list:
            pm.warning("No Files to Render!")
        elif self.output_dir == "":
            pm.warning("No Output Directory Selected!")
        else:
            self.render()


def show_window():
    window = BatchRenderer()
    window.show()


"""
in maya:
import batch_renderer as br
from importlib import reload
reload(br)
br.show_window()
"""
