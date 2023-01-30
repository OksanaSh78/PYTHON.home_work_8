data = []

path = 'home_work_8\data.txt'

def load_file(file_name='data.txt'):
    global data
    with open(file_name, 'r') as f:
        data = f.read()


def enter_data(input_data):
    global data
    data = input_data


def get_data():
    global data
    return data


def prepare_data():
    global data
    data = data.replace(' ', '')
    for sym in '+-*/':
        data = data.replace(sym, ' ' + sym + ' ')


def calculate():
    prepare_data()
    global data
    example = list(data.split())
    while len(example) > 1:
        while '*' in example or '/' in example:
            i = 0
            while i < len(example):
                if example[i] == '*':
                    example[i-1] = int(example[i - 1]) * int(example[i + 1])
                    example.pop(i)                                  # pop – УДАЛЕНИЕ
                    example.pop(i)
                elif example[i] == '/':
                    example[i-1] = int(example[i - 1]) / int(example[i + 1])
                    example.pop(i)                                  
                    example.pop(i)
                i += 1
        while '+' in example or '-' in example:
            i = 0
            while i < len(example):
                if example[i] == '+':
                    example[i-1] = int(example[i - 1]) + int(example[i + 1])
                    example.pop(i)                                  
                    example.pop(i)
                elif example[i] == '-':
                    example[i-1] = int(example[i - 1]) - int(example[i + 1])
                    example.pop(i)                                  
                    example.pop(i)
                i += 1
        return example





