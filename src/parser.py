actions = {
    '[a-zA-Z][a-zA-Z0-9]*\s*\(.*\)\s*;': 'function-call',
    '[a-zA-Z][a-zA-Z0-9]*\s*=\s*.+\s*;': 'var-assign'
}

class Command:

    def __init__(self, type, args):
        self.type = type
        self.args = args

    type = ''
    args = []

# splits a string by given chars, keeping string literals together
def split(string, chars):

    in_string = False
    term = ''
    terms = []
    i = 0

    for char in string: # for each character

        if char == '"': in_string = not in_string # toggle in string

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

    if (type == 'function-call'):
        sides = split(string, '();') # get out and in of function
        args.append(sides[0].strip()) # append function name
        terms = split(sides[1], ',') # split inside
        for term in terms: args.append(term.strip()) # append stripped terms
    elif (type == 'var-assign'):
        sides = split(string, '=;') # get both sides of assignment
        args = [side.strip() for side in sides] # strip args

    return args

# returns given flex program parsed into commands
def parse(program):

    commands = []

    return commands
