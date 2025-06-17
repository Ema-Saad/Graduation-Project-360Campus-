<template>
  <div>
    <main>
      <h2 class="section-title">Weekly Schedule</h2>

      <div v-for="(schedule, index) in schedules" :key="index">
        <h3 class="schedule-day-title">{{ schedule.day }}</h3>
        <table class="schedule-table">
          <thead>
            <tr>
              <th>Slot</th>
              <th>Course Code</th>
              <th>Course Name</th>
              <th>Session Type</th>
              <th>Group</th>
              <th>Room</th>
              <th>Instructor</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(session, i) in schedule.sessions" :key="i" 
                :class="i % 2 === 0 ? 'orange-row' : 'white-row'">
              <!-- Slot Column with Rowspan -->
              <td v-if="session.showSlot" :rowspan="session.rowspan">{{ session.slot }}</td>
              
              <td>{{ session.courseCode }}</td>
              <td>{{ session.courseName }}</td>
              <td>{{ session.sessionType }}</td>
              <td>{{ session.group }}</td>
              <td>{{ session.room }}</td>
              <td class="instructor">{{ session.instructor }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      schedules: [
        {
          day: "Saturday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
        {
          day: "Sunday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
        {
          day: "Monday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
        {
          day: "Tuesday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
        {
          day: "Wednesday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
        {
          day: "Wednesday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
        {
          day: "Thursday",
          sessions: [
            { slot: "Slot 1", courseCode: "AID422-TUT", courseName: "Natural Language Processing (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 AID 2-1", room: "B18 G7", instructor: "Sarah (TA)", showSlot: true, rowspan: 3 },  
            { slot: "Slot 1", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-2", room: "LAB COE F2.17-A", instructor: "Alshaimaa (TA)", showSlot: false },
            { slot: "Slot 1", courseCode: "CSC422-LEC", courseName: "Fundamentals of Cloud Computing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.07", instructor: "Karim Hassanien (Professor)", showSlot: false },

            { slot: "Slot 2", courseCode: "AID421-LEC", courseName: "Computer Vision (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 2", courseCode: "CSC427-LEC", courseName: "Design Patterns (LEC)", sessionType: "Lecture", group: "CSIT Year 4 CSC 1-0", room: "B10 F1.08", instructor: "Moamen (Professor)", showSlot: false },

            { slot: "Slot 3", courseCode: "AID422-LEC", courseName: "Natural Language Processing (LEC)", sessionType: "Lecture", group: "CSIT Year 4 AID 2-0", room: "Theater B18 G22", instructor: "Moustafa (Professor)", showSlot: true, rowspan: 2 },
            { slot: "Slot 3", courseCode: "CSC422-LAB", courseName: "Fundamentals of Cloud Computing (LAB)", sessionType: "Lab", group: "CSIT Year 4 CSC 1-1", room: "LAB COE G08-B", instructor: "Abdelrahman (TA)", showSlot: false },

            { slot: "Slot 4", courseCode: "AID421-LAB", courseName: "Computer Vision (LAB)", sessionType: "Lab", group: "CSIT Year 4 AID 2-1", room: "B18 G16", instructor: "Sarah (TA)", showSlot: true, rowspan: 2 },
            { slot: "Slot 4", courseCode: "CSC427-TUT", courseName: "Design Patterns (TUT)", sessionType: "Tutorial", group: "CSIT Year 4 CSC 1-1", room: "B10 F1.07", instructor: "Mariam (TA)", showSlot: false },
          ],
        },
      ],
    };
  }
};
</script>

<style scoped>
/* Reset Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Page Styling */
body {
  font-family: "Poppins", Arial, sans-serif;
  background-color: #fff;
  color: #333;
  line-height: 1.5;
}

main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

/* Section Title */
.section-title {
  font-size: 30px;
  font-weight: 700;
  color: #201887;
  text-align: center;
  margin-bottom: 20px;
}

/* Schedule Day Title */
.schedule-day-title {
  font-size: 24px;
  font-weight: 700;
  background-color: #F17E0B;
  color: #fff;
  padding: 6px 14px;
  border-radius: 8px;
  margin: 30px 0 16px;
  display: inline-block;
}

/* Table Styling */
.schedule-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 30px;
  border: 2px solid #201887;
}

.schedule-table th {
  background-color: #201887;
  color: #FFFFFF;
  font-weight: 600;
  padding: 10px;
  text-align: left;
}

.schedule-table td {
  border: 1px solid #dddddd;
  padding: 8px 12px;
  text-align: left;
  vertical-align: top;
  font-family: 'Poppins', Arial, sans-serif;
}

/* Row-Based Colors */
.orange-row {
  background-color: #F4C462; /* Light Orange */
}

.white-row {
  background-color: #FFFFFF; /* White */
}

/* Ensure the Slot column follows the row color */
.orange-row td:first-child {
  background-color: #F4C462;
}

.white-row td:first-child {
  background-color: #FFFFFF;
}

/* Instructor Name Styling */
.instructor {
  font-style: italic;
}
</style>
