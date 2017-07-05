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
    print(os.listdir("."))
    print(os.listdir("./lib"))
    os.system("cd .. && conan export user/channel") # This will improve next 0.25 with an --cwd=.. arg
    os.system("conan package_files Test/0.1@user/channel -f")  # -f in case it exists, overwrite
    os.system("conan search Test/0.1@user/channel") # To show the package binary
    # os.system("conan upload Test/0.1@user/channel --all -r=")
finally:
    os.chdir(old)