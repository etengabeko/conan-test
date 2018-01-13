from conans import ConanFile

class DeployTest(ConanFile):
    name = "DeployTest"
    version = "0.1"
    description = "DepolyTest"
    settings = "os", "compiler", "build_type", "arch"
    options = { "shared": [True, False], "devel": [True, False] }
    default_options = "shared=True", "devel=False"

    def requirements(self):
        self.requires("TestBin/0.1@demo/testing")

    def imports(self):
        self.copy("*", src="bin", dst="{}/bin".format(self.imports_folder))
        self.copy("*", src="lib", dst="{}/lib".format(self.imports_folder))
        if self.options.devel:
            self.copy("*.h", src="include", dst="{}/include".format(self.imports_folder))

    def test(self):
        self.run("LD_LIBRARY_PATH={}/lib {}/bin/TestBin".format(self.build_folder, self.build_folder))

