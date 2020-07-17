from faker import name
#
# fn = name.find_name()
#
# print(fn)

def fullname():
    fn = name.find_name()
    ln = name.last_name()
    fl= fn +" "+ ln
    return fl

print(fullname())

def email():
    email= str(fullname()).replace(" ","_")+"@testmail.com"
    return  email

print(email())