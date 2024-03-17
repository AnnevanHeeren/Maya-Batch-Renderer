import os

import maya.OpenMayaUI as omui
import maya.mel as mel
import pymel.core as pm
import mtoa.utils as mutils
from shiboken2 import wrapInstance

from PySide2.QtWidgets import *

import batch_renderer_ui


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
    return wrapInstance(int(main_window_pointer), batch_renderer_ui.QWidget)


class BatchRenderer(batch_renderer_ui.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(BatchRenderer, self).__init__(parent)
        self.ui = batch_renderer_ui.Ui_BatchRenderer()
        self.ui.setupUi(self)
        self.create_connections()
        self.setup_scene()

        app = batch_renderer_ui.QApplication.instance()
        for widget in app.topLevelWidgets():
            # if the name of the dialog already exists as another dialog,
            # close it
            if widget.objectName() == self.ui.object_name:
                widget.close()

        self.file_dict = {}
        self.original_file_dict = {}
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
        self.ui.btn_clear_list.clicked.connect(self.clear_file_dict)

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
        self.file_dict.clear()
        self.folder_dir = QFileDialog().getExistingDirectory(self,
                                                             "Select Directory")

        # Changes the directory label to the selected dir
        self.ui.lbl_selected_dir.setEnabled(True)
        self.ui.lbl_selected_dir.setText(self.folder_dir)
        self.file_dict.clear()
        self.get_files()
        # print(self.file_dict)
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
        self.file_dict = self.filter_files()
        self.list_files()
        print(self.file_type_list)
        print(self.file_dict)

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
                        self.file_dict[f'{path}/{file}'] = file
        else:
            for item in os.listdir(self.folder_dir):
                if os.path.isfile(f'{self.folder_dir}/{item}'):
                    file_type = item.split('.')[-1]
                    if file_type in self.file_type_list:
                        self.file_dict[f'{self.folder_dir}/{item}'] = item

        # In order for the filters to work correctly,
        # there needs to be an original and current file dict/list
        self.original_file_dict = self.file_dict

    def list_files(self):
        """
        Lists all files from the file dict in the list widget
        In order to update correctly, the widget is cleared first
        """
        self.ui.lst_active.clear()
        for file in self.file_dict:
            self.ui.lst_active.addItem(file)

    def filter_files(self):
        """
        Is called in the update checkbox method
        Creates a temporary dict with only the checked filetypes
        :returns: a dict with only checked file types
        """
        filtered_file_dict = {}
        for full_path, file in self.original_file_dict.items():
            file_type = self.original_file_dict[full_path].split('.')[-1]
            if file_type in self.file_type_list:
                filtered_file_dict[full_path] = file
        return filtered_file_dict

    def add_files(self):
        """
        Opens a dialog to select files from
        Dialog returns a tuple
        Then filters them according to the file types selected
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.Detail)
        file_names, file_type = dialog.getOpenFileNames(
            self, caption="Select Files to Add")
        for full_path in file_names:
            if full_path not in self.original_file_dict:
                file = full_path.split('/')[-1]
                self.original_file_dict[full_path] = file
                self.file_dict[full_path] = file
        # print(self.file_dict)
        self.file_dict = self.filter_files()
        self.list_files()

    def delete_files(self):
        """
        Deletes all files that are selected in the list widget
        Gets all selected items as list from widget
        Converts each item from pointer to text that matches file dict key
        Creates a list of selected files and removes each item from file dict
        """
        selected_files = [file.text()
                          for file in self.ui.lst_active.selectedItems()]

        for file in selected_files:
            self.original_file_dict.pop(file, None)
            self.file_dict.pop(file, None)
        self.list_files()
        print(self.file_dict)

    def clear_file_dict(self):
        self.file_dict.clear()
        self.list_files()

    def rotate_object(self, geo):
        # Rotates object 360* from start till end of frame range
        pm.setKeyframe(geo, attribute='rotateY',
                       time=self.START_FRAME, value=0)
        pm.setKeyframe(geo, attribute='rotateY',
                       time=self.END_FRAME, value=360)

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
        pm.makeIdentity(geo, apply=True, translate=True,
                        rotate=True, scale=True)
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
        for full_path, file in self.file_dict.items():
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
        if not self.file_dict:
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
