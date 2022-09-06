from datetime import datetime
import os


# начало конструктора

def get_log_constructor(file_name, file_path=None):
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    # начало декоратора

    def get_log(func):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            func_name = func.__name__
            result = list(func(*args, **kwargs))
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return foo
    return get_log


