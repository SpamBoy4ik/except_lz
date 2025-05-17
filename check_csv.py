import pandas as pd

class CSV_file:
    def check_columns_order(self, file):
        template = pd.read_csv('template.csv')
        self.template_columns_names = template.columns.to_list()
        self.file_columns_names = file.columns.to_list()
        for index in range(0, len(self.file_columns_names)):
            if self.file_columns_names[index] != self.template_columns_names[index]:
                print('Названия столбцов не совпадают.')
                print(f'Ожидаемые: {self.template_columns_names}\nФактические: {self.file_columns_names}')
                raise NameError
    
    def check_columns_types(self, file):
        template = pd.read_csv('template.csv')
        self.template_columns_types = template.dtypes.to_list()
        self.file_columns_types = file.dtypes.to_list()
        flag_bad = 0
        for index in range(0, len(self.template_columns_types)):
            if self.template_columns_types[index] != self.file_columns_types[index]:
                print(f'В столбике "{self.file_columns_names[index]}" неверный тип данных.')
                print(f'Ожидается: {self.template_columns_types[index]}, Фактический: {self.file_columns_types[index]}')
                flag_bad = 1
        if flag_bad: raise TypeError
        
    def full_check(self):
        try:
            file = pd.read_csv(self.file_name)
        except FileNotFoundError: print('Файла нет в директории.')
        except UnicodeDecodeError: print('Битый файл.')
        except pd.errors.EmptyDataError: print('Файл пустой.')
        except: print('Непредусмотренная ошибка!!!')
        else:
            try:
                self.check_columns_order(file)
                self.check_columns_types(file)
            except NameError: pass
            except TypeError: pass
            except: print('Непредусмотренная ошибка!!!')
            else:
                print('Чтение датафрейма завершено успешно.')


    def __init__(self, file_name):
        self.file_name = file_name
        self.full_check()

    def __del__(self):
        pass
