
# from typing import List,Tuple,TypeVar
# from enum import Enum
# from collections.abc import Sequence as sequence
#from ctypes import c_int8 as


# __all__ = [
#     "long",
#     "ulong",
#     "longlong",
#     "ulonglong",
#     "uint8",
#     "int16",
#     "uint16",
#     "int32",
#     "uint32",
#     "data",
#     "json",
#     "jsondata",
#     "uint",
#     "double",
#     "float32",
#     ## other types
#     "TypeVar",
#     "struct",
#     "List",
#     "Tuple",
#     "callback",
#     "call_class",
#     "call_target",
#     "swift_func",
#     "EventDispatcher",
#     "Codable",
#     "direct",
#     "wrapper",
#     "python",
#     "Enum",
#     "send_self",
#     "sequence",
#     "ObjectStrEnum",
#     "ObjectIntEnum"
#     ]
class int():
    """
    +--------+-----+-------+
    | python | <-> | swift |
    +========+=====+=======+
    | int    |     | Int   |
    +--------+-----+-------+
    """

class uint():
    """
    +--------+-----+-------+
    | python | <-> | swift |
    +========+=====+=======+
    | int    |     | UInt  |
    +--------+-----+-------+
    """

class int32():
    """
    +--------+-----+-------+
    | python | <-> | swift |
    +========+=====+=======+
    | int    |     | Int32 |
    +--------+-----+-------+
    """

class uint32():
    """
    +--------+-----+---------+
    | python | <-> | swift   |
    +========+=====+=========+
    | int    |     | UInt32  |
    +--------+-----+---------+
    """
    
class int16():
    """
    py: int <-> swift: Int16
    """

class uint16():
    """
    py: int <-> swift: UInt16
    """
    
class int8():
    """
    py: int <-> swift: Int8
    """

class uint8():
    """
    +--------+-----+--------+
    | python | <-> | swift  |
    +========+=====+========+
    | str    |     | String |
    +--------+-----+--------+
    """
    
class str():
    """
    py: :attr:`str` <-> swift: :attr:`String`
    """

class list():
    """
    py: list <-> swift: Array

        #list[int] <-> Array<Int>
        #list[uint8] <-> Array<UInt8>
        #list[str] <-> Array<String>
        
    """
    
class memoryview():
    """
    py: memoryview <-> swift: Array

        memoryview[int] <-> Array<Int>
        memoryview[uint8] <-> Array<UInt8>
        memoryview[str] <-> Array<String>
        
    """
    
class data():
    """
    py: memoryview[uint8] <-> swift: Data
    """
    
# long = object
# ulong = object
# longlong = object
# ulonglong = object
# uint8 = object
# short = object
# int16 = object
# ushort = object
# uint16 = object
# data = object
# json = object
# jsondata = object
# uint = object
# double = object
# float32 = object
# longdouble = object


# def EventDispatcher(_(): list[str])(): ...

# def callback(direct(): bool)(): ...

# def call_class(class_name(): str)(): ...

# def call_target(class_name(): str)(): ...

# def swift_func()(): ...

# def _direct()(): ...

# #def codable()(): ...

# class Codable(): ...

# #def wrapper(dispatch_events(): bool = False, events(): list[str] = [], singleton(): bool = True)(): ...

# class wrapper():
    
#     def __init__(self, *args, **kwargs): ...
    
#     def __call__(self, *args, **kwargs): ...

# def python(): ...


# def send_self(): ...

# ObjectStrEnum = Enum

# ObjectIntEnum = Enum

# direct = _direct()