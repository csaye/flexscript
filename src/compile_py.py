import re

skip_types = ['var-create', 'array-create', 'bracket-start', 'bracket-end', 'declaration']

def get_function(function, content):
    if function == 'slen' or function == 'alen': return f'len({content})'
    else: return f'{function}({content})'

def style_function(match_obj):
    function = match_obj.group(1)
    content = match_obj.group(2)
    return get_function(function, content)

def compile_py(outpath, commands):

    program = ''
    spaces = 0

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        # update boolean names
        args = [
            arg if '"' in arg else
            arg.replace('false', 'False').replace('true', 'True')
            for arg in args
        ]

        # update function names
        args = [
            re.sub('([a-zA-Z][a-zA-Z0-9]*)\s*\((.*)\)', style_function, arg)
            for arg in args
        ]

        # append spacing
        if type not in skip_types: program += '    ' * spaces

        if type == 'function-def':
            params = [' '.join(arg.split()[1:]) for arg in args[2:]]
            program += f'def {args[1]}({", ".join(params)}):'
        elif type == 'function-call':
            function = args[0]
            content = ", ".join(args[1:])
            program += get_function(function, content)
        elif type == 'var-set': program += f'{args[1]} = {args[2]}'
        elif type == 'var-update': program += ' '.join(args)
        elif type == 'array-set': program += f'{args[1]} = [{", ".join(args[2:])}]'
        elif type == 'array-update': program += f'{args[0]} = [{", ".join(args[2:])}]'
        elif type == 'array-index-update': program += f'{args[0]}[{args[1]}] = {args[2]}'
        elif type == 'comment': program += f'# {args[0]}'
        elif type == 'statement-args': program += f'{args[0]} {args[1]}:'
        elif type == 'statement-for':
            program += f'for {args[0]} in range({args[1]}, {args[2]}):'
        elif type == 'statement-foreach':
            program += f'for {args[1]} in {args[2]}:'
        elif type == 'statement-raw':
            if args[0] == 'else': program += 'else:'
            else: program += args[0][0:-1]
        elif type == 'statement-return': program += f'return{args[0]}'
        elif type == 'bracket-start': spaces += 1
        elif type == 'bracket-end': spaces -= 1

        if type not in skip_types: program += '\n' # newline

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
