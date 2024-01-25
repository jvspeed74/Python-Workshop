def get_credentials(first_name, middle_name, last_name, phone_number):
    print("Getting credentials for", first_name, last_name)

    # username
    print("Username: ", end="")
    if middle_name is None:
        print(last_name[:6] + first_name[0])
    else:
        print(last_name[:6] + middle_name[0] + first_name[0])

    # password
    print("Password: ", end="")
    if middle_name is None:
        print(first_name[:2] + phone_number[-4:])
    else:
        print(first_name[:2] + middle_name[1::2] + phone_number[-4:])

    section_decorator()


def section_decorator():
    print("=" * 15)


def main():
    # Students:
    # Linus Benedict Torvalds, (317)-555-1969
    # Alan Mathison Turing, (317)-555-5346
    # Stephan Gary Wozniak, (317)-555-3720
    # Adele Goldberg, (317)-555-2345
    section_decorator()
    get_credentials("Linus", "Benedict", "Torvalds", "(317)-555-1969")
    get_credentials("Alan", "Mathison", "Turing", "(317)-555-5346")
    get_credentials("Stephan", "Gary", "Wozniak", "(317)-555-3720")
    get_credentials("Adele", None, "Goldberg", "(317)-555-2345")


main()


