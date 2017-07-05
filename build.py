import os, shutil

try:
    shutil.rmtree("mypkg")
except:
    pass

os.system("conan install")
os.makedirs("mypkg")
try:
    old = os.getcwd()
    os.chdir("mypkg")
    os.system("conan package .. --build_folder=../")
    print os.listdir(".")
    print os.listdir("./lib")
finally:
    os.chdir(old)