def new_password(oldpassword,newpassword):
    if oldpassword != newpassword:
        if len(newpassword) >= 6:
            return False
    else:
        return ("password mag niet hetzelfde zijn")


print(new_password("cba","edfgasd"))