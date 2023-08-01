def check_pin(pin):
    return (pin is not None
            and len(pin) > 3
            and pin.isdigit()
            and "1234" != pin)


def check_pass(password):
    return (password is not None
            and len(password) > 8
            and password.isalpha() is not True
            and password.isdigit() is not True)


def check_email(email):
    return (email is not None
            and email.find('@') > -1
            and email.find('.') > -1)


def check_name(name):
    return (name is not None
            and name.isalpha())


# print(f"'12554' = {check_pin('124')}")
# print(f"none = {check_pin(None)}")
# print(f"123456789 = {check_pass('123jghjghfg')}")
# print(f"none = {check_pass(None)}")
# print(f"sdff@dfsdf.fdj = {check_email('sdff@dfsd.ffdj')}")
# print(f"none = {check_email(None)}")
# print(f"john = {check_name('johnta')}")
# print(f"none = {check_name(None)}")
