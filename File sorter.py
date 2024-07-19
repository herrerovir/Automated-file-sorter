#File Sorter by Virginia Herrero

import os, shutil

#Set path to downloads folder
home = os.path.expanduser("~")
path = os.path.join(home, "Downloads/")

files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

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
print("Sorting files...")

for file in files:
    ext = os.path.splitext(file)[1]
    if ext in images:
        shutil.move(path + file, path + "Images/" + file)
    elif ext in audios:
        shutil.move(path + file, path + "Audios/" + file)
    elif ext in videos:
        shutil.move(path + file, path + "Videos/" + file)
    elif ext in text:
        shutil.move(path + file, path + "Texts/" + file)
    elif ext in spreadsheets:
        shutil.move(path + file, path + "Spreadsheets/" + file)
    elif ext in applications:
        shutil.move(path + file, path + "Applications/" + file)
    elif ext in codes:
        shutil.move(path + file, path + "Codes/" + file)
    else:
        shutil.move(path + file, path + "Others/" + file)

print("Files sorted successfully!")


