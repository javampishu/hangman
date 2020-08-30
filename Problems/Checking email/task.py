def check_email(string):
    
    if (" " in string) or ("@" not in string) or ("@." in string):
        return False
    elif string.find("@") < string.find(".", string.find("@")):
        return True
    else: 
        return False
