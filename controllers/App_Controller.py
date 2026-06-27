import mysql.connector

class MySQLConnection:
    def __init__(self):
        self.host = "localhost"                         # Địa chỉ máy chủ MySQL
        self.user = "restaurantManagementSoftware_user" # Tên người dùng MySQL
        self.password = "Vka9!U!u4!7!6He0"              # Mật khẩu MySQL
        self.database = "restaurantManagementSoftware"  # Tên database

    def connect(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conn        
        except mysql.connector.Error as err:
            print(f"Connection error: {err}")
            return None