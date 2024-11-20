# Write your MySQL query statement below
select em.unique_id, es.name from Employees as es left join  EmployeeUNI as  em on es.id = em.id