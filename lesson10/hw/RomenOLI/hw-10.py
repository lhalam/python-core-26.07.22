#1. CheckEmail
def valid_email(email):
    Try:
        if email.count("@")>1:
            raise ValueError("email error")
    except ValueError as err:
        print("Email is not valid")


print(valid_email(input("input email - ")))