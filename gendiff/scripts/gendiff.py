#!/usr/bin/env python3

import argparse
import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    

# def main():
#     parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.', 
#                                      usage='gendiff [-h] [-f FORMAT] first_file second_file')
#     # parser.add_argument('first_file', help='Path to the first configuration file')
#     # parser.add_argument('second_file', help='Path to the second configuration file')
#     parser.add_argument('first_file', help='first file')
#     parser.add_argument('second_file', help='second file')

#     args = parser.parse_args()

#     # Здесь будет логика сравнения файлов
#     print(f"Сравниваем файлы: {args.first_file} и {args.second_file}")
def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)

    # print('File 1:', data1)
    # print('File 2:', data2)

    # for key, value in data1.items():
    #     for key1, value1 in data2.items():
    #         if key == key1 and value == value1:
    #             print(f"{key}: {value}")
    # for key, value in data1.items():
    #     for key1, value1 in data2.items():
    #         if key != key1 or value != value1:
    #             print(f"- {key}: {value}")
    #             break
    # for key, value in data1.items():
    #     for key1, value1 in data2.items():
    #         if key1 != key or value1 != value:
    #             print(f"+ {key}: {value}")
    #             break
    # def print_diff(data1, data2):
    #     all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    #     for key in all_keys:
    #         val1 = data1.get(key)
    #         val2 = data2.get(key)
    #         if key in data1 and key not in data2:
    #             print(f"- {key}: {val1}")
    #         elif key not in data1 and key in data2:
    #             print(f"+ {key}: {val2}")
    #         elif val1 != val2:
    #             print(f"- {key}: {val1}")
    #             print(f"+ {key}: {val2}")
    #         else:
    #             print(f"  {key}: {val1}")
    # print_diff(data1, data2)
    # def print_diff(data1, data2):
    #     all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    #     new_sort = {}
    #     for key in all_keys:
    #         val1 = data1.get(key)
    #         val2 = data2.get(key)
    #         if key in data1 and key not in data2:
    #             new_sort[key] = val1
    #         elif key not in data1 and key in data2:
    #             new_sort[key] = val2
    #         elif val1 != val2:
    #             new_sort[key] = val1
    #             new_sort[key] = val2
    #         else:
    #             new_sort[key] = val1
    #     # new_sort = list(set(new_sort))
    #     json_format = json.dumps(new_sort)
    #     print(json_format)
    # (print_diff(data1, data2))
    def format_value(val):
        if isinstance(val, bool):
            return str(val).lower()
        elif val is None:
            return 'null'
        elif isinstance(val, str):
            return val
        return val

    def format_stylish(data1, data2):
        all_keys = sorted(set(data1.keys()) | set(data2.keys()))
        lines = []
        for key in all_keys:
            val1 = data1.get(key)
            val2 = data2.get(key)
            if key in data1 and key not in data2:
                lines.append(f"  - {key}: {format_value(val1)}")
            elif key not in data1 and key in data2:
                lines.append(f"  + {key}: {format_value(val2)}")
            elif val1 == val2:
                lines.append(f"    {key}: {format_value(val1)}")
            else:
                lines.append(f"  - {key}: {format_value(val1)}")
                lines.append(f"  + {key}: {format_value(val2)}")
        return "{\n" + "\n".join(lines) + "\n}"
    print(format_stylish(data1, data2))



if __name__ == "__main__":
    main()

json.load(open('file1.json'))
json.load(open('file2.json'))