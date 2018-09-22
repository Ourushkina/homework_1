from model.contact import Contact
import random


def test_modify_some_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_info = Contact(firstname="New contact")
    contact_info.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_info)
    assert len(old_contacts) == app.contact.count()
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)