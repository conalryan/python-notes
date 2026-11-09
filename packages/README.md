# Packages
Package is a folder containing related modules or subpackages
The grouping is physical, it's a folder that contains one or more modules.
It's a way of giving a hierarchical structure to the module namespace so that all modules do not live in the same folder
Packages can be nested
__init__.py
    Optional
    Initialization script that is executed when the package or any of its contents are loaded
    Setup data or other resources that will be used by multiple modules within a package
    Required for a regular package; omitted only for deliberate namespace packages.
    Configure import
        Load modules into package's namespace
        Specify modules to loade when * is used
        For convenience you can put import statements in a package's __init__py to autoload the modules into the package namespace
        This will enable to import <some-package> imports all/or just selected modules in the package
        __all__
            If variable is present in __init__.py and set to a list of module names, then only these modules will be loaded when the import is from <some-package> import *
Modules in packages are accessed by prefixing the module with the package name
    Package spam
        Module eggs
            Function scramble
    spam.eggs.scramble()
Importing a regular package executes its __init__.py once; submodules are not
automatically loaded unless that initializer imports them. Keep initializers light.
Usually import the module using the package name
    from spam import eggs
Documenting
    Use docstrings
    Described in PEP 257
    Generate docs with Sphinx (optional)
        Gather docstrings from an entire application and format them as a single HTML, PDF, or EPUB document
    In addition to comments, which are for the maintainer of your code, you should add docstrings, which provide documentation for the user of your code
    If the first statement in a module, function, or class is an unassigned string, it is assigned as the docstring of that object
    It is stored in the special attribute __doc__ so it is available to code
    Can use any form of literal string, but triple double quotes are preferred for consistency

Example
 sound/                     Top-level package
      __init__.py           Initialize the sound package (optional)
      formats/              Subpackage for file formats
          __init__.py           Initialize the formats package (optional)
          wavread.py
          wavwrite.py
          aiffread.py
          aiffwrite.py
          auread.py
          auwrite.py
          ...
      effects/              Subpackage for sound effects
          __init__.py           Initialize the formats package (optional)
          echo.py
          surround.py
          reverse.py
          ...
      filters/              Subpackage for filters
          __init__.py           Initialize the filters package (optional)
          equalizer.py


```python
from sound.formats import aiffread
import sound.effects
import sound.filters.equalizer
```

Given the following package and module layout, the table below describes how __init__.py affects imports

```
my_package
     |------__init__.py
     |------module_a.py
     |         function_a()
     |------module_b.py
     |         function_b()
     |------module_c.py
               function_c()
```


Import statement                    What it does
-------------------------------------------------
If __init__.py is empty
-------------------------------------------------
import my_package                   Executes its initializer and binds the package name; does not automatically load submodules.

import my_package.module_a          Imports module_a into my_package namespace. Objects in module_a must be prefixed with my_package.module_a

from my_package import module_a     Imports module_a into main namespace. Objects in module_a must be prefixed with module_a

from my_package import module_a,    Imports module_a and module_b into main namespace.
module_b

from my_package import *            Binds public names already defined by the initializer unless __all__ controls them.

from my_package.module_a import *   Imports all contents of module_a (that do not start with an underscore) into main namespace. Not generally recommended.

-------------------------------------------------
If __init__.py contains:
__all__ = ['module_a', 'module_b']
-------------------------------------------------
import my_package                   Executes the initializer; __all__ does not itself eagerly import submodules.

from my_package import module_a     As before, imports module_a into main namespace. Objects in module_a must be prefixed with module_a

from my_package import *            Imports module_a and module_b, but not module_c into main namespace.

-------------------------------------------------
If __init__.py contains:
__all__ = ['module_a', 'module_b']
from . import module_a
from . import module_b
-------------------------------------------------
import my_package                   Imports module_a and module_b into the my_package namespace. Objects in module_a must be prefixed with my_package.module_a. Now this is useful.

from my_package import module_a     Imports module_a into main namespace. Objects in module_a must be prefixed with module_a

from my_package import *            Only imports module_a and module_b into main namespace.

from my_package import module_c     Imports module_c into the main namespace.

## Current Packaging

Declare build metadata and optional dependencies in `pyproject.toml`, build wheels
through a PEP 517 backend, and install into an isolated environment. These notes
use Hatchling; the Rust extension uses maturin. `uv.lock` records the resolved
environment, while wheel metadata declares compatible dependency ranges.

Prefer explicit imports and `python -m package.module` entry points. Namespace
packages are for deliberately distributed namespaces, not a reason to remove every
initializer. `__all__` describes a public wildcard-import surface; it is not access
control. Avoid eager imports that load ML models, initialize devices, or start servers.
