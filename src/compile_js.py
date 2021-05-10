def get_function(function):
    if function == 'print': return 'console.log'
    else: return function

def compile_js(outpath, commands):

    program = ''
    spaces = 0

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        # append spacing
        if type != 'bracket-end': program += '    ' * spaces
        else: program += '    ' * (spaces - 1)

        if type == 'function-call':
            function = get_function(args[0])
            program += f'{function}({", ".join(args[1:])});'
        elif type == 'var-set': program += f'{args[1]} = {args[2]};'
        elif type == 'var-update': program += f'{" ".join(args)};'
        elif type == 'comment': program += f'// {args[0]}'
        elif type == 'statement-args': program += f'{args[0]} ({args[1]})'
        elif type == 'statement-else': program += 'else'
        elif type == 'bracket-start':
            program += '{'
            spaces += 1
        elif type == 'bracket-end':
            program += '}'
            spaces -= 1

        if type != 'var-create': program += '\n'; # newline

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
