import os
import pandas as pd
import exceptions

class CSV_file:
    desired_order = ["Участники гражданского оборота","Тип операции","Сумма операции","Вид расчета","Место оплаты","Терминал оплаты","Дата оплаты","Время оплаты","Результат операции","Cash-back","Сумма cash-back"]
    desired_types = ['object','object','float','object','object','object','object','object','object','object','float']
    def existence(self, file_name):
        if file_name not in os.listdir():
            print('Файла нет в директории.')
            raise FileNotFoundError

    def check_file(self, file_name):
        try: pd.read_csv(file_name)
        except: raise UnicodeDecodeError

    def check_order(self, file_name):
        df = pd.read_csv(file_name)
        self.columns_name = df.columns
        if self.columns_name == self.desired_order: pass
        else: raise NameError
    
    def check_columns_order(self):
        
        df = pd.read_csv(file_name)
        df_types = list(df.select_dtypes(['object', 'float']).columns)
        for index in range(0, len(self.desired_order)):
            if self.desired_types[index] not in list(df.select_dtypes('object').columns):
                raise 
                

    
    
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.full_check()
        except Exception:
            print('Возникла ошибка: ')
            match Exception.__class__.__name__:
                case "FileNotFoundError": print('Файла нет в директории.')
                case "UnicodeDecodeError": print('Битый файл.')
                case "NameError":
                    print(f'Структура датафрейма НЕ соответствует ожидаемой:\n\r- Названия столбцов не совпадают.\nОжидаемые: {self.desired_order}\nФактические: {self.columns_name}')
        else: print('Чтение датафрейма завершено успешно.')

    def full_check(self):
        self.existence(self.file_name)


    def __del__(self):
        pass

file_name = 'test.csv'

File = CSV_file('test.csv')
    