select e.name as employee from employee e  JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;