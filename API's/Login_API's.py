import re



def login(email,mobile,password):
    valid_email = "xyz@gmail.com"
    valid_mobile = "9999999999"
    valid_password = "1234@5678"

    if (email != valid_email or mobile != valid_mobile) and (password !=valid_password):
        print("You have login successfully")
    else:
        print('You have entered invalid')


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern,email)

def is_valid_password(password):
    # Check for all conditions
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[@#$%^&*!]', password)):
        return True
    return False

def signup(email,mobile,password):
    if not is_valid_email(email):
        print("Invalid email format")
        return
    if len(mobile) != 10 or not mobile.isdigit():
        print("Please enter the valid 10 digit mobile number")
        return
    if not is_valid_password(password):
        print(
            "Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character.")
        return
    print("You have signed up successfully")

signup("test.user@gmail.com","9999999999","Abcd@123")

def is_valid_mobile(number):
    return len(number) == 10 and number.isdigit()


def mobile_update():
    valid_mobile = "9999999999"
    prev_mobile = input("Enter the prev mobile number")
    if valid_mobile == prev_mobile:
        new_mobile = input("Enter the new mobile number")
        if is_valid_mobile(new_mobile):
            print("Your new mobile number has been updated")
        return new_mobile
    else:
        print("your current mobile number is incorrect please enter a valid mobile number")

def email_update():
    valid_email = "xyz@gmail.com"
    current_email = input("enter the current email")
    if valid_email == current_email:
        new_email = input("enter the new email")
        if is_valid_email(new_email):
            print("Your email updated successfully")
            return new_email

    else:
        print("your current email does not match with the available data")
def password_update():
    valid_password = "Abc@123"
    current_password = input("enter the current password")
    if valid_password == current_password:
        new_password = input("enter the new password")
        if is_valid_password(new_password):
            print("you have updated new password successfully")
            return new_password
        else:
            print("you have enter incorrect password as a current password")


