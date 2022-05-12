carol_contact = '11,Carol,carol@carol.com.br\n'
andreza_contact = '12,Andreza,andreza@andreza.com.br\n'

with open('data/contacts-writing.csv', encoding='latin1', mode='w', newline='') as file1:
    file1.write(carol_contact)

with open('data/contacts-writing.csv', encoding='latin1', mode='a', newline='') as file2:
    file2.write(andreza_contact)
