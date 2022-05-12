f_contacts = open('data/contacts-writing.csv', encoding='latin1', mode='w+', newline='')

contacts = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contact in contacts:
    f_contacts.write(contact)

f_contacts.flush()
f_contacts.seek(28)
f_contacts.write('12,Ana,ana@ana.com.br\n'.upper())
f_contacts.flush()
f_contacts.seek(0)

for line in f_contacts:
    print(line)
