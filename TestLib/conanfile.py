from conans import ConanFile

class TestLib(ConanFile):
    name = "TestLib"
    version = "0.1"
    description = "TestLib"
    settings = "os", "compiler", "build_type", "arch"
    options = { "shared": [True, False] }
    default_options = "shared=True"
    generators = "qmake"
    exports_sources = "*"

    def build(self):
        self.run("qmake CONFIG+={}".format(str(self.settings.build_type).lower()))
        self.run("make")

    def package(self):
        self.copy("*.h", src=".", dst="include", keep_path=False)
        self.copy("*.so*", src="./build/lib", dst="lib", keep_path=False, symlinks=True)

    def package_info(self):
        self.cpp_info.libs = ["TestLib"]

