# 01 - Email Validator 📧

## Description

This project checks whether an email address is valid or not.

The user enter an email address, and the program checks whether it is valid based on specific validation rules.

If the email is valid, the program displays a congratulations message.

If the email is invalid, the program shows the reason why it is invalid so the user can correct it and try again.

## Features

* Checks for invalid characters and spaces
* Checks for uppercase letters
* Validates the `@` symbol
* Checks username length
* Validates the domain name
* Supports `.com` and `.in` domains
* Displays the reason when an email is invalid
* Shows a success message for valid emails

## Concepts Used

* Functions
* If-Else Statements
* For Loop
* `break` Statement
* String Methods (`split()`, `count()`)
* Logical Operators (`and`, `or`, `not`)
* Boolean Flag (`is_valid`)

## How to Run

1. Clone this repository
2. Navigate to the project folder
3. Run the Python file:

```bash
python main.py
```

## Example

```text
=============================================
        📧 EMAIL VALIDATOR
=============================================

📩 Enter your email: example@gmail.com

---------------------------------------------
🎉 EMAIL STATUS: VALID
✅ Your email is valid. Congratulations!
---------------------------------------------
```

## Project Structure

```text
01-email-validator/
│
├── main.py
└── README.md
```

---

⭐ This project is part of my Python learning journey.
