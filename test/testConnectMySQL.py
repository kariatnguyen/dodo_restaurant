import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="restaurantManagementSoftware_user",
            password="Vka9!U!u4!7!6He0",
            database="restaurantManagementSoftware"
        )
        print("connect successfully")
        return conn
    except Exception as e:
        print("error:", e)
        return None
    
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        conn.close()