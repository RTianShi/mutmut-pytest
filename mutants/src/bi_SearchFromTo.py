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
def x_bi_SearchFromTo__mutmut_orig(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_1(elements, key, froom, to):

    low = None
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_2(elements, key, froom, to):

    low = froom
    high = None

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_3(elements, key, froom, to):

    low = froom
    high = to

    while low < high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_4(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = None
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_5(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high) / 2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_6(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low - high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_7(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//3
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_8(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = None

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_9(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal <= key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_10(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = None

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_11(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid - 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_12(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 2

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_13(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal >= key:
                high = mid - 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_14(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = None
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_15(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid + 1
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_16(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 2
            else:
                return mid
    return -(low + 1)
def x_bi_SearchFromTo__mutmut_17(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return +(low + 1)
def x_bi_SearchFromTo__mutmut_18(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low - 1)
def x_bi_SearchFromTo__mutmut_19(elements, key, froom, to):

    low = froom
    high = to

    while low <= high:
        mid = (low + high)//2
        midVal = elements[mid]

        if midVal < key:
            low = mid + 1

        else:
            if midVal > key:
                high = mid - 1
            else:
                return mid
    return -(low + 2)

x_bi_SearchFromTo__mutmut_mutants : ClassVar[MutantDict] = {
'x_bi_SearchFromTo__mutmut_1': x_bi_SearchFromTo__mutmut_1, 
    'x_bi_SearchFromTo__mutmut_2': x_bi_SearchFromTo__mutmut_2, 
    'x_bi_SearchFromTo__mutmut_3': x_bi_SearchFromTo__mutmut_3, 
    'x_bi_SearchFromTo__mutmut_4': x_bi_SearchFromTo__mutmut_4, 
    'x_bi_SearchFromTo__mutmut_5': x_bi_SearchFromTo__mutmut_5, 
    'x_bi_SearchFromTo__mutmut_6': x_bi_SearchFromTo__mutmut_6, 
    'x_bi_SearchFromTo__mutmut_7': x_bi_SearchFromTo__mutmut_7, 
    'x_bi_SearchFromTo__mutmut_8': x_bi_SearchFromTo__mutmut_8, 
    'x_bi_SearchFromTo__mutmut_9': x_bi_SearchFromTo__mutmut_9, 
    'x_bi_SearchFromTo__mutmut_10': x_bi_SearchFromTo__mutmut_10, 
    'x_bi_SearchFromTo__mutmut_11': x_bi_SearchFromTo__mutmut_11, 
    'x_bi_SearchFromTo__mutmut_12': x_bi_SearchFromTo__mutmut_12, 
    'x_bi_SearchFromTo__mutmut_13': x_bi_SearchFromTo__mutmut_13, 
    'x_bi_SearchFromTo__mutmut_14': x_bi_SearchFromTo__mutmut_14, 
    'x_bi_SearchFromTo__mutmut_15': x_bi_SearchFromTo__mutmut_15, 
    'x_bi_SearchFromTo__mutmut_16': x_bi_SearchFromTo__mutmut_16, 
    'x_bi_SearchFromTo__mutmut_17': x_bi_SearchFromTo__mutmut_17, 
    'x_bi_SearchFromTo__mutmut_18': x_bi_SearchFromTo__mutmut_18, 
    'x_bi_SearchFromTo__mutmut_19': x_bi_SearchFromTo__mutmut_19
}

def bi_SearchFromTo(*args, **kwargs):
    result = _mutmut_trampoline(x_bi_SearchFromTo__mutmut_orig, x_bi_SearchFromTo__mutmut_mutants, args, kwargs)
    return result 

bi_SearchFromTo.__signature__ = _mutmut_signature(x_bi_SearchFromTo__mutmut_orig)
x_bi_SearchFromTo__mutmut_orig.__name__ = 'x_bi_SearchFromTo'

