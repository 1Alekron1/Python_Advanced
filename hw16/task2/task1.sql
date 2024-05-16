SELECT cus.full_name, m.full_name, o.date, o.purchase_amount FROM customer AS cus
    JOIN manager m on cus.manager_id = m.manager_id
    JOIN "order" o on cus.customer_id = o.customer_id