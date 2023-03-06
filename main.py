from modules import creat_data_table, add_contact, show_all_contacts, find_contact


while True:
  cmd = input ('Enter your command: ')
  if cmd == '/start':
    print (''' 
Тебя приветствует чат-бот, который будет хранить все твои контакты в одном месте.
Используй навигацию ниже, чтобы общаться со мной!
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
    pass

  if cmd == '/delete':
    pass