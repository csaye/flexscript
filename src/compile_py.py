def compile_py(outpath, commands):

    program = ''

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        if type == 'function-call':
            program += f'{args[0]}({", ".join(args[1:])})\n'
        elif type == 'var-assign':
            program += f'{args[0]} = {args[1]}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
