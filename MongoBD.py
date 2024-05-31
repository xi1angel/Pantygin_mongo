from pymongo import MongoClient
from datetime import datetime, timedelta
import random

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Pantygin_RGR']

# Внесение данных

# 1. Данные о направлениях
majors = [
    {"Название": "Информатика и информационные технологии"},
    {"Название": "Фундаметальная математика"},
    {"Название": "Физика квантовых систем"}
]

major_ids = db.majors.insert_many(majors).inserted_ids

# 2. Данные о группах
groups = [
    {"Номер группы": "ИН101", "Направление": major_ids[0]},
    {"Номер группы": "ИН102", "Направление": major_ids[0]},
    {"Номер группы": "ИН202", "Направление": major_ids[0]},
    {"Номер группы": "ФМ101", "Направление": major_ids[1]},
    {"Номер группы": "ФМ201", "Направление": major_ids[1]},
    {"Номер группы": "ФМ202", "Направление": major_ids[1]},
    {"Номер группы": "ФКС101", "Направление": major_ids[2]},
    {"Номер группы": "ФКС201", "Направление": major_ids[2]},
    {"Номер группы": "ФКС302", "Направление": major_ids[2]}
]

group_ids = db.groups.insert_many(groups).inserted_ids

# 3. Данные о студентах
import datetime

