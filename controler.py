from __future__ import annotations
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from interface.design import Ui_MainWindow

class new_img(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.cwd = os.getcwd()

        self.btnChooseFile.clicked.connect(self.open_image)
        self.btnResizeByWidth.clicked.connect(self.resize_by_width)
        self.btnResizeByHeight.clicked.connect(self.resize_by_height)
        self.btnSave.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open Image',
            self.cwd
            #options=QFileDialog.DontUseNativeDialog
        )
        if image != '':
            self.inputOpenFile.setText(image)

            self.original_img = QPixmap(image)
            self.labelImg.setPixmap(self.original_img)

            self.inputWidth.setText(str(self.original_img.width()))
            self.inputHeight.setText(str(self.original_img.height()))          

    def resize_by_width(self):
        width = int(self.inputWidth.text())
        self.new_img = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_img)

        self.inputWidth.setText(str(self.new_img.width()))
        self.inputHeight.setText(str(self.new_img.height()))

    def resize_by_height(self):
        height = int(self.inputHeight.text())
        self.new_img = self.original_img.scaledToHeight(height)
        self.labelImg.setPixmap(self.new_img)

        self.inputWidth.setText(str(self.new_img.width()))
        self.inputHeight.setText(str(self.new_img.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save Image',
            self.cwd
            #options=QFileDialog.DontUseNativeDialog
        )
        self.new_img.save(image, 'PNG')    

