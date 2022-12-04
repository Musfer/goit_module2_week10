import connect
from models import Contact
import re


phone_pattern = "\s\+?[-\s]?(?:\d{2,3})?[-\s]?(?:\([-\s]?\d{2,3}[-\s]?\)|\d{2,3})?[-\s]?\d{2,3}[-\s]?\d{2,3}[-\s]?\d{2,3}\s"
# mail_pattern = r"[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z][a-zA-Z]+"
mail_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def find_name(text: str):
    """converts sting into a valid name of contact"""
    return text.strip().lower().title()


def name_number(text: str):
    """splits 'text' into name and email"""
    contacts = Contact.objects()
    known_names = [x.name for x in contacts]
    name = None
    for known_name in known_names:
        if known_name.lower() in text.lower():
            name = known_name
    if name is None:
        return None, None

    template = re.compile(phone_pattern)
    text = text.lower().replace(name.lower(), "", 1).strip()
    phone = template.findall(" " + text + " ")
    if phone and phone[0]:
        phone = phone[0].strip()
        return name, phone
    return name, None


def name_email(text: str):
    """splits 'text' into name and email"""
    contacts = Contact.objects()
    known_names = [x.name for x in contacts]
    name = None
    for known_name in known_names:
        if known_name.lower() in text.lower():
            name = known_name
    if name is None:
        return None, None
    template = re.compile(mail_pattern)
    text = text.lower().replace(name.lower(), "", 1).strip()
    mail = template.findall(" " + text + " ")
    if mail and mail[0]:
        mail = mail[0].strip()
        return name, mail
    return name, None

