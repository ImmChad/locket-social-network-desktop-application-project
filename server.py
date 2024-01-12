import socketio
import threading
import tkinter as tk
from tkinter import scrolledtext
from flask import Flask
import configdatabase  

class Service:
    instance = None

    def __init__(self, text_area):
        self.text_area = text_area
        self.list_client = []
        self.list_user_id_client = []

    @classmethod
    def get_instance(cls, text_area):
        if cls.instance is None:
            cls.instance = cls(text_area)
        return cls.instance

    def start_server(self):
        sio = socketio.Server(cors_allowed_origins='*')
        app = Flask(__name__)

        @sio.event
        def connect(sid, environ):
            self.text_area.insert(tk.END, f"One client connected with SID: {sid}\n")

        @sio.event
        def disconnect(sid):
            user_id = self.remove_client(sid)
            if user_id:
                self.user_disconnect(user_id)
                
        
        @sio.on('login')  # Thêm sự kiện đăng nhập
        def login(sid, data):
            username = data.get('username')
            password = data.get('password')
            user = configdatabase.check_login(username, password)
            if user:
                friends = configdatabase.get_friends(user['id']) 
                my_img = configdatabase.get_my_images(user['id'])
                posts = configdatabase.get_my_posts(user['id'])
                print(user)
                print(friends)
                print(my_img)         
                print(posts)      
                # Gửi thông tin user về cho client (ví dụ)
                sio.emit('login_success', user, room=sid)
                sio.emit('update_list_friend', friends, room=sid)
                sio.emit('update_my_images', my_img, room=sid)
                sio.emit('update_my_posts', posts, room=sid)
                # Thêm SID của client vào danh sách
                self.list_client.append(sid)
                self.text_area.insert(tk.END, f"One client connected with SID: {self.list_client}\n")
                
            else:
                # Gửi thông báo lỗi về cho client (ví dụ)
                sio.emit('login_failed', room=sid)

        @sio.on('insert_post')  # Thêm sự kiện post
        def insert_post(sid, data):
            print("post")
            print(data)
            
            content = data.get('content')
            img = data.get('image')
            user_id = data.get('user_id')
            reciever_id = data.get('reciever_id')
            configdatabase.insert_post(user_id, content, img, reciever_id)
            friends = configdatabase.get_friends(user_id) 
            
            for i in self.list_client:
                sio.emit('notify_post', friends, room=i)
            
            
        @sio.on('load_after_insert_post')  # Thêm sự kiện post
        def load_after_insert_post(sid, data):
            user_id = data.get('user_id')
            
            friends = configdatabase.get_friends(user_id) 
            my_img = configdatabase.get_my_images(user_id)
            posts = configdatabase.get_my_posts(user_id)
            
            sio.emit('update_list_friend', friends, room=sid)
            sio.emit('update_my_images', my_img, room=sid)
            sio.emit('update_my_posts', posts, room=sid)

        port = 9999
        self.text_area.insert(tk.END, f"Server is running on http://localhost:{port}\n")

        app = socketio.WSGIApp(sio, app)
        import eventlet
        eventlet.wsgi.server(eventlet.listen(('localhost', port)), app)
        
        

    def user_disconnect(self, user_id):
        for sid in self.list_client:
            sio.emit('user_status', (user_id, False), room=sid)

    def remove_client(self, sid):
        if sid in self.list_client:
            self.list_client.remove(sid)
            return 1  # Replace this with the actual user ID
        return 0


class ServerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Server UI")
        self.root.geometry("400x300")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Server", command=self.start_server)
        self.start_button.pack(pady=10)

        self.service = None
        self.server_thread = None

    def start_server(self):
        self.text_area.delete(1.0, tk.END)  # Clear previous content
        self.service = Service.get_instance(self.text_area)

        # Create a new thread to run the server
        self.server_thread = threading.Thread(target=self.service.start_server)
        self.server_thread.start()

def main():
    root = tk.Tk()
    app = ServerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
