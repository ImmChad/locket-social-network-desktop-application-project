# configdatabase.py

import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="locket_db",
        port=3307  # Thay your_mysql_port bằng cổng MySQL của bạn, ví dụ: 3306
    )


def check_login(username, password):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def get_friends(user_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Lấy danh sách bạn bè của người dùng với user_id
    query = "SELECT u.id, u.username, u.image FROM friends f JOIN users u ON f.userid2 = u.id WHERE f.userid1 = %s"
    cursor.execute(query, (user_id,))

    friends = cursor.fetchall()

    cursor.close()
    connection.close()

    return friends

def get_my_images(user_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Lấy danh sách bạn bè của người dùng với user_id
    query = "SELECT posts.image FROM posts WHERE posts.user_id = %s"
    cursor.execute(query, (user_id,))

    my_img = cursor.fetchall()

    cursor.close()
    connection.close()

    return my_img

def get_my_posts(user_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Lấy tất cả bài viết từ bảng posts
    query = "SELECT posts.*, users.username, users.image FROM posts LEFT JOIN users ON posts.user_id = users.id WHERE (posts.user_id = %s OR posts.reciever_id = %s OR (posts.reciever_id = 0 AND posts.user_id != %s))"
    cursor.execute(query, (user_id, user_id, user_id))

    posts = cursor.fetchall()

    cursor.close()
    connection.close()

    return posts

def insert_post(user_id, content, image, reciever_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Chèn bài viết vào bảng posts
    query = "INSERT INTO posts (user_id, content, image, reciever_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, content, image, reciever_id))

    # Lưu thay đổi và đóng kết nối
    connection.commit()
    cursor.close()
    connection.close()


    
