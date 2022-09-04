#1. CheckEmail
def valid_email(email):
    try:
        if email.count("@") == 0 or email.count("@") > 1:
            raise ValueError("@ error")
        personal_info = email[:email.find("@")]
        if len(personal_info) == 0:
            raise ValueError("personal info error")
        domain_info = email[email.find("@")+1:]
        if len(domain_info) == 0:
            raise ValueError("domain info error")
        if "_" in domain_info:
            raise ValueError("domain info error")
        if domain_info[-1] == "." or domain_info.find("..") != -1:
            raise ValueError("domain info error")
        dom = domain_info[::-1]
        if not dom[:dom.find(".")].isalpha():
            raise ValueError("domain error")
    except ValueError as err:
        print("Email is not valid - ", err)
    else:
        print("Email is valid")

valid_email(input("input email - "))