import sqlite3
import hashlib
import re
while True:
    conn_main = sqlite3.connect("db1.db")
    conn = conn_main.cursor()
    print("1.Register\n")
    print("2.Login\n")
    print("3. Logout\n")
    print("4.Change password\n")
    print("5.Exit\n")
    choice = int(input("Enter choice\n"))
    match choice:
        case 1:

            def check():
                while True:
                    Username = input("Enter a username\n")
                    if Username.strip():
                        return Username
                    else:
                        print("Enter a valid username\n")

            Username = check()
            Password = input("Enter password\n")
            Pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,20}$"
            def password_check(Pattern,Password):
                if re.match(Pattern,Password):
                    return Password
            password_check(Pattern, Password)
            hash_object = hashlib.sha3_256(Password.encode())
            hash_hex = hash_object.hexdigest()
            is_logged_in = 0

            #conn.execute("CREATE TABLE USER (USER_NAME VARCHAR(50) PRIMARY KEY,PASSWORD VARCHAR(20) ,IS_LOGGED_IN INTEGER)")
            conn.execute( "INSERT INTO USER (USER_NAME,PASSWORD ,IS_LOGGED_IN) VALUES (?,?,?)", (Username,Password,is_logged_in))
            conn_main.commit()
            print("User registered successfully\n")
            conn.close()

        case 2:
            def check():
                while True:
                    login_name = input("Enter a username\n")
                    if login_name.strip():
                        return login_name
                    else:
                        print("Enter a valid username\n")

            login_name = check()
            login_pwd = input("Enter password\n")
            conn.execute("UPDATE USER SET IS_LOGGED_IN = 1 WHERE USER_NAME = ? AND PASSWORD = ? AND IS_LOGGED_IN != ?",
                         (login_name, login_pwd, 1))
            print("User login successfully\n")
            conn.close()

        case 3:
            conn.execute("UPDATE USER SET IS_LOGGED_IN = 0 WHERE IS_LOGGED_IN == 1")
            print("User logout successfully\n")
            conn.close()

        case 4:
            def check():
                while True:
                    Username = input("Enter a username\n")
                    if Username.strip():
                        return Username
                    else:
                        print("Enter a valid username\n")

            Username = check()
            curr_pwd = input("Enter current password\n")
            hash_object = hashlib.sha3_256(curr_pwd.encode())
            hash_e = hash_object.hexdigest()
            conn.execute("SELECT Password FROM USER where user_name =?", (Username,))
            password = conn.fetchone()
            if curr_pwd == password[0]:
                updated_pwd = input("Enter updated password")
                Pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,20}$"
                def password_check(Pattern, Password):
                    if re.match(Pattern, Password):
                        return Password
                password_check(Pattern, updated_pwd)
                hash_object = hashlib.sha3_256(updated_pwd.encode())
                hash_h = hash_object.hexdigest()
                conn.execute("UPDATE USER SET PASSWORD = ? where user_name == ? and IS_LOGGED_IN == ?",(updated_pwd,Username,1))
                print("Password updated successfully\n")
                conn_main.commit()
            else:
                print("Invalid")

            conn.close()
        case 5:
            quit()