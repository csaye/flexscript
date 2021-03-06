import re

skip_types = ['array-create', 'declaration']

def get_vartype(vartype):
    if vartype == 'string': return 'std::string'
    else: return vartype

def get_statement(statement):
    if statement == 'elif': return 'else if'
    else: return statement

def get_function(function, content):
    if function == 'print': return f'std::cout << {content} << std::endl'
    elif function == 'alen' or function == 'slen': return f'std::size({content})'
    else: return f'{function}({content})'

def style_function(match_obj):
    function = match_obj.group(1)
    content = match_obj.group(2)
    return get_function(function, content)

def style_array(match_obj):
    vartype = match_obj.group(1)
    varname = match_obj.group(2)
    return f'{vartype} {varname}[]'

def compile_cpp(outpath, commands):

    program = ''
    spaces = 0

    # get import statements
    for command in commands:
        if command.type == 'function-call' and command.args[0] == 'print':
            program += '#include <iostream>\n\n'
            break

    # for each command
    for command in commands:

        # get command data
        type = command.type
        args = command.args

        # update function names
        args = [
            re.sub('([a-zA-Z][a-zA-Z0-9]*)\s*\((.*)\)', style_function, arg)
            for arg in args
        ]

        # update array variable styling
        # int[] array -> int array[]
        args = [
            re.sub(
                f'([a-zA-Z][a-zA-Z0-9]*)\s*\[\s*\]\s*([a-zA-Z][a-zA-Z0-9]*)',
                style_array,
                arg
            )
            for arg in args
        ]

        # append spacing
        if type == 'bracket-end': program += '    ' * (spaces - 1)
        elif type not in skip_types: program += '    ' * spaces

        if type == 'function-def':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]}({", ".join(args[2:])})'
        elif type == 'function-call':
            function = args[0]
            content = ", ".join(args[1:])
            program += f'{get_function(function, content)};'
        elif type == 'var-create':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]};'
        elif type == 'var-set':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]} = {args[2]};'
        elif type == 'var-update': program += f'{" ".join(args)};'
        elif type == 'array-set':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]}[] = {{ {", ".join(args[2:])} }};'
        elif type == 'array-update':
            vartype = get_vartype(args[1])
            program += f'{vartype} {args[0]}[] = {{ {", ".join(args[2:])} }};'
        elif type == 'array-index-update': program += f'{args[0]}[{args[1]}] = {args[2]};'
        elif type == 'comment': program += f'// {args[0]}'
        elif type == 'declaration':
            if args[0] == 'MAIN':
                program += 'int main()\n'
                program += '{\n'
                spaces += 1
        elif type == 'statement-args':
            statement = get_statement(args[0])
            program += f'{statement} ({args[1]})'
        elif type == 'statement-for':
            program += f'for (int {args[0]} = {args[1]}; {args[0]} < {args[2]}; {args[0]}++)'
        elif type == 'statement-foreach':
            vartype = get_vartype(args[0])
            program += f'for ({vartype} {args[1]} : {args[2]})'
        elif type == 'statement-raw': program += args[0]
        elif type == 'statement-return': program += f'return{args[0]};'
        elif type == 'bracket-start':
            program += '{'
            spaces += 1
        elif type == 'bracket-end':
            program += '}'
            spaces -= 1

        if type not in skip_types: program += '\n' # newline

    # close class
    if spaces > 0: program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
