<template>
  <div class="todo-page">
    <!-- Tabbed Navigation -->
    <div class="tabs">
      <div :class="['tab', { active: activeTab === 'assigned' }]" @click="setActiveTab('assigned')">Assigned</div>
      <div :class="['tab', { active: activeTab === 'missing' }]" @click="setActiveTab('missing')">Missing</div>
      <div :class="['tab', { active: activeTab === 'done' }]" @click="setActiveTab('done')">Done</div>
    </div>

    <div class="tab-separator"></div>

    <!-- Task Sections for Assigned Tab -->
    <div v-if="activeTab === 'assigned'" class="task-sections">
      <div class="task-box" v-for="(tasks, section) in tasksBySection.assigned" :key="section">
        <div class="section-header" @click="toggleSection(section)">
          <span>{{ sectionTitles[section] }}</span>
          <div class="expand-icon-wrapper">
            <span class="task-count">{{ tasks.length }}</span>
            <span class="expand-icon" :class="{ open: isSectionOpen(section) }">⌄</span>
          </div>
        </div>
        <div v-show="isSectionOpen(section)" class="task-list">
          <div v-for="task in tasks" :key="task.id" class="task-item">
            <router-link :to="task.link" class="task-link">
              <div class="task-icon">
                <i class="fas" :class="[task.icon]"></i>
              </div>
              <div class="details">
                <div class="task-name">{{ task.title }}</div>
                <div class="task-course">{{ task.classroom.course.title }}</div>
              </div>
              <div class="due">{{ computeDueString(task.deadline) }}</div>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Missing Tasks Section -->
    <div v-if="activeTab === 'missing'" class="missing-section">
      <div class="missing-content">
        <h2>Missing Tasks</h2>
        <div v-if="tasksBySection.missing.length === 0" class="missing-image">
          <img src="@/assets/nothing.png" alt="No Tasks Image" />
        </div>
        <div v-else v-for="task in tasksBySection.missing">
          <router-link :to="task.link" class="task-link">
              <div class="task-icon">
                <i class="fas fa-file-alt"></i>
              </div>
              <div class="details">
                <div class="task-name">{{ task.title }}</div>
                <div class="task-course">{{ task.classroom.course.title }}</div>
              </div>
              <div class="due">Missed</div>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Done Tasks Section -->
    <div v-if="activeTab === 'done'" class="task-sections">
      <div class="task-box" v-for="(tasks, section) in tasksBySection.done" :key="section">
        <div class="section-header" @click="toggleSection(section)">
          <span>{{ sectionTitles[`done${section[0].toUpperCase()}${section.substring(1)}`] }}</span>
          <div class="expand-icon-wrapper">
            <span class="task-count">{{ tasks.length }}</span>
            <span class="expand-icon" :class="{ open: isSectionOpen(section) }">⌄</span>
          </div>
        </div>
        <div v-show="isSectionOpen(section)" class="task-list">
          <div v-for="task in tasks" :key="task.id" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.id } }" class="task-link">
              <div class="task-icon">
                <i class="fas fa-file-alt"></i>
              </div>
              <div class="details">
                <div class="task-name">{{ task.title }}</div>
                <div class="task-course">{{ task.classroom.course.title }}</div>
              </div>
              <div class="due">Turned In</div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  // Task Types

  export default {
    data() {
      return {
        activeTab: "assigned",
        openedSections: {
          thisWeek: false,
          nextWeek: false,
          later: false,
          doneThisWeek: false,
          doneNextWeek: false,
          doneLater: false,
        },
        sectionTitles: {
          noDueDate: "No Due Date",
          thisWeek: "This Week",
          nextWeek: "Next Week",
          later: "Later",
          doneNoDueDate: "No Due Date",
          doneEarly: "Done Early",
          doneThisWeek: "This Week",
          donePreviousWeek: "Last Week",
          doneEarlier: "Done Earlier",
        },
        tasksBySection: {
          assigned: {
            noDueDate: [],
            thisWeek: [],
            nextWeek: [],
            later: [],
          },
          missing: [],
          done: {
            noDueDate: [],
            early: [],
            thisWeek: [],
            previousWeek: [],
            earlier: [],
          },
        },
      };
    },
    beforeMount() {
      let registered_classroom = this.$root.request_api_endpoint('api/registered_classrooms', 'get', null);

      const TYPE_ASSIGNMENT = 'a', TYPE_ONLINE_MEETING = 'o', TYPE_QUIZ = 'q';

      let get_icon = (t) => {
        if (t === TYPE_ONLINE_MEETING)
          return 'fa-video';
        //else if (t === TYPE_QUIZ)
        //  return ''
        else
          return 'fa-file-alt';
      };

      let get_page_link = (d, ...other) => {
        console.log(d);

        if (d.kind === TYPE_ONLINE_MEETING)
          return { name: 'Meeting', params: { id: d.id } };
        else
          return { name: 'taskDetail', params: { taskId: d.id } };
      };

      registered_classroom.then((data) => {
        for (let classroom of data) {
          let tasks = this.$root.request_api_endpoint(`api/course/${classroom.id}/classroom/tasks`, 'get', null);
          let assignments = this.$root.request_api_endpoint(`api/course/${classroom.id}/classroom/assignments`, 'get', null);
          let submitted_assignments = this.$root.request_api_endpoint(`api/course/${classroom.id}/classroom/assignments/submitted`, 'get', null);

          tasks.then((data) => {
            let transform = (d) => ({ 
              ...d, 
              deadline: d.time ? new Date(d.time) : null, 
              classroom: classroom, 
              icon: get_icon(d.kind),
              link: get_page_link(d, classroom),
            });

            let tasks = data.map(transform);

            let assigned_thisWeek = this.tasksBySection.assigned.thisWeek;
            let assigned_nextWeek = this.tasksBySection.assigned.nextWeek;
            let assigned_later = this.tasksBySection.assigned.later;

            const MILLISECONDS_IN_DAY = 24 * 60 * 60 * 1000;

            let is_past = (d) => Date.now() > d.deadline;
            let is_due_this_week = (d) => !is_past(d) && d.deadline - Date.now() <= 7 * MILLISECONDS_IN_DAY;
            let is_due_next_week = (d) => !is_past(d) && !is_due_this_week(d) && d.deadline - Date.now() <= 14 * MILLISECONDS_IN_DAY;
            let is_due_later = (d) => !is_past(d) && d.deadline - Date.now() > 14 * MILLISECONDS_IN_DAY;

            this.tasksBySection.assigned.thisWeek = [...assigned_thisWeek, ...tasks.filter(is_due_this_week)]
            this.tasksBySection.assigned.nextWeek = [...assigned_nextWeek, ...tasks.filter(is_due_next_week)]
            this.tasksBySection.assigned.later = [...assigned_later, ...tasks.filter(is_due_later)]

          });

          Promise.all([assignments, submitted_assignments]).then((data) => {
            let transform = (d) => ({ 
              ...d, 
              deadline: d.time ? new Date(d.time) : null,
              classroom: classroom,
              icon: get_icon(d.icon),
              link: get_page_link(d, classroom),
            });

            let submitted_assignments = data[1].map(transform);
            let unsubmitted_assignments = data[0]
              .filter((d) => undefined === submitted_assignments.find((e) => e.id === d.id))
              .map(transform);

            let deadlined_submitted_assignments = submitted_assignments.filter((e) => e.deadline);
            let deadlined_unsubmitted_assignments = unsubmitted_assignments.filter((e) => e.deadline);

            let assigned_noDueDate = this.tasksBySection.assigned.noDueDate;
            let assigned_thisWeek = this.tasksBySection.assigned.thisWeek;
            let assigned_nextWeek = this.tasksBySection.assigned.nextWeek;
            let assigned_later = this.tasksBySection.assigned.later;
            let missing = this.tasksBySection.missing;
            let done_noDueDate = this.tasksBySection.done.noDueDate;
            let done_early = this.tasksBySection.done.early;
            let done_thisWeek = this.tasksBySection.done.thisWeek;
            let done_previousWeek = this.tasksBySection.done.previousWeek;
            let done_earlier = this.tasksBySection.done.earlier;

            const MILLISECONDS_IN_DAY = 24 * 60 * 60 * 1000;

            let is_missing = (d) => Date.now() > d.deadline;
            let is_due_this_week = (d) => !is_missing(d) && d.deadline - Date.now() <= 7 * MILLISECONDS_IN_DAY;
            let is_due_next_week = (d) => !is_missing(d) && !is_due_this_week(d) && d.deadline - Date.now() <= 14 * MILLISECONDS_IN_DAY;
            let is_due_later = (d) => !is_missing(d) && d.deadline - Date.now() > 14 * MILLISECONDS_IN_DAY;

            this.tasksBySection.assigned.noDueDate = [...assigned_noDueDate, ...unsubmitted_assignments.filter((e) => !e.deadline)];
            this.tasksBySection.assigned.thisWeek = [...assigned_thisWeek, ...deadlined_unsubmitted_assignments.filter(is_due_this_week)]
            this.tasksBySection.assigned.nextWeek = [...assigned_nextWeek, ...deadlined_unsubmitted_assignments.filter(is_due_next_week)]
            this.tasksBySection.assigned.later = [...assigned_later, ...deadlined_unsubmitted_assignments.filter(is_due_later)]

            this.tasksBySection.missing = [...missing, ...unsubmitted_assignments.filter(is_missing)];

            let is_done_early = (d) => d.deadline > Date.now();
            let is_done_this_week = (d) => !is_done_early(d) && Date.now() - d.deadline <= 7 * MILLISECONDS_IN_DAY;
            let is_done_previous_week = (d) => !is_done_early(d) && !is_done_this_week(d) && Date.now() - d.deadline <= 14 * MILLISECONDS_IN_DAY;
            let is_done_earlier = (d) => !is_done_early(d) && Date.now() - d.deadline > 14 * MILLISECONDS_IN_DAY;

            this.tasksBySection.done.noDueDate = [...done_noDueDate, ...submitted_assignments.filter((e) => !e.deadline)];
            this.tasksBySection.done.early = [...done_early, ...deadlined_submitted_assignments.filter(is_done_early)];
            this.tasksBySection.done.thisWeek = [...done_thisWeek, ...deadlined_submitted_assignments.filter(is_done_this_week)]
            this.tasksBySection.done.previousWeek = [...done_previousWeek, ...deadlined_submitted_assignments.filter(is_done_previous_week)]
            this.tasksBySection.done.earlier = [...done_earlier, ...deadlined_submitted_assignments.filter(is_done_earlier)]
          });
        }
      });

    },
    methods: {
      computeDueString(date) {
        const MILLISECONDS_IN_DAY = 24 * 60 * 60 * 1000;
        const DAYS = [
          "Sunday", "Monday", "Tuesday", 
          "Wednesday", "Thursday", "Friday", "Saturday"
        ];
        const MONTHS = [
          "Jan", "Feb", "Mar", "Apr",
          "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec",
        ];

        let hour = `${date.getHours().toString().padStart(2, "0")}:${date.getMinutes().toString().padStart(2, "0")}`;
        if (Date.now() > date) {
          return "Missed";

        } else if (date - Date.now() <= MILLISECONDS_IN_DAY) {
          return `Due Today at ${hour}`;

        } else if (date - Date.now() <= 2 * MILLISECONDS_IN_DAY) {
          return `Due Tomorrow at ${hour}`;

        } else if (date - Date.now() <= 7 * MILLISECONDS_IN_DAY) {
          return `Due ${DAYS[date.getDay()]} at ${hour}`;
        } else {
          return `Due ${MONTHS[date.getMonth()]}. ${date.getDate().toString().padStart(2, "0")} at ${hour}`;
        }

      },
      setActiveTab(tab) {
        this.activeTab = tab;
      },
      toggleSection(section) {
        this.openedSections[section] = !this.openedSections[section];
      },
      isSectionOpen(section) {
        return this.openedSections[section];
      },
    },
  };