students = [
    {"ФИО": "Подин Алексей Михайлович", "Дата рождения": datetime(2000, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 1}, "Телефоны": ["+79161234567"], "Email": "podin@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Комаров Иван Андреевич", "Дата рождения": datetime(2001, 7, 19), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 2}, "Телефоны": ["+79161234568"], "Email": "komarov@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Михайлов Андрей Васильевич", "Дата рождения": datetime(2000, 8, 23), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 3}, "Телефоны": ["+79161234569"], "Email": "mikhailov@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Дмитриев Александр Сергеевич", "Дата рождения": datetime(2002, 4, 15), "Адрес": {"Город": "Москва", "Улица": "Садовая", "Дом": 4}, "Телефоны": ["+79161234570"], "Email": "dmitriev@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Петров Сергей Владимирович", "Дата рождения": datetime(2001, 3, 5), "Адрес": {"Город": "Москва", "Улица": "Красная", "Дом": 5}, "Телефоны": ["+79161234571"], "Email": "petrov@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Васильев Владимир Николаевич", "Дата рождения": datetime(1999, 12, 11), "Адрес": {"Город": "Москва", "Улица": "Советская", "Дом": 6}, "Телефоны": ["+79161234572"], "Email": "vasiliev@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Алексеев Николай Михайлович", "Дата рождения": datetime(2000, 11, 22), "Адрес": {"Город": "Москва", "Улица": "Центральная", "Дом": 7}, "Телефоны": ["+79161234573"], "Email": "alekseev@mail.com", "Группа": group_ids[0], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Иванов Валентин Федорович", "Дата рождения": datetime(2000, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 1}, "Телефоны": ["+79161234567"], "Email": "ivanov@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Смирнов Павел Алексеевич", "Дата рождения": datetime(2001, 7, 19), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 2}, "Телефоны": ["+79161234568"], "Email": "smirnov@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Федоров Илья Владимирович", "Дата рождения": datetime(2000, 8, 23), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 3}, "Телефоны": ["+79161234569"], "Email": "fedorov@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Козлов Павел Станиславович", "Дата рождения": datetime(2000, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 1}, "Телефоны": ["+79161234567"], "Email": "kozlov@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Николаев Максим Петрович", "Дата рождения": datetime(2001, 7, 19), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 2}, "Телефоны": ["+79161234568"], "Email": "nikolaev@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Кузьмин Даниил Дмитриевич", "Дата рождения": datetime(2000, 8, 23), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 3}, "Телефоны": ["+79161234569"], "Email": "kuzmin@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Жуков Игорь Александрович", "Дата рождения": datetime(2002, 4, 15), "Адрес": {"Город": "Москва", "Улица": "Садовая", "Дом": 4}, "Телефоны": ["+79161234570"], "Email": "zhukov@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Петров Илья Игоревич", "Дата рождения": datetime(2000, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 1}, "Телефоны": ["+79161234567"], "Email": "petrov_ilya@mail.com", "Группа": group_ids[1], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Сидоров Игорь Сергеевич", "Дата рождения": datetime(2001, 7, 19), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 2}, "Телефоны": ["+79161234568"], "Email": "sidorov_igor@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Васильев Федор Алексеевич", "Дата рождения": datetime(2000, 8, 23), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 3}, "Телефоны": ["+79161234569"], "Email": "vasiliev_fedor@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Алексеев Павел Владимирович", "Дата рождения": datetime(2002, 4, 15), "Адрес": {"Город": "Москва", "Улица": "Садовая", "Дом": 4}, "Телефоны": ["+79161234570"], "Email": "alekseev_pavel@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Михайлов Иван Дмитриевич", "Дата рождения": datetime(2001, 3, 5), "Адрес": {"Город": "Москва", "Улица": "Красная", "Дом": 5}, "Телефоны": ["+79161234571"], "Email": "mikhailov_ivan@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Иванов Андрей Петрович", "Дата рождения": datetime(1999, 12, 11), "Адрес": {"Город": "Москва", "Улица": "Советская", "Дом": 6}, "Телефоны": ["+79161234572"], "Email": "ivanov_andrey@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": False},
    {"ФИО": "Попов Максим Васильевич", "Дата рождения": datetime(2000, 11, 22), "Адрес": {"Город": "Москва", "Улица": "Центральная", "Дом": 7}, "Телефоны": ["+79161234573"], "Email": "popov_maxim@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Смирнов Артем Николаевич", "Дата рождения": datetime(2000, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 1}, "Телефоны": ["+79161234567"], "Email": "smirnov_artem@mail.com", "Группа": group_ids[2], "Направление": major_ids[0], "Бюджет": True},
    {"ФИО": "Петров Илья Васильевич", "Дата рождения": datetime(2001, 7, 19), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 2}, "Телефоны": ["+79161234568"], "Email": "petrov_ilya2@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Сидоров Игорь Валентинович", "Дата рождения": datetime(2000, 8, 23), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 3}, "Телефоны": ["+79161234569"], "Email": "sidorov_igor2@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Васильев Федор Иванович", "Дата рождения": datetime(2002, 4, 15), "Адрес": {"Город": "Москва", "Улица": "Садовая", "Дом": 4}, "Телефоны": ["+79161234570"], "Email": "vasiliev_fedor2@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Андреев Виктор Сергеевич", "Дата рождения": datetime(2001, 3, 17), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 8}, "Телефоны": ["+79161234574"], "Email": "andreev_victor@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Дмитриев Алексей Иванович", "Дата рождения": datetime(2002, 6, 25), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 9}, "Телефоны": ["+79161234575"], "Email": "dmitriev_alexey@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Куликов Денис Сергеевич", "Дата рождения": datetime(2000, 2, 14), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 10}, "Телефоны": ["+79161234576"], "Email": "kulikov_denis@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Романов Петр Андреевич", "Дата рождения": datetime(2001, 11, 23), "Адрес": {"Город": "Москва", "Улица": "Садовая", "Дом": 11}, "Телефоны": ["+79161234577"], "Email": "romanov_petr@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Федоров Сергей Михайлович", "Дата рождения": datetime(2002, 1, 15), "Адрес": {"Город": "Москва", "Улица": "Красная", "Дом": 12}, "Телефоны": ["+79161234578"], "Email": "fedorov_sergey@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Егоров Павел Анатольевич", "Дата рождения": datetime(1999, 8, 7), "Адрес": {"Город": "Москва", "Улица": "Советская", "Дом": 13}, "Телефоны": ["+79161234579"], "Email": "egorov_pavel@mail.com", "Группа": group_ids[3], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Мартынов Виктор Павлович", "Дата рождения": datetime(2000, 12, 29), "Адрес": {"Город": "Москва", "Улица": "Центральная", "Дом": 14}, "Телефоны": ["+79161234580"], "Email": "martynov_victor@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Богданов Кирилл Алексеевич", "Дата рождения": datetime(2001, 5, 11), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 15}, "Телефоны": ["+79161234581"], "Email": "bogdanov_kirill@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Ильин Артем Игоревич", "Дата рождения": datetime(2002, 9, 16), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 16}, "Телефоны": ["+79161234582"], "Email": "ilin_artem@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Гаврилов Максим Анатольевич", "Дата рождения": datetime(2000, 10, 20), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 17}, "Телефоны": ["+79161234583"], "Email": "gavrilov_maxim@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Смирнов Илья Александрович", "Дата рождения": datetime(2001, 4, 12), "Адрес": {"Город": "Москва", "Улица": "Тверская", "Дом": 18}, "Телефоны": ["+79161234584"], "Email": "smirnov_ilya@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Чернов Алексей Павлович", "Дата рождения": datetime(2002, 6, 8), "Адрес": {"Город": "Москва", "Улица": "Новая", "Дом": 19}, "Телефоны": ["+79161234585"], "Email": "chernov_alexey@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Яковлев Денис Владимирович", "Дата рождения": datetime(2000, 2, 19), "Адрес": {"Город": "Москва", "Улица": "Восточная", "Дом": 20}, "Телефоны": ["+79161234586"], "Email": "yakovlev_denis@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Захаров Михаил Сергеевич", "Дата рождения": datetime(2001, 7, 25), "Адрес": {"Город": "Москва", "Улица": "Западная", "Дом": 21}, "Телефоны": ["+79161234587"], "Email": "zaharov_mikhail@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Николаев Павел Андреевич", "Дата рождения": datetime(2002, 1, 5), "Адрес": {"Город": "Москва", "Улица": "Южная", "Дом": 22}, "Телефоны": ["+79161234588"], "Email": "nikolaev_pavel@mail.com", "Группа": group_ids[4], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Орлов Игорь Иванович", "Дата рождения": datetime(1999, 9, 17), "Адрес": {"Город": "Москва", "Улица": "Северная", "Дом": 23}, "Телефоны": ["+79161234589"], "Email": "orlov_igor@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Лебедев Сергей Павлович", "Дата рождения": datetime(2000, 11, 11), "Адрес": {"Город": "Москва", "Улица": "Центральная", "Дом": 24}, "Телефоны": ["+79161234590"], "Email": "lebedev_sergey@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Фролов Дмитрий Алексеевич", "Дата рождения": datetime(2001, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Красная", "Дом": 25}, "Телефоны": ["+79161234591"], "Email": "frolov_dmitry@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Макаров Андрей Владимирович", "Дата рождения": datetime(2002, 8, 30), "Адрес": {"Город": "Москва", "Улица": "Мира", "Дом": 26}, "Телефоны": ["+79161234592"], "Email": "makarov_andrey@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Тарасов Юрий Александрович", "Дата рождения": datetime(2000, 10, 22), "Адрес": {"Город": "Москва", "Улица": "Советская", "Дом": 27}, "Телефоны": ["+79161234593"], "Email": "tarasov_yuriy@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Киселев Алексей Михайлович", "Дата рождения": datetime(2001, 3, 12), "Адрес": {"Город": "Москва", "Улица": "Октябрьская", "Дом": 28}, "Телефоны": ["+79161234594"], "Email": "kiselev_alexey@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Сафонов Андрей Вячеславович", "Дата рождения": datetime(2002, 5, 16), "Адрес": {"Город": "Москва", "Улица": "Ленина", "Дом": 29}, "Телефоны": ["+79161234595"], "Email": "safonov_andrey@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Романов Игорь Дмитриевич", "Дата рождения": datetime(2000, 12, 3), "Адрес": {"Город": "Москва", "Улица": "Пушкина", "Дом": 30}, "Телефоны": ["+79161234596"], "Email": "romanov_igor@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": True},
    {"ФИО": "Белов Юрий Сергеевич", "Дата рождения": datetime(2001, 7, 22), "Адрес": {"Город": "Москва", "Улица": "Кирова", "Дом": 31}, "Телефоны": ["+79161234597"], "Email": "belov_yuriy@mail.com", "Группа": group_ids[5], "Направление": major_ids[1], "Бюджет": False},
    {"ФИО": "Федоров Алексей Иванович", "Дата рождения": datetime(2002, 9, 19), "Адрес": {"Город": "Москва", "Улица": "Гагарина", "Дом": 32}, "Телефоны": ["+79161234598"], "Email": "fedorov_alexey@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Воронов Денис Владимирович", "Дата рождения": datetime(1999, 10, 25), "Адрес": {"Город": "Москва", "Улица": "Советская", "Дом": 33}, "Телефоны": ["+79161234599"], "Email": "voronov_denis@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Павлов Михаил Петрович", "Дата рождения": datetime(2000, 1, 18), "Адрес": {"Город": "Москва", "Улица": "Цветочная", "Дом": 34}, "Телефоны": ["+79161234600"], "Email": "pavlov_mikhail@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Мартынов Артем Андреевич", "Дата рождения": datetime(2001, 2, 6), "Адрес": {"Город": "Москва", "Улица": "Садовая", "Дом": 35}, "Телефоны": ["+79161234601"], "Email": "martynov_artem@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Титов Роман Алексеевич", "Дата рождения": datetime(2002, 3, 24), "Адрес": {"Город": "Москва", "Улица": "Московская", "Дом": 36}, "Телефоны": ["+79161234602"], "Email": "titov_roman@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Ермаков Константин Вячеславович", "Дата рождения": datetime(2000, 4, 9), "Адрес": {"Город": "Москва", "Улица": "Спортивная", "Дом": 37}, "Телефоны": ["+79161234603"], "Email": "ermakov_konstantin@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Зайцев Дмитрий Игоревич", "Дата рождения": datetime(2000, 5, 4), "Адрес": {"Город": "Москва", "Улица": "Бородинская", "Дом": 38}, "Телефоны": ["+79161234604"], "Email": "zaitsev_dmitry@mail.com", "Группа": group_ids[6], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Смирнов Павел Александрович", "Дата рождения": datetime(2001, 6, 15), "Адрес": {"Город": "Москва", "Улица": "Гоголя", "Дом": 39}, "Телефоны": ["+79161234605"], "Email": "smirnov_pavel@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Чернов Виталий Андреевич", "Дата рождения": datetime(2002, 7, 26), "Адрес": {"Город": "Москва", "Улица": "Набережная", "Дом": 40}, "Телефоны": ["+79161234606"], "Email": "chernov_vitaliy@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Гусев Олег Николаевич", "Дата рождения": datetime(2000, 8, 7), "Адрес": {"Город": "Москва", "Улица": "Вокзальная", "Дом": 41}, "Телефоны": ["+79161234607"], "Email": "gusev_oleg@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Лебедев Сергей Васильевич", "Дата рождения": datetime(2001, 9, 18), "Адрес": {"Город": "Москва", "Улица": "Песочная", "Дом": 42}, "Телефоны": ["+79161234608"], "Email": "lebedev_sergey@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Фролов Евгений Ильич", "Дата рождения": datetime(2002, 10, 29), "Адрес": {"Город": "Москва", "Улица": "Полевая", "Дом": 43}, "Телефоны": ["+79161234609"], "Email": "frolov_evgeniy@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Тарасов Андрей Романович", "Дата рождения": datetime(1999, 11, 11), "Адрес": {"Город": "Москва", "Улица": "Комсомольская", "Дом": 44}, "Телефоны": ["+79161234610"], "Email": "tarasov_andrey@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Борисов Максим Валерьевич", "Дата рождения": datetime(2000, 12, 12), "Адрес": {"Город": "Москва", "Улица": "Лесная", "Дом": 45}, "Телефоны": ["+79161234611"], "Email": "borisov_maxim@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Волков Виктор Олегович", "Дата рождения": datetime(2001, 1, 23), "Адрес": {"Город": "Москва", "Улица": "Строительная", "Дом": 46}, "Телефоны": ["+79161234612"], "Email": "volkov_victor@mail.com", "Группа": group_ids[7], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Семенов Артем Валерьевич", "Дата рождения": datetime(2002, 2, 3), "Адрес": {"Город": "Москва", "Улица": "Парковая", "Дом": 47}, "Телефоны": ["+79161234613"], "Email": "semenov_artem@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Федоров Дмитрий Игоревич", "Дата рождения": datetime(2000, 5, 14), "Адрес": {"Город": "Москва", "Улица": "Речная", "Дом": 48}, "Телефоны": ["+79161234614"], "Email": "fedorov_dmitry@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Орлов Антон Михайлович", "Дата рождения": datetime(2001, 6, 25), "Адрес": {"Город": "Москва", "Улица": "Восточная", "Дом": 49}, "Телефоны": ["+79161234615"], "Email": "orlov_anton@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Соколов Кирилл Алексеевич", "Дата рождения": datetime(2002, 7, 6), "Адрес": {"Город": "Москва", "Улица": "Западная", "Дом": 50}, "Телефоны": ["+79161234616"], "Email": "sokolov_kirill@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Матвеев Павел Романович", "Дата рождения": datetime(2000, 8, 17), "Адрес": {"Город": "Москва", "Улица": "Южная", "Дом": 51}, "Телефоны": ["+79161234617"], "Email": "matveev_pavel@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Морозов Андрей Николаевич", "Дата рождения": datetime(2001, 9, 28), "Адрес": {"Город": "Москва", "Улица": "Северная", "Дом": 52}, "Телефоны": ["+79161234618"], "Email": "morozov_andrey@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": True},
    {"ФИО": "Киселев Иван Сергеевич", "Дата рождения": datetime(2002, 10, 9), "Адрес": {"Город": "Москва", "Улица": "Пролетарская", "Дом": 53}, "Телефоны": ["+79161234619"], "Email": "kiselev_ivan@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": False},
    {"ФИО": "Сергеев Максим Олегович", "Дата рождения": datetime(1999, 11, 20), "Адрес": {"Город": "Москва", "Улица": "Трудовая", "Дом": 54}, "Телефоны": ["+79161234620"], "Email": "sergeev_maxim@mail.com", "Группа": group_ids[8], "Направление": major_ids[2], "Бюджет": True}
]


