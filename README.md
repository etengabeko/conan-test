Example for C++ package manager **Conan**
=========================================

Structure:
----------

    TestLib
        conanfile.py
        build script
        headers
        sources
    TestBin
        conanfile.py
        build script
        sources
    Deploy
        conanfile.py

Requirements graph:
-------------------

    DeployTest
        Requires:
            TestBin
    TestBin
        Required by:
            DeployTest
        Requires:
            TestLib
    TestLib
        Required by:
            TestBin

Build instructions:
-------------------

    TestLib, TestBin:
        conan create ...
        conan upload ... [optional]
    
    Deploy:
        conan install ...
        conan test ... [optional]

