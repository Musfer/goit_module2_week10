from abc import abstractmethod, ABC
from models import Contact, Phone, Email


class IRepr(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def show(self):  # generates a string with info about contact from record
        pass


class Helper(IRepr):
    def __init__(self, commands: list):
        self.commands = commands

    def show(self):
        sorted_commands = sorted(self.commands, key=(lambda x: x[1]))
        sorted_strings = [x[0] for x in sorted_commands]
        return "\t"+"\n\t".join(sorted_strings)


class ShowContact(IRepr):
    def __init__(self, contact: Contact):
        self.contact = contact

    def show(self):
        if self.contact is None:
            return ""
        string = ""
        string += f"{self.contact.name}:"
        numbers = self.contact.phones
        numbers = [x.number for x in numbers]
        emails = self.contact.emails
        emails = [x.mail for x in emails]
        string += f"\n\tPhone numbers: {', '.join(numbers) if numbers  else 'empty'}"
        string += f"\n\tMails: {', '.join(emails) if emails  else 'empty'}"
        return string
