import os, os.path, sys, time, datetime
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from threading import Thread

defaultfont = QtGui.QFont('Times New Roman', 30)

class Window(QMainWindow): # класс Window на основе класса QMainWindow
   def __init__(self): # конструктор
      super(Window, self).__init__() # Метод super для наследования базовых классов 
      self.dir_path = 'E:/TRASSA/EXPORT' # Папка со всеми объектами 
      self.interval = 1080 # Интервал работы скрипты
      self.clearConsoleInterval = 7200 # Интервал очистки консоли

      self.currentDir = '' # Папка, с которой работает скрипт в настоящий момент времени
      self.dictFiles = {} # Объект, в котором хранятся все директории и количество файлов в них
      self.notifications = {} # Объект, в котором хранятся кол-во уведомлений

      self.message = QMessageBox(self) # Создание объекта MessageBox
      self.message.setIcon(QMessageBox.Warning) # Иконка для MessageBox
      self.message.setFont(defaultfont) # Шрифт для MessageBox
      self.message.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);} ")
      self.message.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);} QLabel{min-width: 1000px; min-height: 600px;}") # Стили для MessageBox
      
      self.btnClearAll = QtWidgets.QPushButton(self.message) # Создание кнопки для очистки объекта notifications
      self.btnClearAll.move(60, 570) # Расположение кнопки
      self.btnClearAll.setText('Возобновить все уведомления') # Текст кнопки
      self.btnClearAll.setFixedWidth(230) # Ширина
      self.btnClearAll.setFixedHeight(50) # Высота
      self.btnClearAll.clicked.connect(self.clear_all) # Вызов функции по клику "clear_all"

      self.btnClearAll = QtWidgets.QPushButton(self.message) # Создание кнопки для очистки объекта notifications
      self.btnClearAll.move(310, 570) # Расположение кнопки
      self.btnClearAll.setText('Возобновить уведомления по объекту') # Текст кнопки
      self.btnClearAll.setFixedWidth(230) # Ширина
      self.btnClearAll.setFixedHeight(50) # Высота
      self.btnClearAll.clicked.connect(self.clear_current) # Вызов функции по клику "clear_all"

      self.btnClearAll = QtWidgets.QPushButton(self.message) # Создание кнопки для очистки объекта notifications
      self.btnClearAll.move(560, 570) # Расположение кнопки
      self.btnClearAll.setText('Отключить уведомления по объекту') # Текст кнопки
      self.btnClearAll.setFixedWidth(230) # Ширина
      self.btnClearAll.setFixedHeight(50) # Высота
      self.btnClearAll.clicked.connect(self.disable_current) # Вызов функции по клику "clear_all"

      print(f"[{datetime.datetime.now()}]: Скрипт запущен \n Путь к директорию c объектами: {self.dir_path} \n Интервал работы: {self.interval} секунд ({self.interval / 60} минут) \n Очищение консоли через: {self.clearConsoleInterval} секунд ({self.clearConsoleInterval / 60} минут) ")

      self.writeToFile(f"[{datetime.datetime.now()}]: Скрипт запущен \n Путь к директорию c объектами: {self.dir_path} \n Интервал работы: {self.interval} секунд ({self.interval / 60} минут) \n")
      
      self.clear_console = Thread(target=self.clear_console_func).start()
      self.showMessage()
   
   def __del__(self): # Деструктор
      self.file.close()
   

   def writeToFile(self, text): # Функция записи в файл
      try:
         self.file = open(f'{self.dir_path}/notifierlog.txt', 'a', encoding='utf-8')
         self.file.write(text)
         self.file.close()
      except Exception as e:
         print(f"[{datetime.datetime.now()}]: {e}")

   def clear_all(self): # Очистка объекта notifications
      self.notifications = {}
      print(f'[{datetime.datetime.now()}]: Уведомления по всем объектам включены')
      self.writeToFile(f'[{datetime.datetime.now()}]: Уведомления по всем объектам включены \n')

   def clear_current(self): # Очистка значения объекта notifications
      self.notifications[self.currentDir] = 0
      print(f"[{datetime.datetime.now()}]: Уведомления по объекту {self.currentDir} включены")
      self.writeToFile(f"[{datetime.datetime.now()}]: Уведомления по объекту {self.currentDir} включены \n")

   def disable_current(self): # Отключение уведомлений по объекту
      self.notifications[self.currentDir] = 100
      print(f"[{datetime.datetime.now()}]: Уведомления по объекту {self.currentDir} выключены")
      self.writeToFile(f"[{datetime.datetime.now()}]: Уведомления по объекту {self.currentDir} выключены \n")

   def clear_console_func(self): # функция очистки консоли
      time.sleep(self.clearConsoleInterval)
      os.system('cls||clear')
      print(f"[{datetime.datetime.now()}]: Консоль была очищена")    

   def showMessage(self): # Объявление функции
      while True:
         try: 
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

                  if (self.lastValue == self.dictFiles[self.currentDir]): # Сравниваем прошлое и текущее значение
                     self.notifications[self.currentDir] = self.lastNotifications + 1 # Увеличение количества уведомлений на единицу

                     if (self.notifications[self.currentDir] < 3) : # Сообщение об уведомлениях
                        self.notificationMessage =  f"<span style='color: green;'>Серия уведомлений: {self.notifications[self.currentDir]}</span></p>"
                     else:
                        self.notificationMessage =  f"<span style='color: red;'>Серия уведомлений: {self.notifications[self.currentDir]}</span></p><p style='color: red; font-size: 18px'>Последнее уведомление. Необходимо возобновить уведомления, если хотите продолжить их получать</p>"
                     
                     if (self.notifications[self.currentDir]) < 4:
                        print(f"[{datetime.datetime.now()}]: Количество файлов в папке {self.currentDir} не изменилось \n[{datetime.datetime.now()}]: Ожидание ответа ...") 
                        self.writeToFile(f"[{datetime.datetime.now()}]: Количество файлов в папке {self.currentDir} не изменилось \n {datetime.datetime.now()}]: Ожидание ответа ... \n") 
                        self.message.setText(f"<p style='color: red; font-size: 100px;'>ВНИМАНИЕ !!!</p><p style='margin-top: 80px'> Кол-во файлов в папке не изменилось</p><p><span style='color: red; font-size: 80px;'>{self.currentDir}</span></p>\n \
                        <p style='margin-top: 60px';>{self.notificationMessage}") # Текст сообщения 
                        self.message.setWindowTitle(f"Объект: {self.currentDir}    Дата и время: {str(datetime.datetime.now())}") # Заголовок сообщения
                        self.message.show() # Вызов сообщения
                        self.retval = self.message.exec_() # Корректное завершение
                        print(f"[{datetime.datetime.now()}]: Ответ обработан")
                        self.writeToFile(f"[{datetime.datetime.now()}]: Ответ обработан")
                     else: 
                        print(f"[{datetime.datetime.now()}]: Количество файлов в папке {self.currentDir} не изменилось. Уведомление отключено")
                        self.writeToFile(f"[{datetime.datetime.now()}]: Количество файлов в папке {self.currentDir} не изменилось. Уведомление отключено \n")
                  else:
                     print(f"[{datetime.datetime.now()}]: Объект: {self.currentDir}, Кол-во файлов: {self.dictFiles[self.currentDir]}")
                     self.writeToFile(f"[{datetime.datetime.now()}]: Объект: {self.currentDir}, Кол-во файлов: {self.dictFiles[self.currentDir]} \n")
                     self.notifications[self.currentDir] = 0 # Обнуляем количество уведомлений

         except Exception as e:
            print(f"[{datetime.datetime.now()}]: {e}")
         time.sleep(self.interval) # Интервал, через который работает скрипт

def application(): # Приложение
   app = QApplication(sys.argv) # Инициализация приложения
   window = Window() # Окно на основе класса Window

if __name__ == "__main__":
   application() # Вызов функции