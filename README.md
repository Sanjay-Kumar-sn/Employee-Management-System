# Employee Record System

## Overview

Employee Record System is a command-line application developed in Python for managing employee information. The system provides functionalities to add, update, remove, search, and display employee records while ensuring data persistence through file handling.

## Features

* Add new employee records
* Update existing employee details
* Remove employee records
* Search employees by ID or Name
* Display all employee records
* Validate unique Employee IDs
* Handle invalid user inputs gracefully
* Save employee records to a file
* Automatically load employee records at startup

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling

## Employee Information

Each employee record contains:

* Employee ID
* Employee Name
* Position
* Department
* Salary
* Joining Date

## Data Persistence

Employee records are stored in a text file, allowing data to persist between program executions.

## Error Handling

The system includes exception handling for:

* Invalid user input
* Duplicate Employee IDs
* Employee not found scenarios
* File access and file operation errors

## Project Structure

```text
Employee_Record_System/
│
├── employee_record_system.py
├── Samples.txt
└── README.md
```

## Future Enhancements

* Database integration using SQLite or MySQL
* Graphical User Interface (GUI)
* Advanced employee filtering and sorting
* Report generation functionality

## License

This project is developed for learning and portfolio purposes.
