import tkinter as tk
import customtkinter
from PIL import Image, ImageTk, ImageDraw


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
    # Hàm xử lý chức năng upload ảnh
    pass

def run_app():
    # Tạo cửa sổ gốc
    root = tk.Tk()
    root.geometry("1100x680")
    root.configure(bg="white")

    # Tạo panel chính
    panel_home = tk.Frame(root, width=1100, height=680, bg="white")
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
    image_frames = create_image_frames(image_list, scrollable_frame2)



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
    root.mainloop()
    
run_app()