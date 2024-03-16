import pyfiglet
from time import sleep

def fancy_text(text):
    return '\033[94;1m' + pyfiglet.figlet_format(text, font='isometric1') +  '\033[=0m'

name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")

output = ["My name is " + name + " and My dream job is " + dream_job + "."]

for line in output:
    fancy_line = fancy_text(line)
    for c in fancy_line:
        print(c, end='', flush=True)
        sleep(0.001)
    print('')