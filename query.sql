SELECT DISTINCT
    Users.name,
    Users.email
FROM Users
JOIN Orders
    ON Users.id = Orders.user_id
WHERE Orders.order_total > 100;