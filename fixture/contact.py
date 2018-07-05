from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add"))) > 0:
            wd.find_element_by_link_text("home").click()

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.open_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("title", contact.title)
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("home", contact.home)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("work", contact.work)
        self.change_field_value_contact("fax", contact.fax)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("email2", contact.email2)
        self.change_field_value_contact("email3", contact.email3)
        self.change_field_value_contact("homepage", contact.homepage)
        self.change_field_value_contact("address2", contact.address2)
        self.change_field_value_contact("phone2", contact.phone2)
        self.change_field_value_contact("notes", contact.notes)

    def change_field_value_contact(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirmation
        wd.switch_to_alert().accept()
        self.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_group_creation(self):
        wd = self.app.wd
        self.submit_group_creation()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_css_selector("input[type='checkbox']").get_attribute("value")
            lastname = element.find_element_by_css_selector("td:nth-child(2)")  # find_element_by_xpath('//tr/td[2]')
            # print(lastname.get_attribute("textContent"))
            firstname = element.find_element_by_css_selector("td:nth-child(3)").get_attribute("textContent")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts



