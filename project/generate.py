import board
import sys


def main():
    if len(sys.argv) != 2:
        print('usage: python generate.py <target_file>')
        exit(1)

    height = board.HEIGHT
    width = board.WIDTH

    filename = sys.argv[1]
    with open(filename, 'w') as f:
        for i in range(height):
            line = str()
            for j in range(width):
                line += '_'
            f.write(line + '\n')
    f.close()
    return 0

if __name__ == '__main__':
    main()