import os, os.path, sys, time, datetime
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

defaultfont = QtGui.QFont('Times New Roman', 30)

class Window(QMainWindow): # класс Window на основе класса QMainWindow
   def __init__(self): # конструктор
      super(Window, self).__init__() # Метод super для наследования базовых классов 
      self.dir_path='E:/python/test' # Папка со всеми объектами 
      self.currentDir = '' # Папка, с которой работает скрипт в настоящий момент времени
      self.dictFiles = {} # Объект, в котором хранятся все директории и количество файлов в них
      self.notifications = {} # Объект, в котором хранятся кол-во уведомлений
      self.message = QMessageBox(self) # Создание объекта MessageBox
      self.message.setIcon(QMessageBox.Warning) # Иконка для MessageBox
      self.message.setFont(defaultfont) # Шрифт для MessageBox
      self.message.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);} ")
      self.message.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);} QLabel{min-width: 1000px; min-height: 600px;}") # Стили для MessageBox

      while True: 
         self.showMessage() # Запуск функции на бесконечное выполнение

   def showMessage(self): # Объявление функции 
      for element in os.listdir(self.dir_path): # Цикл, считывающий все элементы, находящиеся в папке
         self.element_path = os.path.join(self.dir_path, element) # Получаем ссылку на элемент
         
         if os.path.isdir(self.element_path): # Проверка является ли элемент директорием 
            self.lastValue = 0 # Прошлое количество файлов
            self.lastNotifications = 0 # Прошлое количество уведомлений
            self.currentDir = os.path.split(self.element_path)[-1] # Имя текущего директория

            if (self.currentDir in self.dictFiles.keys()): # Проверка есть ли информация по данному директорию в объекте
               self.lastValue = self.dictFiles[self.currentDir] # Записываем прошлое значение в переменную
            
            if (self.currentDir in self.notifications.keys()): # Проверка были ли уже уведомления по объекту
               self.lastNotifications = self.notifications[self.currentDir] # Записываем прошлое значение в переменную

            self.dictFiles[self.currentDir] = sum(1 for files in os.scandir(self.element_path) if files.is_file) # Получаем текущее количество файлов

            if(self.lastValue == self.dictFiles[self.currentDir]): # Сравниваем прошлое и текущее значение
               self.notifications[self.currentDir] = self.lastNotifications + 1
               self.message.setText(f"<p style='color: red; font-size: 100px;'>ВНИМАНИЕ !!!</p><p style='margin-top: 80px'> Кол-во файлов в папке <span style='color: red; font-size: 60px;'>{self.currentDir}</span> не изменилось</p>\n \
               <p style='margin-top: 80px';> <span style='color: green;'>Серия уведомлений: {self.notifications[self.currentDir]}</span></p>") # Текст сообщения 
               self.message.setWindowTitle(f"Объект: {self.currentDir}    Дата и время: {str(datetime.datetime.now())}") # Заголовок сообщения
               self.message.show() # Вызов сообщения
               self.retval = self.message.exec_() # Корректное завершение 
            print(self.dictFiles, self.notifications)  
      time.sleep(5) # Интервал, через который работает скрипт

def application(): # Приложение
   app = QApplication(sys.argv) # Инициализация приложения
   window = Window() # Окно на основе класса Window

if __name__ == "__main__":
   application() # Вызов функции