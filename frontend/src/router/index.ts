import { createRouter, createWebHistory } from 'vue-router';

// Student
import HomePage from '../components/Student/HomePage.vue';
import MaterialsPage from '../components/Student/MaterialsPage.vue';
import MyClassPage from '../components/Student/MyClassPage.vue';
import TimeTablePage from '../components/Student/TimeTablePage.vue';
import EventsPage from '../components/Student/EventsPage.vue';
import GraduationProjectPage from '../components/Student/GraduationProjectPage.vue';
import MapPage from '../components/Student/MapPage.vue';
import CourseDetails from '../components/Student/CourseDetails.vue';
import TutorialChat from '@/components/Student/TutorialChat.vue';
import AssignmentPage from '@/components/Student/AssignmentPage.vue';
import MeetingCard from "@/components/Student/MeetingCard.vue";
import ProjectDetails from '@/components/Student/ProjectDetails.vue';
import LoginPage from '@/components/Student/LoginPage.vue';
import ForgotPasswordPage from '@/components/Student/ForgotPasswordPage.vue';
import VerificationPage from '@/components/Student/VerificationPage.vue';
import ResetPasswordPage from '@/components/Student/ResetPassword.vue';
import CongratulationsPage from '@/components/Student/CongratulationsPage.vue';
import ErrorPage from '@/components/Student/ErrorPage.vue';
import ProfilePage from "@/components/Student/ProfilePage.vue";
import MyCourses from '@/components/Student/MyCourses.vue';
import ToDoPage from "@/components/Student/ToDoPage.vue";
import MyCourseDetail from '@/components/Student/MyCourseDetail.vue';
import TaskDetail from '@/components/Student/TaskDetail.vue';
import SettingsSection from '@/components/Student/SettingsSection.vue';
import QuizPage from '@/components/Student/QuizPage.vue';
import Timeline from "@/components/Student/Timeline.vue";
import AssignmentNumberVue from '../components/Student/assignmentnumber.vue';

// Doctor
import LoginPageDOC from '../components/Doctor/LoginPageDOC.vue';
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
  { path: '/doctor', component: HomePageDOC, name: 'DoctorHome' },
  { path: '/doctor/login', component: LoginPageDOC, name: 'DoctorLogin' },
  { path: '/doctor/verification', component: VerificationDOC, name: 'DoctorVerification' },
  { path: '/doctor/forgot-password', component: ForgotPasswordDOC, name: 'DoctorForgotPassword' },
  { path: '/doctor/reset-password', component: ResetPasswordDOC, name: 'DoctorResetPassword' },
  { path: '/doctor/error', component: ErrorDOC, name: 'DoctorError' },
  { path: '/doctor/congratulations', component: CongratulationsDOC, name: 'DoctorCongratulations' },
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
  { name: 'StudentHome', path: '/home', component: HomePage,  },
  { name: 'ProfilePage', path: '/profile', component: ProfilePage,  },
  { name: 'Login', path: '/login', component: LoginPage,  },
  { name: 'Verification', path: '/verification', component: VerificationPage,  },
  { name: 'ForgotPassword', path: '/forgot-password', component: ForgotPasswordPage,  },
  { name: 'ResetPassword', path: '/reset-password', component: ResetPasswordPage,  },
  { name: 'Error', path: '/error', component: ErrorPage,  },
  { name: 'Timeline', path: '/timeline', component: Timeline,  },
  { name: 'Settings', path: '/settings', component: SettingsSection,  },
  { name: 'Materials', path: '/materials', component: MaterialsPage,  },
  { name: 'MyClass', path: '/myclass', component: MyCourses,  },
  { name: 'taskDetail', props: true, path: '/task/:classroomId/:taskId', component: TaskDetail,  },
  { name: 'MyCourses', path: '/my-courses', component: MyCourses,  },
  { name: 'MyCourseDetail', props: true, path: '/my-course/:course_id', component: MyCourseDetail,  },
  { name: 'CourseDetails', props: true, path: '/course/details/:id', component: CourseDetails,  },
  { name: 'Events', path: '/events', component: EventsPage,  },
  { name: 'ToDoPage', path: '/todo', component: ToDoPage,  },
  { name: 'TimeTable', path: '/timetable', component: TimeTablePage,  },
  { name: 'GraduationProject', path: '/graduation', component: GraduationProjectPage,  },
  { name: 'ProjectDetails', props: true, path: '/project/:id', component: ProjectDetails,  },
  { name: 'Map', path: '/map', component: MapPage,  },
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
