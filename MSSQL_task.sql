-- 3.1
SELECT 
    s.LastName + ' ' + s.FirstName + ' ' + ISNULL(s.MiddleName, '') AS FullName,
    CASE WHEN s.Budget = 1 THEN 'Бюджет' ELSE 'Внебюджет' END AS Status,
    g.GroupName,
    d.DirectionName
FROM Students s
JOIN Groups g ON s.GroupID = g.GroupID
JOIN Directions d ON g.DirectionID = d.DirectionID
WHERE d.DirectionName = 'Physics'
ORDER BY s.LastName, s.FirstName, s.MiddleName;


-- 3.2
SELECT 
    s.LastName + ' ' + s.FirstName + ' ' + ISNULL(s.MiddleName, '') AS FullName,
    g.GroupName,
    d.DirectionName
FROM Students s
JOIN Groups g ON s.GroupID = g.GroupID
JOIN Directions d ON g.DirectionID = d.DirectionID
WHERE s.LastName LIKE 'P%'
ORDER BY s.LastName, s.FirstName, s.MiddleName;


-- 3.3
SELECT 
    s.LastName + ' ' + LEFT(s.FirstName, 1) + '.' + LEFT(s.MiddleName, 1) + '.' AS FullName,
    DAY(s.BirthDate) AS BirthDay,
    DATENAME(MONTH, s.BirthDate) AS BirthMonth,
    g.GroupName,
    d.DirectionName
FROM Students s
JOIN Groups g ON s.GroupID = g.GroupID
JOIN Directions d ON g.DirectionID = d.DirectionID
ORDER BY MONTH(s.BirthDate), DAY(s.BirthDate), s.LastName, s.FirstName, s.MiddleName;


-- 3.4
SELECT 
    s.LastName + ' ' + s.FirstName + ' ' + ISNULL(s.MiddleName, '') AS FullName,
    DATEDIFF(YEAR, s.BirthDate, GETDATE()) AS Age
FROM Students s
ORDER BY Age, s.LastName, s.FirstName, s.MiddleName;


-- 3.5
SELECT 
    s.LastName + ' ' + s.FirstName + ' ' + ISNULL(s.MiddleName, '') AS FullName,
    g.GroupName,
    d.DirectionName,
    DAY(s.BirthDate) AS BirthDay
FROM Students s
JOIN Groups g ON s.GroupID = g.GroupID
JOIN Directions d ON g.DirectionID = d.DirectionID
WHERE MONTH(s.BirthDate) = MONTH(GETDATE())
ORDER BY BirthDay, s.LastName, s.FirstName, s.MiddleName;


-- 3.6
SELECT 
    d.DirectionName,
    COUNT(s.StudentID) AS StudentCount
FROM Students s
JOIN Groups g ON s.GroupID = g.GroupID
JOIN Directions d ON g.DirectionID = d.DirectionID
GROUP BY d.DirectionName
ORDER BY StudentCount DESC;


-- 3.7
SELECT 
    g.GroupName,
    d.DirectionName,
    SUM(CASE WHEN s.Budget = 1 THEN 1 ELSE 0 END) AS BudgetCount,
    SUM(CASE WHEN s.Budget = 0 THEN 1 ELSE 0 END) AS NonBudgetCount
FROM Students s
JOIN Groups g ON s.GroupID = g.GroupID
JOIN Directions d ON g.DirectionID = d.DirectionID
GROUP BY g.GroupName, d.DirectionName
ORDER BY g.GroupName, d.DirectionName;


-- 5.1
SELECT 
    sub.SubjectName,
    t.LastName + ' ' + t.FirstName + ' ' + ISNULL(t.MiddleName, '') AS TeacherName,
    g.GroupName
FROM Subjects sub
JOIN Teachers t ON sub.TeacherID = t.TeacherID
JOIN Directions d ON sub.DirectionID = d.DirectionID
JOIN Groups g ON d.DirectionID = g.DirectionID
ORDER BY sub.SubjectName, g.GroupName;


-- 5.2
SELECT TOP 1
    sub.SubjectName,
    COUNT(g.GradeID) AS StudentCount
FROM Grades g
JOIN Subjects sub ON g.SubjectID = sub.SubjectID
GROUP BY sub.SubjectName
ORDER BY StudentCount DESC;


