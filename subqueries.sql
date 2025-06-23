use w3schools;
--  product name with the highest price.
select productName, Price
from products
where price = (select max(price) from products);


-- products that have never ordered
select productName from products
where productId not in (select distinct productId 
from order_details);

-- all product names where the supplier is from a country where there is at least one customer.
select productname from products
where supplierId in (select supplierId from suppliers
where country in (select distinct country from customers)
);

-- supplier names who supply more than 2 products.
select suppliername from suppliers
where supplierId in (select supplierid from products 
group by supplierid 
having count(*) > 2
);

-- countries with more than 3 customers and sort by number of customers descending.
select country , count(*) as customer_count
from customers
group by country
having count(*) > 3
order by customer_count desc;