# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _SecureUnionID
else:
    import _SecureUnionID

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def HASHIT(hashstring, m):
    return _SecureUnionID.HASHIT(hashstring, m)

def randomSeed():
    return _SecureUnionID.randomSeed()

def genRandSeed():
    return _SecureUnionID.genRandSeed()

def MasterKeygen(ran):
    return _SecureUnionID.MasterKeygen(ran)

def genMasterKey(rnd):
    return _SecureUnionID.genMasterKey(rnd)

def Keygen(masterKey, dspid):
    return _SecureUnionID.Keygen(masterKey, dspid)

def System_Keygen(arg1, arg2, numofmedia):
    return _SecureUnionID.System_Keygen(arg1, arg2, numofmedia)

def Blinding(did, seed):
    return _SecureUnionID.Blinding(did, seed)

def Blind(did, seed):
    return _SecureUnionID.Blind(did, seed)

def Enc(skstring, Mstring):
    return _SecureUnionID.Enc(skstring, Mstring)

def Unblinding(STRING_ARRAY, numofmedia, betastring, sysg1string):
    return _SecureUnionID.Unblinding(STRING_ARRAY, numofmedia, betastring, sysg1string)

def verify_individual(arg1, arg2, arg3, did, numofmedia, betastring):
    return _SecureUnionID.verify_individual(arg1, arg2, arg3, did, numofmedia, betastring)

def batch_verify(arg1, arg2, sysg2string, numofdid):
    return _SecureUnionID.batch_verify(arg1, arg2, sysg2string, numofdid)


