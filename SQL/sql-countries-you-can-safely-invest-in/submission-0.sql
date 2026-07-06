-- Write your query below

--Write a query to find the countries where the average call 
--duration is strictly greater than the global average. 
--A call is associated with a country based on the phone numbers 
--of both the caller and callee.

SELECT c.name AS country
FROM person p
JOIN country c ON SUBSTRING(p.phone_number, 1, 3) = c.country_code
JOIN calls ca ON p.id = ca.caller_id OR p.id = ca.callee_id
GROUP BY c.name
HAVING AVG(ca.duration) > (SELECT AVG(duration) FROM calls);
