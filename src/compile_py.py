def compile_py(outpath, commands):

    program = ''

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        if type == 'function-call':
            program += f'{args[0]}({", ".join(args[1:])})\n'
        elif type == 'var-set':
            program += f'{args[1]} = {args[2]}\n'
        elif type == 'var-update':
            program += f'{args[0]} = {args[1]}\n'
        elif type == 'comment':
            program += f'# {args[0]}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
