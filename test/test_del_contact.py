from model.contact import Contact


def test_delete_first_contact(app):
   old_contacts = app.contact.get_contact_list()
   #print(len(old_contacts))
   if app.contact.count() == 0:
       app.contact.create(Contact(firstname="test"))
   app.contact.delete_first_contact()
   new_contacts = app.contact.get_contact_list()
   #print(len(new_contacts))
   assert len(old_contacts) - 1 == len(new_contacts)
