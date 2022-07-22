# Write your MySQL query statement below
SELECT name FROM SalesPerson Where sales_id NOT IN
(SELECT a.sales_id FROM Orders a JOIN Company b on a.com_id = b.com_id WHERE b.name = 'RED')