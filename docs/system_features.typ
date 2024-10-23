#show regex("\.[A-Za-z]+"): strong

== User Management
=== Description
Manage accounts of users of the system.

Priority: High
=== Functional Requirements
- *Accounts*
  - .Students: Every student in the university will have an account on the system.
    - .Permissions: Student accounts shall have the following permissions by default:
                    - view uploaded materials
                    - use chat rooms of their classrooms 
                    - view events and register to attend events

      - .Revocable: An admin can revoke any permission of any student, at any time. This revoking action must be logged for
                    auditing purposes.

  - .Admins: Admins will have an account on the system.
    - .Permissions: Admin accounts shall have the following permissions by default:
                    - Add, edit and remove student accounts.
                    - Grant and revoke permissions from student accounts.
                    - Create, edit and remove classrooms.
                    - Add and remove students to/from classrooms.
                    - Add and remove materials to/from classrooms.
                    - Create, edit and remove events.
    - .Initial: Admin accounts shall be created by the System Administrator.
== Course Management
=== Description
Manage courses and their related content.

Priority: High
=== Functional Requirements
- *Courses*
  - .Create: Admins shall be able to create courses.
  - .Materials: Courses shall contains materials, these materials shall be uploaded by admins.
    - .StudentSubmit: Students may be allowed to submit materials.
  - .Offer: Admins shall be able to offer courses for enrollment.
  - .Prerequiste: Courses shall be able to have prerequistes. Students must pass prerequistes of a course
                  in order to be able to register that course, if it's offered.
== Event Management
=== Description

Priority: High
=== Functional Requirements
- *Events*
  - .Create: Admins shall be able to create events.
  - .Register: Students with sufficient permissions shall be able to register for events.
  - .Calender: The Website shall show a calender of upcoming events.

== Attendance Tracking
=== Description
Automatic logging of students' attendance.

Priority: Medium
=== Functional Requirements
- *Attendance*
== Performance Analysis
=== Description
Track the performance of students and staff

Priority: Medium
=== Functional Requirements
- *Performance*
  - .Initial: The System Administrator shall create admin accounts and will have full control over all 
              performance analysis features. 

  - .Student: Every student in the university shall have access to performance analysis system.
    - .Permissions: Student accounts shall have the following permissions by default
      - View their graph representing their registered courses and grades
      - View and download performance reports.
      // - Grades will be calculated based on attendance and assessments
  - .ProfessorTA: Professsors and TAs shall have acccess to performance analysis for the courses they manage.
    - .Permissions: TA and professor accounts shall have the following permissions by default: 
      - View student performance data in their courses (individual grades, class 
        averages, participation). 
      - Generate detailed performance reports for each class or student. 
      - Provide feedback on student performance based on the analysis. 

    - .Admins: Admins shall have full access to manage the performance analysis system. 
      - .Permissions: Admin accounts shall have the following permissions by default:
        - Add, edit, and remove student, TA, and professor performance data. 
        - View and manage overall system performance metrics (department-level or 
          university-wide reports). 
        - Grant or revoke access to performance analysis tools for students, TAs, and 
          professors. 

== Graduation Project Tracking
=== Description
View and discover students' graduation projects. 

Priority: Medium
=== Functional Requirements
- *GraduationProject*
  - .Students: Studenst shall be able to view and discover students' graduation projects.
  - .Professors
    - .Manage: Professors shall be able to upload detailed 
               records of past graduation projects they have supervised, including project descriptions, team 
               members, final grades, and comprehensive details such as technologies used, challenges faced, 
               and outcomes achieved. This data will be available for future reference and exploration by 
               students and staff.
  - .Admins: Admins shall be able to create, edit, and remove graduation projects from the system. 
== Report Generation
=== Description
Automatic generation of reports

Priority: Medium
=== Functional Requirements
- *Report*
  - .AutomaticGen: The system shall automatically generate reports based on 
    predefined criteria (student performance, attendance). 
  - .ScheduledGen: Admins shall be able to schedule automatic report generation (e.g., weekly, 
    monthly, end of semester) for key metrics such as GPA trends, course pass rates, and project 
    evaluations. 
  - .Download: Users shall be able to download reports in multiple formats, such as 
    PDF, CSV, or Excel. 
  - .Share: Admins and professors shall be able to share generated reports with other 
    authorized users via email or within the system. 
  - .Visualise: The system shall generate visual representations (e.g., charts, graphs) within 
    reports to better illustrate trends and key performance indicators. 
  - .Audit: Every report generated, customized, or shared shall be logged in the system for 
    auditing purposes. 

== Virtual Classroom
=== Description
An app that allows students to be grouped based on the course,
allowing communication between the student and the instructor and between the students.

Priority: Low
=== Functional Requirements

- *Classroom*
  - .Create: Admins shall be able to create classrooms.
    - .CourseExists: Admins shall create classrooms only for available courses.
  - .AutomaticAdd: The system shall automatically add students to a classroom of a specific course and instructor, if that student
                   registered that course with that instructors.
  - .ManualAdd: Admins shall be able to add students to classrooms.
  - .MainChatroom: Each classroom shall have a main chat room which will be accessible to 
                   all the students and the instructor in that classroom.
  - .PrivateChat: Students shall be able to open private chat rooms with students and instructors whom they share a classroom with.
  - .Video: The system may allow an instructor to stream video and audio with the students in a classroom.


== Timetable Generation
=== Description
Automatic generation of timetables.

Priority: Low
=== Functional Requirements
- *Timetable*
  - .Create: Admins shall create timetables.
  - .Constraints: Admins shall supply constraints for timetable generation. Constraints include
                  - Available rooms, and their capacities.
                  - Student Sections. // TODO: a better name for that.
                  - Time intervals where professors and teaching assistants are available.
  - .Conflicts: The system shall fail to generate a timetable when a conflict is detected and a warning
                shall be sent to the admins.
