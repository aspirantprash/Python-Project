#Email Validator Project 

print("\n" + "=" * 45)
print("        📧 EMAIL VALIDATOR")
print("=" * 45)

def validate_email():

    email = input("\n📩 Enter your email: ").strip().lower()

    is_valid = True

    # Check space and invalid symbols
    for ch in email:
        if ch in " !#$%^&*()=+{}[]|\\:;\"'<>?,/" or ch.isspace():
            print("\n⚠️ Error: Extra character or space found.")
            is_valid = False
            break

    # Check capital letters
    for ch in email:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("\n⚠️ Error: Capital letters are not allowed.")
            is_valid = False
            break

    # Empty check
    if not email:
        print("\n⚠️ Error: Email cannot be empty.")
        is_valid = False
    
    # Length check
    if len(email) > 50:
        print("\n⚠️ Error: Email is too long.")
        is_valid = False

    
    # Check @ symbol
    if email.count("@") != 1:
        print("\n⚠️ Error: Email must contain exactly one '@' symbol.")
        is_valid = False

    else:
        username, domain = email.split("@")

        if len(username) <= 3:
            print("\n⚠️ Error: Username must be at least 3 characters.")
            is_valid = False

        if username.startswith('.') or username.endswith('.'):
            print("\n⚠️ Error: Username cannot start or end with a dot.")
            is_valid = False

        if "." not in domain:
            print("\n⚠️ Error: Domain format is incorrect.")
            is_valid = False

        else:
            domainName, tldomain = domain.rsplit(".", 1)

            if domainName != "gmail":
                print("\n⚠️ Error: Only Gmail addresses are allowed.")
                is_valid = False

            if tldomain not in ["com", "in", "org", "co.in"]:
                print("\n⚠️ Error: Only .com, .in, .org, and .co.in domains are allowed.")
                is_valid = False

    # Final Result
    print("\n" + "-" * 45)

    if is_valid:
        print("🎉 EMAIL STATUS: VALID")
        print("✅ Your email is valid. Congratulations!")
    else:
        print("❌ EMAIL STATUS: INVALID")
        print("🔍 Please check the errors above and try again.")

    print("-" * 45)


validate_email()

# Multiple email testing option
if __name__ == "__main__":
    while True:
        validate_email()
        choice = input("\n🔄 Check another email? (yes/no): ").lower()
        if choice != 'yes':
            print("\n👋 Thank you for using Email Validator!")
            break