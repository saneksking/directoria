# Программа для подсчета файлов и папок используя определенный путь
import sys
import os


def main():
    user_path = sys.argv
    print(user_path)

    x = user_path[1]

    count_dirs = 0
    count_files = 0

    for path, dirs, files in os.walk(x):
        for d in dirs:
            print(os.path.join(path, d))
            count_dirs += 1
        for f in files:
            print(os.path.join(path, f))
            count_files += 1

    print('-------------------------------')
    print(f'Количества папок: {count_dirs}')
    print(f'Количество файлов: {count_files}')


if __name__ == '__main__':
    main()
