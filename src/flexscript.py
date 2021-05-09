# imports
import sys, os
from compile_py import compile_py
from compile_js import compile_js
from parser import parse

# returns whether file exists at given path
def file_exists(path): return os.path.exists(path)

# return base nae of file at path
def file_name(path): return os.path.basename(path)

# available flex compilers
compilers = {
  'py': compile_py,
  'js': compile_js
}

# get arguments
args = sys.argv

# if no path given
if len(args) < 2:

    # throw error and quit
    print('error: no program given')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)}>')
    sys.exit()

# get program path
path = args[1]

# if path not a .flex file
if not path.endswith('.flex') or not file_exists(path):

    # throw error and quit
    print(f'error: {path} is not a valid .flex program')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)}>')
    sys.exit()

# if no output type given
if len(args) < 3:

    # throw error and quit
    print('error: no output type given')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)}>')
    sys.exit()

# get output type
output = args[2]

# if output type invalid
if output not in compilers:

    # throw error and quit
    print(f'error: {output} is not a valid output type')
    print(f'usage: ./compile.sh <program.flex> <{" | ".join(compilers)}>')
    sys.exit()

# open file and read program
file = open(path, 'r')
program = file.read()
file.close()

commands = parse(program) # parse commands
if not commands: sys.exit() # if could not parse, exit
outpath = f'{path[:-5]}.{output}' # get program outpath
compilers[output](outpath, commands) # compile commands to outpath
