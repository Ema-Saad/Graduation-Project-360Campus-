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
  { name: 'Map', path: '/map', component: MapView,  },
  { name: 'TimeTable', path: '/timetable', component: TimetableView,  },
  { name: 'ToDoPage', path: '/todo', component: ToDoPage,  },
  { name: 'Congratulations', path: '/congratulations', component: CongratulationsPage,  },
  { name: 'CourseList', path: '/course/list', component: CourseList,  },
  { name: 'ClassroomList', path: '/classroom/list', component: ClassroomList,  },
  { name: 'AssignmentView', props: true, path: '/assignment/:assignmentId', component: TaskView,  },
  { name: 'ClassroomView', props: true, path: '/classroom/:courseId', component: ClassroomView, },
  { name: 'CourseView', props: true, path: '/course/:courseId', component: CourseView,  },
  { name: 'EventList', path: '/event/list', component: EventList,  },
  { name: 'GraduationProjectList', path: '/graduation-project/list', component: GraduationProjectList,  },
  { name: 'GraduationProjectView', props: true, path: '/graduation-project/:graduationProjectId', component: GraduationProjectView, },
  { name: 'OnlineMeetingView', path: '/meeting/:onlineMeetingId', component: MeetingCard, props: true },
  { name: 'QuizView', props: true, path: '/quiz/:quizId', component: QuizView,  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