student_ids = db.students.insert_many(students).inserted_ids

# 4. Данные о преподавателях и предметах
teachers = [
    {"ФИО": "Иванов Иван Петрович"},
    {"ФИО": "Петров Петр Иванович"},
    {"ФИО": "Сидоров Сидор Петрович"},
    {"ФИО": "Кузнецов Алексей Викторович"},
    {"ФИО": "Попов Александр Викторович"}
]

teacher_ids = db.teachers.insert_many(teachers).inserted_ids

subjects = [
    {"Название предмета": "Математика", "Преподаватель": teacher_ids[0]},
    {"Название предмета": "Физика", "Преподаватель": teacher_ids[1]},
    {"Название предмета": "Информатика", "Преподаватель": teacher_ids[2]},
    {"Название предмета": "Теория графов", "Преподаватель": teacher_ids[3]},
    {"Название предмета": "Линейная алгебра", "Преподаватель": teacher_ids[4]},
    {"Название предмета": "История", "Преподаватель": teacher_ids[0]},
    {"Название предмета": "Программирование", "Преподаватель": teacher_ids[1]}
]

subject_ids = db.subjects.insert_many(subjects).inserted_ids

# 5. Данные об оценках
grades = [
    {"Студент": student_ids[0], "Предмет": subject_ids[0], "Оценка": 5},
    {"Студент": student_ids[1], "Предмет": subject_ids[0], "Оценка": 4},
    {"Студент": student_ids[2], "Предмет": subject_ids[1], "Оценка": 3},
    {"Студент": student_ids[3], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[4], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[5], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[6], "Предмет": subject_ids[2], "Оценка": 3}
    {"Студент": student_ids[7], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[8], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[9], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[10], "Предмет": subject_ids[2], "Оценка": 3},
    {"Студент": student_ids[11], "Предмет": subject_ids[0], "Оценка": 5},
    {"Студент": student_ids[12], "Предмет": subject_ids[0], "Оценка": 4},
    {"Студент": student_ids[13], "Предмет": subject_ids[1], "Оценка": 3},
    {"Студент": student_ids[14], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[15], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[16], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[17], "Предмет": subject_ids[2], "Оценка": 3}
    {"Студент": student_ids[18], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[19], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[20], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[21], "Предмет": subject_ids[2], "Оценка": 3},
    {"Студент": student_ids[22], "Предмет": subject_ids[0], "Оценка": 5},
    {"Студент": student_ids[23], "Предмет": subject_ids[0], "Оценка": 4},
    {"Студент": student_ids[24], "Предмет": subject_ids[1], "Оценка": 3},
    {"Студент": student_ids[25], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[26], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[27], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[28], "Предмет": subject_ids[2], "Оценка": 3}
    {"Студент": student_ids[29], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[30], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[31], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[32], "Предмет": subject_ids[2], "Оценка": 3},
    {"Студент": student_ids[33], "Предмет": subject_ids[0], "Оценка": 5},
    {"Студент": student_ids[34], "Предмет": subject_ids[0], "Оценка": 4},
    {"Студент": student_ids[35], "Предмет": subject_ids[1], "Оценка": 3},
    {"Студент": student_ids[36], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[37], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[38], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[39], "Предмет": subject_ids[2], "Оценка": 3}
    {"Студент": student_ids[40], "Предмет": subject_ids[1], "Оценка": 2},
    {"Студент": student_ids[41], "Предмет": subject_ids[2], "Оценка": 5},
    {"Студент": student_ids[42], "Предмет": subject_ids[2], "Оценка": 4},
    {"Студент": student_ids[43], "Предмет": subject_ids[2], "Оценка": 3}
]

