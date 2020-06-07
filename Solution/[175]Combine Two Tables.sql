# Write your MySQL query statement below
Select A.FirstName, A.LastName, B.City, B.State
From Person as A left join Address as B
on A.PersonId = B.PersonId