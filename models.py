from mongoengine import EmbeddedDocument, Document, ReferenceField
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Phone(EmbeddedDocument):
    number = StringField()


class Email(EmbeddedDocument):
    mail = StringField()


class Contact(Document):
    name = StringField(required=True)
    phones = ListField(EmbeddedDocumentField(Phone))
    emails = ListField(EmbeddedDocumentField(Email))