grages_ids = db.grades.insert_many(grades)

# 6. Данные о расписании
schedules = [
    {"Номер пары": 1, "Время начала": "08:00", "Время окончания": "09:30"},
    {"Номер пары": 2, "Время начала": "09:40", "Время окончания": "11:10"},
    {"Номер пары": 3, "Время начала": "11:20", "Время окончания": "12:50"},
    {"Номер пары": 4, "Время начала": "13:30", "Время окончания": "15:00"},
    {"Номер пары": 5, "Время начала": "15:10", "Время окончания": "16:40"},
    {"Номер пары": 6, "Время начала": "16:50", "Время окончания": "18:20"}
]

schedule_ids = db.schedule.insert_many(schedules).inserted_ids

# 7. Данные о посещениях студентов
def generate_attendances():
    attendances = []
    for student in student_ids:
        for _ in range(10):  # Генерация 10 посещений на студента
            date = datetime(2023, random.randint(1, 12), random.randint(1, 28))
            pair_number = random.choice([1, 2, 3, 4, 5, 6])
            subject = random.choice(subject_ids)
            teacher = db.teachers.find_one({"_id": db.subjects.find_one({"_id": subject})["Преподаватель"]})
            
            attendances.append({
                "Студент": student,
                "Дата": date,
                "Номер пары": pair_number,
                "Предмет": subject,
                "Преподаватель": teacher["_id"]
            })
    
    return attendances

