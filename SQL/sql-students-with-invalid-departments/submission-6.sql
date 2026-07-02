SELECT id, name 
FROM students
WHERE NOT EXISTS (SELECT 1 FROM departments d WHERE d.id = students.department_id);