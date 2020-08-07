
"""
Utilities for type hints not provided by the #typing module.
"""

__all__ = [
  'type_repr',
]


def _type_repr(obj):
  # Borrowed from typing in CPython 3.7
  if isinstance(obj, type):
      if obj.__module__ == 'builtins':
          return obj.__qualname__
      return f'{obj.__module__}.{obj.__qualname__}'
  if obj is ...:
      return('...')
  if isinstance(obj, types.FunctionType):
      return obj.__name__
  return repr(obj)


try:
  from typing import _type_repr as type_repr
except ImportError:
  type_repr = _type_repr
