-- Find Customers Whose Total Order Amount Exceeds the 
-- Average Order Amount in Their Region
select c.customer_id, c.customer_name
from customers c join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name, c.region
having sum(o.total_amount) > (select avg(o.total_amount) from orders o2 
join customers c2 on  c2.customer_id = o2.customer_id
where c2.region = e2.region);

-- Find Orders Containing Products from All Categories
select od.order_id
from order_details od join
products p on od.product_id = p.product_id
group by od.order_id
having count(distinct p.category) = (select count(distinct category) 
from products);

-- Find the Most Expensive Product Ordered by Each Customer
--  After a Specific Date
with expensive_prod as (select p.product_id, p.product_name,o.customer_id,od.unit_price,
row_number() over (partition by o.customer_id order by od.unit_price desc) as rnk
from products p 
join order_details od on p.product_id = od.product_id
join orders o on od.order_id = o.order_id
where o.order_date > '2023-01-10'
)
select customer_id,product_id,unit_price
from expensive_prod
where rnk = 1;


-- Find Regions Where No Customer Ordered a Specific Product
select distinct(region) from customers
where region not in (
select distinct(c.region) from customers c 
left join orders o on c.customer_id = o.customer_id
left join order_details od on o.order_id = od.order_id
where od.product_id = 201);
