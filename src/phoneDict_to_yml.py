import sys
import getopt


def main():

    inFile  = sys.argv[1]

    if not inFile.lower().endswith('.txt'):
        sys.exit(1)
        print(f'{inFile} is not a `.txt` file')

main()
