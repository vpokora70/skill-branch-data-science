import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
X = pd.read_csv('C:\\Users\\vpokora\\PycharmProjects\\Python_Dlay_Slojnih_zadach\\Skill_brunch\sberbank_housing_market.csv', sep = ',')

#функция `calculate_data_shape`, принимает на вход датафрейм `X` и возвращает его размерность
def calculate_data_shape(df):
    return df.shape
#функцию `take_columns`, принимает на вход датафрейм `X` и возвращает название его столбцов.
def take_columns(df):
    return df.columns

#функция `calculate_target_ratio`, которая принимает на вход датафрейм `X`
# и название целевой переменной `target_name` - возвращает среднее значение целевой переменной.
# Округлить выходное значение до 2-го знака внутри функции.
def calculate_target_ratio(df, target_name):
    return df[target_name].mean()

#функцию calculate_data_dtypes, принимает на вход датафрейм X и возвращает
# количество числовых признаков и категориальных признаков.
# Категориальные признаки имеют тип object.
def calculate_data_dtypes(col_X):
    on = 0 # инициализируем счетчик к-во записей типа object
    nn = 0 # инициализируем счетчик к-во записей числового типа
    for k in range(len(col_X)):
        if (col_X.iloc[k]) =='object':
            on = on+1
        elif(col_X.iloc[k]) =='float64' or (col_X.iloc[k])=='int64':
            nn = nn+1
    return on, nn
#функцию calculate_cheap_apartment, принимает на вход датафрейм X
# и возвращает количество квартир, стоимость которых не превышает 1 млн. рублей.
def calculate_cheap_apartment(df, pr):
    # формируем массив квартир с ценой <1 000 000
    list_price=df[df.price_doc <= pr]['price_doc']
    return  len(list_price)
#функция calculate_squad_in_cheap_apartment, принимает на вход датафрейм X и возвращает
#среднюю площадь квартир, стоимость которых не превышает 1 млн. рублей.
#Признак, отвечающий за площадь - full_sq. Ответ округлить целого значения.
def calculate_squad_in_cheap_apartment(X, pr_d='price_doc', price=1000000, sq='full_sq'):
    sq_cheap_app=X[X[pr_d] <= price][sq]
    return sq_cheap_app

# функция calculate_mean_price_in_new_housing,
# принимает на вход датафрейм X и возвращает среднюю стоимость
# трехкомнатных квартир в доме, который не старше 2010 года. Ответ округлить до целого значения.
def calculate_mean_price_in_new_housing(X, b_year, n_r):
    cm_in_nh=X[(X.build_year>=b_year) & (X.num_room==n_r)].groupby(['build_year', 'num_room'])['price_doc'].aggregate(['mean'])
    return cm_in_nh.round(2)

#функцию `calculate_mean_squared_by_num_rooms`,
#принимает на вход датафрейм `X` и возвращает среднюю площадь квартир
#в зависимости от количества комнат. Каждое значение площади округлить до 2-го знака.
def calculate_mean_squared_by_num_rooms(df):
    return df.groupby(['num_room'])['full_sq'].aggregate(['mean']).round(2)

#функцию calculate_squared_stats_by_material, которая принимает на вход датафрейм X
# и возвращает максимальную и минимальную площадь квартир в зависимости
# от материала изготовления дома. Каждое значение площади округлить до 2-го знака.
def calculate_squared_stats_by_material(df):
    #cssm - calculate_squared_stats_by_material
    cssm= df.groupby(['material'])['full_sq'].aggregate(['min', 'max'])
    return cssm.round(2)

#функцию calculate_crosstab, которая принимает на вход датафрейм X и возвращает СРЕДНЮЮ СТОИМОСТЬ
# квартир в зависимости от района города и цели покупки.
# Ответ - сводная таблица, где индекс - район города (признак - sub_area),
# столбцы - цель покупки (признак - product_type). Каждое значение цены округлить до 2-го знака, пропуски заполнить нулем.
def calculate_crosstab(df):
    return df.groupby(['sub_area', 'product_type'])['price_doc'].aggregate(['mean']).round(2)

#pd.set_option('display.max_rows', 100500)

print('Задание 1. calculate_data_shape:')
print("calculate_data_shape:", calculate_data_shape(X))  # Размерность
#col_X dataframe название столбцов
col_X=pd.Series(take_columns(X))
print('Задание 2 . Hазвание столбцов:')
print(col_X)

mean_X=np.round(pd.Series(calculate_target_ratio(X, col_X[2:])),2)
print('Задание 3. Среднее значение столбцов:')
print(mean_X)

сol_type=(X.dtypes) #Series объект содержит тип значений колонок
dim_сol_type=len(сol_type) #длина объекта сol_type как котрольная сумма к-во запсией
cdt = calculate_data_dtypes(сol_type)
print('Задание 4 ')
print('К-во признаков object=', cdt[0], '. К-во числовых признаков=', cdt[1])

chek_num = cdt[0]+cdt[1] #общее колво записей по типам
if dim_сol_type == chek_num:
    print('Контрольная сумма совпала')
else:

    print('Контрольная сумма НЕ совпала')
price = 1000000 #инициалиируем граничную цену квартиры

numbers_cheap_apartment=calculate_cheap_apartment(X, price) # вызываем ф-цию calculate_cheap_apartment

print('Задание 5')
print('К-во квартир, стоимость которых не превышает 1 млн. рублей=', numbers_cheap_apartment)

price_attribute='price_doc'
sq_m_attribute='full_sq'
cheap_appartments=calculate_squad_in_cheap_apartment(X, price_attribute, price, sq_m_attribute )
print('Средняя площадь квартир стоимостью < 1 000 000.')
print(cheap_appartments)

num_r = 3 # number room
b_y = 2010 # build_year
cpr = calculate_mean_price_in_new_housing(X, b_y, num_r)
print("Cредняя стоимость трехкомнатных квартир в доме, который не старше 2010 года:")
print(cpr)

print("Средняя площадь квартир в зависимости от количества комнат:")
print(calculate_mean_squared_by_num_rooms(X))

print("MAX  и MIN площади квартир в зависимости от материала:")
print(calculate_squared_stats_by_material(X))

print("Средняя стоимость квартиры в зависимости от района и цели покупки:")
c_cr_tab=calculate_crosstab(X)
print(c_cr_tab)