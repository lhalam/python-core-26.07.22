# https://docs.python.org/3/library/exceptions.html
#
# while True:
#     a = input("a:")
#     if a == "exit":
#         break
#     b = input("b:")
#     is_not_err = False
#     try:
#         print(int(a) / int(b))
#         is_not = True
#     except ZeroDivisionError as err:
#         print("ZeroDivisionError", type(err), err)
#     except ArithmeticError as err:
#         print("ArithmeticError", type(err), err)
#     except ValueError as err:
#         print("ValueError", type(err), err)
#     except Exception as err:
#         print("error", type(err), err)
#     finally:
#         print("end")
#
#     if is_not_err:
#         print("good")
#
# try:
#     "code"
# except:
#     pass
#
# try:
#     "code"
# finally:
#     pass
#
# try:
#     "code"
# except:
#     pass
# else:
#     pass
#
# try:
#     "code"
# except:
#     pass
# finally:
#     pass
#
# try:
#     "code"
# except:
#     pass
# else:
#     pass
# finally:
#     pass



# while True:
#     a = input("a:")
#     if a == "exit":
#         break
#     b = input("b:")
#     try:
#         print(int(a) / int(b))
#     except (ZeroDivisionError, ValueError) as err:
#         print("Error:", type(err), err)
#     except Exception as err:
#         print("Exception", type(err), err)
#     finally:
#         print("end")

import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(process)d-%(asctime)s-  %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
class ZnamenykError(ArithmeticError):
    def __init__(self, data):
        logging.info(f"create ZnamenykError {data}")
        logging.debug(f"DDDcreate ZnamenykError {data}")
        self.data = data
    def __str__(self):
        return repr(self.data)


class ZnamenykError2(ZnamenykError):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def read_znamenyk():
    a = input("b:")
    if not a.isnumeric():
        raise ZnamenykError("my error")
    if a == 0:
        raise ZnamenykError2("AAA")
    return a

while True:
    a = input("a:")
    if a == "exit":
        break
    try:
        b = read_znamenyk()
        print(int(a) / int(b))
    except (ZeroDivisionError, ValueError) as err:
        logging.error(err)
    except Exception as err:
        logging.critical(err)


logging.warning('This will get logged to a file')
