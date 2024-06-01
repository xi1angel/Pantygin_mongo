CREATE TABLE Directions (
    DirectionID INT PRIMARY KEY IDENTITY,
    DirectionName NVARCHAR(100) NOT NULL
);

CREATE TABLE Groups (
    GroupID INT PRIMARY KEY IDENTITY,
    GroupName NVARCHAR(50) NOT NULL,
    DirectionID INT NOT NULL,
    FOREIGN KEY (DirectionID) REFERENCES Directions(DirectionID)
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    MiddleName NVARCHAR(50),
    BirthDate DATE NOT NULL,
    City NVARCHAR(100) NOT NULL,
    Street NVARCHAR(100) NOT NULL,
    HouseNumber NVARCHAR(10) NOT NULL,
    Email NVARCHAR(100) NOT NULL,
    GroupID INT NOT NULL,
    Budget BIT NOT NULL,
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID)
);

CREATE TABLE Phones (
    PhoneID INT PRIMARY KEY IDENTITY,
    StudentID INT NOT NULL,
    PhoneNumber NVARCHAR(15) NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY IDENTITY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    MiddleName NVARCHAR(50)
);

CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY IDENTITY,
    SubjectName NVARCHAR(100) NOT NULL,
    DirectionID INT NOT NULL,
    TeacherID INT NOT NULL,
    FOREIGN KEY (DirectionID) REFERENCES Directions(DirectionID),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

CREATE TABLE Grades (
    GradeID INT PRIMARY KEY IDENTITY,
    StudentID INT NOT NULL,
    SubjectID INT NOT NULL,
    Grade INT CHECK (Grade IN (2, 3, 4, 5)),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);

CREATE TABLE Schedules (
    ScheduleID INT PRIMARY KEY IDENTITY,
    SubjectID INT NOT NULL,
    GroupID INT NOT NULL,
    DayOfWeek NVARCHAR(20) NOT NULL,
    TimeSlot NVARCHAR(20) NOT NULL,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID),
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID)
);

CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY IDENTITY,
    StudentID INT NOT NULL,
    ScheduleID INT NOT NULL,
    AttendanceDate DATE NOT NULL,
    Attended BIT NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (ScheduleID) REFERENCES Schedules(ScheduleID)
);


INSERT INTO Directions (DirectionName) VALUES 
('Computer Science'),
('Mathematics'),
('Physics');

INSERT INTO Groups (GroupName, DirectionID) VALUES 
('CS101', 1),
('CS102', 1),
('CS103', 1),
('MATH101', 2),
('MATH102', 2),
('MATH103', 2),
('PHYS101', 3),
('PHYS102', 3),
('PHYS103', 3);


INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Ivan', 'Ivanov', 'Ivanovich', '2000-01-01', 'Moscow', 'Lenina', '10', 'ivan.ivanov@example.com', 1, 1),
('Petr', 'Petrov', 'Petrovich', '2000-02-01', 'Moscow', 'Lenina', '12', 'petr.petrov@example.com', 1, 0),
('Sergey', 'Sergeev', 'Sergeevich', '2000-03-01', 'Moscow', 'Lenina', '14', 'sergey.sergeev@example.com', 1, 1),
('Alexey', 'Nikolaev', 'Ivanovich', '2000-10-01', 'Moscow', 'Lenina', '16', 'alexey.nikolaev@example.com', 1, 1),
('Vladimir', 'Lebedev', 'Ivanovich', '2000-01-15', 'Moscow', 'Lenina', '18', 'vladimir.lebedev@example.com', 1, 0),
('Irina', 'Pavlova', 'Ivanovna', '2000-04-15', 'Moscow', 'Lenina', '20', 'irina.pavlova@example.com', 1, 1),
('Anton', 'Sorokin', 'Ivanovich', '2000-07-15', 'Moscow', 'Lenina', '22', 'anton.sorokin@example.com', 1, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Olga', 'Sidorova', 'Ivanovna', '2000-04-01', 'Saint Petersburg', 'Nevskaya', '20', 'olga.sidorova@example.com', 2, 0),
('Elena', 'Kuznetsova', 'Petrovna', '2000-05-01', 'Saint Petersburg', 'Nevskaya', '22', 'elena.kuznetsova@example.com', 2, 1),
('Natalya', 'Popova', 'Sergeevna', '2000-06-01', 'Saint Petersburg', 'Nevskaya', '24', 'natalya.popova@example.com', 2, 0),
('Maria', 'Vasilieva', 'Petrovna', '2000-11-01', 'Saint Petersburg', 'Nevskaya', '26', 'maria.vasilieva@example.com', 2, 0),
('Svetlana', 'Voronova', 'Petrovna', '2000-02-15', 'Saint Petersburg', 'Nevskaya', '28', 'svetlana.voronova@example.com', 2, 1),
('Oleg', 'Titov', 'Petrovich', '2000-05-15', 'Saint Petersburg', 'Nevskaya', '30', 'oleg.titov@example.com', 2, 0),
('Anastasia', 'Mikhailova', 'Petrovna', '2000-08-15', 'Saint Petersburg', 'Nevskaya', '32', 'anastasia.mikhailova@example.com', 2, 1);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Dmitry', 'Sokolov', 'Ivanovich', '2000-07-01', 'Novosibirsk', 'Kirova', '30', 'dmitry.sokolov@example.com', 3, 1),
('Andrey', 'Smirnov', 'Petrovich', '2000-08-01', 'Novosibirsk', 'Kirova', '32', 'andrey.smirnov@example.com', 3, 0),
('Anna', 'Fedorova', 'Sergeevna', '2000-09-01', 'Novosibirsk', 'Kirova', '34', 'anna.fedorova@example.com', 3, 1),
('Igor', 'Kuzmin', 'Sergeevich', '2000-12-01', 'Novosibirsk', 'Kirova', '36', 'igor.kuzmin@example.com', 3, 1),
('Yuri', 'Zaitsev', 'Sergeevich', '2000-03-15', 'Novosibirsk', 'Kirova', '38', 'yuri.zaitsev@example.com', 3, 0),
('Tatiana', 'Yakovleva', 'Sergeevna', '2000-06-15', 'Novosibirsk', 'Kirova', '40', 'tatiana.yakovleva@example.com', 3, 1),
('Maxim', 'Romanov', 'Sergeevich', '2000-09-15', 'Novosibirsk', 'Kirova', '42', 'maxim.romanov@example.com', 3, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Yana', 'Kozlova', 'Ivanovna', '2000-01-01', 'Moscow', 'Arbat', '10', 'yana.kozlova@example.com', 4, 1),
('Oksana', 'Novikova', 'Petrovna', '2000-02-01', 'Moscow', 'Arbat', '12', 'oksana.novikova@example.com', 4, 0),
('Vladislav', 'Morozov', 'Sergeevich', '2000-03-01', 'Moscow', 'Arbat', '14', 'vladislav.morozov@example.com', 4, 1),
('Mikhail', 'Belyaev', 'Ivanovich', '2000-04-01', 'Moscow', 'Arbat', '16', 'mikhail.belyaev@example.com', 4, 1),
('Alina', 'Makarova', 'Petrovna', '2000-05-01', 'Moscow', 'Arbat', '18', 'alina.makarova@example.com', 4, 0),
('Ekaterina', 'Rogova', 'Sergeevna', '2000-06-01', 'Moscow', 'Arbat', '20', 'ekaterina.rogova@example.com', 4, 1),
('Nikolay', 'Voronin', 'Ivanovich', '2000-07-01', 'Moscow', 'Arbat', '22', 'nikolay.voronin@example.com', 4, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Polina', 'Goncharova', 'Petrovna', '2000-08-01', 'Saint Petersburg', 'Ligovka', '24', 'polina.goncharova@example.com', 5, 1),
('Kirill', 'Filippov', 'Sergeevich', '2000-09-01', 'Saint Petersburg', 'Ligovka', '26', 'kirill.filippov@example.com', 5, 0),
('Roman', 'Davydov', 'Ivanovich', '2000-10-01', 'Saint Petersburg', 'Ligovka', '28', 'roman.davydov@example.com', 5, 1),
('Valentina', 'Solovieva', 'Petrovna', '2000-11-01', 'Saint Petersburg', 'Ligovka', '30', 'valentina.solovieva@example.com', 5, 1),
('Artem', 'Zhukov', 'Sergeevich', '2000-12-01', 'Saint Petersburg', 'Ligovka', '32', 'artem.zhukov@example.com', 5, 0),
('Ludmila', 'Vorontsova', 'Ivanovna', '2000-01-02', 'Saint Petersburg', 'Ligovka', '34', 'ludmila.vorontsova@example.com', 5, 1),
('Alexandra', 'Miloslavskaya', 'Petrovna', '2000-02-02', 'Saint Petersburg', 'Ligovka', '36', 'alexandra.miloslavskaya@example.com', 5, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Viktor', 'Orlov', 'Ivanovich', '2000-03-02', 'Novosibirsk', 'Dzerzhinskogo', '38', 'viktor.orlov@example.com', 6, 1),
('Angelina', 'Akimova', 'Petrovna', '2000-04-02', 'Novosibirsk', 'Dzerzhinskogo', '40', 'angelina.akimova@example.com', 6, 0),
('Konstantin', 'Gerasimov', 'Sergeevich', '2000-05-02', 'Novosibirsk', 'Dzerzhinskogo', '42', 'konstantin.gerasimov@example.com', 6, 1),
('Semyon', 'Troitsky', 'Ivanovich', '2000-06-02', 'Novosibirsk', 'Dzerzhinskogo', '44', 'semyon.troitsky@example.com', 6, 1),
('Nina', 'Nesterova', 'Petrovna', '2000-07-02', 'Novosibirsk', 'Dzerzhinskogo', '46', 'nina.nesterova@example.com', 6, 0),
('Boris', 'Klimov', 'Sergeevich', '2000-08-02', 'Novosibirsk', 'Dzerzhinskogo', '48', 'boris.klimov@example.com', 6, 1),
('Tamara', 'Efimova', 'Ivanovna', '2000-09-02', 'Novosibirsk', 'Dzerzhinskogo', '50', 'tamara.efimova@example.com', 6, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Vera', 'Yakimova', 'Petrovna', '2000-10-02', 'Moscow', 'Krasnaya', '52', 'vera.yakimova@example.com', 7, 1),
('Grigory', 'Melnikov', 'Sergeevich', '2000-11-02', 'Moscow', 'Krasnaya', '54', 'grigory.melnikov@example.com', 7, 0),
('Marina', 'Semenova', 'Ivanovna', '2000-12-02', 'Moscow', 'Krasnaya', '56', 'marina.semenova@example.com', 7, 1),
('Vadim', 'Bykov', 'Petrovich', '2000-01-03', 'Moscow', 'Krasnaya', '58', 'vadim.bykov@example.com', 7, 1),
('Tatyana', 'Shestakova', 'Sergeevna', '2000-02-03', 'Moscow', 'Krasnaya', '60', 'tatyana.shestakova@example.com', 7, 0),
('Alexander', 'Rodionov', 'Ivanovich', '2000-03-03', 'Moscow', 'Krasnaya', '62', 'alexander.rodionov@example.com', 7, 1),
('Sofia', 'Gordeeva', 'Petrovna', '2000-04-03', 'Moscow', 'Krasnaya', '64', 'sofia.gordeeva@example.com', 7, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Leonid', 'Yashin', 'Sergeevich', '2000-05-03', 'Saint Petersburg', 'Zelenaya', '66', 'leonid.yashin@example.com', 8, 1),
('Diana', 'Ermakova', 'Ivanovna', '2000-06-03', 'Saint Petersburg', 'Zelenaya', '68', 'diana.ermakova@example.com', 8, 0),
('Yaroslav', 'Borisov', 'Petrovich', '2000-07-03', 'Saint Petersburg', 'Zelenaya', '70', 'yaroslav.borisov@example.com', 8, 1),
('Zoya', 'Lapina', 'Sergeevna', '2000-08-03', 'Saint Petersburg', 'Zelenaya', '72', 'zoya.lapina@example.com', 8, 1),
('Vitaly', 'Grigoryev', 'Ivanovich', '2000-09-03', 'Saint Petersburg', 'Zelenaya', '74', 'vitaly.grigoryev@example.com', 8, 0),
('Evgenia', 'Maltseva', 'Petrovna', '2000-10-03', 'Saint Petersburg', 'Zelenaya', '76', 'evgenia.maltseva@example.com', 8, 1),
('Stepan', 'Karelin', 'Sergeevich', '2000-11-03', 'Saint Petersburg', 'Zelenaya', '78', 'stepan.karelin@example.com', 8, 0);

INSERT INTO Students (FirstName, LastName, MiddleName, BirthDate, City, Street, HouseNumber, Email, GroupID, Budget) VALUES 
('Inna', 'Chernyshova', 'Ivanovna', '2000-12-03', 'Novosibirsk', 'Oktyabrskaya', '80', 'inna.chernyshova@example.com', 9, 1),
('Vasiliy', 'Ignatov', 'Petrovich', '2000-01-04', 'Novosibirsk', 'Oktyabrskaya', '82', 'vasiliy.ignatov@example.com', 9, 0),
('Larisa', 'Belova', 'Sergeevna', '2000-02-04', 'Novosibirsk', 'Oktyabrskaya', '84', 'larisa.belova@example.com', 9, 1),
('Denis', 'Alekseev', 'Ivanovich', '2000-03-04', 'Novosibirsk', 'Oktyabrskaya', '86', 'denis.alekseev@example.com', 9, 1),
('Elizaveta', 'Sukhova', 'Petrovna', '2000-04-04', 'Novosibirsk', 'Oktyabrskaya', '88', 'elizaveta.sukhova@example.com', 9, 0),
('Ruslan', 'Kolesnikov', 'Sergeevich', '2000-05-04', 'Novosibirsk', 'Oktyabrskaya', '90', 'ruslan.kolesnikov@example.com', 9, 1),
('Lidia', 'Isaeva', 'Ivanovna', '2000-06-04', 'Novosibirsk', 'Oktyabrskaya', '92', 'lidia.isaeva@example.com', 9, 0);

INSERT INTO Phones (StudentID, PhoneNumber) VALUES
(1, '+7-900-000-0001'), 
(1, '+7-900-000-0002'), 
(2, '+7-900-000-0003'),
(3, '+7-900-000-0004'), 
(3, '+7-900-000-0005'),
(4, '+7-900-000-0006'),
(5, '+7-900-000-0007'),
(6, '+7-900-000-0008'), 
(6, '+7-900-000-0009'),
(7, '+7-900-000-0010'),
(8, '+7-900-000-0011'),
(9, '+7-900-000-0012'),
(10, '+7-900-000-0013'),
(11, '+7-900-000-0014'), 
(11, '+7-900-000-0015'),
(12, '+7-900-000-0016'),
(13, '+7-900-000-0017'), 
(13, '+7-900-000-0018'),
(14, '+7-900-000-0019'),
(15, '+7-900-000-0020'),
(16, '+7-900-000-0021'),
(17, '+7-900-000-0022'),
(18, '+7-900-000-0023'),
(19, '+7-900-000-0024'),
(20, '+7-900-000-0025'),
(21, '+7-900-000-0026'), 
(21, '+7-900-000-0027'),
(22, '+7-900-000-0028'),
(23, '+7-900-000-0029'),
(24, '+7-900-000-0030'),
(25, '+7-900-000-0031'),
(26, '+7-900-000-0032'),
(27, '+7-900-000-0033'),
(28, '+7-900-000-0034'),
(29, '+7-900-000-0035'),
(30, '+7-900-000-0036'),
(31, '+7-900-000-0037'),
(32, '+7-900-000-0038'),
(33, '+7-900-000-0039'),
(34, '+7-900-000-0040'),
(35, '+7-900-000-0041'),
(36, '+7-900-000-0042'),
(37, '+7-900-000-0043'),
(38, '+7-900-000-0044'),
(39, '+7-900-000-0045'),
(40, '+7-900-000-0046'),
(41, '+7-900-000-0047'),
(42, '+7-900-000-0048'),
(43, '+7-900-000-0049'),
(44, '+7-900-000-0050'),
(45, '+7-900-000-0051'),
(46, '+7-900-000-0052'),
(47, '+7-900-000-0053'),
(48, '+7-900-000-0054'),
(49, '+7-900-000-0055'),
(50, '+7-900-000-0056'),
(51, '+7-900-000-0057'),
(52, '+7-900-000-0058'),
(53, '+7-900-000-0059'),
(54, '+7-900-000-0060'),
(55, '+7-900-000-0061'),
(56, '+7-900-000-0062'),
(57, '+7-900-000-0063'),
(58, '+7-900-000-0064'),
(59, '+7-900-000-0065'),
(60, '+7-900-000-0066'),
(61, '+7-900-000-0067'),
(62, '+7-900-000-0068'),
(63, '+7-900-000-0069');

INSERT INTO Teachers (FirstName, LastName, MiddleName) VALUES 
('Andrey', 'Ivanov', 'Petrovich'),
('Elena', 'Smirnova', 'Ivanovna'),
('Olga', 'Kuznetsova', 'Vladimirovna'),
('Sergey', 'Sokolov', 'Mikhailovich'),
('Vladimir', 'Popov', 'Sergeevich');

INSERT INTO Subjects (SubjectName, DirectionID, TeacherID) VALUES 
('Programming', 1, 1), ('Algorithms', 1, 2), ('Databases', 1, 3),
('Calculus', 2, 4), ('Linear Algebra', 2, 5), ('Statistics', 2, 1),
('Mechanics', 3, 2), ('Optics', 3, 3), ('Thermodynamics', 3, 4);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(1, 1, 2), (1, 2, 4), (1, 3, 3), 
(2, 1, 4), (2, 2, 3), (2, 3, 5), 
(3, 1, 2), (3, 2, 4), (3, 3, 2),
(4, 1, 5), (4, 2, 2), (4, 3, 3), 
(5, 1, 2), (5, 2, 2), (5, 3, 2), 
(6, 1, 2), (6, 2, 4), (6, 3, 5),
(7, 1, 5), (7, 2, 2), (7, 3, 2);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(8, 1, 4), (8, 2, 3), (8, 3, 5), 
(9, 1, 3), (9, 2, 4), (9, 3, 5),
(10, 1, 5), (10, 2, 4), (10, 3, 2), 
(11, 1, 2), (11, 2, 3), (11, 3, 5), 
(12, 1, 2), (12, 2, 2), (12, 3, 2),
(13, 1, 5), (13, 2, 4), (13, 3, 2), 
(14, 1, 4), (14, 2, 3), (14, 3, 5);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(15, 1, 3), (15, 2, 4), (15, 3, 5),
(16, 1, 5), (16, 2, 4), (16, 3, 3), 
(17, 1, 4), (17, 2, 3), (17, 3, 5), 
(18, 1, 5), (18, 2, 5), (18, 3, 5),
(19, 1, 5), (19, 2, 2), (19, 3, 3), 
(20, 1, 2), (20, 2, 3), (20, 3, 2),
(21, 1, 3), (21, 2, 4), (21, 3, 5);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(22, 4, 5), (22, 5, 4), (22, 6, 3), 
(23, 4, 4), (23, 5, 3), (23, 6, 2), 
(24, 4, 3), (24, 5, 2), (24, 6, 2),
(25, 4, 2), (25, 5, 2), (25, 6, 3), 
(26, 4, 4), (26, 5, 3), (26, 6, 5), 
(27, 4, 3), (27, 5, 4), (27, 6, 5),
(28, 4, 5), (28, 5, 4), (28, 6, 3);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(29, 4, 4), (29, 5, 3), (29, 6, 5), 
(30, 4, 3), (30, 5, 4), (30, 6, 5),
(31, 4, 5), (31, 5, 2), (31, 6, 3), 
(32, 4, 4), (32, 5, 3), (32, 6, 2), 
(33, 4, 3), (33, 5, 2), (33, 6, 2),
(34, 4, 5), (34, 5, 2), (34, 6, 3), 
(35, 4, 4), (35, 5, 3), (35, 6, 5);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(36, 4, 3), (36, 5, 4), (36, 6, 5),
(37, 4, 5), (37, 5, 4), (37, 6, 3), 
(38, 4, 2), (38, 5, 3), (38, 6, 5), 
(39, 4, 3), (39, 5, 4), (39, 6, 2),
(40, 4, 2), (40, 5, 2), (40, 6, 3), 
(41, 4, 4), (41, 5, 3), (41, 6, 5),
(42, 4, 3), (42, 5, 4), (42, 6, 5);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(43, 7, 5), (43, 8, 4), (43, 9, 3), 
(44, 7, 2), (44, 8, 3), (44, 9, 5), 
(45, 7, 2), (45, 8, 4), (45, 9, 5),
(46, 7, 5), (46, 8, 4), (46, 9, 3), 
(47, 7, 4), (47, 8, 3), (47, 9, 2), 
(48, 7, 3), (48, 8, 2), (48, 9, 2),
(49, 7, 5), (49, 8, 2), (49, 9, 3);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(50, 7, 4), (50, 8, 3), (50, 9, 5), 
(51, 7, 3), (51, 8, 4), (51, 9, 2),
(52, 7, 2), (52, 8, 2), (52, 9, 3), 
(53, 7, 4), (53, 8, 3), (53, 9, 5), 
(54, 7, 3), (54, 8, 2), (54, 9, 2),
(55, 7, 2), (55, 8, 4), (55, 9, 3), 
(56, 7, 4), (56, 8, 3), (56, 9, 5);

INSERT INTO Grades (StudentID, SubjectID, Grade) VALUES
(57, 7, 3), (57, 8, 4), (57, 9, 5),
(58, 7, 5), (58, 8, 4), (58, 9, 2), 
(59, 7, 2), (59, 8, 3), (59, 9, 2), 
(60, 7, 3), (60, 8, 2), (60, 9, 2),
(61, 7, 5), (61, 8, 2), (61, 9, 3), 
(62, 7, 2), (62, 8, 3), (62, 9, 5),
(63, 7, 3), (63, 8, 4), (63, 9, 5);


INSERT INTO Schedules (SubjectID, GroupID, DayOfWeek, TimeSlot) VALUES 
(1, 1, 'Monday', '8:00-9:30'), (2, 1, 'Wednesday', '9:40-11:10'), (3, 1, 'Friday', '11:20-12:50'),
(4, 4, 'Monday', '8:00-9:30'), (5, 4, 'Wednesday', '9:40-11:10'), (6, 4, 'Friday', '11:20-12:50'),
(7, 7, 'Monday', '8:00-9:30'), (8, 7, 'Wednesday', '9:40-11:10'), (9, 7, 'Friday', '11:20-12:50');

INSERT INTO Attendance (StudentID, ScheduleID, AttendanceDate, Attended) VALUES 
(1, 1, '2024-01-01', 1), (1, 2, '2024-01-03', 1), (1, 3, '2024-01-05', 0),
(2, 1, '2024-01-01', 1), (2, 2, '2024-01-03', 0), (2, 3, '2024-01-05', 1),
(3, 1, '2024-01-01', 1), (3, 2, '2024-01-03', 1), (3, 3, '2024-01-05', 1),
(4, 1, '2024-01-01', 0), (4, 2, '2024-01-03', 1), (4, 3, '2024-01-05', 0),
(5, 1, '2024-01-01', 1), (5, 2, '2024-01-03', 1), (5, 3, '2024-01-05', 1),
(6, 1, '2024-01-01', 1), (6, 2, '2024-01-03', 0), (6, 3, '2024-01-05', 0),
(7, 1, '2024-01-01', 1), (7, 2, '2024-01-03', 1), (7, 3, '2024-01-05', 1);

INSERT INTO Attendance (StudentID, ScheduleID, AttendanceDate, Attended) VALUES 
(22, 4, '2024-01-01', 1), (22, 5, '2024-01-03', 1), (22, 6, '2024-01-05', 0),
(23, 4, '2024-01-01', 1), (23, 5, '2024-01-03', 0), (23, 6, '2024-01-05', 1),
(24, 4, '2024-01-01', 1), (24, 5, '2024-01-03', 1), (24, 6, '2024-01-05', 1),
(25, 4, '2024-01-01', 0), (25, 5, '2024-01-03', 1), (25, 6, '2024-01-05', 0),
(26, 4, '2024-01-01', 1), (26, 5, '2024-01-03', 1), (26, 6, '2024-01-05', 1),
(27, 4, '2024-01-01', 1), (27, 5, '2024-01-03', 0), (27, 6, '2024-01-05', 0),
(28, 4, '2024-01-01', 1), (28, 5, '2024-01-03', 1), (28, 6, '2024-01-05', 1);

INSERT INTO Attendance (StudentID, ScheduleID, AttendanceDate, Attended) VALUES 
(43, 7, '2024-01-01', 1), (43, 8, '2024-01-03', 1), (43, 9, '2024-01-05', 0),
(44, 7, '2024-01-01', 1), (44, 8, '2024-01-03', 0), (44, 9, '2024-01-05', 1),
(45, 7, '2024-01-01', 1), (45, 8, '2024-01-03', 1), (45, 9, '2024-01-05', 1),
(46, 7, '2024-01-01', 0), (46, 8, '2024-01-03', 1), (46, 9, '2024-01-05', 0),
(47, 7, '2024-01-01', 1), (47, 8, '2024-01-03', 1), (47, 9, '2024-01-05', 1),
(48, 7, '2024-01-01', 1), (48, 8, '2024-01-03', 0), (48, 9, '2024-01-05', 0),
(49, 7, '2024-01-01', 1), (49, 8, '2024-01-03', 1), (49, 9, '2024-01-05', 1);

