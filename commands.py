from functions import add_contact, delete_contact, show_contact, empty, help_me, add_number, show_all, delete_number
from functions import add_email, delete_email, find


commands = {
    "hello": lambda *_: "How can I help you?",
    "bye": lambda *_: "Good bye!",
    "add_contact": add_contact,
    "delete_contact": delete_contact,
    "show": show_contact,
    "empty": empty,
    "help_me": help_me,
    "add_number": add_number,
    "show_all": show_all,
    "delete_number": delete_number,
    "add_email": add_email,
    "delete_email": delete_email,
    "find": find,


    0: lambda *_: "Sorry I can't understand you. Try 'help' command to see what I can.",
}


def def_mod(string: str):
    try:
        mods = {
            "hello": "hello",
            "good bye": "bye",
            "close": "bye",
            "exit": "bye",
            "add contact": "add_contact",
            "delete contact": "delete_contact",
            "show contact": "show",
            "help": "help_me",
            "add number": "add_number",
            "show all": "show_all",
            "delete number": "delete_number",
            "add email": "add_email",
            "delete email": "delete_email",
            "find": "find",

        }
        if not string:
            return "empty", ""
        for key_word in mods.keys():
            if key_word in string.lower():
                return mods[key_word], string.replace(key_word, "", 1)
        return 0, ""
    except Exception as err:
        return err
