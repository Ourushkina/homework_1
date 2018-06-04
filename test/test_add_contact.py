# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application_contact import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.feel_address_book_entry_form(Contact(firstname="Olga", middlename="new", lastname="Urushkina", nickname="Redfox",
                                      title="company", company="ipder", address="jjjjj",
                                      home="1111111111", mobile="2222222222", work="3333333333", fax="8888888888",
                                      email="data@rambler.ru", email2="few@mail.com", email3="hpme@yamdex.ru",
                                      homepage="www.ggg.net", address2="rrrrr", phone2="yyyyy", notes="bbbbb"))
    app.session.logout()