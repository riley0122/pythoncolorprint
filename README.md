# pythoncolorprint

this is a simple script that makes it easy to print in color

## Installation

copy and paste the class in your project
```python
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def printc(text, color):
      print(f'{color}{text}{colors.ENDC}')
```

## Usage
default
```python
classname.printc("WARNING: 1 + 1 isn't 3", colors.WARNING)
```
custom
```python
classname.functionname("WARNING: 1 + 1 isn't 3", classname.Colorname)
```
## Customize
you can change all the names used for more information [open main.py](main.py)

## License
[MIT](https://choosealicense.com/licenses/mit/)
