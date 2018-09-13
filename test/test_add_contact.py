# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Olga", lastname="Urushkina", address="jjjjj",
                      home="1111111111", mobile="2222222222", work="3333333333", phone2="8888888888",
                      email="data@rambler.ru", email2="few@mail.com", email3="hpme@yamdex.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

