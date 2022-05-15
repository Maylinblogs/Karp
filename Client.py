import os
import socket
import time

import stdiomask
from prettytable import PrettyTable




class Car:
    def __init__(self):
        self.model=input("Введите модель")
        self.massa=int(input("Ведите массу машины"))
class Time:
    def __init__(self):
        print("Рабочее время пароковки с 9.00 до 22.00")
class Ordered_Time(Time):
    def __init__(self):
        super().__init__()
        self.day=int(input('Введите день месяца'))
        self.start=int(input('Введите начало'))
        self.hors=int(input("Насколько часов бронируете стоянку?"))

class Person:

    # initialization or constructor method of
    def __init__(self):
        # class Student
        self.name = input('Введите имя заказчика:')
        self.surname = input('Введите фамилию заказчика:')
        self.patronymic = input('Введите фамилию заказчика:')
        self.number=inputnumber()

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def get_number(self):
        return self.number

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
def inputnumber():
    while True:
        number=input("Введите номер телефона:+375 ")
        if len(number)==9:
            return number
        else:
            print("Попробуйте еще раз")
def clear(): os.system('cls')
def expert():
    while True:
        print('=====Метод последовательных сравнений=====')
        print('Проведем оценку наиболее выгодного значения для установления цены парковки')
        coins=[]
        cars=[]
        sum=0
        n=4
        for i in range(n):
            mass=int(input('enter price '))
            cars.append(mass)
            clear()
        print(cars)
        maxelem=max(cars)
        for elem in cars:
            if elem!=maxelem:
                sum+=elem
        while maxelem<sum:
            maxelem=maxelem*1.2
        print('Получаем нормированные оценки...')
        time.sleep(2)
        for elem in cars:
            sum+=elem

        v_1=cars[0]/sum
        v_2 = cars[1]/sum
        v_3 = cars[2]/sum
        v_4 = cars[3]/sum
        print('Наилучшая цена')
        print(maxelem)
        time.sleep(2)
        clear()
        break



def total(person):
    watch_record_client(person)
    k = []
    sum = 0
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
            if person.name == name and person.surname == surname and person.patronymic == patronymic:
                k.append(money)
    array = [int(numeric_string) for numeric_string in k]
    for elem in array:
        sum += elem

    print("|Итого:")
    print(sum)
def delete_record_client(person):
    while True:
        watch_record_client(person)
        choice=input('1.Удалить все 2.Удалить одну запись')
        if choice=='1':
            l = []
            d=[]
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
                    if person.name != name and person.surname != surname and person.patronymic != patronymic:
                        myline = line.split(' ')
                        d.append(myline)

            with open('tabl.txt', 'w') as x:
                for sub_list in d:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            l.clear()
            d.clear()
            break
        elif choice=="2":

            l = []
            l.clear()
            d = []
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
                    if person.name != name and person.surname != surname and person.patronymic != patronymic:
                        myline = line.split(' ')
                        d.append(myline)
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
                    if person.name == name and person.surname == surname and person.patronymic == patronymic:
                        myline = line.split(' ')
                        l.append(myline)
            index = int(input('Какой заказ удалить?: '))
            del l[index - 1]
            f = open('tabl.txt', 'w')
            f.close()
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            with open('tabl.txt', 'a') as x:
                for sub_list in d:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            l.clear()
            d.clear()
            watch_record_client(person)
            break
def new_record_client(person):
    clear()
    while True:
        car = Car()
        time = Ordered_Time()
        money = time.hors * car.massa
        file = open('tabl.txt', 'a')
        file.write('%s %s %s %s %s %d %d %d %d %d\n' % (
            person.name, person.surname, person.patronymic, person.number, car.model, car.massa, time.day, time.start,
            time.hors, money))
        file.close()
        clear()
        break
