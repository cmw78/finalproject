/*
Find courses Christina is taking
*/
select course.id, course.name from Course JOIN (select * from Taking, Student where 
Taking.studentId = Student.id and Student.name = 'Christina') as T on T.courseId = Course.id;

/*
Find courses bookbagged by Owen
*/
select course.id, course.name from Course JOIN (select * from Bookbag, Student where 
Bookbag.studentId = Student.id and Student.name = 'Owen') as T on T.courseId = Course.id;

-- Find courses with a net rating of at least 1 -- 
SELECT Course.id 
FROM Course, Taken
WHERE Course.id = Taken.courseId
GROUP BY Course.id
HAVING SUM(rating) >= 1;

-- Find courses taught by Rong Ge --

SELECT Teaches.courseId 
FROM Teaches, Professor
WHERE Teaches.profId = Professor.id
AND Professor.name = 'Rong Ge';

-- Find names of James' Friends who have taken LIT 274 --
SELECT distinct(S2.name)
FROM Student as S1, Student as S2, isFriendsWith, Taken
WHERE S1.name = 'James' and S1.id = id1 and id2 = S2.id AND Taken.courseId = 'LIT 274' AND Taken.studentId = S2.id;

-- Find everyone who has bookbagged ORGANIC CHEMISTRY I--
SELECT distinct(Student.name)
FROM Student, Bookbag, Course
WHERE Student.id = Bookbag.studentId and Course.id = Bookbag.courseId and Course.name = 'ORGANIC CHEMISTRY I';

--Find courses taught by Chad J Kuyper--
SELECT course.name
FROM Course, Professor, Teaches
WHERE course.id = teaches.courseId AND Teaches.profId = Professor.id and Professor.name = 'Chad J Kuyper';

--Find ratings for all courses--
SELECT SUM(rating), Taken.courseId
FROM Taken
GROUP BY Taken.courseId;

--Find ratings for all courses taught by Salman Azhar--
SELECT SUM(rating), Taken.courseId
FROM Taken, Professor, Teaches
WHERE Teaches.profId = Professor.id and Professor.name = 'Salman Azhar' and Teaches.courseId = Taken.courseId
GROUP BY Taken.courseId;

--Find the highest rating given to each course taught by Alex Glass--
SELECT MAX(rating), Taken.courseId
FROM Taken, Professor, Teaches
WHERE Teaches.profId = Professor.id and Professor.name = 'Alex Glass' and Teaches.courseId = Taken.courseId
GROUP BY Taken.courseId;

--Find all of Dominic's Friends--
SELECT distinct(S2.name)
FROM Student as S1, Student as S2, isFriendsWith
WHERE id1 = S1.id AND id2 = S2.id AND S1.name = 'Dominic';

--Find all the courses bookbagged by Dominic's Friends--
SELECT distinct Bookbag.courseId, Course.name
FROM Student as S1, Student as S2, isFriendsWith, Bookbag, Course
WHERE S1.name = 'Dominic' and S1.id=S2.id and S2.id = Bookbag.studentId and Course.id = Bookbag.courseId;

--Find netIDs and names of all students who have taken courses in Owen's bookbag--
SELECT S2.id, S2.name
FROM Student as S1, Student as S2, Bookbag, Taken
WHERE S2.id = Taken.studentId and S1.name = 'Owen' and Bookbag.studentId = S1.id and Bookbag.courseId = Taken.courseId;

--Find netIDs and names of all students who have bookbagged the same courses as Owen--
SELECT distinct S2.id, S2.name
FROM Student as S1, Student as S2, Bookbag as B1, Bookbag as B2
WHERE S1.id = B1.studentId and S2.id = B2.studentId and B1.courseId = B2.courseId and S1.name = 'Owen' AND S1.name>S2.name;

--Find names of all courses Bookbagged by Owen--
SELECT course.id
FROM Course, Bookbag, Student
WHERE Student.name = 'Owen' and Bookbag.courseId = Course.id and Bookbag.studentId = Student.id;

--Find names of all students who have bookbagged EGR 201L--
SELECT Student.name
FROM Bookbag, Student
WHERE Bookbag.courseId = 'EGR 201L' and Bookbag.studentId = Student.id;



