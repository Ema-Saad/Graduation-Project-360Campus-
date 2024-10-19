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

Priority: Medium
=== Functional Requirements
- *Performance*

== Graduation Project Tracking
=== Description
Management of students' graduation projects.

Priority: Medium
=== Functional Requirements
- *GraduationProject*
== Report Generation
=== Description
Automatic generation of reports

Priority: Medium
=== Functional Requirements
- *Report*

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
