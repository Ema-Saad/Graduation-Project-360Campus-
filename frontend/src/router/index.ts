import { createRouter, createWebHistory } from 'vue-router';

// Student
import HomePage from '../components/Student/HomePage.vue';
import CourseList from '../components/CourseList.vue';
import MyClassPage from '../components/Student/MyClassPage.vue';
import TimeTablePage from '../components/Student/TimeTablePage.vue';
import EventList from '../components/EventList.vue';
import GraduationProjectList from '../components/GraduationProjectList.vue';
import MapView from '../components/MapView.vue';
import CourseView from '../components/CourseView.vue';
import TutorialChat from '@/components/Student/TutorialChat.vue';
import AssignmentPage from '@/components/Student/AssignmentPage.vue';
import MeetingCard from "@/components/Student/MeetingCard.vue";
import GraduationProjectView from '@/components/GraduationProjectView.vue';
import LoginPage from '@/components/LoginPage.vue';
import ForgotPasswordPage from '@/components/ForgotPasswordPage.vue';
import VerificationPage from '@/components/Student/VerificationPage.vue';
import ResetPasswordPage from '@/components/Student/ResetPassword.vue';
import CongratulationsPage from '@/components/CongratulationsPage.vue';
import ErrorPage from '@/components/ErrorPage.vue';
import ProfileView from "@/components/ProfileView.vue";
import ClassroomList from '@/components/ClassroomList.vue';
import ToDoPage from "@/components/Student/ToDoPage.vue";
import ClassroomView from '@/components/ClassroomView.vue';
import TaskView from '@/components/TaskView.vue';
import SettingsPage from '@/components/SettingsPage.vue';
import QuizPage from '@/components/Student/QuizPage.vue';
import Timeline from "@/components/Student/Timeline.vue";
import AssignmentNumberVue from '../components/Student/assignmentnumber.vue';

// Doctor
import ForgotPasswordDOC from '@/components/Doctor/ForgotPasswordDOC.vue';
import VerificationDOC from '@/components/Doctor/VerificationDOC.vue';
import ResetPasswordDOC from '@/components/Doctor/ResetPasswordDOC.vue';
import CongratulationsDOC from '@/components/Doctor/CongratulationsDOC.vue';
import ErrorDOC from '@/components/Doctor/ErrorDOC.vue';
import HomePageDOC from '../components/Doctor/HomePageDOC.vue';
import DOCProfile from '@/components/Doctor/DOCProfile.vue';
import EventsDOC from '../components/Doctor/EventsDOC.vue';
import MapPageDOC from '../components/Doctor/MapPageDOC.vue';
import GraduationProjectDOC from '../components/Doctor/GraduationProjectDOC.vue';
import MyClassDOC from '@/components/Doctor/MyClassDOC.vue';
import TimetableDOC from '@/components/Doctor/TimetableDOC.vue';
import MaterialDOC from '@/components/Doctor/MaterialDOC.vue';
import DOCSettings from '@/components/Doctor/DOCSettings.vue';
import DOCTimeline from '@/components/Doctor/DOCTimeline.vue';
import MATCourseDOC from '@/components/Doctor/MATCourseDOC.vue';
import DOCLecture from '@/components/Doctor/DOCLecture.vue';
import DOCTutorial from '@/components/Doctor/DOCTutorial.vue';
import DOCLab from '@/components/Doctor/DOCLab.vue';
import DOCAssignment from '@/components/Doctor/DOCAssignment.vue';

const routes = [
  // Redirect root to doctor home (can be changed to student home if needed)
// { path: '/', redirect: '/doctor' },

  // Doctor Routes
  { path: '/doctor-profile', component: DOCProfile, name: 'DOCProfile' },
  { path: '/doctor-settings', component: DOCSettings, name: 'DOCSettings' },
  { path: '/doctor-timeline', component: DOCTimeline, name: 'DOCTimeline' },
  { path: '/doctor-graduation', component: GraduationProjectDOC, name: 'DoctorGraduationProject' },
  { path: '/doctor-map', component: MapPageDOC, name: 'DoctorMap' },
  { path: '/doctor-events', component: EventsDOC, name: 'DoctorEvents' },
  { path: '/doctor-myclass', component: MyClassDOC, name: 'DoctorMyClass' },
  { path: '/doctor-timetable', component: TimetableDOC, name: 'DoctorTimetable' },
  { path: '/doctor-materials', component: MaterialDOC, name: 'DoctorMaterials' } ,

  { path: '/doctor/mat-course/:id', component: MATCourseDOC, name: 'MATCourseDOC', props: true }, // ✅ FIXED
  { path: '/doctor/course/:id/lecture', component: DOCLecture, name: 'DOCLecture', props: true },
  { path: '/doctor/course/:id/tutorial', component: DOCTutorial, name: 'DOCTutorial', props: true },
  { path: '/doctor/course/:id/lab', component: DOCLab, name: 'DOCLab', props: true },
  { path: '/doctor/course/:id/assignment', component: DOCAssignment, name: 'DOCAssignmentById', props: true },



  // Student Routes
  { path: '/', redirect:'/home'},
  { name: 'Home', path: '/home', component: HomePage,  },
  { name: 'ProfileView', path: '/profile', component: ProfileView,  },
  { name: 'Login', path: '/login', component: LoginPage,  },
  { name: 'Verification', path: '/verification', component: VerificationPage,  },
  { name: 'ForgotPassword', path: '/forgot-password', component: ForgotPasswordPage,  },
  { name: 'ResetPassword', path: '/reset-password', component: ResetPasswordPage,  },
  { name: 'Error', path: '/error', component: ErrorPage,  },
  { name: 'Timeline', path: '/timeline', component: Timeline,  },
  { name: 'Settings', path: '/settings', component: SettingsPage,  },
  { name: 'CourseList', path: '/course/list', component: CourseList,  },
  { name: 'MyClass', path: '/myclass', component: ClassroomList,  },
  { name: 'taskDetail', props: true, path: '/task/:taskId', component: TaskView,  },
  { name: 'MyCourses', path: '/my-courses', component: ClassroomList,  },
  { name: 'MyCourseDetail', props: true, path: '/my-course/:course_id', component: ClassroomView, },
  { name: 'CourseDetails', props: true, path: '/course/details/:id', component: CourseView,  },
  { name: 'Events', path: '/events', component: EventList,  },
  { name: 'ToDoPage', path: '/todo', component: ToDoPage,  },
  { name: 'TimeTable', path: '/timetable', component: TimeTablePage,  },
  { name: 'GraduationProject', path: '/graduation', component: GraduationProjectList,  },
  { name: 'ProjectDetails', props: true, path: '/project/:id', component: GraduationProjectView,  },
  { name: 'Map', path: '/map', component: MapView,  },
  { name: 'TutorialChat', props: true, path: '/tutorialchat/:courseId/week/:weekId', component: TutorialChat,  },
  { name: 'AssignmentById', path: '/assignment/:id', component: AssignmentPage,  },
  { name: 'AssignmentByNumber', props: true, path: '/assignment/number/:assignmentNumber', component: AssignmentNumberVue,  },
  { name: 'Meeting', path: '/meeting/:id', component: MeetingCard,  },
  { name: 'Quiz', props: true, path: '/quiz/:weekId', component: QuizPage,  },
  { name: 'Congratulations', path: '/congratulations', component: CongratulationsPage,  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
