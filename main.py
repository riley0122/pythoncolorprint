#to use this in your own project copy this class to your file 
#you can (if you want) change the class name by changing colors to the name you want but make sure to keep the :
class colors:
    #aslo you can change the names of the colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #if you change the name make sure to also change ENDC down at print
    ENDC = '\033[0m'
    #you can change the function name from classname.printc() to for example classname.helloworld()
    def printc(text, color):
      #if you changed ENDC make sure to also change this 
      print(f'{color}{text}{colors.ENDC}')
#to use type colors.printc(text, color)
#or if you changed the class name classname.fuctionname(text, color)

#for example
colors.printc("hello world", colors.OKBLUE)
