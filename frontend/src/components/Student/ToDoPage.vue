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
          <div v-for="task in tasks" :key="task.name" class="task-item">
            <router-link v-if="task.name === 'Online Lecture'" :to="{ path: '/meeting' }" class="task-link">
              <div class="task-icon">
                <i :class="task.icon"></i>
              </div>
              <div class="details">
                <div class="task-name">{{ task.name }}</div>
                <div class="task-course">{{ task.course }}</div>
              </div>
              <div class="due">{{ task.due }}</div>
            </router-link>
            <!-- Default task link for other tasks -->
            <router-link v-else :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="task-icon">
                <i :class="task.icon"></i>
              </div>
              <div class="details">
                <div class="task-name">{{ task.name }}</div>
                <div class="task-course">{{ task.course }}</div>
              </div>
              <div class="due">{{ task.due }}</div>
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
        <div v-else>
          <p>Your missing tasks will be listed here...</p>
        </div>
      </div>
    </div>

    <!-- Done Tasks Section -->
    <div v-if="activeTab === 'done'" class="task-sections">
      <div class="task-box" v-for="(tasks, section) in tasksBySection.done" :key="section">
        <div class="section-header" @click="toggleSection(section)">
          <span>{{ sectionTitles[section] }}</span>
          <div class="expand-icon-wrapper">
            <span class="task-count">{{ tasks.length }}</span>
            <span class="expand-icon" :class="{ open: isSectionOpen(section) }">⌄</span>
          </div>
        </div>
        <div v-show="isSectionOpen(section)" class="task-list">
          <div v-for="task in tasks" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="task-icon">
                <i :class="task.icon"></i>
              </div>
              <div class="details">
                <div class="task-name">{{ task.name }}</div>
                <div class="task-course">{{ task.course }}</div>
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
          thisWeek: "This Week",
          nextWeek: "Next Week",
          later: "Later",
          doneThisWeek: "Done This Week",
          doneNextWeek: "Done Next Week",
          doneLater: "Done Later",
        },
        tasksBySection: {
          assigned: {
            thisWeek: [
              { name: "Assignment 1", course: "CSC 410 Software Quality", due: "Today, 11:59 pm", icon: "fas fa-file-alt" },
              { name: "Online Lecture", course: "CSC 412 Software Security", due: "Tomorrow, 1:00 pm", icon: "fas fa-video" },
            ],
            nextWeek: [
              { name: "Assignment 2", course: "CSC 410 Software Quality", due: "Monday, 11:59 pm", icon: "fas fa-file-alt" },
            ],
            later: [
              { name: "Assignment 3", course: "CSC 411 Machine Learning", due: "Next Month, 11:59 pm", icon: "fas fa-file-alt" },
            ],
          },
          missing: [],
          done: {
            thisWeek: [
              { name: "Assignment 1", course: "CSC 410 Software Quality", due: "Turned In", icon: "fas fa-file-alt" },
            ],
            nextWeek: [],
            later: [],
          },
        },
      };
    },
    methods: {
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
