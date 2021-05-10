# imports
import sys, os
from compile_py import compile_py
from compile_js import compile_js
from compile_cs import compile_cs
from compile_java import compile_java
from compile_cpp import compile_cpp
from parser import parse

# returns whether file exists at given path
def file_exists(path): return os.path.exists(path)

# available flex compilers
compilers = {
  'py': compile_py,
  'js': compile_js,
  'cs': compile_cs,
  'java': compile_java,
  'cpp': compile_cpp
}

# get arguments
args = sys.argv

# if no path given
if len(args) < 2:

    # throw error and quit
    print('error: no program given')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)} | all>')
    sys.exit()

# get program path
path = args[1]

# if path not a .flex file
if not path.endswith('.flex') or not file_exists(path):

    # throw error and quit
    print(f'error: {path} is not a valid .flex program')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)} | all>')
    sys.exit()

# if no output type given
if len(args) < 3:

    # throw error and quit
    print('error: no output type given')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)} | all>')
    sys.exit()

# get output type
output = args[2]

# if output type invalid
if output not in compilers and output != 'all':

    # throw error and quit
    print(f'error: {output} is not a valid output type')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)} | all>')
    sys.exit()

# open file and read program
file = open(path, 'r')
program = file.read()
file.close()

commands = parse(program) # parse commands
if commands == None: sys.exit() # if could not parse, exit

for command in commands: print(f'{command.type} {command.args}') # debug

if output == 'all': # compile all
    for out in compilers: # for each compiler
        outpath = f'{path[:-5]}.{out}' # get program outpath
        compilers[out](outpath, commands) # compile commands to outpath
else: # compile one
    outpath = f'{path[:-5]}.{output}' # get program outpath
    compilers[output](outpath, commands) # compile commands to outpath
