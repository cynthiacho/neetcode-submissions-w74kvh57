-- Write your query below

WITH RECURSIVE subtask_numbers AS (
    SELECT task_id, 1 AS subtask_id, subtasks_count
    FROM tasks
    UNION ALL
    SELECT task_id, subtask_id + 1, subtasks_count
    FROM subtask_numbers
    WHERE subtask_id < subtasks_count
)
SELECT s.task_id, s.subtask_id
FROM subtask_numbers s
LEFT JOIN executed e
    ON s.task_id = e.task_id AND s.subtask_id = e.subtask_id
WHERE e.task_id IS NULL;
