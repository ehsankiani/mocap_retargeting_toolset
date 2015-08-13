import maya.OpenMayaUI as omui
from PySide import QtCore, QtGui

# generates bindings for C++ libraries using CPython source code. 
from shiboken import wrapInstance

# function to return the converted c++ QWidget pointer of Maya
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)
    
##
class mcr_ui(QtGui.QWidget):
    ##
    def __init__(self, parent = maya_main_window()):
        super(mcr_ui, self).__init__(parent)
        self.setWindowTitle("Mocap Retargeting")
        self.setWindowFlags(QtCore.Qt.Window)
        self.resize(QtCore.QSize(500, 5))
        
    ##
    def create_widgets(self):
        self.get_path_line_edit = QtGui.QLineEdit("Enter mocap file path ...")
        self.get_path_push_button = QtGui.QPushButton("Get File")
        
        self.mocap_group_box = QtGui.QGroupBox("Mocap Objects")
        self.mocap_get_scene_push_button = QtGui.QPushButton("Load Selected")
        self.mocap_get_path_push_button = QtGui.QPushButton("Load Path")
        self.mocap_clear_push_button = QtGui.QPushButton("Clear")
        self.mocap_tree = QtGui.QTreeView()
        
        self.target_group_box = QtGui.QGroupBox("Target Objects")
        self.target_get_scene_push_button = QtGui.QPushButton("Load Selected")
        self.target_clear_push_button = QtGui.QPushButton("Clear")
        self.target_tree = QtGui.QTreeView()
    
    ##    
    def create_layouts(self):
        main_layout = QtGui.QVBoxLayout()
        
        path_layout = QtGui.QHBoxLayout()                
        path_layout.addWidget(self.get_path_line_edit)
        path_layout.addWidget(self.get_path_push_button)
        
        group_layout = QtGui.QHBoxLayout()
        group_layout.addWidget(self.mocap_group_box)
        group_layout.addWidget(self.target_group_box)
        
        main_layout.addLayout(path_layout)
        main_layout.addLayout(group_layout)
        
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
    ##
    def draw(self):
        self.create_widgets()
        self.create_layouts()
        
###
if __name__ == "__main__":
    
    try:
        test_ui.close()
    except:
        pass
        
    test_ui = mcr_ui()
    test_ui.draw()
    test_ui.show()
        
        
        
 