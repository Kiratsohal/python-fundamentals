# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'



def colour_text(text:str,effect:str)->None:
    output="{0}{1}{2}".format(effect,text,RESET)
    print(output)
colour_text("this is a test",RED)
colour_text("this is a test",YELLOW)
colour_text("this is a test",BLUE)
colour_text("this is a test",CYAN)

