SELECT
    users.first_name,
    users.last_name,
    posts.title,
    posts.created_at
FROM users
JOIN posts
    ON users.user_id = posts.user_id
WHERE posts.created_at >= '2026-09-05';
