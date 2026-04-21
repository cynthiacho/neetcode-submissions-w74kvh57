SELECT DISTINCT title from content c 
JOIN tv_program t
ON c.content_id = t.content_id
WHERE program_date >= '2020-06-01' AND program_date < '2020-07-01'
AND kids_content = 'Y' AND content_type = 'Movies';