from conans import ConanFile

class TestBin(ConanFile):
    name = "TestBin"
    version = "0.1"
    description = "TestBin"
    settings = "os", "compiler", "build_type", "arch"
    options = { "shared": [True, False] }
    default_options = "shared=True"
    generators = "qmake"
    exports_sources = "*"

    def requirements(self):
        self.requires("TestLib/0.1@demo/testing")

    def build(self):
        self.run("qmake CONFIG+={}".format(str(self.settings.build_type).lower()))
        self.run("make")

    def package(self):
        self.copy("*", src="./build/bin", dst="bin", keep_path=False)

