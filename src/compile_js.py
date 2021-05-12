import re

skip_types = ['declaration']

def get_statement(statement):
    if statement == 'elif': return 'else if'
    else: return statement

def get_function(function, content):
    if function == 'print': return f'console.log({content})'
    elif function == 'len': return f'{content}.length'
    else: return f'{function}({content})'

def style_function(match_obj):
    function = match_obj.group(1)
    content = match_obj.group(2)
    return get_function(function, content)

def compile_js(outpath, commands):

    program = ''
    spaces = 0

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        # update function names
        args = [
            re.sub('([a-zA-Z][a-zA-Z0-9]*)\s*\((.*)\)', style_function, arg)
            for arg in args
        ]

        # append spacing
        if type == 'bracket-end': program += '    ' * (spaces - 1)
        elif type not in skip_types: program += '    ' * spaces

        if type == 'function-def':
            params = [' '.join(arg.split()[1:]) for arg in args[2:]]
            program += f'function {args[1]}({", ".join(params)})'
        elif type == 'function-call':
            function = args[0]
            content = ", ".join(args[1:])
            program += f'{get_function(function, content)};'
        elif type == 'var-create': f'var {args[1]};'
        elif type == 'var-set': program += f'var {args[1]} = {args[2]};'
        elif type == 'var-update': program += f'{" ".join(args)};'
        elif type == 'array-create': program += f'var {args[1]};'
        elif type == 'array-set': program += f'var {args[1]} = [{", ".join(args[2:])}];'
        elif type == 'array-update': program += f'{args[0]} = [{", ".join(args[2:])}];'
        elif type == 'array-index-update': program += f'{args[0]}[{args[1]}] = {args[2]};'
        elif type == 'comment': program += f'// {args[0]}'
        elif type == 'statement-args':
            statement = get_statement(args[0])
            program += f'{statement} ({args[1]})'
        elif type == 'statement-for':
            program += f'for (var {args[0]} = {args[1]}; {args[0]} < {args[2]}; {args[0]}++)'
        elif type == 'statement-foreach':
            program += f'for (var {args[1]} of {args[2]})'
        elif type == 'statement-raw': program += args[0]
        elif type == 'statement-return': program += f'return{args[0]};'
        elif type == 'bracket-start':
            program += '{'
            spaces += 1
        elif type == 'bracket-end':
            program += '}'
            spaces -= 1

        if type not in skip_types: program += '\n'; # newline

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
