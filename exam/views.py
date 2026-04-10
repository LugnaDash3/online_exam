from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Choice, Course, Lesson, Submission


def course_detail(request, course_id=None):
    course = None
    if course_id is None:
        course = Course.objects.first()
    else:
        course = get_object_or_404(Course, id=course_id)

    return render(request, 'exam/course_details_bootstrap.html', {
        'course': course,
    })


def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = lesson.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        student_name = request.POST.get('student_name', 'Guest')
        selected_choice_ids = [int(value) for key, value in request.POST.items() if key.startswith('question_') and value.isdigit()]
        selected_choices = Choice.objects.filter(id__in=selected_choice_ids)

        total_questions = questions.count()
        score = sum(1 for question in questions if question.choices.filter(id__in=selected_choice_ids, is_correct=True).exists())

        submission = Submission.objects.create(
            lesson=lesson,
            student_name=student_name,
            score=score,
            total_questions=total_questions,
        )
        submission.selected_choices.set(selected_choices)

        return redirect(reverse('show_exam_result', args=[submission.id]))

    return render(request, 'exam/submit_exam.html', {
        'lesson': lesson,
        'questions': questions,
    })


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    correct_count = submission.score
    total = submission.total_questions
    percentage = round((correct_count / total) * 100, 2) if total else 0

    return render(request, 'exam/show_exam_result.html', {
        'submission': submission,
        'correct_count': correct_count,
        'total': total,
        'percentage': percentage,
    })
