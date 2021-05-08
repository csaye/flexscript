import sys

# get arguments
args = sys.argv

# if no path given
if len(args) < 2:

    # throw error and quit
    print('error: no program given')
    print('usage: ./compile.sh <program.flex>')
    sys.exit()

# get path
path = args[1]

# if path not a .flex file
if not path.endswith('.flex'):

    # throw error and quit
    print('error: not a .flex program')
    print('usage: ./compile.sh <program.flex>')
    sys.exit()

# open program and read lines
file = open(path, 'r')
lines = file.read().splitlines()
file.close()
