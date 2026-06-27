from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

#Kết nối Cơ sở dữ liệu MySQL
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

# =========================================================
# AUTH
# =========================================================
# Trang đăng nhập
@app.route('/login')
def login():
    return render_template('login.html')


# =========================================================
# ADMIN ROUTES
# =========================================================
@app.route('/admin')
@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/index.html')


@app.route('/admin/menu')
def admin_menu():
    return render_template('admin/menu.html')


@app.route('/admin/staff')
def admin_staff():
    return render_template('admin/staff.html')


@app.route('/admin/table-management')
def admin_table_management():
    return render_template('admin/table_management.html')


@app.route('/admin/warehouse')
def admin_warehouse():
    return render_template('admin/warehouse.html')


# =========================================================
# KITCHEN ROUTES
# =========================================================
@app.route('/kitchen')
@app.route('/kitchen/dashboard')
def kitchen_dashboard():
    return render_template('kitchen/index.html')


# =========================================================
# STAFF ROUTES
# =========================================================
@app.route('/staff')
@app.route('/staff/dashboard')
def staff_dashboard():
    return render_template('staff/index.html')


# =========================================================
# USER ROUTES
# =========================================================
@app.route('/user')
@app.route('/user/dashboard')
def user_dashboard():
    return render_template('user/index.html')

# =========================================================
#  USER NHẬP MÃ BÀN ĂN
# =========================================================
@app.route('/')
# /join-table
@app.route('/join-table', methods=['GET', 'POST'])
def index():
    #requess form để lấy mã bàn ăn
    if request.method == 'POST':
        table_code = request.form.get('table_code')
        #truy vấn vào mã bàn ăn trong database để kiểm tra xem có tồn tại hay không
        #nếu tồn tại thì chuyen hướng đến trang đặt món ăn, nếu không tồn tại thì không làm gì cả
        conn = MySQLConnection().connect()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tables WHERE code = %s", (table_code,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if result:
                # Mã bàn tồn tại, chuyển hướng đến trang đặt món
                return f"<h1>Mã bàn ăn đã nhập: {table_code}</h1>"
            else:
                # Mã bàn không tồn tại
                return "<h1>Mã bàn ăn không hợp lệ</h1>"
        else:
            return "<h1>Lỗi kết nối cơ sở dữ liệu</h1>"
    return render_template('index.html')


# =========================================================
# ERROR HANDLER
# =========================================================
@app.errorhandler(404)
def not_found(error):
    return "<h1>404 - Page Not Found</h1>", 404


# =========================================================
# RUN APP
# =========================================================
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port = int(os.environ.get("PORT", 5000)),
        debug=True
    )