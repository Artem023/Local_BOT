from modules import creat_data_table, add_contact, show_all_contacts, find_contact, edit_contacts, delete_contact


while True:
    print("""
Чтобы начать работу с ботом вам необходимо воспользоваться командой /start.
После этого произойдет создание таблицы базы данных, где будут храниться
все ваши контакты. Следуйте инструкциям и у вас все получиться!
  """)
    cmd = input('\nEnter your command: ')
    if cmd == '/start':
        print(''' 
Тебя приветствует чат-бот, который будет хранить все твои контакты в одном месте.
Используй навигацию ниже, чтобы общаться со мной
    ''')
        creat_data_table()

    if cmd == '/stop':
        print('До скорых встреч!')
        exit()

    if cmd == '/add':
        add_contact()

    if cmd == '/show all':
        show_all_contacts()

    if cmd == '/find':
        find_contact()

    if cmd == '/edit':
        edit_contacts()

    if cmd == '/delete':
        delete_contact()
