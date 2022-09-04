#1. CheckEmail
# def valid_email(email):
#     try:
#         if email.count("@") == 0 or email.count("@") > 1:
#             raise ValueError("@ error")
#         personal_info = email[:email.find("@")]
#         if len(personal_info) == 0:
#             raise ValueError("personal info error")
#         domain_info = email[email.find("@")+1:]
#         if len(domain_info) == 0:
#             raise ValueError("domain info error")
#         if "_" in domain_info:
#             raise ValueError("domain info error")
#         if domain_info[-1] == "." or domain_info.find("..") != -1:
#             raise ValueError("domain info error")
#         dom = domain_info[::-1]
#         if not dom[:dom.find(".")].isalpha():
#             raise ValueError("domain error")
#     except ValueError as err:
#         print("Email is not valid - ", err)
#     else:
#         print("Email is valid")
#
# valid_email(input("input email - "))

# 2. DayOfWeek

def day_of_week(day_n):
    try:
        if not day_n.isnumeric():
            raise TypeError("It is incorrect type!")
        if int(day_n) not in range(1,8):
            raise ValueError("not in range!")
    except ValueError as err:
        print("There is no such day of the week! Please try again. - ", err)
    except TypeError as err:
        print("There is no such day of the week! Please try again. - ", err)
    else:
        match int(day_n):
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")

day_of_week(input("input number of day in a week - "))