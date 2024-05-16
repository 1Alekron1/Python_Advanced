SELECT cus.full_name, man.full_name, ord.order_no FROM customer as cus
    JOIN "order" ord on cus.customer_id = ord.customer_id
    JOIN manager man on man.manager_id = cus.manager_id
WHERE cus.city != man.city