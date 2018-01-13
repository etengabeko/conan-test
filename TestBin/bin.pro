TEMPLATE = app
TARGET = TestBin

CONFIG -= qt

CONFIG += warn_on c++11

CONFIG += conan_basic_setup
include (conanbuildinfo.pri)

DESTDIR = $$PWD/build/bin
OBJECTS_DIR = $$PWD/build/obj

SOURCES += main.cpp
