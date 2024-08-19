#06/05/2023 
#sonra bunu bazi denemeler yap ornegin hangi dosya turlerini kabul ediliyo case sensetive mi ona bak
#eger testlerden gecerse bunu uygulamaya cevir pyside6 pyqt5 yada tkinter ile 

from PIL import Image
import pillow_avif
import pillow_heif
import os
import shutil
import easygui

pillow_heif.register_heif_opener()

inputPath = easygui.diropenbox(title='Select The Input Folder')
outputPath = easygui.diropenbox(title='Select The Output Folder')

total = 0

convert_to = 'webp'
to_convert = ["jpg",'png']
for photo in os.listdir(inputPath):
    print(photo)
for photo in os.listdir(inputPath):
   for type in to_convert:
        if type in photo:
            temp_image = Image.open(inputPath + "/" + photo)
            changed_photo = photo.replace(photo[photo.index(".")+1:len(photo)], convert_to)
            temp_image.save(changed_photo)
    
            shutil.move(os.path.abspath(changed_photo),outputPath)
            total += 1
    
print(f"Total Converted Folder:{total}")