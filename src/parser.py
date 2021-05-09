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

# returns given flex program parsed into commands
def parse(program):

    commands = []

    return commands
