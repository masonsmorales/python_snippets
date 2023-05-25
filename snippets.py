# Alternative approach for solving something like: var = foo or bar or x or a or b or c
def coalesce(*args):
    """Iterate through args until a value is found, then return it, otherwise return None"""
    return next((arg for arg in args if arg is not None), None)

def update_path():
  """
  Updates the system path with the directory that the current file is in
  Sometimes useful for solving import issues between files that were not built as a module in some cases (e.g. Azure Functions)
  """
  sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
