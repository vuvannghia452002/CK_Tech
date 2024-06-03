import os
import glob


def format(path):
    with open(path, 'r', encoding="utf-8") as file:
        contents = file.read()
    
    
    contents = contents.replace(' ​', ' ')
    contents = contents.replace('\\cite', ' \\cite')



    while "	" in contents:
        contents = contents.replace("	", ' ')

    while ' ,' in contents:
        contents = contents.replace(' ,', ',')
    contents = contents.replace(',', ', ')

    while '  ' in contents:
        contents = contents.replace('  ', ' ')

    while '( ' in contents:
        contents = contents.replace('( ', '(')
    while ' )' in contents:
        contents = contents.replace(' )', ')')
    while '[ ' in contents:
        contents = contents.replace('[ ', '[')
    while ' ]' in contents:
        contents = contents.replace(' ]', ']')
    while '{ ' in contents:
        contents = contents.replace('{ ', '{')
    while ' }' in contents:
        contents = contents.replace(' }', '}')

    contents = '\n'.join(line.strip() for line in contents.split('\n'))
    while "\n\n\n" in contents:
        contents = contents.replace("\n\n\n", "\n\n")
    contents = contents.lstrip('\n')
    contents = contents.rstrip('\n')
    with open(path, 'w', encoding="utf-8") as file:
        file.write(contents)


root = r"C:\Users\vvn20206205\Desktop\CK_Tech\contents\latex"
tex_files = glob.glob(os.path.join(root, "**/*.tex"), recursive=True)
for i in tex_files:
    format(i)
print("Xong")
