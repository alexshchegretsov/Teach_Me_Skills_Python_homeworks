"""
Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все четные элементы и сохранить в другой файл.
"""
import json
from random import randint as rd


def matrix_to_json():
    """Function creates a matrix and saves it into a json-file"""
    data_dict = {k: v for k, v in enumerate([[rd(-50, 50) for _ in range(5)] for _ in range(5)])}
    with open('matrix.json', 'w') as file:
        json.dump(data_dict, file, indent=6)


def from_json_to_another_file():
    """Function reads json file - zeroes even numbers of the matrix
    and saves it to another file"""
    with open('matrix.json') as matrix:
        with open('even_to_zero.txt', 'w') as file:
            extract = json.load(matrix)

            for k, v in extract.items():
                for i, num in enumerate(v):
                    if not num % 2:
                        v[i] = 0
                file.writelines(f'{v}\n')

def main():
    matrix_to_json()
    from_json_to_another_file()


if __name__ == "__main__":
    main()
