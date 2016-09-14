TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

ifeq ($(USE_GRAPHICSMAGICK), YES)
  # The following gets rid of the -fno-implicit-templates flag on vxWorks, 
  # so we get automatic template instantiation.
  # This is what we want for miscellaneous/asynPortDriver.cpp
  ifeq (vxWorks,$(findstring vxWorks, $(T_A)))
    CODE_CXXFLAGS=
  endif

  LIBRARY_IOC_Linux = URLDriver
  LIBRARY_IOC_WIN32 = URLDriver
  LIBRARY_IOC_cygwin32 = URLDriver
  LIBRARY_IOC_Darwin = URLDriver

  DBD += URLDriverSupport.dbd

  LIB_SRCS += URLDriver.cpp

  URLDriver_INCLUDES += -I$(MAGICK_PREFIX)/include/GraphicsMagick

  GRAPHICS_MAGICK_LIBS = $(MAGICK_PREFIX)/lib

  GraphicsMagick_DIR = $(GRAPHICS_MAGICK_LIBS)
  GraphicsMagick++_DIR = $(GRAPHICS_MAGICK_LIBS)
  GraphicsMagickWand_DIR = $(GRAPHICS_MAGICK_LIBS)

  URLDriver_LIBS += GraphicsMagick
  URLDriver_LIBS += GraphicsMagick++
  URLDriver_LIBS += GraphicsMagickWand

  #include $(ADCORE)/ADApp/commonLibraryMakefile
endif

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

