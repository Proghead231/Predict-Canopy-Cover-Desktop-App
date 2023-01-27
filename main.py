from qgis.PyQt.QtWidgets import QMainWindow, QApplication, QDockWidget
from qgis.PyQt import QtCore
from qgis.gui import  QgsMapCanvas, QgsLayerTreeMapCanvasBridge, QgsLayerTreeView
from qgis.core import QgsRasterLayer, QgsVectorLayer, QgsProject, QgsLayerTreeModel, QgsCoordinateReferenceSystem
from qgis.PyQt.QtCore import Qt
from appui import Ui_MainWindow
import sys
import os
from osgeo import gdal
import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.set_qgs()



     #On change/clicked connectors
        self.browser_sat.fileChanged.connect(self.add_sat_image)
        self.dd_swir.activated.connect(self.bandsSelected)
        self.button_export_bands.clicked.connect(self.export_bands)
   
    def set_qgs(self):
        self.project = QgsProject.instance()
        self.root = self.project.layerTreeRoot()
        self.bridge = QgsLayerTreeMapCanvasBridge(self.root, self.canvas)
        self.model = QgsLayerTreeModel(self.root)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeReorder)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeRename)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
        self.model.setFlag(QgsLayerTreeModel.ShowLegend)
        self.view = QgsLayerTreeView()
        self.view.setModel(self.model)
        self.LegendDock = QDockWidget( "Layers", self )
        self.LegendDock.setObjectName( "layers" )
        self.LegendDock.setAllowedAreas( Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea )
        self.LegendDock.setWidget( self.view )
        self.LegendDock.setContentsMargins ( 9, 9, 9, 9 )
        self.addDockWidget( Qt.LeftDockWidgetArea, self.LegendDock)             

    #On change/clicked functions
    
    def add_sat_image(self):
        self.button_disabled = False
        self.sat_file_path = self.browser_sat.filePath()
        
        self.sat_image = QgsRasterLayer(self.sat_file_path, 'True Color')
        crs_layer = self.sat_image.crs().authid()
        self.crs = QgsCoordinateReferenceSystem(crs_layer)
        self.canvas.setDestinationCrs(self.crs)
        self.label_statusbar.setText(f"Coordinate system changed to {self.sat_image.crs().authid()}. Note: When multiple images added, recent one will be used for computation")
        self.project.addMapLayer(self.sat_image)
        
        self.canvas.setLayers([self.sat_image])
        self.canvas.setExtent(self.sat_image.extent())
        
        self.populate_dd()

    def populate_dd(self):
        self.bandno = self.sat_image.bandCount()
        self.bandNames = []
        for x in range(1,self.bandno+1):
            self.bandNames.append(self.sat_image.bandName(x)[8:10]) 
            self.dd_blue.clear()
            self.dd_green.clear()
            self.dd_red.clear()
            self.dd_nir.clear()
            self.dd_swir.clear()
            self.dd_blue.addItems(self.bandNames)
            self.dd_green.addItems(self.bandNames)
            self.dd_red.addItems(self.bandNames)
            self.dd_nir.addItems(self.bandNames)
            self.dd_swir.addItems(self.bandNames)

        
    def bandsSelected(self):
        if self.dd_blue.currentIndex() > -1 and self.dd_green.currentIndex() > -1 and self.dd_red.currentIndex() > -1 and self.dd_nir.currentIndex() > -1 and self.dd_swir.currentIndex() > -1:
            self.button_export_bands.setEnabled(True)
  
        else:
            self.msg_error.setText("Error")
            self.msg_error.setInformativeText('Please select blue band from the dropdown')
            self.msg_error.setWindowTitle("Error")
            self.msg_error.exec_()
    
    def get_band_stats(self, bandx):
                band_min = bandx.GetMinimum()
                band_max = bandx.GetMaximum()
                band_nodata = bandx.GetNoDataValue()
                band_dataType = bandx.DataType
                if band_min == None or band_max == None:
                    self.text_edit.append(f"------------------------Stats: {bandx.GetDescription()}---------------------------------------")
                    self.text_edit.append(f"Band minimum is {band_min}. Band maximum is {band_max}. Computing Stats!")
                    bandx.ComputeStatistics(0)
                    band_min = bandx.GetMinimum()
                    band_max = bandx.GetMaximum()
                    band_nodata = bandx.GetNoDataValue()
                    band_dataType = bandx.DataType
                    self.text_edit.append(f"Band min: {band_min}")
                    self.text_edit.append(f"Band max: {band_max}")
                    self.text_edit.append(f"Band NoData: {band_nodata}")
                    self.text_edit.append(f"Band data type: {band_dataType}")
                    self.text_edit.append("--------------------------------------------------------------------")
                else:
                    self.text_edit.append(f"------------------------Stats: {bandx.GetDescription()}---------------------------------------")
                    self.text_edit.append(f"Band min: {band_min}")
                    self.text_edit.append(f"Band max: {band_max}")
                    self.text_edit.append(f"Band NoData: {band_nodata}")
                    self.text_edit.append(f"Band data type: {band_dataType}")
                    self.text_edit.append("--------------------------------------------------------------------")

    def export_bands(self):
        self.text_edit.show()
        self.ds = gdal.Open(self.sat_file_path)
        self.gt = self.ds.GetGeoTransform()
        self.proj = self.ds.GetProjection()
        self.output_path = r"outputs"

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        
        self.band_list = ["blue", "green", "red", "nir", "swir"]
        self.band_index = [self.dd_blue.currentIndex(), self.dd_green.currentIndex(), 
                        self.dd_red.currentIndex(), self.dd_nir.currentIndex(),
                        self.dd_swir.currentIndex()]
                                    
        self.text_edit.insertHtml( 
                            "<font size=4>" + "Bands Assigned:" + "</font>" + "<br>"+
                            "<font size=3>" +
                            ">>"+str(self.dd_blue.currentText())+ ": " + self.band_list[0] + "<br>" + 
                            ">>"+str(self.dd_green.currentText())+ ": " + self.band_list[1] + "<br>"+
                            ">>"+str(self.dd_red.currentText())+ ": " + self.band_list[2] + "<br>"+
                            ">>"+str(self.dd_nir.currentText())+ ": " + self.band_list[3] + "<br>"+
                            ">>"+str(self.dd_swir.currentText())+ ": " + self.band_list[4]+
                            "</font>"+ "<br>"
                            )

                            
                                
        
        
        for i in self.band_index:
            self.band = self.ds.GetRasterBand(i+1)
            print(f"Index used: {i+1}")
            print(f"Band at i+1 index: {self.band.GetDescription()}")
            print(f"Band Name Assigned: {self.band_list[i]}")
            self.array = self.band.ReadAsArray()
            self.band_nodata = self.band.GetNoDataValue()
            self.dataType = self.band.DataType
            self.final_array = np.where((self.array == self.band_nodata), np.nan, self.array) #where arr = nodata set it as nan otherwise return arr
            
            self.driver = gdal.GetDriverByName("GTiff")
            self.driver.Register()
            self.outds = self.driver.Create(os.path.join(self.output_path, self.band_list[i] + ".tif"), self.final_array.shape[1], 
                                self.final_array.shape[0], 1, self.dataType)
            
            self.outds.SetGeoTransform(self.gt)
            self.outds.SetProjection(self.proj)
            
            self.outband = self.outds.GetRasterBand(1)
            self.outband.WriteArray(self.final_array)
            self.outband.DeleteNoDataValue()
            
            self.get_band_stats(self.outband)

            self.outband.FlushCache()
            self.outband = None
            self.outds = None
        self.ds = None
        

    def calc_indices():
        fp = "outputs"
        red_ds = gdal.Open(os.path.join(fp, "red.tif"))
        nir_ds = gdal.Open(os.path.join(fp, "nir.tif"))
        swir_ds = gdal.Open(os.path.join(fp, "swir.tif"))
        blue_ds = gdal.Open(os.path.join(fp, "blue.tif"))
        red_arr = red_ds.GetRasterBand(1).ReadAsArray()
        nir_arr = nir_ds.GetRasterBand(1).ReadAsArray()
        swir_arr = swir_ds.GetRasterBand(1).ReadAsArray()
        blue_arr = blue_ds.GetRasterBand(1).ReadAsArray()


        ndvi = (nir_arr - red_arr)/(nir_arr + red_arr)
        bi = (((swir_arr + red_arr) - (nir_arr + blue_arr)) / ((swir_arr + red_arr) + (nir_arr + blue_arr))) * 100 + 100
        
        
        driver = gdal.GetDriverByName("GTiff")
        driver.Register()
        outds = driver.Create("outputs/ndvi.tif", ndvi.shape[1], 
                            ndvi.shape[0], 1, red_ds.GetRasterBand(1).DataType)

        outds.SetGeoTransform(red_ds.GetGeoTransform())
        outds.SetProjection(red_ds.GetProjection())

        outband = outds.GetRasterBand(1)
        outband.WriteArray(ndvi)
        outband.DeleteNoDataValue()
        outband.FlushCache()
        outband = None
        outds = None
        red_ds = None
        nir_ds = None


def executeApp():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

executeApp()
