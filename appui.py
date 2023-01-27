# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qgis.PyQt import QtCore, QtGui, QtWidgets
from qgis.PyQt.QtWidgets import QDockWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1460, 856)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = gui.QgsMapCanvas(self.centralwidget)
        self.canvas.setEnabled(True)
        self.canvas.setGeometry(QtCore.QRect(9, 9, 1161, 811))
        self.canvas.setObjectName("canvas")
        self.verticalWidget_3 = QtWidgets.QWidget(self.canvas)
        self.verticalWidget_3.setGeometry(QtCore.QRect(860, 180, 291, 81))
        self.verticalWidget_3.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.right_panel_2 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.right_panel_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.right_panel_2.setContentsMargins(0, 0, 0, 0)
        self.right_panel_2.setSpacing(7)
        self.right_panel_2.setObjectName("right_panel_2")
        self.label_import_lc = QtWidgets.QLabel(self.verticalWidget_3)
        self.label_import_lc.setEnabled(True)
        self.label_import_lc.setStyleSheet("")
        self.label_import_lc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_import_lc.setObjectName("label_import_lc")
        self.right_panel_2.addWidget(self.label_import_lc)
        self.browser_lc = gui.QgsFileWidget(self.verticalWidget_3)
        self.browser_lc.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.browser_lc.setObjectName("browser_lc")
        self.right_panel_2.addWidget(self.browser_lc)
        self.verticalWidget_2 = QtWidgets.QWidget(self.canvas)
        self.verticalWidget_2.setGeometry(QtCore.QRect(860, 10, 291, 169))
        self.verticalWidget_2.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.right_panel = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.right_panel.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.right_panel.setContentsMargins(0, 0, 0, 0)
        self.right_panel.setSpacing(7)
        self.right_panel.setObjectName("right_panel")
        self.label_import_sat = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_import_sat.setStyleSheet("")
        self.label_import_sat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_import_sat.setObjectName("label_import_sat")
        self.right_panel.addWidget(self.label_import_sat)
        self.browser_sat = gui.QgsFileWidget(self.verticalWidget_2)
        self.browser_sat.setStyleSheet("\n"
"\n"
"background-color: rgb(244, 244, 244);")
        self.browser_sat.setObjectName("browser_sat")
        self.right_panel.addWidget(self.browser_sat)
        self.lable_select_bands = QtWidgets.QLabel(self.verticalWidget_2)
        self.lable_select_bands.setStyleSheet("")
        self.lable_select_bands.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_select_bands.setObjectName("lable_select_bands")
        self.right_panel.addWidget(self.lable_select_bands)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dd_blue = QtWidgets.QComboBox(self.verticalWidget_2)
        self.dd_blue.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.dd_blue.setObjectName("dd_blue")
        self.dd_blue.setPlaceholderText("Blue Band")
        self.horizontalLayout_2.addWidget(self.dd_blue)
        self.dd_green = QtWidgets.QComboBox(self.verticalWidget_2)
        self.dd_green.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.dd_green.setObjectName("dd_green")
        self.dd_green.setPlaceholderText("Green Band")
        
        self.horizontalLayout_2.addWidget(self.dd_green)
        self.dd_red = QtWidgets.QComboBox(self.verticalWidget_2)
        self.dd_red.setEnabled(True)
        self.dd_red.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.dd_red.setObjectName("dd_red")
        self.dd_red.setPlaceholderText("Red Band")
        self.horizontalLayout_2.addWidget(self.dd_red)
        self.right_panel.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dd_nir = QtWidgets.QComboBox(self.verticalWidget_2)
        self.dd_nir.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.dd_nir.setObjectName("dd_nir")
        self.dd_nir.setPlaceholderText("NIR Band")
        self.horizontalLayout.addWidget(self.dd_nir)
        self.dd_swir = QtWidgets.QComboBox(self.verticalWidget_2)
        self.dd_swir.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.dd_swir.setObjectName("dd_swir")
        self.dd_swir.setPlaceholderText("SWIR Band")
        self.horizontalLayout.addWidget(self.dd_swir)
        self.right_panel.addLayout(self.horizontalLayout)
        
        self.button_export_bands = QtWidgets.QPushButton("Confirm Bands")
        self.right_panel.addWidget(self.button_export_bands)
        self.button_export_bands.setEnabled(False)

        self.add_sat_to_map = QtWidgets.QPushButton(self.verticalWidget_2)
        self.add_sat_to_map.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.add_sat_to_map.setObjectName("add_sat_to_map")
        self.right_panel.addWidget(self.add_sat_to_map)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.label_statusbar_static = QtWidgets.QLabel("Status: ")
        self.statusbar.addWidget(self.label_statusbar_static)
        self.label_statusbar = QtWidgets.QLabel("")
        self.statusbar.addWidget(self.label_statusbar)
        MainWindow.setStatusBar(self.statusbar)
        self.msg_error = QtWidgets.QMessageBox()
        self.msg_error.setIcon(QtWidgets.QMessageBox.Critical)
        
        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setWindowTitle("Processing")
        self.text_edit.setReadOnly(True)
        self.text_edit.setGeometry(370, 170, 450, 500)







        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_import_lc.setText(_translate("MainWindow", "Import Land Cover Dataset"))
        self.label_import_sat.setText(_translate("MainWindow", "Import Satellite Image"))
        self.lable_select_bands.setText(_translate("MainWindow", "Select Blue, Green, Red, NIR and SWIR1 Bands"))
        self.add_sat_to_map.setText(_translate("MainWindow", "Add Image to Map"))
from qgis import gui


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
