def input_data(message: str) -> int:
    data = int(input(message))
    return data


def enter_line(message: str) -> int:
    data = input(message)
    return data


def show_results(calculation, results):

    print(f'{calculation} = {results}')
