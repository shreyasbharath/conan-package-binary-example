from conans import ConanFile, tools
import glob, os, shutil

class TestConan(ConanFile):
    name = "Test"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    description = "Package for Test"
    url = "None"
    license = "None"

    def package(self):
        self.copy("*", dst="lib", src="obj/libs")

    def package_info(self):
        self.cpp_info.libs = ["ModuleA", "ModuleB"] # This would be the right names
