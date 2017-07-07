# conan-package-binary-example
A working example of packaging pre-built binaries (libs + header files) and uploading them to a Conan remote for consumption

This repository is an example of integrating Conan into your existing build process where the artifacts already exist.

The structure of the example project is as follows -
  - code
    - inc -> contains public APIs (header files) of modules
  - ModuleA -> contains source files for ModuleA
  - ModuleB -> contains source files for ModuleB
  - obj
    - libs -> pre-built static libraries of ModuleA and ModuleB
    - ModuleA -> corresponding object files for source files of ModuleA
    - ModuleB -> corresponding object files for source files of ModuleB
    
The idea is to create a package that has the public header files and the pre-compiled static libraries from this project.
