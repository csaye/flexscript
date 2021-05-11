skip_types = ['var-create', 'bracket-start', 'bracket-end', 'declaration']

def compile_py(outpath, commands):

    program = ''
    spaces = 0

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        args = [
            arg if '"' in arg else
            arg.replace('false', 'False').replace('true', 'True')
            for arg in args
        ]

        # append spacing
        if type not in skip_types: program += '    ' * spaces

        if type == 'function-def':
            params = [' '.join(arg.split()[1:]) for arg in args[2:]]
            program += f'def {args[1]}({", ".join(params)}):'
        elif type == 'function-call':
            program += f'{args[0]}({", ".join(args[1:])})'
        elif type == 'var-set': program += f'{args[1]} = {args[2]}'
        elif type == 'var-update': program += ' '.join(args)
        elif type == 'comment': program += f'# {args[0]}'
        elif type == 'statement-args': program += f'{args[0]} {args[1]}:'
        elif type == 'statement-for':
            program += f'for {args[0]} in range({args[1]}, {args[2]}):'
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