-- 5.3
SELECT 
    t.LastName + ' ' + t.FirstName + ' ' + ISNULL(t.MiddleName, '') AS TeacherName,
    COUNT(DISTINCT g.StudentID) AS StudentCount
FROM Teachers t
JOIN Subjects sub ON t.TeacherID = sub.TeacherID
JOIN Grades g ON sub.SubjectID = g.SubjectID
GROUP BY t.LastName, t.FirstName, t.MiddleName
ORDER BY StudentCount DESC;


-- 5.4
SELECT 
    sub.SubjectName,
    CAST(SUM(CASE WHEN g.Grade >= 3 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(g.GradeID) AS PassRate
FROM Grades g
JOIN Subjects sub ON g.SubjectID = sub.SubjectID
GROUP BY sub.SubjectName
ORDER BY PassRate DESC;


-- 5.5
SELECT 
    sub.SubjectName,
    AVG(CAST(g.Grade AS FLOAT)) AS AverageGrade
FROM Grades g
JOIN Subjects sub ON g.SubjectID = sub.SubjectID
WHERE g.Grade >= 3
GROUP BY sub.SubjectName
ORDER BY AverageGrade DESC;


-- 5.6
SELECT TOP 1
    g.GroupName,
    AVG(CAST(gr.Grade AS FLOAT)) AS AverageGrade
FROM Grades gr
JOIN Students s ON gr.StudentID = s.StudentID
JOIN Groups g ON s.GroupID = g.GroupID
GROUP BY g.GroupName
ORDER BY AverageGrade DESC;


-- 5.7
SELECT 
    s.LastName + ' ' + s.FirstName + ' ' + ISNULL(s.MiddleName, '') AS FullName,
    g.GroupName
FROM Students s
JOIN Grades gr ON s.StudentID = gr.StudentID
JOIN Groups g ON s.GroupID = g.GroupID
GROUP BY s.StudentID, s.LastName, s.FirstName, s.MiddleName, g.GroupName
HAVING MIN(gr.Grade) >= 5;


-- 5.8
SELECT 
    s.LastName + ' ' + s.FirstName + ' ' + ISNULL(s.MiddleName, '') AS FullName,
    g.GroupName,
    COUNT(gr.GradeID) AS FailedSubjects
FROM Students s
JOIN Grades gr ON s.StudentID = gr.StudentID
JOIN Groups g ON s.GroupID = g.GroupID
WHERE gr.Grade < 3
GROUP BY s.StudentID, s.LastName, s.FirstName, s.MiddleName, g.GroupName
HAVING COUNT(gr.GradeID) >= 2
ORDER BY FailedSubjects DESC;


-- 7.1
SELECT 
    sub.SubjectName,
    COUNT(*) AS [Количество посещенных занятий]
FROM 
    Attendance a
    JOIN Schedules s ON a.ScheduleID = s.ScheduleID
    JOIN Subjects sub ON s.SubjectID = sub.SubjectID
WHERE
    sub.SubjectName = 'Programming'
    AND a.Attended = 1
GROUP BY
    sub.SubjectName;


-- 7.2
SELECT 
    sub.SubjectName,
    COUNT(*) AS [Количество пропущенных занятий]
FROM 
    Attendance a
    JOIN Schedules s ON a.ScheduleID = s.ScheduleID
    JOIN Subjects sub ON s.SubjectID = sub.SubjectID
WHERE
    sub.SubjectName = 'Programming'
    AND a.Attended = 0
GROUP BY
    sub.SubjectName;


-- 7.3
SELECT 
    sub.SubjectName,
    COUNT(*) AS [Количество пропущенных занятий]
FROM 
    Attendance a
    JOIN Schedules s ON a.ScheduleID = s.ScheduleID
    JOIN Subjects sub ON s.SubjectID = sub.SubjectID
WHERE
    sub.SubjectName = 'Programming'
    AND a.Attended = 0
GROUP BY
    sub.SubjectName;


-- 7.4
SELECT 
    a.StudentID,
    s.SubjectID,
    SUM(DATEDIFF(MINUTE, 8.00, 9.30)) AS [Время (в минутах)]
FROM 
    Attendance a
    JOIN Schedules s ON a.ScheduleID = s.ScheduleID
GROUP BY
    a.StudentID, s.SubjectID;
