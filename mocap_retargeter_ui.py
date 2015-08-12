import maya.OpenMayaUI as omui
from PySide import QtCore, QtGui

# generates bindings for C++ libraries using CPython source code. 
from shiboken import wrapInstance

# function to return the converted c++ QWidget pointer of Maya
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)
    
    
