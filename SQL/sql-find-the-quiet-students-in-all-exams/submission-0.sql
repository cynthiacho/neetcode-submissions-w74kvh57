-- Write your query below

WITH exam_stats AS (
    SELECT
        exam_id,
        MAX(score) AS max_score,
        MIN(score) AS min_score
    FROM exam
    GROUP BY exam_id
),
loud_students AS (
    SELECT DISTINCT e.student_id
    FROM exam e
    JOIN exam_stats es ON e.exam_id = es.exam_id
    WHERE e.score = es.max_score OR e.score = es.min_score
)
SELECT s.student_id, s.student_name
FROM student s
WHERE s.student_id IN (SELECT student_id FROM exam)
  AND s.student_id NOT IN (SELECT student_id FROM loud_students)
ORDER BY s.student_id;
