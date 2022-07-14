# Write your MySQL query statement below
select product_id
from Products
where low_fats NOT IN('N') AND recyclable NOT IN('N')