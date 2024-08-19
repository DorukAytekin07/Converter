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


sayi = 0
eklenen = 0
#src = "C:/Users/horat/OneDrive/Masaüstü/Deneme"
#dest = "C:/Users/horat/OneDrive/Masaüstü/Convert"
convert_to = 'webp'
to_convert = [".jpg",'png']
for photo in os.listdir(inputPath):
    print(photo)
for photo in os.listdir(inputPath):
   for i in to_convert:
        if i in photo:
            print(photo[photo.index(".")+1:len(photo)])
            temp_image = Image.open(inputPath + "/" + photo)
            png_photo = photo.replace(photo[photo.index(".")+1:len(photo)], convert_to)
            print(png_photo)
            temp_image.save(png_photo)
            print(os.path.abspath(png_photo))
            shutil.move(os.path.abspath(png_photo),outputPath)
            sayi += 1
            print(f"Donusturulen Dosya Sayisi:{sayi}")
        else:
            continue
