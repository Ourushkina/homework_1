from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olga"))
    contacts = db.get_contact_list()
    contact_to_move = random.choice(contacts)
    groups = db.get_group_list()
    group_for_moving_in = random.choice(groups)
    app.contact.move_contact_to_group(contact_id=contact_to_move.id, group_id=group_for_moving_in.id)
    contacts_in_group = db_orm.get_contacts_in_group(Group(id=group_for_moving_in.id))
    assert contact_to_move in contacts_in_group