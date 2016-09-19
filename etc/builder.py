import copy

from iocbuilder import Device, AutoSubstitution
from iocbuilder.arginfo import *

from iocbuilder.modules.asyn import Asyn, AsynPort
from iocbuilder.modules.ADCore import ADCore, ADBaseTemplate, includesTemplates, makeTemplateInstance

class ADURL(Device):
    '''Library dependencies for ADURL'''
    Dependencies = (ADCore,)
    # Device attributes
    LibFileList = ['URLDriver']
    DbdFileList = ['URLDriverSupport']
    AutoInstantiate = True

@includesTemplates(ADBaseTemplate)
class _URLDriver(AutoSubstitution):
    '''areaDetector base template wrapper'''
    TemplateFile = "URLDriver.template"

class URLDriver(AsynPort):
    """This plugin creates a URLDriver object"""
    # This tells xmlbuilder to use PORT instead of name as the row ID
    UniqueName = "PORT"

    _SpecificTemplate = _URLDriver
    Dependencies = (ADURL,)

    def __init__(self, PORT, BUFFERS = 10, MEMORY = 0, **args):
        # Init the superclass (AsynPort)
        self.__super.__init__(PORT)
        # Update the attributes of self from the commandline args
        self.__dict__.update(locals())
        # Make an instance of our template
        makeTemplateInstance(self._SpecificTemplate, locals(), args)

    def Initialise(self):
        print '# URLDriverConfig(portName, maxBuffers, maxMemory)' % self.__dict__
        print 'URLDriverConfig("%(PORT)s", %(BUFFERS)d, %(MEMORY)d)' % self.__dict__

    # __init__ arguments
    ArgInfo = _SpecificTemplate.ArgInfo + makeArgInfo(__init__,
        PORT = Simple('Port name for the plugin', str),
        BUFFERS = Simple('Maximum number of NDArray buffers to be created for '
            'plugin callbacks', int),
        MEMORY = Simple('Max memory to allocate, should be maxw*maxh*nbuffer '
            'for driver and all attached plugins', int))


