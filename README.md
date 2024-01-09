# Batch Renderer
A Python script for batch rendering objects in Maya.
You can select a directory to get files from, and they will be listed in the UI.
You can filter by file type, and add and delete files.
Select an output directory to render to, and select an image size and type.
The objects will then be rendered consecutively.

## Resources
- https://doc.qt.io/qtforpython-6/index.html
- https://help.autodesk.com/cloudhelp/2022/JPN/Maya-Tech-Docs/PyMel/modules.html

## Libraries
  ### PySide2
Used for a custom UI in Maya.
The UI was designed in QtDesigner.

  ### OpenMayaUI
A module that contains classes relating to interactions with Maya's UI.

  ### PyMel
An alternative to maya.cmds that allows for more pythonic code.
Might need to be installed first:
- https://help.autodesk.com/view/MAYAUL/2022/ENU/?guid=GUID-2AA5EFCE-53B1-46A0-8E43-4CD0B2C72FB4


  ### MtoA
The Arnold for Maya Python library.
Used to create Arnold lights.

  ### Shiboken2
Offers Python bindings for Qt C++ classes. BatchRenderer
