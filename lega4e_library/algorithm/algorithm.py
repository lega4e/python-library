from typing import Callable, Iterable, Any, List, Optional


def rdc(
  fun: Callable,
  iterable: Iterable,
  start: Any = None,
  letNone: bool = False,
):
  for value in iterable:
    if start is None and not letNone:
      start = value
    else:
      start = fun(start, value)
  return start


def unite(values: Iterable[Any], initial=0):
  return rdc(lambda a, b: a | b, values, initial)


def ibtw(values: List[Any], term: Any) -> List[Any]:
  if len(values) == 0:
    return values
  result = [values[0]]
  for value in values[1:]:
    result.extend([term, value])
  return result


def nn(
  values: Iterable[Any],
  notEmpty: bool = True,
  transform: Callable = lambda v: v,
) -> Optional[List[Any]]:
  result = [transform(v) for v in values if v is not None]
  return None if len(result) == 0 and notEmpty else result


def find_if(predicat: Callable, iterable: Iterable, default=None) -> Any:
  for value in iterable:
    if predicat(value):
      return value
  return default