from conans import ConanFile, tools
import glob, os, shutil

class TestConan(ConanFile):
    name = "Test"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    description = "Package for Test"
    url = "None"
    license = "None"

    def build(self):
        if not os.path.exists("build/include"):
            os.makedirs("build/include")
            
        if not os.path.exists("build/lib"):
            os.makedirs("build/lib")

        header_files = glob.glob("code/**/*.h", recursive=True)
        for file in header_files:
            if os.path.isfile(file):
                shutil.copy2(file, "build/include/" + os.path.basename(file))
                
        lib_files = glob.glob("obj/**/*.a", recursive=True)
        for file in lib_files:
            if os.path.isfile(file):
                shutil.copy2(file, "build/lib/" + os.path.basename(file))

    def package(self):
        self.copy("build")

    def package_info(self):
        self.cpp_info.libs = ["Test"]
