import connect
from models import Contact, Phone, Email


def find_contact_by_phone(number: str) -> Contact:
    contacts = Contact.objects()
    for contact in contacts:
        for phone in contact.phones:
            if phone.number == number:
                return contact
    return None


def find_contact_by_name(name: str) -> Contact:
    contacts = Contact.objects()
    for contact in contacts:
        if contact.name == name:
            return contact
    return None

