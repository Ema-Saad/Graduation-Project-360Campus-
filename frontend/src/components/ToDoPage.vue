<template>
  <div class="todo-page">
    <!-- Tabbed Navigation -->
    <div class="tabs">
      <div :class="['tab', { active: activeTab === 'assigned' }]" @click="setActiveTab('assigned')">Assigned</div>
      <div :class="['tab', { active: activeTab === 'missing' }]" @click="setActiveTab('missing')">Missing</div>
      <div :class="['tab', { active: activeTab === 'done' }]" @click="setActiveTab('done')">Done</div>
    </div>

    <!-- Task Sections for Assigned Tab -->
    <div v-if="activeTab === 'assigned'" class="task-sections">
      <!-- This Week Section -->
      <div class="task-box">
        <div class="section-header" @click="toggleSection('thisWeek')">
          <span>This Week</span>
          <span class="expand-icon" :class="{ open: isSectionOpen('thisWeek') }">⌄</span>
        </div>
        <div v-show="isSectionOpen('thisWeek')" class="task-list">
          <div v-for="task in tasksBySection.assigned.thisWeek" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="icon">
                <span :class="task.icon"></span>
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

      <!-- Next Week Section -->
      <div class="task-box">
        <div class="section-header" @click="toggleSection('nextWeek')">
          <span>Next Week</span>
          <span class="expand-icon" :class="{ open: isSectionOpen('nextWeek') }">⌄</span>
        </div>
        <div v-show="isSectionOpen('nextWeek')" class="task-list">
          <div v-for="task in tasksBySection.assigned.nextWeek" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="icon">
                <span :class="task.icon"></span>
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

      <!-- Earlier Section -->
      <div class="task-box">
        <div class="section-header" @click="toggleSection('earlier')">
          <span>Earlier</span>
          <span class="expand-icon" :class="{ open: isSectionOpen('earlier') }">⌄</span>
        </div>
        <div v-show="isSectionOpen('earlier')" class="task-list">
          <div v-for="task in tasksBySection.assigned.earlier" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="icon">
                <span :class="task.icon"></span>
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

    <!-- Task Sections for Missing Tab -->
    <div v-if="activeTab === 'missing'" class="missing-section">
      <div class="missing-content">
        <h2>Missing Tasks</h2>
        <div v-if="tasksBySection.missing && tasksBySection.missing.length === 0" class="missing-image">
          <img src="@/assets/nothing.png" alt="No Tasks Image" />
        </div>
        <div v-else>
          <p>Your missing tasks will be listed here...</p>
        </div>
      </div>
    </div>

    <!-- Task Sections for Done Tab -->
    <div v-if="activeTab === 'done'" class="task-sections">
      <!-- This Week Section -->
      <div class="task-box">
        <div class="section-header" @click="toggleSection('doneThisWeek')">
          <span>This Week</span>
          <span class="expand-icon" :class="{ open: isSectionOpen('doneThisWeek') }">⌄</span>
        </div>
        <div v-show="isSectionOpen('doneThisWeek')" class="task-list">
          <div v-for="task in tasksBySection.done.thisWeek" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="icon">
                <span :class="task.icon"></span>
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

      <!-- Next Week Section -->
      <div class="task-box">
        <div class="section-header" @click="toggleSection('doneNextWeek')">
          <span>Next Week</span>
          <span class="expand-icon" :class="{ open: isSectionOpen('doneNextWeek') }">⌄</span>
        </div>
        <div v-show="isSectionOpen('doneNextWeek')" class="task-list">
          <div v-for="task in tasksBySection.done.nextWeek" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="icon">
                <span :class="task.icon"></span>
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

      <!-- Earlier Section -->
      <div class="task-box">
        <div class="section-header" @click="toggleSection('doneEarlier')">
          <span>Earlier</span>
          <span class="expand-icon" :class="{ open: isSectionOpen('doneEarlier') }">⌄</span>
        </div>
        <div v-show="isSectionOpen('doneEarlier')" class="task-list">
          <div v-for="task in tasksBySection.done.earlier" :key="task.name" class="task-item">
            <router-link :to="{ name: 'taskDetail', params: { taskId: task.name } }" class="task-link">
              <div class="icon">
                <span :class="task.icon"></span>
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
        activeTab: "assigned", // Active tab
        openedSections: {
          thisWeek: false,
          nextWeek: false,
          earlier: false,
          doneThisWeek: false,
          doneNextWeek: false,
          doneEarlier: false,
        },
        tasksBySection: {
          assigned: {
            thisWeek: [
              { name: "Assignment 1", course: "CSC 410 Software Quality", due: "Today, 11:59 pm", icon: "icon-assignment" },
              { name: "Online Lecture", course: "CSC 412 Software Security", due: "Tomorrow, 1:00 pm", icon: "icon-lecture" },
            ],
            nextWeek: [
              { name: "Assignment 2", course: "CSC 410 Software Quality", due: "Monday, 11:59 pm", icon: "icon-assignment" },
            ],
            earlier: [
              { name: "Assignment 3", course: "CSC 411 Machine Learning", due: "Last Week, 11:59 pm", icon: "icon-assignment" },
            ],
          },
          missing: [],
          done: {
            thisWeek: [
              { name: "Assignment 1", course: "CSC 410 Software Quality", due: "Turned In", icon: "icon-assignment" },
            ],
            nextWeek: [],
            earlier: [],
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
  /* Style for tabs */
  .tabs {
    display: flex;
    justify-content: space-around;
    margin-bottom: 20px;
  }

  .tab {
    cursor: pointer;
    padding: 10px;
    font-size: 16px;
  }

    .tab.active {
      font-weight: bold;
      color: #42b983;
    }

  /* Task Box Styling */
  .task-box {
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .section-header {
    padding: 10px;
    cursor: pointer;
    background-color: #f4f4f4;
    border-radius: 5px;
    display: flex;
    justify-content: space-between;
  }

  .expand-icon.open {
    transform: rotate(180deg);
  }

  .task-list {
    padding: 10px;
    background-color: #fafafa;
    display: flex;
    flex-direction: column;
  }

  .task-item {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
  }

    .task-item:last-child {
      border-bottom: none;
    }

  .task-link {
    display: flex;
    justify-content: space-between;
    width: 100%;
  }

  .details {
    flex: 1;
    margin-left: 10px;
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
</style>
