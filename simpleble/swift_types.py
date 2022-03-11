
from typing import List,Tuple,TypeVar
from enum import Enum
from collections.abc import Sequence as sequence
#from ctypes import c_int8 as


__all__ = [
    "long",
    "ulong",
    "longlong",
    "ulonglong",
    "uint8",
    "int16",
    "uint16",
    "int32",
    "uint32",
    "data",
    "json",
    "jsondata",
    "uint",
    "double",
    "float32",
    ## other types
    "TypeVar",
    "struct",
    "List",
    "Tuple",
    "callback",
    "call_class",
    "call_target",
    "swift_func",
    "EventDispatcher",
    "Codable",
    "direct",
    "wrapper",
    "python",
    "Enum",
    "send_self",
    "sequence",
    "ObjectStrEnum",
    "ObjectIntEnum"
    ]

int32 = object
uint32 = object
long = object
ulong = object
longlong = object
ulonglong = object
uint8 = object
short = object
int16 = object
ushort = object
uint16 = object
data = object
json = object
jsondata = object
uint = object
double = object
float32 = object
longdouble = object


def EventDispatcher(_: list[str]): ...

def callback(direct: bool): ...

def call_class(class_name: str): ...

def call_target(class_name: str): ...

def swift_func(): ...

def _direct(): ...

#def codable(): ...

class Codable: ...

#def wrapper(dispatch_events: bool = False, events: list[str] = [], singleton: bool = True): ...

class wrapper:
    
    def __init__(self, *args, **kwargs): ...
    
    def __call__(self, *args, **kwargs): ...

def python(): ...


def send_self(): ...

ObjectStrEnum = Enum

ObjectIntEnum = Enum

direct = _direct()