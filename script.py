import os, os.path

dir_path='E:/python/test'

def countFiles():
   for element in os.listdir(dir_path):
      element_path = os.path.join(dir_path, element)
      if os.path.isdir(element_path):
         print(element_path, sum(1 for element in os.scandir(element_path) if element.is_file))

 
countFiles()