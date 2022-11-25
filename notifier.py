import os, os.path
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
import sys

class Window(QMainWindow):
   def __init__(self):
      super(Window,self).__init__()
      self.dir_path='E:/python/test'
      self.currentDir = ''
      self.dictFiles = {}
      self.message = QMessageBox(self)
      self.message.setIcon(QMessageBox.Critical)

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
               self.message.setText("Количество файлов в папке " + self.currentDir + " не изменилось")
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