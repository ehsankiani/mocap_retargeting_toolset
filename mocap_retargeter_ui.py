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
        self.resize(QtCore.QSize(450, 600))
        
    ##
    def create_widgets(self):
        ## main_tabs
        self.main_tabs = QtGui.QTabWidget()
        self.parse_tab = QtGui.QWidget()
        self.cleanup_tab = QtGui.QWidget()
        self.retarget_tab = QtGui.QWidget()
        self.control_graphs_tab = QtGui.QWidget()
        
        ## parse_tab
        self.get_path_line_edit = QtGui.QLineEdit("Enter mocap file path ...")
        self.get_path_push_button = QtGui.QPushButton("Open File")
        self.clear_push_button = QtGui.QPushButton("Clear")
        self.parse_push_button = QtGui.QPushButton("Parse")
        self.parse_push_button.setStyleSheet("background-color: red")
        self.parser_group_box = QtGui.QGroupBox("Mocap File")        
        self.parser_tree = QtGui.QTreeView()
        self.parser_tree.setMinimumHeight(350)
        
        ## retarget_tab
        self.mocap_group_box = QtGui.QGroupBox("Mocap Objects")
        self.mocap_get_scene_push_button = QtGui.QPushButton("Load Selected")
        self.mocap_clear_push_button = QtGui.QPushButton("Clear")
        self.mocap_tree = QtGui.QTreeView()
        self.mocap_tree.setMinimumHeight(350)
        
        self.match_push_button = QtGui.QPushButton("<")
        self.match_push_button.setMinimumHeight(450)
        self.match_retarget_push_button = QtGui.QPushButton("Re-Target")
        self.match_retarget_push_button.setStyleSheet("background-color: red")
        
        self.target_group_box = QtGui.QGroupBox("Target Objects")
        self.target_get_scene_push_button = QtGui.QPushButton("Load Selected")
        self.target_clear_push_button = QtGui.QPushButton("Clear")
        self.target_tree = QtGui.QTreeView()
    
    ##    
    def create_layouts(self):
        ## parse_tab        
        path_layout = QtGui.QHBoxLayout()
        path_layout.addWidget(self.get_path_line_edit)
        path_layout.addWidget(self.get_path_push_button)
        path_layout.addWidget(self.clear_push_button)
        path_layout.addWidget(self.parse_push_button)
        
        parser_layout = QtGui.QVBoxLayout()
        parser_layout.addWidget(self.parser_tree)  
        parser_layout.addLayout(path_layout)
        
        self.parser_group_box.setLayout(parser_layout)
        
        self.parser_main_layout = QtGui.QVBoxLayout()
        self.parser_main_layout.addWidget(self.parser_group_box)
        self.parse_tab.setLayout(self.parser_main_layout)
        
        ## retarget_tab
        match_layout = QtGui.QVBoxLayout()
        match_layout.addWidget(self.match_push_button)
        
        group_layout = QtGui.QHBoxLayout()
        group_layout.addWidget(self.mocap_group_box)
        group_layout.addLayout(match_layout)
        group_layout.addWidget(self.target_group_box)
        group_layout.setStretch(0, 2)
        group_layout.setStretch(2, 2)
        
        mocap_layout = QtGui.QVBoxLayout()
        mocap_layout.addWidget(self.mocap_get_scene_push_button)
        mocap_layout.addWidget(self.mocap_tree)
        mocap_layout.addWidget(self.mocap_clear_push_button)
        self.mocap_group_box.setLayout(mocap_layout)
        
        target_layout = QtGui.QVBoxLayout()
        target_layout.addWidget(self.target_get_scene_push_button)
        target_layout.addWidget(self.target_tree)
        target_layout.addWidget(self.target_clear_push_button)
        self.target_group_box.setLayout(target_layout)
        
        self.retarget_main_layout = QtGui.QVBoxLayout()
        self.retarget_main_layout.addLayout(group_layout)
        self.retarget_main_layout.addWidget(self.match_retarget_push_button)
        
        self.retarget_tab.setLayout(self.retarget_main_layout)
        
        ## main_layout        
        self.main_tabs.addTab(self.parse_tab, "Parser")
        self.main_tabs.addTab(self.cleanup_tab, "Cleanup")
        self.main_tabs.addTab(self.retarget_tab, "Retargeting")
        self.main_tabs.addTab(self.control_graphs_tab, "Key Graphs")
                
        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(self.main_tabs)
                
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
        
