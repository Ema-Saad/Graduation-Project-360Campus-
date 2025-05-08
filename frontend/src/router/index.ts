import { createRouter, createWebHistory } from 'vue-router';

// Student
import HomePage from '../components/HomePage.vue';
import CourseList from '../components/CourseList.vue';
import MyClassPage from '../components/Student/MyClassPage.vue';
import TimetableView from '../components/TimetableView.vue';
import EventList from '../components/EventList.vue';
import GraduationProjectList from '../components/GraduationProjectList.vue';
import MapView from '../components/MapView.vue';
import CourseView from '../components/CourseView.vue';
import MeetingCard from "@/components/MeetingCard.vue";
import GraduationProjectView from '@/components/GraduationProjectView.vue';
import LoginPage from '@/components/LoginPage.vue';
import ForgotPasswordPage from '@/components/ForgotPasswordPage.vue';
import VerificationPage from '@/components/VerificationPage.vue';
import ResetPasswordPage from '@/components/ResetPasswordPage.vue';
import CongratulationsPage from '@/components/CongratulationsPage.vue';
import ErrorPage from '@/components/ErrorPage.vue';
import ProfileView from "@/components/ProfileView.vue";
import ClassroomList from '@/components/ClassroomList.vue';
import ToDoPage from "@/components/ToDoPage.vue";
import ClassroomView from '@/components/ClassroomView.vue';
import TaskView from '@/components/TaskView.vue';
import SettingsPage from '@/components/SettingsPage.vue';
import QuizView from '@/components/QuizView.vue';

const routes = [
  // Redirect root to doctor home (can be changed to student home if needed)
// { path: '/', redirect: '/doctor' },

  { path: '/', redirect:'/home'},
  { name: 'Home', path: '/home', component: HomePage,  },
  { name: 'ProfileView', path: '/profile', component: ProfileView,  },
  { name: 'Login', path: '/login', component: LoginPage,  },
  { name: 'Verification', path: '/verification', component: VerificationPage,  },
  { name: 'ForgotPassword', path: '/forgot-password', component: ForgotPasswordPage,  },
  { name: 'ResetPassword', path: '/reset-password', component: ResetPasswordPage,  },
  { name: 'Error', path: '/error', component: ErrorPage,  },
  { name: 'Settings', path: '/settings', component: SettingsPage,  },
  { name: 'CourseList', path: '/course/list', component: CourseList,  },
  { name: 'MyClass', path: '/myclass', component: ClassroomList,  },
  { name: 'taskDetail', props: true, path: '/task/:taskId', component: TaskView,  },
  { name: 'MyCourses', path: '/my-courses', component: ClassroomList,  },
  { name: 'MyCourseDetail', props: true, path: '/my-course/:course_id', component: ClassroomView, },
  { name: 'CourseDetails', props: true, path: '/course/details/:id', component: CourseView,  },
  { name: 'Events', path: '/events', component: EventList,  },
  { name: 'ToDoPage', path: '/todo', component: ToDoPage,  },
  { name: 'TimeTable', path: '/timetable', component: TimetableView,  },
  { name: 'GraduationProject', path: '/graduation', component: GraduationProjectList,  },
  { name: 'ProjectDetails', props: true, path: '/project/:id', component: GraduationProjectView,  },
  { name: 'Map', path: '/map', component: MapView,  },
  { name: 'Meeting', path: '/meeting/:id', component: MeetingCard,  },
  { name: 'Quiz', props: true, path: '/quiz/:weekId', component: QuizView,  },
  { name: 'Congratulations', path: '/congratulations', component: CongratulationsPage,  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