attendances = generate_attendances()
db.attendances.insert_many(attendances)

# Запросы

# 1. Вывести списки групп по заданному направлению с указанием номера группы в формате ФИО, бюджет/внебюджет. Студентов выводить в алфавитном порядке.
def get_students_by_major(major_name):
    major = db.majors.find_one({"Название": major_name})
    if not major:
        print(f"Направление {major_name} не найдено.")
        return

    groups = db.groups.find({"Направление": major["_id"]})
    for group in groups:
        print(f"Группа {group['Номер группы']}:")
        students = db.students.find({"Группа": group["_id"]}).sort("ФИО", 1)
        for student in students:
            print(f"ФИО: {student['ФИО']}, Бюджет: {'Да' if student['Бюджет'] else 'Нет'}")
        print()

get_students_by_major("Информатика")

# 2. Вывести студентов с фамилией, начинающейся с первой буквы вашей фамилии, с указанием ФИО, номера группы и направления обучения.
def get_students_by_surname_initial(initial):
    students = db.students.find({"ФИО": {"$regex": f"^{initial}"}})
    for student in students:
        group = db.groups.find_one({"_id": student["Группа"]})
        major = db.majors.find_one({"_id": student["Направление"]})
        print(f"ФИО: {student['ФИО']}, Группа: {group['Номер группы']}, Направление: {major['Название']}")

