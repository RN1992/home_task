# from dataclasses import dataclass, field, asdict
# import json
# import os.path
#
#
# @dataclass(order=True)
# class Data:
#     color: str
#     doors: int
#     year_of_build: int = field(compare=True)
#
#
# """Из json в инстанс датакласса"""
#
# with open('data.json') as json_file:
#     raw_data = json.load(json_file)
#     print(raw_data)
#
# data1 = Data(**raw_data[0])
# print(data1)
#
# """Из датакласса в json """
#
# to_json = asdict(data1)
# with open('new_data.json', 'w') as json_file:
#     json.dump(to_json, json_file)
#
# """Сравнение инстансов датакласса"""
#
# data2 = Data('red', 4, 2010)
# print(data1 < data2)
#
# """Функция, которая создаёт несколько инстансов и сохраняет их в файл если файла нет или он пустой """
#
#
# def function():
#     data3 = Data('yellow', 4, 1999)
#     data4 = Data('Grey', 2, 2005)
#     if os.path.exists("C:/Users/Dima/PycharmProjects/Homeworks/file.json") and os.stat("file.json").st_size != 0:
#         print('Файл существует и не пуст')
#     else:
#         with open('file.json', 'w') as file:
#             json.dump([asdict(data3), asdict(data4)], file)
#
#
# function()

# [
#   {
#     "color": "white",
#     "doors": "2",
#     "year_of_build": 2020
#   }
# ] 