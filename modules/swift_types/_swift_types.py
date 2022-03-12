
# from typing import List,Tuple,TypeVar
# from enum import Enum
# from collections.abc import Sequence as sequence
#from ctypes import c_int8 as
from builtins import *

# __all__ = im[
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

__all__ = [
    "callback"
] 

class SignedIntegers:

    class int(int):
        """\
        +--------+-----+-------+
        | python | <-> | swift |
        +========+=====+=======+
        |   int  |     |  Int  |
        +--------+-----+-------+
        """

    class int32(int):
        """
        +--------+-----+-------+
        | python | <-> | swift |
        +========+=====+=======+
        | int    |     | Int32 |
        +--------+-----+-------+
        """

        
    class int16(int):
        """
        +--------+-----+-------+
        | python | <-> | swift |
        +========+=====+=======+
        | int    |     | Int16 |
        +--------+-----+-------+
        """

    class int8():
        """
        +--------+-----+-------+
        | python | <-> | swift |
        +========+=====+=======+
        | int    |     | Int8  |
        +--------+-----+-------+
        """

class UnsignedIntegers:

    class uint():
        """
        +--------+-----+-------+
        | python | <-> | swift |
        +========+=====+=======+
        | int    |     | UInt  |
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

    class uint16():
        """
        +--------+-----+--------+
        | python | <-> |  swift |
        +========+=====+========+
        |   int  |     | UInt16 |
        +--------+-----+--------+
        """
        


    class uint8():
        """
        +--------+-----+-------+
        | python | <-> | swift |
        +========+=====+=======+
        |   int  |     | UInt8 |
        +--------+-----+-------+
        """
    
class String_Bytes():

    class str:
        """
        py: :attr:`str` <-> swift: :attr:`String`
        """
class Sequences:
    class list():
        """
        +------------+-----+-------------+
        |   python   | <-> |    swift    |
        +============+=====+=============+
        | list[type] |     | Array<type> |
        +------------+-----+-------------+

            +-------------------------------------+
            |           Python <-> Swift          |
            +=====================================+
            | list[**int**] <-> Array<**Int**>    |
            +-------------------------------------+
            | list[**int**] <-> Array<**UInt8**>  |
            +-------------------------------------+
            | list[**str**] <-> Array<**String**> |
            +-------------------------------------+
            
        """
        
    class memoryview():
        """
        +------------------+-----+-------------+
        |      python      | <-> |    swift    |
        +==================+=====+=============+
        | memoryview[type] |     | Array<type> |
        +------------------+-----+-------------+

            +-------------------------------------------+
            |              Python <-> Swift             |
            +===========================================+
            | memoryview[**int**] <-> Array<**Int**>    |
            +-------------------------------------------+
            | memoryview[**int**] <-> Array<**UInt8**>  |
            +-------------------------------------------+
            | memoryview[**str**] <-> Array<**String**> |
            +-------------------------------------------+
            
        """
        
    class data():
        """
        py: memoryview[:attr:`uint8`] <-> swift: Data
        """


class ClassDecorators:
    """

    """
    class wrapper:
        """

        """
        def __init__(self, singleton=True, event_dispatch=False, events: list[str] = []): ...
    class python:
        """

        """

class FunctionDecorators:
    """

    """
    class callback:
        """
        callback
        """
        def __init__(self, optional=False, direct=False):...
    class swift_function:
        """

        """
        
        
callback = FunctionDecorators.callback
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