f = open('data/contacts-writing.csv', encoding='latin1', mode='a+', newline='')

print(type(f))
text_in_bytes = bytes('This is a text in bytes', 'latin1')
# print(text_in_bytes)
# print(type(text_in_bytes))

contact = bytes('14,Verônica,veronica@veronica.com.br\n', 'latin1')
f.buffer.write(contact)

f.close()
