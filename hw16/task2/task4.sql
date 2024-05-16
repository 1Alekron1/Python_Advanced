SELECT cus.full_name, ord.order_no FROM customer as cus
    JOIN "order" ord on cus.customer_id = ord.customer_id
    WHERE cus.manager_id IS NULL