try:
    with open('data/contacts.csv', encoding='latin_1', mode='r') as f_contacts:
        for line in f_contacts:
            print(line, end='')

except FileNotFoundError:
    print('File not found!')

except PermissionError:
    print('No writing permission.')