def watch_record_client(person):
    clear()
    while True:
        mytable = PrettyTable()
        mytable.field_names = ["Имя", "Фамилия", "Отчество", "Номер", "Модель", "Масса", "День", "Начало", "Часы",
                            "Деньги"]
        with open("tabl.txt", 'r') as file:
            for line in (line.rstrip() for line in file.readlines()):
                (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
                if person.name == name and person.surname == surname and person.patronymic == patronymic:
                    mytable.add_row([name, surname, patronymic, number, model, massa, day, start, hours, money])

        file.close()
        print(mytable)
        time.sleep(3)
        mytable.clear_rows()
        clear()
        break
def change_record_client(person):
    while True:
        l = []
        d = []
        l.clear()
        d.clear()
        print(l)

        watch_record_client(person)
        with open("tabl.txt", 'r') as file:
            for line in (line.rstrip() for line in file.readlines()):
                (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
                if person.name != name and person.surname != surname and person.patronymic != patronymic:
                    myline = line.split(' ')
                    d.append(myline)
        with open("tabl.txt", 'r') as file:
            for line in (line.rstrip() for line in file.readlines()):
                (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
                if person.name == name and person.surname == surname and person.patronymic == patronymic:
                    myline = line.split(' ')
                    l.append(myline)
        print(l)
        index = int(input('Введите какой заказ изменить: '))
        del l[index - 1]
        f = open('tabl.txt', 'w')
        f.close()
        with open('tabl.txt', 'w') as x:
            for sub_list in l:
                for item in sub_list:
                    x.write(item + ' ')
                x.write('\n')
        with open('tabl.txt', 'a') as x:
            for sub_list in d:
                for item in sub_list:
                    x.write(item + ' ')
                x.write('\n')
        l.clear()
        d.clear()
        new_record_client(person)
        break
def admin():
    clear()
    while True:
        clear()
        print("1.Добавление записи\n")
        print("2.Просмотр записи\n")
        print("3.Редактирование записи\n")
        print("4.Удаление записи\n")
        print("5.Работа с пользователями\n")
        print('6.асчет дохода')
        print("7.Выход\n")
        choice_3 = input("Выберите действие: ")
        if choice_3 == '1':
            new_record()
        elif choice_3 == '2':
            watch_records()
        elif choice_3 == '3':
            change_record()
        elif choice_3 == '4':
            delete_record()
        elif choice_3 == '5':
            work()
        elif choice_3 == '6':
            break
        else:
            print('try again')
def new_record():
    clear()
    while True:
        person = Person()
        car = Car()
        time = Ordered_Time()
        money = time.hors*car.massa
        file = open('tabl.txt', 'a')
        file.write('%s %s %s %s %s %d %d %d %d %d\n' % (
            person.name, person.surname, person.patronymic, person.number, car.model, car.massa, time.day, time.start, time.hors,
            money))
        file.close()
        clear()
        break
def change_record():
    clear()
    while True:
        grid = 9
        l = []
        watch_records()
        with open("tabl.txt", 'r') as f:
            for line in (line.rstrip() for line in f.readlines()):
                myline = line.split(' ')
                l.append(myline)

        index = int(input('Какую запись изменить? '))
        l.pop(index - 1)
        with open('tabl.txt', 'w') as x:
            for sub_list in l:
                for item in sub_list:
                    x.write(item + ' ')
                x.write('\n')

        l.clear()
        new_record()
        watch_records()
        break
def watch_records():
    clear()
    myytable = PrettyTable()
    myytable.field_names = ["Имя", "Фамилия", "Отчество", "Номер", "Модель", "Масса", "День", "Начало", "Часы",
                            "Деньги"]
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, number, model, massa, day, start, hours, money) = line.split(' ')
            myytable.add_row([name, surname, patronymic, number, model, massa, day, start, hours, money])

    file.close()
    print(myytable)
    time.sleep(3)
    myytable.clear_rows()
def delete_record():
    clear()
    while True:
        choice = input('1.Удалить всех 2 Удаление 1 записи')
        if choice == '1':
            grid = 9
            l = []
            watch_records()
            with open("tabl.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)
            l.clear()
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')

            break
        elif choice == '2':
            grid = 9
            l = []
            watch_records()
            with open("tabl.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)

            index = int(input('Какую колонку удалить?: '))
            l.pop(index - 1)
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')

            l.clear()
            watch_records()
            break
        else:
            print('Еще раз!')
def client():
    person = Person()
    clear()
    while True:
        print('1.Добавление записи')
        print('2.Просмотр записей')
        print('3.Редактирование записей')
        print('4.Удаление записей')
        print('5.Расчет суммы заказов')
        print('6.Выход')
        choice = input('Ваш выбор>>:')
        if choice == '1':
            clear()
            new_record_client(person)
        elif choice == '2':
            clear()
            watch_record_client(person)
        elif choice == '3':
            clear()
            change_record_client(person)
        elif choice == '4':
            clear()
            delete_record_client(person)
        elif choice == '5':
            clear()
            break
        elif choice == '6':
            clear()
            total(person)
        else:
            print("Попробуйте еще раз")
            clear()
def authorization():
    while True:
        clear()
        login=input('Введите логин:')

        pas=input("Введите пароль: ")
        if login=='admin' and pas=="admin":
            admin()
            break
        else:
            #users = {}
            with open("person.txt",'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (key, value) = line.split(' ')
                    if login==key and pas==value:
                        clear()
                        client()
                        break

        if EOFError:
            break
def registration():
    clear()
    key = input('Введите логин :')
    value = input("Введите пароль :")
    while True:
       if len(key)>5 and len(value)>5:
            file = open("person.txt", "a")
            file.write('%s %s\n' % (key, value))
            file.close()
            break
       else:
           break
def enter():

    while True:
        clear()
        answer=input('1.Регистрация\n2.Вход\n3.Работа экспертов\n4.Выход\n')
        if answer=='1':
            registration()
        elif answer=='2':
            authorization()
        elif answer=='3':
            expert()
        elif answer=='4':
            break
        else:
            print("Неверно.Попробуйте еще раз: ")
def work():
    users=[]
    with open("person.txt.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (key, value) = line.split(' ')

            users[key] = value
    while True:
        choice=input('1.Удаление 2.Добавление 3.Выход')
        if choice=='1':
            grid = 9
            l = []

            with open("users.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)
            print(l)
            index = int(input('Какого пользователя удалить? '))
            del l[index-1]
            file=open('users.txt', 'w')
            file.close()
            with open('users.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item)
                        x.write(" ")
                    x.write('\n')

            l.clear()

            break
        elif choice=='2':
            registration()
            break
        elif choice=='3':
            break
        else:
            print('Попробуйте еще раз')
def Main():
    while True:
        Input = input('Do you want to enter?yes or no ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        Response=Response.decode('utf-8')
        if Response=='im ready':
            enter()
            break
        else:
            print('bye')
            break


    ClientSocket.close()
if __name__ == '__main__':
    Main()