import os
import subprocess

name_system = os.name
program = ''
if name_system == 'nt':
    program = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    if not os.path.isfile(program):
        print('Программа не нашлась')
        program = ''
        
if name_system == 'posix':
    program = 'google-chrome'

if not program:
    print('Программа не нашлась')
print(program)


subprocess.run(program)