# Write your MySQL query statement below
select new_table.class
from (select * from courses group by student, class) as new_table
group by class
having count(class) >= 5
