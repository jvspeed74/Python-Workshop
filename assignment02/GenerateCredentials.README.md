# Assignment 2 - Question 1

# Credential Generator

`GenerateCredentials.py` defines a function `get_credentials` that generates a username and password based on the provided input parameters. The `main` function then demonstrates the usage of this function with sample data.

### What is the purpose of this program?

The program is designed to provide a simple tool for generating credentials (username and password) for elementary
school students.

### What does this program take as input?

The program takes the following parameters as input:

- `first_name`: (Required) The first name of the individual.
- `middle_name`: (Optional) The middle name of the individual. It can be `None` if not applicable.
- `last_name`: (Required) The last name of the individual.
- `phone_number`: (Required) The phone number of the individual. It should be in the format (XXX)-XXX-XXXX.

### What is the expected output of the program?

The expected output of the program is the display of generated credentials for each set of input parameters.
The output includes a username and a password, formatted for readability.

```
==============================
Credentials for Linus Torvalds
Username: TorvalLB
Password: Lieei1969
==============================
```

### What type of execution is included in your program?

- Sequential Execution
- Conditional Execution  

### How could your program be improved?

- Inclusion of randomization in the generation process.
- Changing parameters to pass through a record of name, phone number in a dictionary 
- Ability to configure attributes of username/password (i.e length, special characters, amount of numbers)
