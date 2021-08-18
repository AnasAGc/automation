from automation import __version__
from automation import *
import re

def test_version():
    assert __version__ == '0.1.0'


def test_email_format():

    with open('automation/assest/Email.txt','r') as emails:
        emails=emails.read()
        emails=emails.split()

    for email in emails:
        match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', email)
        assert bool(match)


def test_phone_format():

    with open('automation/assest/phone.txt','r') as phones:
        phones=phones.read()
        phones=phones.split()

    for phone in phones:
        match = re.search(r'\d{3}-\d{3}-\d{4}$', phone)
        assert bool(match)

