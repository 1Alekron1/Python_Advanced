SELECT cus.full_name FROM customer as cus
    WHERE NOT EXISTS(
        SELECT 1 FROM "order" as ord
            WHERE ord.customer_id == cus.customer_id
        )