get_students_by_surname_initial("И")

# 3. Вывести список студентов для поздравления по месяцам в формате Фамилия И.О., день и название месяца рождения, номером группы и направлением обучения.
def get_birthday_list():
    students = db.students.find()
    for student in students:
        birth_date = student["Дата рождения"]
        month_name = birth_date.strftime("%B")
        formatted_date = birth_date.strftime("%d %B")
        group = db.groups.find_one({"_id": student["Группа"]})
        major = db.majors.find_one({"_id": student["Направление"]})
        print(f"{student['ФИО']}, {formatted_date}, Группа: {group['Номер группы']}, Направление: {major['Название']}")

get_birthday_list()

# 4. Вывести студентов с указанием возраста в годах.
def get_students_with_age():
    students = db.students.find()
    current_date = datetime.now()
    for student in students:
        birth_date = student["Дата рождения"]
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        print(f"ФИО: {student['ФИО']}, Возраст: {age} лет")

get_students_with_age()

# 5. Вывести студентов, у которых день рождения в текущем месяце.
def get_students_with_birthday_this_month():
    current_month = datetime.now().month
    students = db.students.find({"Дата рождения": {"$regex": f"-{current_month:02d}-"}})
    for student in students:
        print(f"ФИО: {student['ФИО']}, Дата рождения: {student['Дата рождения'].strftime('%Y-%m-%d')}")

get_students_with_birthday_this_month()

# 6. Вывести количество студентов по каждому направлению.
def get_student_count_by_major():
    majors = db.majors.find()
    for major in majors:
        count = db.students.count_documents({"Направление": major["_id"]})
        print(f"Направление: {major['Название']}, Количество студентов: {count}")

get_student_count_by_major()

