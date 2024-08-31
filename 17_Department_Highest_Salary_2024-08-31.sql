select e.name as employee,d.name as Department ,salary FROM employee e
JOIN department d ON e.departmentId = d.id 
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);