import os

def file_organizer(files,ext):
    arrenged_list=[file for file in files.endwith(ext)]
    print(arrenged_list)
    
    if not(os.path.exist("images")):
        os.mkdir("images")
        
        
    for i , file in enumerate(arrenged_list):
        os.rename(file,f"photos-{i+1}{ext}")
        
        
        
if __name__=="__main__":
    files=os.listdir()
    file_organizer(files, ".jpg")        
    