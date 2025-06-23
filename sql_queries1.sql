-- Find Employees Earning More Than Their Department’s Average Salary
select e.emp_name, e.salary, d.dept_name 
from employees e
join departments d on e.dept_id = d.dept_id
where e.salary > (select avg(salary) 
from employees where dept_id = e.dept_id);

-- Find Employees Who Worked on All Projects in Their Department
select e.emp_id, e.emp_name from employees e 
join projects p on e.emp_id = p.emp_id
group by e.emp_id, e.emp_name, e.dept_id
having count(distinct p.project_id) = (select count(distinct p2.project_id)
from projects p2 join employees e2 
on p2.emp_id = e2.emp_id
where e2.dept_id = e.dept_id);

-- Find the Highest-Paid Employee in Each Department Who Started After 2020
select e.emp_id, e.emp_name, e.dept_id, e.salary
from employees e 
where e.hire_date >= '2021-01-01' AND e.salary = (
select max(salary) from employees e2
where e2.dept_id = e.dept_id
and e2.hire_date >= '2021-01-01'
);
-- Find Departments Where All Employees Earn Above a Certain Threshold

select d.dept_id, d.dept_name 
from departments d
join employees e on d.dept_id = e.dept_id
group by  d.dept_id, d.dept_name 
having min(e.salary) > 50000;