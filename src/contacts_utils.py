import csv
import pickle
import json

from src.contact import Contact


def csv_to_contact(path, encoding='latin1'):
    contacts = []
    with open(path, encoding=encoding) as f:
        reader = csv.reader(f)
        for line in reader:
            id, name, mail = line

            contact = Contact(id, name, mail)
            contacts.append(contact)

    return contacts


def contacts_to_pickle(contacts, path):
    with open(path, mode='wb') as file:
        pickle.dump(contacts, file)


def pickle_to_contacts(path):
    with open(path, mode='rb') as file:
        contacts = pickle.load(file)

    return contacts


def contacts_to_json(contacts, path):
    with open(path, mode='w') as file:
        json.dump(contacts, file, default=_contact_to_json)


def _contact_to_json(contact):
    return contact.__dict__


def json_to_contacts(path):
    contacts = []
    with open(path) as file:
        contacts_json = json.load(file)

        for contact in contacts_json:
            c = Contact(**contact)
            contacts.append(c)

    return contacts
