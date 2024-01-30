def get_credentials(first_name: str, middle_name: str | None, last_name: str, phone_number: str) -> None:
    """
    Generates a username and password based on input parameters.
    :param first_name: Required
    :param middle_name: Optional
    :param last_name: Required
    :param phone_number: Required: Format (XXX)-XXX-XXXX
    """
    # decorator and styling
    print("=" * 30)
    print("Credentials for", first_name, last_name)

    # username = first 6 of last name, first char of first name, first char of middle name (if exists)
    print("Username: ", end="")
    if middle_name is None:
        print(last_name[:6] + first_name[0])
    else:
        print(last_name[:6] + first_name[0] + middle_name[0])

    # password = first 2 of first name, first 3 human even letters of middle name, last 4 of phone #
    print("Password: ", end="")
    if middle_name is None:
        print(first_name[:2] + phone_number[-4:])
    else:
        print(first_name[:2] + middle_name[1:7:2] + phone_number[-4:])


def main():
    get_credentials("Linus", "Benedict", "Torvalds", "(317)-555-1969")
    get_credentials("Alan", "Mathison", "Turing", "(317)-555-5346")
    get_credentials("Stephan", "Gary", "Wozniak", "(317)-555-3720")
    get_credentials("Adele", None, "Goldberg", "(317)-555-2345")


main()
