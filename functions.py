import re
from models import Contact, Phone, Email
import show_info
import inspect
import types
from parse import find_name, name_number, name_email
from search import find_contact_by_name


no_number = "Sorry, I can't identify a phone number."
no_name = "Sorry, I can't identify a contact's name."


def empty(*_):
    """called if an empty command is passed to assistant.
    works differently if the assistant is in the show records mode.
    shouldn't be decorated ny decorator to work properly"""
    return ""


def add_contact(data: str):
    """help<add contact 'name' -- creates a new contact>help1
        add contact from 'text' to your AddressBook"""
    name = find_name(data)
    if not name:
        return no_name
    contact = find_contact_by_name(name)
    if contact is not None:
        return f"Contact '{name}' already exists"
    else:
        Contact(name=name).save()
        return f"Created contact a new contact '{name}'"


def delete_contact(data: str):
    name = find_name(data)
    if not name:
        return no_name
    contact = find_contact_by_name(name)
    if contact is None:
        return "Contact does not exist"
    else:
        contact.delete()
        return f"Contact {name} has been deleted"


def show_contact(data: str):
    """help<show contact 'name' -- shows a contact with name 'name'>help0
    shows a contact by its name"""
    name = find_name(data)
    if not name:
        return no_name
    contact = find_contact_by_name(name)
    if contact is None:
        return f"Contact '{name}' is not in your contacts"
    else:
        contact_reader = show_info.ShowContact(contact)
        return contact_reader.show()


def show_all(*_):
    """help<show all -- shows all contacts with name >help0
    shows a contact by its name"""
    contacts = Contact.objects()
    result = ""
    for contact in contacts:
        contact_reader = show_info.ShowContact(contact)
        result += contact_reader.show()
        result += "\n"
    return result if result else "Your book is empty"


def add_number(data: str):
    """help<add phone 'name' 'valid phone number' -- adds a new phone number to the contact>help1
    adds a number from 'text' to an existing contact from 'text'"""
    name, number = name_number(data)
    if not name:
        return f"Sorry, I can't find identify existing contact name"
    if not number:
        return no_number
    contact = find_contact_by_name(name)
    if contact is None:
        return f"Contact '{name}' does not exists"
    else:
        contacts_phones = contact.phones
        contacts_phones = [x.number for x in contacts_phones]
        if number in contacts_phones:
            return f"Contact {name} already has number {number}"
        else:
            phone = Phone(number=number)
            contact.phones.append(phone)
            contact.save()
            return f"Added new number {number} to contact {name}"


def delete_number(data: str):
    """help<delete number 'name' 'phone number' -- deletes the 'phone number' from the contact>help2
    deletes a number of contact from 'data'"""
    name, number = name_number(data)
    if not name:
        return "Can't find an existing contact name"
    if not number:
        return "Can't find a valod phone number"
    contact = find_contact_by_name(name)
    if contact is None:
        return f"Contact '{name}' does not exists"
    else:
        new_phone_list = []
        for phone_number in contact.phones:
            if phone_number.number != number:
                new_phone_list.append(phone_number)
        contact.update(phones=new_phone_list)
        contact.save()
        return f"Successfully deleted number {number} from contact {name}"


def add_email(data: str):
    """help<add email 'name' 'email' -- ands a new email to the contact>help1
        adds email to the existing contact"""
    name, email = name_email(data)
    if not name:
        return f"Sorry, I can't find identify existing contact name"
    if not email:
        return f"No valid email found"
    contact = find_contact_by_name(name)
    if contact is None:
        return f"Contact '{name}' does not exists"
    else:
        contacts_emails = contact.emails
        contacts_emails = [x.mail for x in contacts_emails]
        if email in contacts_emails:
            return f"Contact {name} already has email address {email}"
        else:
            new_email = Email(mail=email)
            contact.emails.append(new_email)
            contact.save()
            return f"Added new email address {email} to contact {name}"


def delete_email(data: str):
    """help<delete email 'name' 'email' -- deletes an email from the contact>help2
    deletes one email"""
    name, email = name_email(data)
    if not name:
        return "Can't find an existing contact name"
    if not email:
        return "Can't find a valod email address"
    contact = find_contact_by_name(name)
    if contact is None:
        return f"Contact '{name}' does not exists"
    else:
        new_email_list = []
        for mail_address in contact.emails:
            if mail_address.mail != email:
                new_email_list.append(mail_address)
        contact.update(emails=new_email_list)
        contact.save()
        return f"Successfully deleted email address {email} from contact {name}"


def find(data: str):
    data = data.strip()
    result = ""

    contacts = Contact.objects()
    matches_contacts = []
    for contact in contacts:
        if data in contact.name:
            matches_contacts.append(contact)
            continue
        for phone in contact.phones:
            if data in phone.number:
                matches_contacts.append(contact)
                break
        if contact in matches_contacts:
            continue
        for email in contact.emails:
            if data in email.mail:
                matches_contacts.append(contact)
                break
        if contact in matches_contacts:
            continue
    if matches_contacts:
        result += "Matches in contacts:\n"
        for match in matches_contacts:
            result += show_contact(match.name)
            result += "\n"
    return result if result else "No matches found"


def help_me(*_):
    """help<\t'valid phone number' should be 7 digits long + optional 3 digits of city code + optional 2 digits of country code + optional '+' sign
    \t'email' name1.name2@domen1.domen2, should have at least one name and two domain names>help9
    """
    #     \t'birthday' should be in forman 'mm.dd' or 'mm.dd.year'
    commands = dir(__import__(inspect.getmodulename(__file__)))  # all objects in module
    functions = list(filter(lambda x: (isinstance(eval(x), types.FunctionType)), commands))  # only functions

    def help_line(func_name: str):  # returns info for help function from func_name function
        pattern = r"help<([\s\S]+)>help(\d)"
        function = eval(func_name)
        if function.__doc__:
            doc = function.__doc__
        else:
            return None
        m = re.findall(pattern, doc)
        if m:
            message, priority = m[0]
            return message, priority
        else:
            return None

    help_list = []
    for func in functions:
        line = help_line(func)
        if line:
            help_list.append(line)

    helper = show_info.Helper(help_list)
    return helper.show()
