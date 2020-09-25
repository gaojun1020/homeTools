import sys
from colorama import init

def printMe(score):
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    
    from termcolor import cprint 
    from pyfiglet import figlet_format

    if score == 100:
        cprint(figlet_format(str(score) + ' !', font='starwars'),
        'yellow', 'on_red', attrs=['bold'])
    elif score >= 90:
        cprint(figlet_format(str(score), font='starwars'),
        'white', 'on_red', attrs=['bold'])
    elif score < 60:
        cprint(figlet_format(str(score), font='starwars'),
        'grey', 'on_white', attrs=['bold'])
    else:
        cprint(figlet_format(str(score), font='starwars'),
        'white', 'on_blue', attrs=['bold'])