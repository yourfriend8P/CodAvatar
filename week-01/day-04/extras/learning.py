# Here lies random codes to test and run

# DECORATOR in Python
print("DECORATOR IN PYTHON: \n")


def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())
print(changecase(myfunction)())  # instead of using @changecase

# ----------------------------------------------------------------------
