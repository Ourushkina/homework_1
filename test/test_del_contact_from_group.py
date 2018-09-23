from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olga"))
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    chosen_group = random.choice(groups)
    contacts_in_group = db_orm.get_contacts_in_group(chosen_group)
    if len(contacts_in_group) == 0:
        app.contact.move_contact_to_group((random.choice(contacts)).id, chosen_group.id)
    contact_to_delete = random.choice(contacts_in_group)
    app.contact.del_contact_from_group(contact_id=contact_to_delete.id, group_id=chosen_group.id)
    contacts_in_group = db_orm.get_contacts_in_group(chosen_group)
    assert contact_to_delete not in contacts_in_group