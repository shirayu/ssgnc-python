# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ssgnc', [dirname(__file__)])
        except ImportError:
            import _ssgnc
            return _ssgnc
        if fp is not None:
            try:
                _mod = imp.load_module('_ssgnc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ssgnc = swig_import_helper()
    del swig_import_helper
else:
    import _ssgnc
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ssgnc.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _ssgnc.SwigPyIterator_value(self)
    def incr(self, n = 1): return _ssgnc.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _ssgnc.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _ssgnc.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _ssgnc.SwigPyIterator_equal(self, *args)
    def copy(self): return _ssgnc.SwigPyIterator_copy(self)
    def next(self): return _ssgnc.SwigPyIterator_next(self)
    def __next__(self): return _ssgnc.SwigPyIterator___next__(self)
    def previous(self): return _ssgnc.SwigPyIterator_previous(self)
    def advance(self, *args): return _ssgnc.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _ssgnc.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _ssgnc.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _ssgnc.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _ssgnc.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _ssgnc.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _ssgnc.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _ssgnc.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _ssgnc.IntVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _ssgnc.IntVector___nonzero__(self)
    def __bool__(self): return _ssgnc.IntVector___bool__(self)
    def __len__(self): return _ssgnc.IntVector___len__(self)
    def pop(self): return _ssgnc.IntVector_pop(self)
    def __getslice__(self, *args): return _ssgnc.IntVector___getslice__(self, *args)
    def __setslice__(self, *args): return _ssgnc.IntVector___setslice__(self, *args)
    def __delslice__(self, *args): return _ssgnc.IntVector___delslice__(self, *args)
    def __delitem__(self, *args): return _ssgnc.IntVector___delitem__(self, *args)
    def __getitem__(self, *args): return _ssgnc.IntVector___getitem__(self, *args)
    def __setitem__(self, *args): return _ssgnc.IntVector___setitem__(self, *args)
    def append(self, *args): return _ssgnc.IntVector_append(self, *args)
    def empty(self): return _ssgnc.IntVector_empty(self)
    def size(self): return _ssgnc.IntVector_size(self)
    def clear(self): return _ssgnc.IntVector_clear(self)
    def swap(self, *args): return _ssgnc.IntVector_swap(self, *args)
    def get_allocator(self): return _ssgnc.IntVector_get_allocator(self)
    def begin(self): return _ssgnc.IntVector_begin(self)
    def end(self): return _ssgnc.IntVector_end(self)
    def rbegin(self): return _ssgnc.IntVector_rbegin(self)
    def rend(self): return _ssgnc.IntVector_rend(self)
    def pop_back(self): return _ssgnc.IntVector_pop_back(self)
    def erase(self, *args): return _ssgnc.IntVector_erase(self, *args)
    def __init__(self, *args): 
        this = _ssgnc.new_IntVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _ssgnc.IntVector_push_back(self, *args)
    def front(self): return _ssgnc.IntVector_front(self)
    def back(self): return _ssgnc.IntVector_back(self)
    def assign(self, *args): return _ssgnc.IntVector_assign(self, *args)
    def resize(self, *args): return _ssgnc.IntVector_resize(self, *args)
    def insert(self, *args): return _ssgnc.IntVector_insert(self, *args)
    def reserve(self, *args): return _ssgnc.IntVector_reserve(self, *args)
    def capacity(self): return _ssgnc.IntVector_capacity(self)
    __swig_destroy__ = _ssgnc.delete_IntVector
    __del__ = lambda self : None;
IntVector_swigregister = _ssgnc.IntVector_swigregister
IntVector_swigregister(IntVector)

class IntMap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntMap, name)
    __repr__ = _swig_repr
    def iterator(self): return _ssgnc.IntMap_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _ssgnc.IntMap___nonzero__(self)
    def __bool__(self): return _ssgnc.IntMap___bool__(self)
    def __len__(self): return _ssgnc.IntMap___len__(self)
    def __getitem__(self, *args): return _ssgnc.IntMap___getitem__(self, *args)
    def __delitem__(self, *args): return _ssgnc.IntMap___delitem__(self, *args)
    def has_key(self, *args): return _ssgnc.IntMap_has_key(self, *args)
    def keys(self): return _ssgnc.IntMap_keys(self)
    def values(self): return _ssgnc.IntMap_values(self)
    def items(self): return _ssgnc.IntMap_items(self)
    def __contains__(self, *args): return _ssgnc.IntMap___contains__(self, *args)
    def key_iterator(self): return _ssgnc.IntMap_key_iterator(self)
    def value_iterator(self): return _ssgnc.IntMap_value_iterator(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __setitem__(self, *args): return _ssgnc.IntMap___setitem__(self, *args)
    def __init__(self, *args): 
        this = _ssgnc.new_IntMap(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _ssgnc.IntMap_empty(self)
    def size(self): return _ssgnc.IntMap_size(self)
    def clear(self): return _ssgnc.IntMap_clear(self)
    def swap(self, *args): return _ssgnc.IntMap_swap(self, *args)
    def get_allocator(self): return _ssgnc.IntMap_get_allocator(self)
    def begin(self): return _ssgnc.IntMap_begin(self)
    def end(self): return _ssgnc.IntMap_end(self)
    def rbegin(self): return _ssgnc.IntMap_rbegin(self)
    def rend(self): return _ssgnc.IntMap_rend(self)
    def count(self, *args): return _ssgnc.IntMap_count(self, *args)
    def erase(self, *args): return _ssgnc.IntMap_erase(self, *args)
    def find(self, *args): return _ssgnc.IntMap_find(self, *args)
    def lower_bound(self, *args): return _ssgnc.IntMap_lower_bound(self, *args)
    def upper_bound(self, *args): return _ssgnc.IntMap_upper_bound(self, *args)
    __swig_destroy__ = _ssgnc.delete_IntMap
    __del__ = lambda self : None;
IntMap_swigregister = _ssgnc.IntMap_swigregister
IntMap_swigregister(IntMap)

class Database(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Database, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Database, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _ssgnc.new_Database()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ssgnc.delete_Database
    __del__ = lambda self : None;
    def search(self, *args): return _ssgnc.Database_search(self, *args)
    def open(self, *args): return _ssgnc.Database_open(self, *args)
    def parseQuery(self, *args): return _ssgnc.Database_parseQuery(self, *args)
Database_swigregister = _ssgnc.Database_swigregister
Database_swigregister(Database)

class Query(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Query, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Query, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _ssgnc.new_Query()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ssgnc.delete_Query
    __del__ = lambda self : None;
    def setOption(self, *args): return _ssgnc.Query_setOption(self, *args)
Query_swigregister = _ssgnc.Query_swigregister
Query_swigregister(Query)

class Agent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Agent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Agent, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _ssgnc.new_Agent()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ssgnc.delete_Agent
    __del__ = lambda self : None;
Agent_swigregister = _ssgnc.Agent_swigregister
Agent_swigregister(Agent)

class MyAgent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MyAgent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MyAgent, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ssgnc.new_MyAgent(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ssgnc.delete_MyAgent
    __del__ = lambda self : None;
    def next(self): return _ssgnc.MyAgent_next(self)
    def getFreq(self, *args): return _ssgnc.MyAgent_getFreq(self, *args)
    def getToken(self, *args): return _ssgnc.MyAgent_getToken(self, *args)
MyAgent_swigregister = _ssgnc.MyAgent_swigregister
MyAgent_swigregister(MyAgent)



