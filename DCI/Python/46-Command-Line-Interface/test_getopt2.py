import getopt, sys


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:b:", ["help", "add="])
    except getopt.GetoptError:
        print('test.py -a <value1> -b <value2>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print('test.py -a <value1> -b <value2>')
            sys.exit()
        elif opt in ("-a", "--add"):
            value1 = arg
        elif opt in ("-b", "--add"):
            value2 = arg
    print(f"Sum: {int(value1) + int(value2)}")


if __name__ == "__main__":
    main(sys.argv[1:])