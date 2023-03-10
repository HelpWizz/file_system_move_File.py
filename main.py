import os

source = "C:/Users/seane/Downloads/Apex.exe" 
dest = "C:/Users/seane/Downloads/mallard.jpg"

fileName = os.path.splitext(dest)[1]

os.rename(source, fileName)
