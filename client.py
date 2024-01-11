import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
import socketio
from tkinter import messagebox


user = []
friends = []
my_imgs = []
posts = []

class SocketIOManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SocketIOManager, cls).__new__(cls)
            cls._instance.sio = socketio.Client()
        return cls._instance

    def __init__(self):
        self.user = None

    def connect_server(self):
        @self.sio.event
        def connect():
            print('Connected to server')

        @self.sio.event
        def disconnect():
            print('Disconnected from server')
            
        @self.sio.event
        def login_success(data):
            print('Login successful')
            # Hiển thị thông báo khi đăng nhập thành công
            messagebox.showinfo("Success", "Login sucessfully!")
            user = data
            
        @self.sio.event
        def update_list_friend(data):
            friends = data

        @self.sio.event
        def update_my_images(data):
            my_imgs = data
            
        @self.sio.event
        def update_my_posts(data):
            posts = data
            
        @self.sio.event
        def login_failed():
            print('Login failed')
            # Hiển thị thông báo khi đăng nhập thất bại
            messagebox.showerror("Error", "Login failed. Invalid username or password.")



        self.sio.connect('http://localhost:9999')

    def login(self, username, password):
        # Gửi thông tin đăng nhập tới server (giả sử sử dụng sự kiện 'login')
        self.sio.emit('login', {'username': username, 'password': password})


socketio_manager = SocketIOManager()
socketio_manager.connect_server()

def submit_login():
    username = username_entry.get()
    password = password_entry.get()
    
    socketio_manager.login(username, password)



login_window = tk.Tk()
login_window.title("Login Interface")

# Thiết lập kích thước cửa sổ
window_width = 600
window_height = 400
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))
login_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")



# Load hình ảnh background và hiển thị nó
background_image = Image.open("images/layouts/background.png")  # Thay đường dẫn đến hình ảnh của bạn
background_image = background_image.resize((600, 400))  # Đổi kích thước hình ảnh
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(login_window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# Thiết kế giao diện đăng nhập bằng Frame
# frame = tk.Frame(login_window, padx=20, pady=10, bg="#FFC0CB", bd=0)  # Màu hồng nhạt (#FFC0CB)
frame = customtkinter.CTkFrame(login_window, width=500, height=350, fg_color="#FFC0CB", corner_radius=10, border_color="white")
frame.pack(padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")


# Giao diện đăng nhập nằm trong frame
title_label = tk.Label(frame, text="LOGIN", font=("Arial", 20, "bold"), fg="white", bg="#FFC0CB")  # Màu hồng nhạt (#FFC0CB)
title_label.grid(row=0, columnspan=2, padx=5, pady=10)

username_label = tk.Label(frame, text="USERNAME:", font=("Arial", 10, "bold"), fg="white", bg="#FFC0CB")  # Màu hồng nhạt (#FFC0CB)
username_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

# username_entry = tk.Entry(frame, font=("Arial", 12), width=20)
username_entry = customtkinter.CTkEntry(frame, font=("Arial", 12), width=190, fg_color="white", text_color="black", border_color="white")
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(frame, text="PASSWORD:", font=("Arial", 10, "bold"), fg="white", bg="#FFC0CB")  # Màu hồng nhạt (#FFC0CB)
password_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

# password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=20)
password_entry = customtkinter.CTkEntry(frame, font=("Arial", 12), width=190, fg_color="white", text_color="black", show="*", border_color="white")
password_entry.grid(row=2, column=1, padx=5, pady=5)

# back_button = tk.Button(frame, text="BACK", font=("Arial", 10, "bold"), command=login, bg="#FFFFFF", fg="black", activebackground="#C71585", padx=10)  # Màu hồng (#FF1493)
# back_button.grid(row=3, columnspan=2, padx=5, pady=10)

submit_button = customtkinter.CTkButton(frame, text="SUBMIT", font=("Arial", 10, "bold"), text_color="white", fg_color=("#FF1493"), hover=False, command=submit_login) 
submit_button.grid(row=3, columnspan=2, padx=5, pady=10)

login_window.mainloop()


