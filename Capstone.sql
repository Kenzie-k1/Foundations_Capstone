CREATE TABLE IF NOT EXISTS Users(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT,
    phone TEXT,
    date_hired TEXT,
    user_created_date TEXT, 
    user_type INTEGER DEFAULT 0,
    user_active INTEGER DEFAULT 1
);


CREATE TABLE IF NOT EXISTS Compentencies(
    compentency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date_created TEXT
);

CREATE TABLE IF NOT EXISTS Assessments(
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    compentency_id INTEGER,
    name TEXT,
    date_created TEXT,
    FOREIGN KEY(compentency_id)
        REFERENCES Compentencies(compentency_id) 
);

CREATE TABLE IF NOT EXISTS Results(
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER,
    employee_id INTEGER,
    manager_id INTEGER DEFAULT NULL,
    date_taken TEXT,
    score TEXT,
    FOREIGN KEY (assessment_id)
        REFERENCES Assessments(assessment_id),
    FOREIGN KEY (employee_id)   
        REFERENCES Users(employee_id),
    FOREIGN KEY (manager_id)
        REFERENCES Users(employee_id)      
);

PRAGMA foreign_keys = ON;

ALTER TABLE Compentencies 
RENAME Competencies;

ALTER TABLE Assessments 
RENAME COLUMN compentency_id TO competency_id;