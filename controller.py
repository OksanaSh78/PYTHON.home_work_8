import view
import model

menu = ['Загрузить из файла выражение',
        'Ввести выражение',
        'Посчитать',
        'Выход']


def main_menu():
    while True:
        for i, line in enumerate(menu, 1):
            print(f"{i}. {line}")
        choice = 0
        while not (1 <= choice <= 4):
            choice = view.input_data('Выберите пункт меню 2-4:  ')

        match choice:
            case 1:
                model.load_file()
                model.prepare_data()
            case 2:
                calculaton = view.enter_line('Введите выражение:  ')
                model.enter_data(calculaton)
                model.prepare_data()
            case 3:
                calculation = model.calculate()
                data = model.get_data()
                view.show_results(data, calculation[0])
            case 4:
                break

