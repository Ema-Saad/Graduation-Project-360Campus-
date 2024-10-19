== User interfaces

- Home Page 
-- Source: University-wide information. 
-- Features: General announcements, university events, and quick links to key sections 
(Materials, Events, Help). 
-- Standard Buttons: Home, Login/Logout, Help. 

- User Dashboard 
-- Source: User profile data from the database. 
-- Features: Personalized view of registered classes, performance metrics, quick access to 
materials, events, and discussions. 
-- Standard Buttons: Home, Logout, Help, View Profile. 
- Materials Section 
-- Source: University-wide materials, available to all. 
-- Features: Access to academic resources (PDF, Word), search by course or department. 
-- Standard Buttons: Search, Download, View Details. 
- 
Classes Section 
-- Source: Data from active class registrations. 
-- Features: Class-specific materials, discussions, assignments, and attendance tracking. 
-- Standard Buttons: View Materials, Submit Assignment, Discussion Board. 
-
Events Section 
-- Source: University events data. 
-- Features: Calendar view, RSVP, add to personal calendar. 
-- Standard Buttons: Add to Calendar, RSVP, View Details. 
- University Map 
-- Source: Campus geographical data. 
--Features: Interactive map of the university campus showing key buildings, departments, 
classrooms, and facilities. Search by location or building name. 
--Standard Buttons: Zoom In/Out, Search, View Location. 

== Software interfaces
- Database Systems

-- Name: MySQL 
-- Purpose: The database will store all essential data, including user profiles, materials, 
class data, events, graduation projects, and performance analytics. 
-- Data Interaction: The system will send SQL queries to the database for data retrieval 
(e.g., fetching class materials, user-specific data like registered courses) and data storage 
(e.g., student performance, attendance tracking). 
-- Shared Data: The database will share user profile data, attendance records, and project 
information across different components (e.g., course management and performance 
analytics).

- Operating Systems: 
-- Name: Windows, macOS, Linux (for desktops); iOS, Android (for mobile devices) 
-- Purpose: The system will be platform-independent and web-based, allowing access 
through any modern web browser on any operating system. 
-- Interaction: No direct dependency on specific operating systems, but the front-end web 
application should be optimized for performance across all operating systems. 
Compatibility with browser versions (e.g., Chrome, Safari, Firefox) will be critical. 

-  Libraries and Frameworks: 
-- Frontend: 
--- Vue.js: For building dynamic user interfaces for the 360Campus platform. 
---  Vuetify: A Material Design component framework that helps maintain consistent 
UI/UX. 
---  
Purpose: The frontend will send HTTP requests to the backend API for retrieving 
or posting data. Vue.js will handle local logic like data presentation and form 
submission. 
-- Backend: 
---  Django REST Framework: Used for creating APIs to manage communication 
between the frontend and backend. 
--- Purpose: Manage routing, handle requests (e.g., fetching class materials, 
attendance reports), and provide the necessary backend logic to store, update, or 
retrieve data. 
- External Tools and APIs: 
-- Google Maps API (version v3.45 or higher): 

--- Purpose: The Google Maps API will be used to power the campus map feature. It 
will allow students to navigate the campus in real-time using mobile devices. 

--- Data Interaction: The API will send location data to the frontend, enabling real-
time maps. The app will not store location data on the server, except for logged-in 
users who may save specific map preferences. 
-- Microsoft Azure Cloud Services: 

--- Purpose: Used for cloud storage and data processing. 

--- Data Interaction: Secure API calls will be made between the system and Azure 
for scalable cloud hosting of files (e.g., project proposals, class materials). 
- Integrated Commercial Components: 
-- Zoom or Microsoft Teams Integration: 

--- 
Purpose: These services will be used for the virtual classroom feature (if 
implemented). 

--- 
Data Interaction: APIs from Zoom or Microsoft Teams will facilitate the 
creation of virtual class sessions, sharing session links with students, and handling 
class attendance automatically. 
-- Forms (Google Forms or Microsoft Forms): 

--- Purpose: For attendance tracking using form submission during class times. 
--- Data Interaction: Form results will be fetched via an API, which will then be 
processed by the backend to update attendance records for students. 

- Data Sharing: 
-- Shared Across Components: User data (profiles, roles), class materials, performance 
analytics, and event details will be accessible across the course management, 
performance analytics, and reporting modules. 
-- Implementation Constraints: Data consistency must be ensured across various services 
and APIs. As multiple components interact with shared data (e.g., profile info or class 
registration), mechanisms like caching and validation will be crucial. 

== Hardware interfaces

- Supported Device Types: 
The 360Campus system will be accessible from a wide range of devices, including: 
-- Desktops and Laptops: Running Windows, macOS, and Linux operating systems. 
-- Tablets and Smartphones: Running iOS and Android operating systems. 

- Nature of Data and Control Interactions: 
The system will interact with hardware components in the following ways: 
-- Input Devices: The system will receive input from standard input devices such as 
keyboards, mice, touchscreens, and styluses. 
-- Output Devices: The system will output data to monitors, mobile screens, and printers. 
-- Storage Devices: The system will store and retrieve data from local devices and 
predominantly through cloud storage services. 
- Communication Protocols: 
-- HTTP/HTTPS: Used for secure communication between the front-end user interfaces and 
back-end servers. 
-- Wi-Fi/Ethernet: For reliable network connectivity to the system's web-based components. 
-- Bluetooth: In some cases, for local device communication, e.g., attendance tracking using 
Bluetooth beacons (if implemented). 
-- API Calls: Communication between application and external services will be facilitated 
through RESTful APIs. 
- Mobile Hardware Specifics: 
-- GPS Access: The university map will leverage GPS features for precise location mapping 
on mobile devices. 
-- Camera Access: The app may use the device camera for features such as QR code 
scanning during event attendance. 
- Cloud Servers and Database Interaction: 
-- The system will interact with cloud-based servers for data storage, processing, and 
retrieval. The backend databases will handle queries and responses between hardware and 
software. 

== Communications interfaces
