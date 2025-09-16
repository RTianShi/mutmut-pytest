from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
def x_add_values__mutmut_orig(data):
    sum = 0
    for i in data:
        sum += i
    return sum
def x_add_values__mutmut_1(data):
    sum = None
    for i in data:
        sum += i
    return sum
def x_add_values__mutmut_2(data):
    sum = 1
    for i in data:
        sum += i
    return sum
def x_add_values__mutmut_3(data):
    sum = 0
    for i in data:
        sum = i
    return sum
def x_add_values__mutmut_4(data):
    sum = 0
    for i in data:
        sum -= i
    return sum

x_add_values__mutmut_mutants : ClassVar[MutantDict] = {
'x_add_values__mutmut_1': x_add_values__mutmut_1, 
    'x_add_values__mutmut_2': x_add_values__mutmut_2, 
    'x_add_values__mutmut_3': x_add_values__mutmut_3, 
    'x_add_values__mutmut_4': x_add_values__mutmut_4
}

def add_values(*args, **kwargs):
    result = _mutmut_trampoline(x_add_values__mutmut_orig, x_add_values__mutmut_mutants, args, kwargs)
    return result 

add_values.__signature__ = _mutmut_signature(x_add_values__mutmut_orig)
x_add_values__mutmut_orig.__name__ = 'x_add_values'
