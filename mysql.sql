CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL
);

-- Thêm dữ liệu vào bảng users
INSERT INTO users (username, password, image) VALUES
    ('kenny', '1234', 'images/avatars/avatar1.jpg'),
    ('eira', '1234', 'images/avatars/avatar2.jpg'),
    ('user3', '1234', 'images/avatars/avatar3.jpg'),
    ('user4', '1234', 'images/avatars/avatar4.jpg'),
    ('user5', 'pass5', 'images/avatars/avatar2.jpg'),
    ('user6', 'pass6', 'images/avatars/avatar1.jpg'),
    ('user7', 'pass7', 'images/avatars/avatar1.jpg'),
    ('user8', 'pass8', 'images/avatars/avatar2.jpg'),
    ('user9', 'pass9', 'images/avatars/avatar4.jpg'),
    ('user10', 'pass10', 'images/avatars/avatar3.jpg');


CREATE TABLE friends (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid1 INT NOT NULL,
    userid2 INT NOT NULL
);

-- Thêm dữ liệu vào bảng friends
INSERT INTO friends (userid1, userid2) VALUES
    (1, 2),
    (1, 3),
    (2, 3),
    (4, 5),
    (4, 6),
    (5, 6),
    (7, 8),
    (7, 9),
    (8, 9),
    (10, 1);

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content VARCHAR(50) NOT NULL,
    image TEXT NOT NULL,
	reciever_id INT NOT NULL
);

-- Thêm dữ liệu vào bảng posts
INSERT INTO posts (user_id, content, image, reciever_id) VALUES
    (1, 'text1', 'images/contents/content(5).png', 3),
    (1, 'text2', 'images/contents/content(3).png', 4),
    (2, 'text3', 'images/contents/content(2).png', 0),
    (2, 'text4', 'images/contents/content(1).png', 2),
		(2, 'text5', 'images/contents/content(4).png', 3),
    (2, 'text6', 'images/contents/content(5).png', 0),
		(2, 'text7', 'images/contents/content(3).png', 0),
    (2, 'text8', 'images/contents/content(2).png', 1),
    (3, 'text9', 'images/contents/content(1).png', 2),
    (3, 'text10', 'images/contents/content(2).png', 2),
    (3, 'text11', 'images/contents/content(3).png', 2),
    (4, 'text12', 'images/contents/content(1).png', 2),
    (4, 'text13', 'images/contents/content(4).png', 0),
    (4, 'text14', 'images/contents/content(5).png', 9);