# 7. Вывести количество бюджетных и внебюджетных мест по группам. Для каждой группы вывести номер и название направления.
def get_budget_non_budget_count_by_group():
    groups = db.groups.aggregate([
        {
            '$lookup': {
                'from': 'students',
                'localField': '_id',
                'foreignField': 'Группа',
                'as': 'students'
            }
        },
        {
            '$lookup': {
                'from': 'majors',
                'localField': 'Направление',
                'foreignField': '_id',
                'as': 'major'
            }
        },
        {'$unwind': '$major'},
        {
            '$project': {
                'Номер группы': 1,
                'major.Название': 1,
                'Бюджет': {'$size': {'$filter': {'input': '$students', 'as': 'student', 'cond': {'$eq': ['$$student.Бюджет', True]}}}},
                'Внебюджет': {'$size': {'$filter': {'input': '$students', 'as': 'student', 'cond': {'$eq': ['$$student.Бюджет', False]}}}}
            }
        }
    ])
    
    for group in groups:
        print(f"Группа: {group['Номер группы']}, Направление: {group['major']['Название']}, Бюджет: {group['Бюджет']}, Внебюджет: {group['Внебюджет']}")

get_budget_non_budget_count_by_group()

# 8. Вывести списки групп каждому предмету с указанием преподавателя.
def get_groups_by_subject():
    subjects = db.subjects.find()
    for subject in subjects:
        print(f"Предмет: {subject['Название предмета']}")
        groups = db.groups.aggregate([
            {
                '$lookup': {
                    'from': 'students',
                    'localField': '_id',
                    'foreignField': 'Группа',
                    'as': 'students'
                }
            },
            {
                '$match': {
                    'students': {'$elemMatch': {'Направление': subject['Преподаватель']}}
                }
            },
            {
                '$lookup': {
                    'from': 'teachers',
                    'localField': 'students.Направление',
                    'foreignField': '_id',
                    'as': 'teacher'
                }
            },
            {'$unwind': '$teacher'},
            {
                '$project': {
                    'Номер группы': 1,
                    'teacher.ФИО': 1
                }
            }
        ])
        
        for group in groups:
            print(f"Группа: {group['Номер группы']}, Преподаватель: {group['teacher']['ФИО']}")
        print()

get_groups_by_subject()

# 9. Определить, какую дисциплину изучает максимальное количество студентов.
def get_most_popular_subject():
    subject_counts = db.grades.aggregate([
        {
            '$group': {
                '_id': '$Предмет',
                'student_count': {'$sum': 1}
            }
        },
        {
            '$lookup': {
                'from': 'subjects',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'subject'
            }
        },
        {'$unwind': '$subject'},
        {'$sort': {'student_count': -1}},
        {'$limit': 1}
    ])
    
    for subject_count in subject_counts:
        print(f"Самая популярная дисциплина: {subject_count['subject']['Название предмета']}, Количество студентов: {subject_count['student_count']}")

get_most_popular_subject()

# 10. Определить сколько студентов обучатся у каждого их преподавателей.
def get_student_count_by_teacher():
    teachers = db.teachers.find()
    for teacher in teachers:
        count = db.students.count_documents({"Направление": {"$in": db.subjects.find({"Преподаватель": teacher["_id"]}).distinct("_id")}})
        print(f"Преподаватель: {teacher['ФИО']}, Количество студентов: {count}")

get_student_count_by_teacher()

# 11. Определить долю ставших студентов по каждой дисциплине (не оценки или 2 считать не сдавшими).
def get_passing_rate_by_subject():
    subjects = db.subjects.find()
    for subject in subjects:
        total_students = db.grades.count_documents({"Предмет": subject["_id"]})
        passed_students = db.grades.count_documents({"Предмет": subject["_id"], "Оценка": {"$gte": 3}})
        if total_students > 0:
            passing_rate = (passed_students / total_students) * 100
            print(f"Предмет: {subject['Название предмета']}, Доля сдавших: {passing_rate:.2f}%")
        else:
            print(f"Предмет: {subject['Название предмета']}, Нет студентов")

get_passing_rate_by_subject()

# 12. Определить среднюю оценку по предметам (для сдавших студентов).
def get_average_grade_by_subject():
    subjects = db.subjects.find()
    for subject in subjects:
        average_grade = db.grades.aggregate([
            {
                '$match': {
                    'Предмет': subject['_id'],
                    'Оценка': {'$gte': 3}
                }
            },
            {
                '$group': {
                    '_id': '$Предмет',
                    'average_grade': {'$avg': '$Оценка'}
                }
            }
        ])
        
        for avg in average_grade:
            print(f"Предмет: {subject['Название предмета']}, Средняя оценка: {avg['average_grade']:.2f}")

