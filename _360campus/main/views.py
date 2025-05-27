from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
import os
from .models import *
from .serializers import *
from .permissions import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def role_view(req):
    return Response(req.user.person_type)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def event_list(req):
    limit = req.query_params['limit'] if 'limit' in req.query_params else 5
    events = Event.objects.all()[:limit]
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_event_list(req):
    registered_events = EventRegistration.objects.filter(person=req.user).values("event")

    return Response(registered_events)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def event_register(req, pk):
    evt = get_object_or_404(Event, pk=pk)

    if EventRegistration.objects.filter(person=req.user, event=evt).exists():
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    today = timezone.now()
    if today > evt.date:
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    EventRegistration.objects.create(event=evt, person=req.user)

    return Response({})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_list(req):
    options = {}
    if 'college' in req.query_params:
        options['college'] = req.query_params['college']

    if 'level' in req.query_params:
        options['level'] = req.query_params['level']

    if 'semester' in req.query_params:
        options['semester_kind'] = req.query_params['semester_kind']

    if 'search_query' in req.query_params:
        options['title__icontains'] = req.query_params['search_query']
        options['description__icontains'] = req.query_params['search_query']

    if 'list_registrable' in req.query_params:
        options['pk__in'] = Classroom.objects.filter(semester=Semester.objects.last()).values('course')

    courses = get_list_or_404(Course, **options)
    serializer = CourseSerializer(courses, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsProfessor])
