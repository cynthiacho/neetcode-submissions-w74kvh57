-- Write your query below
SELECT actor_id, director_id
FROM actor_director 
group by actor_id, director_id
having count(*) >= 3;