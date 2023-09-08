from validator_collection import validators

def main():
    print(response(input("What's your email address? ")))

def response(mail):
    try:
        email = validators.email(mail, allow_empty=False)
        if email == mail:
            return("Valid")
    except(ValueError):
        return("Invalid")
    except(TypeError):
        return("Invalid")


if __name__ == "__main__":
    main()