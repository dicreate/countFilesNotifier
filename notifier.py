import os, os.path
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QDialog
import sys

defaultfont = QtGui.QFont('Times New Roman', 30)

class Window(QMainWindow): # класс Window на основе класса QMainWindow
   def __init__(self): # конструктор
      super(Window, self).__init__()
      self.dir_path='E:/python/test'
      self.currentDir = ''
      self.dictFiles = {}
      self.message = QMessageBox(self)
      self.message.setIcon(QMessageBox.Warning)
      self.message.setFont(defaultfont)
      
      self.message.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);} ")
      self.message.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);} QLabel{min-width: 1000px; min-height: 600px;}")

      while True:
         self.showMessage()

   def showMessage(self):
      for element in os.listdir(self.dir_path):
         self.element_path = os.path.join(self.dir_path, element)
         self.currentValue = 0
         if os.path.isdir(self.element_path):
            self.currentDir = os.path.split(self.element_path)[-1]
            if (self.currentDir in self.dictFiles.keys()):
               self.currentValue = self.dictFiles[self.currentDir]
            self.dictFiles[self.currentDir] = sum(1 for files in os.scandir(self.element_path) if files.is_file)
            if(self.currentValue == self.dictFiles[self.currentDir]):
               self.message.setText(f"<p style='color: red; font-size: 60px;'>ВНИМАНИЕ !!!</p><p style='margin-top: 80px'> Кол-во файлов в папке <span style='color: red; font-size: 60px;'>{self.currentDir}</span> не изменилось</p>\n \
               <p style='margin-top: 80px';> <span style='color: green;'>Серия уведомлений: 2</span></p>")
               self.message.setWindowTitle(self.currentDir)
               self.message.show()
               self.retval = self.message.exec_()
            print(self.dictFiles)  
      time.sleep(5)

def application():
   app = QApplication(sys.argv)
   window = Window()

if __name__ == "__main__":
   application()