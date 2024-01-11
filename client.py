import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
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
            showHome()
            
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


def showHome():
    def upload_popup(root):
        popup = tk.Frame(root, width=480, height=480, bg="white")
        label = tk.Label(popup, text="This is the upload popup.", padx=10, pady=10)
        label.pack()

        close_button = tk.Button(popup, text="Close Popup", command=popup.destroy)
        close_button.pack()

    def load_images(image_paths):
        images = []
        for path in image_paths:
            img = Image.open(path)
            img = img.resize((90, 90), Image.ANTIALIAS)
            img_photo = ImageTk.PhotoImage(img)
            images.append(img_photo)
        return images

    images_per_row = 3

    def create_image_frames(images, scrollable_frame):
        frames = []
        for i, img in enumerate(images):
            frame = customtkinter.CTkFrame(scrollable_frame, width=90, height=90)
            img_label = tk.Label(frame, image=img, bg="white")
            img_label.image = img
            img_label.pack(fill=tk.BOTH, expand=True)
            frame.grid(row=i // images_per_row, column=i % images_per_row, padx=5, pady=5)
            frames.append(frame)
        return frames

    def capture_photo():
        # Hàm xử lý chức năng chụp ảnh
        pass

    def upload_photo():
    
        pass

    
    # Tạo cửa sổ gốc
    home_window = tk.Toplevel()
    home_window.title("Home")
    
    # login_window.destroy()

    # Thiết lập kích thước cửa sổ
    window_width = 1100
    window_height = 680
    screen_width = home_window.winfo_screenwidth()
    screen_height = home_window.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))
    home_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    

    # Tạo panel chính
    panel_home = tk.Frame(home_window, width=1100, height=680, bg="white")
    panel_home.pack(fill=tk.BOTH, expand=True)

    # Tạo frame bên trái
    frame_left = tk.Frame(panel_home, width=300, height=680, bg="white")
    frame_left.pack(side=tk.LEFT)

    # Tạo frame ở giữa
    # frame_middle = tk.Frame(panel_home, width=480, height=680, bg="black")
    frame_middle = customtkinter.CTkFrame(panel_home, width=480, height=680, fg_color="white", border_color="#FF69B4", border_width=5)
    frame_middle.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Tạo frame bên phải
    frame_right = tk.Frame(panel_home, width=300, height=680, bg="lightgrey")
    frame_right.pack(side=tk.LEFT)

    # Tạo các widget trong frame bên trái
    label_friends = tk.Label(frame_left, text="Friend List", bg="white", fg="pink", font=("Arial", int(1.2 * 16), "bold"))
    label_friends.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    scrollable_frame = customtkinter.CTkScrollableFrame(frame_left, width=300, height=680, fg_color="white")
    scrollable_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    
    friends = [
        {"name": "Friend 1", "avatar": "images/avatars/avatar1.jpg"},
        {"name": "Friend 2", "avatar": "images/avatars/avatar2.jpg"},
        {"name": "Friend 3", "avatar": "images/avatars/avatar3.jpg"},
        {"name": "Friend 4", "avatar": "images/avatars/avatar4.jpg"},
        {"name": "Friend 5", "avatar": "images/avatars/avatar1.jpg"},
        {"name": "Friend 3", "avatar": "images/avatars/avatar1.jpg"},
        {"name": "Friend 4", "avatar": "images/avatars/avatar2.jpg"},
        {"name": "Friend 5", "avatar": "images/avatars/avatar3.jpg"},
        {"name": "Friend 3", "avatar": "images/avatars/avatar1.jpg"},
        {"name": "Friend 4", "avatar": "images/avatars/avatar4.jpg"},
        {"name": "Friend 5", "avatar": "images/avatars/avatar1.jpg"},
    ]

    for i, friend in enumerate(friends):
        friend_frame = tk.Frame(scrollable_frame, width=300, height=136, bg="white")
        friend_frame.pack(pady=5)

        # Phần trái - Avatar
        # avatar_frame = tk.Frame(friend_frame, width=75, height=75, bg="white", bd=1, relief="solid")
        avatar_frame = customtkinter.CTkFrame(friend_frame, width=75, height=75)
        avatar_frame.pack(side=tk.LEFT, padx=10)

        # Load ảnh và thay đổi kích thước

        avatar_image = Image.open(friend["avatar"])
        avatar_image = avatar_image.resize((75, 75))

        # Tạo ảnh hình tròn từ ảnh đã chỉnh kích thước
        mask = Image.new("L", (75, 75), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 75, 75), fill=255)
        avatar_image = Image.composite(avatar_image, Image.new("RGB", avatar_image.size), mask)

        # Tạo ảnh đệm từ ảnh đã chỉnh kích thước
        avatar_photo = ImageTk.PhotoImage(avatar_image)

        # Hiển thị ảnh trên khung avatar
        avatar_label = tk.Label(avatar_frame, image=avatar_photo, bg="white")
        avatar_label.image = avatar_photo
        avatar_label.pack()

        # Phần phải - Tên friend
        name_label = tk.Label(friend_frame, text=friend["name"], bg="white", fg="black", font=("Arial", 12))
        name_label.pack(side=tk.LEFT)

    scrollable_frame2 = customtkinter.CTkScrollableFrame(frame_right, width=300, height=680, fg_color="black")
    scrollable_frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    image_paths = [
        "images/avatars/avatar1.jpg",
        "images/avatars/avatar2.jpg",
        "images/avatars/avatar3.jpg",
        "images/avatars/avatar4.jpg",
        "images/avatars/avatar1.jpg",
        "images/avatars/avatar2.jpg",
        "images/avatars/avatar3.jpg",
        "images/avatars/avatar4.jpg",
        "images/avatars/avatar1.jpg",
        "images/avatars/avatar2.jpg",
        "images/avatars/avatar3.jpg",
        "images/avatars/avatar4.jpg",
    ]

    image_list = load_images(image_paths)
    create_image_frames(image_list, scrollable_frame2)

    # Frame 1
    frame1 = customtkinter.CTkFrame(frame_middle, width=400, height=400, fg_color="white", border_color="black", border_width=5 ) 
    frame1.pack(pady=20)

    # Frame 2
    frame2 = customtkinter.CTkFrame(frame_middle, width=400, height=50, fg_color="lightgreen") 
    frame2.pack()


    scrollbar = customtkinter.CTkScrollableFrame(frame1, width=400, height=400,  fg_color="white")
    scrollbar.pack(side=tk.RIGHT, fill="y")


    # Adding widgets to Canvas Frame
    for i in range(10):
        # Frame inside Canvas
        canvas_frame = customtkinter.CTkFrame(scrollbar, width=400, height=400, fg_color="red")
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        label = customtkinter.CTkLabel(canvas_frame, text=f"Frame {i+1}", fg_color="transparent")
        label.place(relx=0.5, rely=0.5, anchor="center")


    # Buttons on Frame 2
    upload_button = tk.Button(frame2, text="Upload", command=upload_popup(root))
    upload_button.grid(row=0, column=0, padx=10, pady=10)

    # Chạy ứng dụng
    home_window.mainloop()
    

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


