TEMPLATE = lib
TARGET = TestLib

CONFIG -= qt

CONFIG += warn_on c++11

DESTDIR = $$PWD/build/lib
OBJECTS_DIR = $$PWD/build/obj

HEADERS += test.h
SOURCES += test.cpp
