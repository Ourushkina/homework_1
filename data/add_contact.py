from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1",
            address="address1", home="home1", mobile="mobile1",
            work="work1", phone2="phone21", email="email11",
            email2="email21", email3="email31"),
    Contact(firstname="firstname2", lastname="lastname2",
            address="address2", home="home2", mobile="mobile2",
            work="work2", phone2="phone22", email="email12",
            email2="email22", email3="email32")
]


def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_name("firstname", 10), lastname=random_name("lastname", 10),
            address=random_name("address", 10), home=random_phone("+7", 10), mobile=random_phone("+7", 10),
            work=random_phone("+7", 10), phone2=random_phone("+7", 10),email=random_email("e1", 10),
            email2=random_email("e2", 10), email3=random_email("e3", 10))
    for i in range(2)
]

