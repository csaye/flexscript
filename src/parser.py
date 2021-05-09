import re

# regex
ws = '\s*' # optional whitespace
name = '[a-zA-Z][a-zA-Z0-9]*' # variable name
any0 = '.*' # optional any character
any1 = '.+' # any character

actions = {
    f'{name}{ws}\({any0}\){ws};': 'function-call',
    f'{name}{ws}{name}{ws}={ws}{any1}{ws};': 'var-set',
    f'{name}{ws}={ws}{any1}{ws};': 'var-update',
    f'#{any0}\n': 'comment'
}

# command class
class Command:

    def __init__(self, type, args):
        self.type = type
        self.args = args

    type = ''
    args = []

# splits a string by given chars, keeping string literals together
def split(string, chars):

    in_string = False
    double_quote = False
    term = ''
    terms = []
    i = 0

    for char in string: # for each character

        # toggle in string
        if in_string:
            if ((char == '"' and double_quote)
            or (char == "'" and not double_quote)):
                in_string = False
        else:
            if char == '"' or char == "'":
                double_quote = char == '"'
                in_string = True

        if not in_string: # if not in string
            if char not in chars: term += char # append if not split char
            elif term != '': # if split char and term exists
                terms.append(term) # append term
                term = '' # clear term
        else: term += char # if in string, append char

        if i == len(string) - 1 and term != '': # if end of string
            terms.append(term) # append term

        i += 1 # increment index

    return terms

# returns list of arguments for given command type
def get_args(type, string):

    args = []

    if type == 'function-call':
        sides = split(string, '();') # get out and in of function
        args.append(sides[0].strip()) # append function name
        terms = split(sides[1], ',') # split inside
        for term in terms: args.append(term.strip()) # append stripped terms
    elif type == 'var-set':
        sides = split(string, '=;') # get both sides of assignment
        args = split(sides[0], ' ') # split left side by space
        args.append(sides[1].strip()) # append end term
    elif type == 'var-update':
        sides = split(string, '=;') # get both sides of assignment
        args = [side.strip() for side in sides] # strip args
    elif type == 'comment':
        content = string[1:].strip() # get comment content
        args.append(content) # append content

    return args

# returns given flex program parsed into commands
def parse(program):

    commands = []

    # for each character in program
    in_string = False
    string = ''
    for char in program:

        # toggle in string
        if char == '"': in_string = not in_string

        string += char # build string
        clean_string = string.strip() # strip string

        # for each action
        for action in actions:

            # if string matches action
            if re.match(f'{ws}{action}{ws}', string):

                type = actions[action] # get command type
                args = get_args(type, clean_string) # get command arguments

                command = Command(type, args) # create command
                commands.append(command) # append command
                string = '' # reset string

                break # do not take any other actions

        # if semicolon on invalid statement
        if not in_string and char == ';' and string != '':

            # throw error and return
            print('error: unrecognized statement')
            print(clean_string)
            return

        # if newline
        if string.endswith('\n\n'):

            # append newline command
            command = Command('newline', [])
            commands.append(command)

    return commands
