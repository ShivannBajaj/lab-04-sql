CREATE TABLE users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100),
    content TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES
(1, 'Alex', 'Smith', 'alex@email.com'),
(2, 'Jordan', 'Lee', 'jordan@email.com'),
(3, 'Taylor', 'Brown', 'taylor@email.com'),
(4, 'Morgan', 'Davis', 'morgan@email.com'),
(5, 'Casey', 'Wilson', 'casey@email.com'),
(6, 'Jamie', 'Moore', 'jamie@email.com'),
(7, 'Riley', 'Taylor', 'riley@email.com'),
(8, 'Avery', 'Anderson', 'avery@email.com'),
(9, 'Cameron', 'Thomas', 'cameron@email.com'),
(10, 'Drew', 'Jackson', 'drew@email.com');

INSERT INTO posts VALUES
(1, 1, 'First Post', 'This is my first post.', '2026-09-01 10:00:00'),
(2, 2, 'SQL Basics', 'Learning SQL today.', '2026-09-02 11:00:00'),
(3, 3, 'Python', 'Working with Python.', '2026-09-03 12:00:00'),
(4, 1, 'Databases', 'Databases are useful.', '2026-09-04 13:00:00'),
(5, 4, 'Data Science', 'Studying data science.', '2026-09-05 14:00:00'),
(6, 5, 'Machine Learning', 'Starting ML.', '2026-09-06 15:00:00'),
(7, 6, 'Pandas', 'Using pandas DataFrames.', '2026-09-07 16:00:00'),
(8, 7, 'MySQL', 'Working with MySQL.', '2026-09-08 17:00:00'),
(9, 8, 'Analytics', 'Analyzing some data.', '2026-09-09 18:00:00'),
(10, 9, 'Final Post', 'Finishing the assignment.', '2026-09-10 19:00:00');
