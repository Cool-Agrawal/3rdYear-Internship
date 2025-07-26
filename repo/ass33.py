import sqlite3
import hashlib
import re

class User:
    def __init__(self,db_name = "db1.db"):
        self.conn_main = sqlite3.connect("db1.db")
        self.conn = self.conn_main.cursor()

    def validate_pwd(self, password):
        pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,20}$"
        return re.match(pattern, password)

    def hash_password(self, password):
        return hashlib.sha3_256(password.encode()).hexdigest()

    def register(self, Username, Password,is_logged_in):
        hashed = self.hash_password(Password)
        self.conn.execute("INSERT INTO USER (USER_NAME,PASSWORD ,IS_LOGGED_IN) VALUES (?,?,?)",
                     (Username, Password, is_logged_in))
        self.conn_main.commit()
        print("User registered successfully\n")
        self.conn.close()

    def login(self, username, password):
        hashed = self.hash_password(password)
        self.conn.execute("""UPDATE USER SET IS_LOGGED_IN = 1 
                               WHERE USER_NAME = ? AND PASSWORD = ? AND IS_LOGGED_IN != 1""",
                            (username, hashed))
        self.conn_main.commit()
        print("User logged in.")

    def logout(self):
        self.conn.execute("UPDATE USER SET IS_LOGGED_IN = 0 WHERE IS_LOGGED_IN == 1")
        self.conn_main.commit()
        print("User logged out.")

    def change_password(self, username, current_password, new_password):
        hashed_current = self.hash_password(current_password)
        self.conn.execute("SELECT PASSWORD FROM USER WHERE USER_NAME = ?", (username,))
        stored_pwd = self.conn.fetchone()
        if stored_pwd and stored_pwd[0] == hashed_current:
            if self.validate_pwd(new_password):
                hashed_new = self.hash_password(new_password)
                self.conn.execute("""UPDATE USER SET PASSWORD = ? 
                                       WHERE USER_NAME = ? AND IS_LOGGED_IN == 1""",
                                    (hashed_new, username))
                self.conn_main.commit()
                print("Password updated.")
            else:
                print("New password format invalid.")
        else:
            print("Invalid current password.")

    def close_connection(self):
        self.conn_main.close()
