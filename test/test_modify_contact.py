from model.contact import Contact


def test_modify_contact_firstname(app):
   old_contacts = app.contact.get_contact_list()
   print(len(old_contacts))
   if app.contact.count() == 0:
       app.contact.create(Contact(firstname="test"))
   app.contact.modify_first_contact(Contact(firstname="New contact"))
   new_contacts = app.contact.get_contact_list()
   print(len(new_contacts))
   assert len(old_contacts) == len(new_contacts)
