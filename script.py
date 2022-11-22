import os, os.path
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

dir_path='E:/python/test'
currentDir = ''
dictFiles = {}


class Window(QMainWindow):
   def __init__(self):
      super(Window,self).__init__()

      self.setWindowTitle("Простая программа")
      self.setGeometry(300, 250, 350, 200)

      self.main_text = QtWidgets.QLabel(self)
      self.main_text.setText("Это базовая надпись")
      self.main_text.move(100,100)
      self.main_text.adjustSize()


def application():
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec_())


def countFiles():
   for element in os.listdir(dir_path):
      element_path = os.path.join(dir_path, element)
      currentValue = 0
      if os.path.isdir(element_path):
         currentDir = os.path.split(element_path)[-1]
         if (currentDir in dictFiles.keys()):
            currentValue = dictFiles[currentDir]
         dictFiles[currentDir] = sum(1 for files in os.scandir(element_path) if files.is_file)
         if(currentValue == dictFiles[currentDir]):
            print('значение не изменилось')
         print(dictFiles)   
   time.sleep(5)

#while True: 
#   countFiles()

application()