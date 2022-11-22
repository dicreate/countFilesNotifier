import os, os.path
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
import sys

dir_path='E:/python/test'
currentDir = ''
dictFiles = {}

class Window(QMainWindow):
   def __init__(self):
      super(Window,self).__init__()

      #self.setWindowTitle("notifier")
      #self.setGeometry(300, 250, 350, 200)

      #self.main_text = QtWidgets.QLabel(self)
      #self.main_text.setText("Скрипт работает")
      #self.main_text.move(100,100)
      #self.main_text.adjustSize()

      #self.btn = QtWidgets.QPushButton(self)
      #self.btn.move(70, 150)
      #self.btn.setText('Нажми на меня')
      #self.btn.setFixedWidth(200)
      #self.btn.clicked.connect(self.showMessage)
      while True:
         self.showMessage()

   def add_label(self):
      print('add')

   def showMessage(self):
      self.message = QMessageBox(self)
      self.message.setIcon(QMessageBox.Critical)
      self.message.setText("Information ")
      self.message.setWindowTitle("Information MessageBox")
      self.message.show()
      self.retval = self.message.exec_()
      time.sleep(5)

def application():
   app = QApplication(sys.argv)
   window = Window()
#  window.show()
# sys.exit(app.exec_())

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