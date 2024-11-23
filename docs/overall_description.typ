== Product perspective

The 360Campus system is a new, self-contained product designed to enhance the university experience 
for students, instructors, and administrators. It is not a follow-on member of an existing product family, 
nor is it intended to replace any specific existing systems. Instead, 360Campus aims to fill a gap in the 
current educational ecosystem by providing an integrated platform that addresses both academic and 
non-academic needs within the university environment. 

*Context and Origin*: The idea for 360Campus originated from the observation of fragmented systems 
currently in use at universities, which often require students and staff to navigate multiple platforms for 
different functions, such as course management, attendance tracking, and event organization. By 
consolidating these functionalities into a single platform, 360Campus seeks to improve user experience, 
enhance collaboration, and streamline administrative processes. 

*System Relationships*: While 360Campus is designed as a standalone solution, it may interface with 
existing university systems, such as student information systems (SIS) and learning management 
systems (LMS), to import/export relevant data. For example, student enrollment data could be 
synchronized with the platform to ensure accurate tracking of attendance and performance. 

*Major Components and Interfaces*: 
The 360Campus system consists of several key components, each addressing specific functionalities: 

-  User Interface Module: Provides access for students, instructors, and administrators to navigate 
   the platform and utilize its features. 

- Content Management System (CMS): Manages course materials, event information, and resources. 

- Analytics Engine: Processes data related to performance analysis, attendance tracking, and report generation. 

- Communication Module: Facilitates class discussions and interactions among users. 

- AI Scheduling System: Automates timetable generation for classes and events.

== User classes and characteristics
#table(
   rows: 4,
   columns: (1fr, 1fr, 2fr, 1fr, 1fr, 1fr) ,
   [User Class], [Use Frequency], [Functions], [Technical Expertise], [Security Level], [Importance],
   [Student], [ Daily ], [ 
   - Access materials and courses
   - Track attendance
   - Use map. 
   ], [ Moderate ], [ Standard user access ], [ High ],

   [Instructors], [ Daily to weekly ], [ 
      - Upload materials
      - Track attendance 
      - Analyze performance 
   ], [ Moderate to high ], [ Elevated access ], [ High ],

   [Administrators], [ Weekly to monthly ], [ 
      - Manage user accounts
      - Oversee courses
   ], [ High ], [ Elevated access ], [ Medium ],
)

== Operating environment
The platform will operate in a cloud environment, ensuring scalability and accessibility. It will support 
major web browsers (Chrome, Firefox, Safari) and mobile platforms (iOS, Android). Users will require 
an internet connection and compatible devices (PCs, tablets, smartphones) to access the system. 

== Design and implementation constraints

The 360Campus system is subject to several constraints that limit development options: 
+ User Interfaces: 
   -  Must be intuitive and accessible for students, instructors, and administrators. 
   - Compatibility with mobile devices is required for access on smartphones and tablets. 
+ Quality of Service: 
   - Response time must be under two seconds for user actions. 
   - Uptime must be at least 99.5% to ensure reliability during peak periods. 
+ Standards Compliance: 
   - Must comply with data protection regulations (e.g., GDPR, FERPA). 
   - Adherence to W3C web standards for compatibility across browsers. 
+ Design and Implementation: 
   - Technology stack may be limited by existing university infrastructure and expertise. 
   - Development must stay within budget and time constraints. 

== Assumptions and dependencies

Assumptions: 
+ User Engagement: It is assumed that students and instructors will actively use the system. 
+ Technology Proficiency: Users will have a basic understanding of technology and web applications. 
+ Infrastructure Stability: The university’s IT infrastructure will support the application’s requirements without significant upgrades. 
+ Data Security Compliance: It is assumed that the system will comply with data protection regulations (e.g., GDPR). 

Dependencies: 
+ Third-Party Tools: The system may rely on third-party software for features like attendance tracking and analytics. 
+ Existing Systems: Integration with current university systems (e.g., Student Information System) is essential for data consistency. 
+ Internet Connectivity: The application’s performance is dependent on reliable internet access for users. 

