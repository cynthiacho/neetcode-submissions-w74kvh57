-- Write your query below

select email
FROM person
group by email
having count(*) > 1;