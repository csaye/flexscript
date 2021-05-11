import re

# regex
s0 = '\s*' # optional whitespace
s1 = '\s+' # whitespace
name = '[a-zA-Z][a-zA-Z0-9]*' # variable name
any0 = '.*' # optional any character
any1 = '.+' # any character
modo = '(=|\+=|-=|\*=|\/=|%=)' # modification operators

actions = {
    f'return{any0};': 'statement-return',
    f'{name}{s1}{name}{s0}\({any0}\){s0}\n': 'function-def',
    f'{name}{s0}\({any0}\){s0};': 'function-call',
    f'{name}{s1}{name}{s0};': 'var-create',
    f'{name}{s1}{name}{s0}={any1};': 'var-set',
    f'{name}{s0}{modo}{any1};': 'var-update',
    f'(#|#[^_]{any0})\n': 'comment',
    f'#_{any0}\n': 'declaration',
    f'(if|elif|while){s0}\({any1}\)': 'statement-args',
    f'for{s0}\(int{s1}{name}{s0}={s0}{any1}{s0};{s0}{name}{s0}<{s0}{any1}{s0};{s0}{name}\+\+{s0}\)': 'statement-for',
    '(else|continue;|break;)': 'statement-raw',
    '{': 'bracket-start',
    '}': 'bracket-end'
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

    if type == 'function-def':
        string = string.strip() # strip string
        sides = split(string, '()') # separate sides
        args = split(sides[0].strip(), ' ') # append function type and name
        if len(sides) > 1:
            terms = split(sides[1], ',') # split inside
            for term in terms: args.append(term.strip()) # append stripped terms
    elif type == 'function-call':
        sides = split(string, '();') # get out and in of function
        args.append(sides[0].strip()) # append function name
        if len(sides) > 1:
            terms = split(sides[1], ',') # split inside
            for term in terms: args.append(term.strip()) # append stripped terms
    elif type == 'var-create':
        args = split(string, '; ') # split terms by semicolon and whitespace
    elif type == 'var-set':
        sides = split(string, '=;') # get both sides of assignment
        args = split(sides[0], ' ') # split left side by space
        args.append(sides[1].strip()) # append end term
    elif type == 'var-update':
        op = split(string, ' ')[1] # get operator
        sides = split(string, ';=+-*/%') # get both sides of assignment
        args.append(sides[0].strip()) # strip left side
        args.append(op) # append operator
        args.append(sides[1].strip()) # strip right side
    elif type == 'comment':
        content = string[1:].strip() # get comment content
        args.append(content) # append content
    elif type == 'declaration':
        content = string[2:].strip() # get declaration content
        args.append(content) # append content
    elif type == 'statement-args':
        sides = split(string, '();') # separate statement from content
        args = [side.strip() for side in sides] # strip sides
    elif type == 'statement-for':
        sides = split(string, '()') # split for from content
        content = sides[1].strip() # get content
        varname = split(content, ' ')[1] # get varname
        args.append(varname) # append varname
        terms = split(content, '=<; ') # split inside
        args.append(terms[2]) # append lower bound
        args.append(terms[4]) # append upper bound
    elif type == 'statement-raw':
        args.append(string.strip()) # append stripped statement
    elif type == 'statement-return':
        content = string[6:-1].rstrip() # strip content on right
        args.append(content) # append content

    return args

# returns given flex program parsed into commands
def parse(program):

    commands = []

    # for each character in program
    in_string = False
    double_quote = False
    in_comment = False
    string = ''
    for char in program:

        # toggle in string
        if in_string:
            if ((char == '"' and double_quote)
            or (char == "'" and not double_quote)):
                in_string = False
        else:
            if char == '"' or char == "'":
                double_quote = char == '"'
                in_string = True

        string += char # build string
        if in_string: continue # skip if in string
        clean_string = string.strip() # strip string

        # for each action
        for action in actions:

            # if string matches action
            if re.match(f'^{s0}{action}{s0}$', string):

                type = actions[action] # get command type
                args = get_args(type, clean_string) # get command arguments

                command = Command(type, args) # create command
                commands.append(command) # append command
                string = '' # reset string

                break # do not take any other actions

        # if newline
        if string.endswith('\n\n'):

            # append newline command
            command = Command('newline', [])
            commands.append(command)

    return commands
