import os, os.path
import time

dir_path='E:/python/test'
currentDir = ''
dictFiles = {}
currentValue = 0

def countFiles():
   for element in os.listdir(dir_path):
      element_path = os.path.join(dir_path, element)
      if os.path.isdir(element_path):
         currentDir = os.path.split(element_path)[-1]
         if (currentDir in dictFiles.keys()):
            currentValue = dictFiles[currentDir]
         dictFiles[currentDir] = sum(1 for files in os.scandir(element_path) if files.is_file)
         if(currentValue == dictFiles[currentDir]):
            print('значение не изменилось')
         print(dictFiles)   
   time.sleep(5)

while True: 
   countFiles()