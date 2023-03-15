import json


def contact_to_dict(c):
    return {"name": c.name, "email": c.email}


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


c = Contact("Scott", "191943344", "scott@microsoft.com")
print(json.dumps(c.__dict__))
print(json.dumps(contact_to_dict(c)))
