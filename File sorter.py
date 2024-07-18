#File Sorter by Virginia Herrero

import os, shutil

path = r"C:/Users/Virginia/Downloads/" 

files = os.listdir(path) 

#Names of the folders where I want to store the files
folders = ["Images", "Audios", "Videos", "Texts", "Spreadsheets", "Applications", "Codes"] 

#Lists of extensions 
images = [".jpeg",".png",".jpg",".gif"] 
audios = [".mp3",".wav",".m4a"] 
videos = [".mp4",".mkv"] 
text = [".doc",".txt",".pdf",".docx"] 
spreadsheets = [".xlsx", ".xls", ".csv"]
applications = [".exe",".lnk"] 
codes = [".py",".ipynb", ".c",".cpp", ".css", ".java", ".js",".html",".php"] 

#Create folders if they don't exist
for name in range (0, 7):
    if not os.path.exists(path + folders[name]):
        os.makedirs(path + folders[name])

#Sort files 
for file in files:
    for ext in images:
        if file.endswith(ext):
            shutil.move(path + file, path + "Images/" + file)

    for ext in audios:
        if file.endswith(ext):
           shutil.move(path + file, path + "Audios/" + file)
           break

    for ext in videos:
        if file.endswith(ext):
            shutil.move(path + file, path + "Videos/" + file)
            break

    for ext in text:
        if file.endswith(ext):
            shutil.move(path + file, path + "Texts/" + file)
            break

    for ext in spreadsheets:
        if file.endswith(ext):
            shutil.move(path + file, path + "Spreadsheets/" + file)
            break

    for ext in applications:
        if file.endswith(ext):
            shutil.move(path + file, path + "Applications/" + file)
            break

    for ext in codes:
        if file.endswith(ext):
            shutil.move(path + file, path + "Codes/" + file)
            break