</script>

<style scoped>
  /* Tabs */
  .tabs {
    display: flex;
    justify-content: space-around;
    margin-bottom: 0; /* Remove any margin between tabs and separator */
    position: relative;
    padding-top: 17px; /* Moves the entire tab section down */
  }
  .tab {
    cursor: pointer;
    padding: 12px 10px; /* Adds more space inside the tabs */
    font-size: 16px;
  }
  /* Orange separator under tabs */
  .tab-separator {
    width: 100%;
    height: 2px;
    background-color: #f68b1e; /* Orange color */
    position: absolute;
    bottom: 79%;
    left: 0;
  }

    .tab.active {
      font-weight: bold;
      color: #1423ce;
      text-decoration: underline 3px #1423ce; /* Adds a blue underline */
      text-underline-offset: 4px; /* Adjusts the spacing of the underline */
    }


  /* Task Box */
  .task-box {
    margin: 10px 0;
    border: 1px solid #ccc;

  }

    .task-box:hover {
      border: 1px solid #007bff;
    }


    .section-header {
    padding: 10px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .expand-icon-wrapper {
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .expand-icon {
    margin-right: 5px;
  }

    .expand-icon.open {
      transform: rotate(180deg);
    }

  .task-count {
    background-color: #ff6a00;
    color: white;
    border-radius: 50%;
    padding: 5px 10px;
  }

  .task-list {
    padding: 10px;
    background-color: white; /* Change background to white */
    display: flex;
    flex-direction: column;
    border-radius: 5px; /* Optional: Add rounded corners */
  }


  .task-item {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    display: flex;
    align-items: center;
  }
    .task-item:last-child {
      border-bottom: none;
    }

  .task-link {
    display: flex;
    align-items: center;
    text-decoration: none;
    color: black;
    width: 100%;
  }

  /* Task Icons */
  .task-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #1a237e;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
  }

    .task-icon i {
      font-size: 20px;
      color: white;
    }

  /* Text */
  .details {
    flex: 1;
  }

  .task-name {
    font-weight: bold;
  }

  .task-course {
    color: gray;
  }

  .due {
    text-align: right;
    color: gray;
  }

  .missing-content {
    text-align: center;
    padding: 20px;
  }

  .missing-image img {
    width: 100%;
    max-width: 300px;
  }

  /* Media Queries for Responsive Design */
  /* Small screens (phones) */
  @media (max-width: 600px) {
    .tabs {
      flex-direction: column;
      align-items: stretch;
    }

    .tab {
      padding: 10px;
      font-size: 14px;
      text-align: center;
    }

    .tab-separator {
      bottom: 65%;
    }

    .task-box {
      padding: 10px;
    }

    .task-link {
      flex-direction: column;
      align-items: flex-start;
    }

    .task-icon {
      margin-bottom: 10px;
    }

    .details {
      text-align: left;
    }

    .task-name {
      font-size: 16px;
    }

    .task-course {
      font-size: 14px;
    }

    .due {
      font-size: 12px;
      margin-top: 5px;
    }
  }

  /* Medium screens (Tablets, small laptops) */
  @media (min-width: 601px) and (max-width: 1024px) {
    .tabs {
      justify-content: space-evenly;
    }

    .tab {
      font-size: 18px;
      padding: 14px;
    }
    .tab-separator {
      bottom: 77%;
    }

    .task-box {
      margin: 15px 0;
    }

    .task-list {
      padding: 15px;
    }

    .task-name {
      font-size: 18px;
    }

    .task-course,
    .due {
      font-size: 16px;
    }

    .task-icon {
      width: 50px;
      height: 50px;
    }
  }
</style>
