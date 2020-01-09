# _python_notes

## Philosophy

- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts

## Design

- Under the hood everything is a dictionary.
- Extensible
- PEP Python Enhancement Proposal: Community development and envolvement

## Uses

- Linux scripting and administration:
  - Manage log files, interact with file system, or config files, test scripts, launch apps, maganage running processes.

## Python Frameworks and Libraries

- Django
  - Web development
  - Pintrest, Instagram, Mozilla Help, Onion, Nasa
- Flask
  - Web development micro-framework
- TensorFlow
  - Artificial intelligence
- SciPy
  - Scientific computation
- PyQt
  - Cross-platform desktop applications
- PIP
  - Python Package Manager

## Python Emplamentation Proposals PEP

## Python 2 vs 3

- Python 2 EOL (End of life) in 2020
- print "Hello World" -> print("Hello World")
- Use Python 3

## Virtual Environments

- Common to have multiple Python version installed on your computer
- $ pip install virtualenv
- $ virtualenv <env_name>
- $ virtualenv pluralsight # Example
- $ virtualenv --python=python2.7 pluralsight
- keep them in one folder -e.g. /home/pythonbo/venvs
- Virtualenv created in /home/pythonbo/venvs/pluralsight
- $ source /home/pythonbo/venvs/pluralsight/bin/activate
- Prompt (pluralsight) PythonBo $
- $ deactivate

## Create Executable File

- pyinstaller
  - Python package that converts your Python code to a binary executable
  - Crossplatform - .exe for windows and .app file for mac
  - https://github.com/pyinstaller/pyinstaller
  - pip install pyinstaller
  - cd to your dir
  - pyinstaller my_main.py
  - pyinstaller creates build and dist folders
  - dist will have the my_main.exe file
- pyinstaller --onefile my_main.py # onefile flag will put everythin into 1 file

## Create a Setup Wizard

- Inno Setup
  - Windows only
  - Source code does not need to be Python
