# create a register and login api with JWT token authentication

user_db = {}

def user_registration():
    user_mobile = input("please enther the 10 digit mobile number").strip()
    user_email = input("please enter the valid email id").strip()

    if not user_email and user_mobile:
        return ("error:","Both email and phone are required")
    if len(user_mobile) != 10 or not user_mobile.isdigit():
        return("please enter the valid mobile number")
    if '@' not in user_email or '.' not in user_email:
        return ("Invalid email format")
    if user_email in user_db:
        return ("this email is already registered")

    user_db[user_email] = {
        "mobile":user_mobile,
        "password":None
    }
    return {"message:","registered successfully"}

def forget_password():
    email = input("enter your email").strip()
    old_password = input("please enter any of the last password")
    if email not in user_db or user_db[email]["password"] != old_password:
        return ("error:","Old password is incorrect")
    return reset_password()
def reset_password():
    user_email = input("please enter the email").strip()
    user_mobile = input("please enter the mobile").strip()
    if user_email not in user_db or user_db[user_email]["mobile"] != user_mobile:
        return ("error:","invalid credentials")
    new_password = input("enter the new password").strip()
    confirm_password = input("confirm the password").strip()

    if new_password != confirm_password:
        return ("error:","please match the new_password and confirm_password")
    user_db[user_email]["password"] = new_password
    return {"message":"password has been reset successfully"}



