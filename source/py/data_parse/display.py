# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4 import QtCore, QtGui
#from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QTimer,  SIGNAL, SLOT, Qt,  QRect
from PyQt4.QtGui import QPainter, QRegion, QPen
import sys, random
from struct import unpack
from functools import partial
from math import floor
from gloveDataParser import ParseView 
from glob import glob


PIXEL_OFFSET = 200 # pixels offsets
 
from Ui_display import Ui_Dialog


class View(QMainWindow, Ui_Dialog):
    """
    Class View inherits the GUI generated by QtDesigner, and add customized actions
    """
    def __init__(self, projectPath,  parent = None):
        """
        Constructor
        """
#        QMainWindow.__init__(self, parent, Qt.FramelessWindowHint)
        QMainWindow.__init__(self, parent)
        self.setStyleSheet("background-color:  rgb(240, 235, 235); margin: 2px;")
        self.setWindowOpacity(0.95)
                                                            
#                                    "QLineEdit { border-width: 20px;border-style: solid; border-color: darkblue; };")
        self.setupUi(self)
        
        self.move(10,  100)
        
        self.x = 200
        self.pen = QPen()

        self.numPt = PIXEL_OFFSET
        self.isPause = False
        self.setWindowTitle(projectPath)
        
        # Search all .bit files, make them selectable 
        sys.path.append(projectPath)
        import os
        print projectPath
        self.lineEdit.setText(str(projectPath))
        self.lineEdit.setStyleSheet("background-color:  rgb(220, 235, 235); margin: 2px;")
        
        for eachBitFile in glob(projectPath+"/*.txt"): 
            (filepath, filename) = os.path.split(eachBitFile) 
#            print filename
            self.listWidget.addItem(filename)
        self.listWidget.setCurrentRow(0)
        self.listWidget.setStyleSheet("background-color:  rgb(220, 235, 235); margin: 2px;")
        
        ## initialization 
        self.digit1=0
        self.digit2=0
        self.digit3=0
        self.digit4=0
        self.digit5=0
        
       
        if (self.isPause):
            return
        size = self.size()
        self.update(QRect(self.x+ 1, 0,size.width() - self.x,size.height()))
        
        if (self.x < size.width() *0.7):  # display line width adjustment
            self.x = self.x + 1  
        else:
            self.x = PIXEL_OFFSET 
            
    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        self.item = item
        


    @pyqtSignature("bool")
    def on_checkBox_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit1 = checked

    
    @pyqtSignature("bool")
    def on_checkBox_2_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit2 = checked
    
    @pyqtSignature("bool")
    def on_checkBox_3_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit3 = checked
        
    @pyqtSignature("bool")
    def on_checkBox_4_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit4 = checked
        
    @pyqtSignature("bool")
    def on_checkBox_5_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit5 = checked
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        
        if self.digit1: 
            pv1= ParseView(str(self.item.text()), 2 )
            self.label_3.setPixmap((QPixmap(str(self.item.text())+"_thumb.png")))
            self.label_3.setScaledContents(True)
            self.label_3.show() 
        if self.digit2: 
            pv2=ParseView(str(self.item.text()), 3 )
            self.label_4.setPixmap((QPixmap(str(self.item.text())+"_index.png")))
            self.label_4.setScaledContents(True)
            self.label_4.show()
        if self.digit3: 
            pv3=ParseView(str(self.item.text()), 4 )
            self.label_5.setPixmap((QPixmap(str(self.item.text())+"_middle.png")))
            self.label_5.setScaledContents(True)
            self.label_5.show()
        
        if self.digit4: 
            pv4=ParseView(str(self.item.text()), 5 ) 
            self.label_6.setPixmap((QPixmap(str(self.item.text())+"_ring.png")))
            self.label_6.setScaledContents(True)
            self.label_6.show()
        
        if self.digit5: 
            pv5=ParseView(str(self.item.text()), 6 ) 
            self.label_7.setPixmap((QPixmap(str(self.item.text())+"_pinky.png")))
            self.label_7.setScaledContents(True)
            self.label_7.show()

        
        
        
      
        
        
        
        
