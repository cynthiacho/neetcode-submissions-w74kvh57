SELECT employee_id, COUNT(team_id) OVER(PARTITION BY team_id) as team_size
FROM employee;

SELECT e.employee_id, COUNT(*) OVER (PARTITION BY e.team_id) AS team_size
FROM employee e;
