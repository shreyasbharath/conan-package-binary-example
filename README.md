# Packaging Existing Artifacts
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

Conan in its current form is heavily geared towards building from source and publishing the artifacts as a result of that build. However, in our case we want Conan to simply slot in to an existing build process and only be responsible for creating a package from existing artifacts and publishing it to a remote for consumption by other projects.

The main scripts of interest are `build.py` and `conanfile.py`. Below are the list of steps they run -

  - Create a temporary directory called 'mypkg' and change to that directory
  - Execute command `conan package .. --build_folder..`, where the arguments `..` points to where the conanfile.py is located and the `--build_folder=..` also points to where the build artifacts are located (both are in the same location). This copies the public header files and static libraries into the `include` and `lib` directories respectively.
  - Execute command `cd .. && conan export myuser/testing` which copies the package recipe into the local Conan cache for the user `myuser` and the `testing` channel
  - Execute command `conan package_files Test/0.1@myuser/testing -f` packages everything under the `mypkg` directory and copies it to the local Conan cache
  - Execute command `conan upload Test/0.1@myuser/testing --all -r=artifactory` uploads the package recipe and its artifacts to the remote named `artifactory`

# Consumption of Uploaded Package
See [conan-package-binary-consume-example](https://github.com/shreyasbharath/conan-package-binary-consume-example) to understand how to extract the contents of the uploaded package to a client project for consumption by the client project's build process.

# Credits
A big thanks to @memsharded and @drodri for their help.