get_average_grade_by_subject()

# 13. Определить группу с максимальной средней оценкой (включая не сдавших).
def get_group_with_highest_average_grade():
    groups = db.groups.aggregate([
        {
            '$lookup': {
                'from': 'students',
                'localField': '_id',
                'foreignField': 'Группа',
                'as': 'students'
            }
        },
        {
            '$lookup': {
                'from': 'grades',
                'localField': 'students._id',
                'foreignField': 'Студент',
                'as': 'grades'
            }
        },
        {
            '$group': {
                '_id': '$_id',
                'average_grade': {'$avg': '$grades.Оценка'}
            }
        },
        {'$sort': {'average_grade': -1}},
        {'$limit': 1}
    ])
    
    for group in groups:
        group_info = db.groups.find_one({"_id": group["_id"]})
        print(f"Группа с максимальной средней оценкой: {group_info['Номер группы']}, Средняя оценка: {group['average_grade']:.2f}")

get_group_with_highest_average_grade()
        

# 14. Вывести студентов со всеми оценками отлично и не имеющих несданный экзамен.
def get_students_with_excellent_grades():
    students = db.students.find()
    for student in students:
        grades = db.grades.find({"Студент": student["_id"], "Оценка": {"$nin": [2, None]}})
        total_grades = grades.count()
        excellent_grades = grades.count_documents({"Оценка": 5})
        if total_grades > 0 and total_grades == excellent_grades:
            print(f"Студент: {student['ФИО']}, Все оценки отлично")

get_students_with_excellent_grades()

# 15. Вывести кандидатов на отчисление (не сдан не менее двух предметов).
def get_students_at_risk():
    students = db.students.find()
    for student in students:
        failed_grades = db.grades.count_documents({"Студент": student["_id"], "Оценка": {"$lt": 3}})
        if failed_grades >= 2:
            print(f"Студент: {student['ФИО']}, Несданных предметов: {failed_grades}")

get_students_at_risk()

# 16. Вывести по заданному предмету количество посещенных занятий.
def get_attendance_count_by_subject(subject_name):
    subject = db.subjects.find_one({"Название предмета": subject_name})
    if not subject:
        print(f"Предмет {subject_name} не найден.")
        return

    total_attendance = db.attendances.count_documents({"Предмет": subject["_id"]})
    print(f"Количество посещенных занятий по предмету {subject_name}: {total_attendance}")

get_attendance_count_by_subject("Информатика")

# 17. Вывести по заданному предмету количество пропущенных занятий.
def get_absenteeism_count_by_subject(subject_name):
    subject = db.subjects.find_one({"Название предмета": subject_name})
    if not subject:
        print(f"Предмет {subject_name} не найден.")
        return

    total_classes = len(db.schedule.distinct("Номер пары"))
    total_attendance = db.attendances.count_documents({"Предмет": subject["_id"]})
    total_absenteeism = total_classes - total_attendance
    print(f"Количество пропущенных занятий по предмету {subject_name}: {total_absenteeism}")

get_absenteeism_count_by_subject("Информатика")

# 18. Вывести по заданному преподавателю количество студентов на каждом занятии.
def get_student_count_by_teacher(subject_name):
    subject = db.subjects.find_one({"Название предмета": subject_name})
    if not subject:
        print(f"Предмет {subject_name} не найден.")
        return

    teacher_id = subject["Преподаватель"]
    attendances = db.attendances.aggregate([
        {
            '$match': {
                'Преподаватель': teacher_id
            }
        },
        {
            '$group': {
                '_id': '$Дата',
                'student_count': {'$sum': 1}
            }
        },
        {
            '$sort': {'_id': 1}
        }
    ])

    for attendance in attendances:
        print(f"Дата: {attendance['_id']}, Количество студентов: {attendance['student_count']}")

get_student_count_by_teacher("Информатика")

# 19. Для каждого студента вывести общее время, потраченное на изучение каждого предмета.
def get_total_study_time_per_student():
    students = db.students.find()
    for student in students:
        print(f"Студент: {student['ФИО']}")
        subjects = db.subjects.find()
        for subject in subjects:
            total_time = db.attendances.count_documents({"Студент": student["_id"], "Предмет": subject["_id"]}) * 90  # 90 минут - длительность одного занятия
            print(f"Предмет: {subject['Название предмета']}, Общее время (в минутах): {total_time}")

get_total_study_time_per_student()