@parser_classes([JSONParser])
def course_edit(req, pk):
    course = get_object_or_404(Course, pk=pk)
    course_serializer = CourseSerializer(instance=course, data=req.data)

    if not course_serializer.is_valid():
        return Response(course_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    course_serializer.save()

    return Response(course_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_classroom_view(req, pk):
    current_semester = Semester.objects.last()

    if not Enrollment.objects.filter(classroom__semester=current_semester, \
                                     classroom__course_id=pk, \
                                     student=req.user.student).exists():
        return Response(status=status.HTTP_403_FORBIDDEN)

    classroom = Classroom.objects.get(course_id=pk, \
                                      semester=current_semester)
    serializer = ClassroomViewSerializer(classroom)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registered_classroom_list(req):
    current_semester = Semester.objects.last()
    if req.user.person_type == 'S':
        classrooms = Classroom.objects.filter(enrollment__student=req.user.student, \
                                              semester=current_semester)
    elif req.user.person_type == 'P':
        classrooms = Classroom.objects.filter(instructor=req.user.professor, \
                                              semester=current_semester)

    serializer = ClassroomViewSerializer(classrooms, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def classroom_list(req, pk):
    current_semester = Semester.objects.last()
    course = get_object_or_404(Course, pk=pk)
    classrooms = get_list_or_404(Classroom, semester=current_semester, \
                                 course=course)
    serializer = ClassroomViewSerializer(classrooms, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def classroom_join(req, pk):
    current_semester = Semester.objects.last()

    if Enrollment.objects.filter(student=req.user.student, \
                                 classroom__course_id=pk, \
                                 classroom__semester=current_semester).exists():
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    classroom = get_object_or_404(Classroom, semester=current_semester, \
                                  course_id=pk)

    Enrollment.objects.create(student=req.user.student, classroom=classroom)
    return Response(data={}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def material_list(req, pk):
    course = get_object_or_404(Course, pk=pk)
    materials = course.material_set.all()
    serializer = MaterialSerializer(materials, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def material_view(req, pk):
    material = get_object_or_404(Material, pk=pk)

    with open(material.file.path, 'rb') as f:
        data = f.read()

    filename = os.path.basename(material.file.path)

    return HttpResponse(data, headers={
        'Access-Control-Expose-Headers': 'Content-Disposition',
        'Content-Disposition': f'attachment; filename="{filename}"'
    })

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated, IsProfessor])
@parser_classes([MultiPartParser])
def material_create_modify(req, pk):
    if req.method == 'POST': # create new material
        req.data['course'] = pk
        serializer = MaterialSerializer(data=req.data)

    elif req.method == 'PUT': # edit existing material
        material = get_object_or_404(Material, pk=pk)
        serializer = MaterialSerializer(instance=material, data=req.data, partial=True)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsProfessor])
def material_delete(req, pk):
    material = get_object_or_404(Material, pk=pk)
    material.file.delete()
    material.delete()

    return Response({})

@api_view(['GET'])
def graduation_project_list(request):
    """
    Returns a list of all graduation projects sorted by rating (highest first).
    Supports optional filtering by:
      - faculty 
      - year 
    """
    projects = GraduationProject.objects.all().order_by('-rate')
    faculty = request.query_params.get('faculty')
    if faculty:
        projects = projects.filter(faculty__iexact=faculty)  # ✅ Case-insensitive

    year = request.query_params.get('year')
    if year:
        projects = projects.filter(year=year)

    serializer = GraduationProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def graduation_project_detail(request, project_id):
    """
    Retrieves details of a specific graduation project.
    """
    project = get_object_or_404(GraduationProject, id=project_id)
    serializer = GraduationProjectSerializer(project)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(req, pk):
    current_semester = Semester.objects.last()

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom__course_id=pk, \
                                     classroom__semester=current_semester).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    classroom = get_object_or_404(Classroom, semester=current_semester, \
                                  course_id=pk)

    # filter out assignments, since they're treated differently
    # and there's a API for them anyways
    tasks = classroom.task_set.filter(~Q(kind='a'))
    serializer = TaskViewSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assignment_list(req, pk):
    current_semester = Semester.objects.last()

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom__course_id=pk, \
                                     classroom__semester=current_semester).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    assignments = Assignment.objects.filter(task_ptr__classroom__course_id=pk, \
                                            task_ptr__classroom__semester=current_semester)
    serializer = AssignmentSerializer(assignments, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def submitted_assignment_list(req, pk):
    current_semester = Semester.objects.last()

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom__course_id=pk, \
                                     classroom__semester=current_semester).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    classroom = get_object_or_404(Classroom, semester=current_semester, \
                                  course_id=pk)

    submitted_assignments = AssignmentSubmission.objects.filter(student=req.user.student, \
                                                                assignment__classroom=classroom) \
                                                        .values('assignment')
    submitted_assignments = Assignment.objects.filter(pk__in=submitted_assignments)
    serializer = AssignmentSerializer(submitted_assignments, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assignment_view(req, assignment_pk):
    assignment = get_object_or_404(Assignment, pk=assignment_pk)

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom=assignment.classroom).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    serializer = AssignmentSerializer(assignment)
    data = serializer.data
    data['submitted'] = AssignmentSubmission.objects.filter(student=req.user.student, \
                                                            assignment=assignment).exists()
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assignment_submission_view(req, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom=assignment.classroom).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    submission = get_object_or_404(AssignmentSubmission, student=req.user.student, assignment=assignment)
    serializer = AssignmentSubmissionViewSerializer(submission)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])
def assignment_submit(req, pk, filename):
    assignment = get_object_or_404(Assignment, pk=pk)

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom=assignment.classroom).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if assignment.deadline and assignment.deadline < timezone.now():
        return Response({'reason': 'deadline passed'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    assignment.submissions.add(req.user.student, through_defaults={'submitted_file': req.data.get('file')})
    assignment.save()

    return Response({}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignment_unsubmit(req, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if not Enrollment.objects.filter(student=req.user.student, \
                                     classroom=assignment.classroom).exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    file = AssignmentSubmission.objects.get(student=req.user.student, assignment=assignment).submitted_file
    file.delete()

    assignment.submissions.remove(req.user.student)
    assignment.save()

    return Response({})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignment_comment(req, course_pk, assignment_pk):
    pass

