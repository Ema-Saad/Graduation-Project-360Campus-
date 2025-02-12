import Vue from 'vue';
import Router from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/Student/HomePage.vue';
import MaterialsPage from '../components/Student/MaterialsPage.vue';
import MyClassPage from '../components/Student/MyClassPage.vue';
import TimeTablePage from '../components/Student/TimeTablePage.vue';
import EventsPage from '../components/Student/EventsPage.vue';
import GraduationProjectPage from '../components/Student/GraduationProjectPage.vue';
import MapPage from '../components/Student/MapPage.vue';
import CourseDetails from '../components/Student/CourseDetails.vue';
import LecturePage from '@/components/Student/LecturePage.vue';
import TutorialPage from '@/components/Student/TutorialPage.vue';
import LabPage from '@/components/Student/LabPage.vue';
import AssignmentPage from '@/components/Student/AssignmentPage.vue';
import ProjectDetails from '@/components/Student/ProjectDetails.vue';
import LoginPage from '@/components/Student/LoginPage.vue';
import ForgotPasswordPage from '@/components/Student/ForgotPasswordPage.vue';
import VerificationPage from '@/components/Student/VerificationPage.vue';
import ResetPasswordPage from '@/components/Student/ResetPassword.vue';
import CongratulationsPage from '@/components/Student/CongratulationsPage.vue';
import ErrorPage from '@/components/Student/ErrorPage.vue';
// import ProfilePage from "@/components/Student/ProfilePage.vue";
import MyCourses from '@/components/Student/MyCourses.vue';
import ToDoPage from "@/components/Student/ToDoPage.vue";
import MyCourseDetail from '@/components/Student/MyCourseDetail.vue';
import TaskDetail from '@/components/Student/TaskDetail.vue';
import SettingsSection from '@/components/Student/SettingsSection.vue';
import Timeline from "@/components/Student/Timeline.vue";

// Define routes
const routes = [
 /* {
    path: '/profile',  // Changed to '/profile' for clarity
    name: 'ProfilePage',  // Fixed name, removed extra dot
    component: ProfilePage
  },*/
  { path: '/', component: HomePage, name: 'Home' },
  { path: '/home', redirect: '/', },
  { path: '/login', component: LoginPage, name: 'Login' },
  { path: '/verification', name: 'Verification', component: VerificationPage },
  { path: '/forgot-password', name: 'ForgotPassword', component: ForgotPasswordPage },
  { path: '/reset-password', name: 'ResetPassword', component: ResetPasswordPage },
  { path: '/error', name: 'Error', component: ErrorPage },

  { path: "/timeline", name: "Timeline", component: Timeline },

  { path: '/settings', name: 'Settings', component: SettingsSection },
  { path: '/materials', name: 'Materials', component: MaterialsPage },
  { path: '/myclass', name: 'MyClass', component: MyClassPage },
  {
    path: '/task/:taskId',
    name: 'taskDetail',
    component: TaskDetail,
    props: true
  },
  { path: '/my-courses', name: 'MyCourses', component: MyCourses },
  {
    path: '/course/:id',
    name: 'MyCourseDetail',
    component: MyCourseDetail,
    props: true
  },
  { path: '/todo', name: 'ToDoPage', component: ToDoPage },
  { path: '/timetable', name: 'TimeTable', component: TimeTablePage },
  { path: '/events', name: 'Events', component: EventsPage },
  { path: '/graduation', name: 'GraduationProject', component: GraduationProjectPage },
  { path: '/project/:id', name: 'ProjectDetails', component: ProjectDetails, props: true },
  { path: '/map', name: 'Map', component: MapPage },
  { path: '/course/:id', name: 'CourseDetails', component: CourseDetails, props: true },
  { path: '/lecture/:id', name: 'Lecture', component: LecturePage },
  { path: '/tutorial/:id', name: 'Tutorial', component: TutorialPage },
  { path: '/lab/:id', name: 'Lab', component: LabPage },
  { path: '/assignment/:id', name: 'Assignment', component: AssignmentPage },
  { path: '/congratulations', name: 'Congratulations', component: CongratulationsPage }
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
