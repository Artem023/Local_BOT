import sqlite3


# Создаем новую таблицу для нового пользователя
def creat_data_table():
    with sqlite3.connect('contacts.db') as db:
        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    number1 INTEGER(11) NOT NULL,
    number2 INTEGER(11) NULL,
    email TEXT NULL,
    UNIQUE(number1, number2, email)
    )''')

        print('Таблица успешно создана')
        db.commit


# _____________________________________________________________________________#

def add_contact():
    db = sqlite3.connect("contacts.db")
    cur = db.cursor()

    print("""
Что вы хотите добавить в список контаков? Введите необходимое число:
1 - имя, номер телефона;
2 - имя, номер телефона 1 и номер телефона 2;
3 - имя, номер телефона 1 и номер телефона 2, email;
  """)
    cmd = int(input("> "))

    if cmd == 1:
        name = input("Имя: ").title()
        surname = input("Фамилия: ").title()
        number = int(input("Номер телефона №1, начиная с 8: "))
        value = [name, surname, number]

        try:
            # cur.execute("SELECT number1 FROM contacts WHERE number1 = ?", number) - выдает ошибку
            cur.execute(f"SELECT * FROM contacts WHERE number1 = {number}")
            if cur.fetchone() is None:
                cur.execute(
                    "INSERT INTO contacts (name, surname, number1) VALUES (?, ?, ?)", value)
                db.commit()
            else:
                print("Контакт с таким номером телефона уже существует")

        except sqlite3.Error as err:
            print(f"ERROR {err}")

        finally:
            cur.close()
            db.close()

    if cmd == 2:

        name = input("Имя: ").title()
        surname = input("Фамилия: ").title()
        number1 = int(input("Номер телефона №1, начиная с 8: "))
        number2 = int(input("Номер телефона №2, начиная с 8: "))
        value = [name, surname, number1, number2]

        try:
            cur.execute(f"SELECT * FROM contacts WHERE number1 = {number1}")
            if cur.fetchone() is None:
                cur.execute(
                    "INSERT INTO contacts (name, surname, number1, number2) VALUES (?, ?, ?, ?)", value)
                db.commit()
            else:
                print("Контакт с таким номером телефона уже существует")

        except sqlite3.Error as err:
            print(f"ERROR {err}")

        finally:
            cur.close()
            db.close()
    # ЧТО-ТО ЛОМАЕТСЯ
    if cmd == 3:
        name = input("Имя: ").title()
        surname = input("Фамилия: ").title()
        number1 = input("Номер телефона №1, начиная с 8: ")
        number2 = input("Номер телефона №2, начиная с 8: ")
        email = input("Email: ").lower()
        value = [name, surname, number1, number2, email]

        try:
            # cur.execute("SELECT number1 FROM contacts WHERE number1 = ?", number1) - код не работет, а ниже работает
            cur.execute(f"SELECT * FROM contacts WHERE number1 = {number1}")
            if cur.fetchone() is None:
                cur.execute(
                    "INSERT INTO contacts (name, surname, number1, number2, email) VALUES (?, ?, ?, ?, ?)", value)
                db.commit()
            else:
                print("Контакт с таким номером телефона уже существует")

        except sqlite3.Error as err:
            print(f"ERROR {err}")

        finally:
            cur.close()
            db.close()

# _____________________________________________________________________________#


def show_all_contacts():
    db = sqlite3.connect("contacts.db")
    cur = db.cursor()

    try:
        # !!!!!!!  В ВЫВОДЕ НУЖНО КАК-ТО УБРАТЬ NONE  !!!!!!!!
        for i in cur.execute("SELECT * FROM contacts"):
            # print(i[0], i[1], i[2], i[3], i[4], i[5])
            if i is None:
                print(" ")
            else:
                print(f"\n{i[1]} {i[2]}: {i[3]} \n{i[4]}")

    except sqlite3.Error as err:
        print(f"ERROR {err}")

    finally:
        cur.close()
        db.close()

# _____________________________________________________________________________#


def find_contact():
    db = sqlite3.connect("contacts.db")
    cur = db.cursor()

    print("""
Как будем искать номер телефона (выбери нужный пункт):
1 - по имени и фамилии
2 - по номеру телефона""")
    cmd = int(input("> "))

    if cmd == 1:
        name = input("Имя: ").title()
        surname = input("Фамилия: ").title()

        try:
            cur.execute(
                "SELECT * FROM contacts WHERE name = ? OR surname = ?", (name, surname))

            if cur.fetchone() is None:
                print(
                    "Такого номера нет в списке! \nХотите добавить новый (введите да / нет)? ")
                cmd = input("> ").lower()
                if cmd == "да":
                    add_contact()
            else:
                for i in cur.execute("SELECT * FROM contacts WHERE name = ? OR surname = ?", (name, surname)):
                    print(f"{i[1]} {i[2]}: {i[3]} \n{i[4]}")

        except sqlite3.Error as err:
            print(f"ERROR {err}")

        finally:
            cur.close()
            db.close()

    if cmd == 2:
        number = input("Number: ")

        try:
            cur.execute(
                f"SELECT * FROM contacts WHERE number1 = {number} OR number2 = {number}")
            if cur.fetchone() is None:
                print(
                    "Такого номера нет в списке! \nХотите добавить новый (введите да / нет)? ")
                cmd = input("> ").lower()
                if cmd == "да":
                    add_contact()
            else:
                for i in cur.execute(f"SELECT * FROM contacts WHERE number1 = {number} OR number2 = {number}"):
                    print(f"{i[1]}: {i[2]} {i[3]} \n{i[4]}")

        except sqlite3.Error as err:
            print(f"ERROR {err}")

        finally:
            cur.close()
            db.close()


# _____________________________________________________________________________#
'''
def edit_contacts():
  print("""
Что вы хотите отредактировать (введите номер команды)?
1 - изменить имя
2 - изменить фамилию
3 - изменить 1-ый номер телефона
4 - изменить 2-ой номер телефона
  """)

  cmd = int(input("> "))

  if cmd == 1:
    name = input("Имя: ").title()
    surname = input("Фамилия: ").title()

    try:
      cur.execute("SELECT * FROM contacts WHERE name = ? OR surname = ?",(name, surname))

      if cur.fetchone() is None:
        print("Такого номера нет в списке! \nХотите добавить новый (введите да / нет)? ")
        cmd = input("> ").lower()
        if cmd == "да":
          add_contact()
      else:
        for i in cur.execute("SELECT * FROM contacts WHERE name = ? OR surname = ?",(name, surname)):
          print(f"{i[1]} {i[2]}: {i[3]} \n{i[4]}")'''
    