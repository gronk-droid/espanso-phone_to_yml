import sys
import os
import re


def main():
    inFile  = sys.argv[1]
    replacements = {}

    if not inFile.lower().endswith('.txt'):
        sys.exit(1)
        print(f'{inFile} is not a `.txt` file')

    with open(f'{inFile}', 'rt') as file:
        for line in file.readlines():
            replacements[line.strip().split('\t')[0]] = line.strip().split('\t')[1]

    print(replacements)

    with open(f'{sys.argv[2]}.yml', 'wt') as outFile:
        sys.stdout = outFile
        print(f'name: {sys.argv[2]}\nparent: default\n\nmatches:')

        for key, value in replacements.items():
            print(f'  - trigger: \"{key}\"\n    replace: \"{value}\"\n')


main()
