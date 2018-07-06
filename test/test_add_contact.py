# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Olga", middlename="new", lastname="Urushkina", nickname="Redfox",
                              title="company", company="ipder", address="jjjjj",
                              home="1111111111", mobile="2222222222", work="3333333333", fax="8888888888",
                              email="data@rambler.ru", email2="few@mail.com", email3="hpme@yamdex.ru",
                              homepage="www.ggg.net", address2="rrrrr", phone2="yyyyy", notes="bbbbb")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    print(old_contacts)
    print(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

