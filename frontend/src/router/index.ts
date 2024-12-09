import Vue from 'vue';
import Router from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import MaterialsPage from '../components/MaterialsPage.vue';
import MyClassPage from '../components/MyClassPage.vue';
import TimeTablePage from '../components/TimeTablePage.vue';
import EventsPage from '../components/EventsPage.vue';
import GraduationProjectPage from '../components/GraduationProjectPage.vue';
import MapPage from '../components/MapPage.vue';
import CourseDetails from '../components/CourseDetails.vue';
import LecturePage from '@/components/LecturePage.vue';
import TutorialPage from '@/components/TutorialPage.vue';
import LabPage from '@/components/LabPage.vue';
import AssignmentPage from '@/components/AssignmentPage.vue';
import ProjectDetails from '@/components/ProjectDetails.vue';
import LoginPage from '@/components/LoginPage.vue';
import ForgotPasswordPage from '@/components/ForgotPasswordPage.vue';
import VerificationPage from '@/components/VerificationPage.vue';
import ResetPasswordPage from '@/components/ResetPassword.vue';
import CongratulationsPage from '@/components/CongratulationsPage.vue';
import ErrorPage from '@/components/ErrorPage.vue';
import ProfilePage from "@/components/ProfilePage.vue";
import MyCourses from '@/components/MyCourses.vue';
import ToDoPage from "@/components/ToDoPage.vue";
import MyCourseDetail from '@/components/MyCourseDetail.vue';
import TaskDetail from '@/components/TaskDetail.vue';
import SettingsSection from '@/components/SettingsSection.vue';
import Timeline from "@/components/Timeline.vue";

// Define routes
const routes = [
  {
    path: '/profile',  // Changed to '/profile' for clarity
    name: 'ProfilePage',  // Fixed name, removed extra dot
    component: ProfilePage
  },
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
