from genericpath import isfile
import subprocess, os

fileList = []
outputList = []
def unblock(filename):
    isFile = os.path.isfile(filename)
    if isFile is False:
        for f in os.listdir(filename):
            o = os.path.join(filename, f)
            u = o.replace("\\", "/")
            isFile = os.path.isfile(u)
            if isFile is True:
                fileList.append(u)
            else:
                recurse(u)
    outputList.clear()
    for b in fileList:
        c = str(b.replace(" ", "` "))
        subprocess.run(["powershell", "Unblock-File", "-Path", f"{c}"], capture_output=True)
        d = str(b.replace(" ", ""))
        outputList.append(d)
    fileList.clear()
    return outputList
    
def recurse(file):
    for i in os.listdir(file):
        k = file + "/" + i
        isFile = os.path.isfile(k)
        if isFile is True:
            fileList.append(k)
        else:
            recurse(k)
    pass


    
