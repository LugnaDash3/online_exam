import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_exam_project.settings')
django.setup()

from exam.models import Course, Lesson, Question, Choice

def populate():
    print("Populating database...")

    # Create a Course
    course, created = Course.objects.get_or_create(
        name="Python Programming for Beginners",
        description="Learn the fundamentals of Python, from syntax to data structures and object-oriented programming."
    )
    if created:
        print(f"Created Course: {course.name}")

    # Create a Lesson
    lesson, created = Lesson.objects.get_or_create(
        course=course,
        title="Introduction to Python Variables",
        content="This lesson covers variables, data types, and basic operations in Python."
    )
    if created:
        print(f"Created Lesson: {lesson.title}")

    # Add Questions and Choices
    q1_text = "What is the correct way to declare a variable in Python?"
    q1, created = Question.objects.get_or_create(lesson=lesson, text=q1_text)
    if created:
        Choice.objects.create(question=q1, text="x = 5", is_correct=True)
        Choice.objects.create(question=q1, text="int x = 5", is_correct=False)
        Choice.objects.create(question=q1, text="var x : 5", is_correct=False)
        Choice.objects.create(question=q1, text="declare x = 5", is_correct=False)
        print(f"Added Question: {q1_text}")

    q2_text = "Which of the following is a Python data type?"
    q2, created = Question.objects.get_or_create(lesson=lesson, text=q2_text)
    if created:
        Choice.objects.create(question=q2, text="List", is_correct=True)
        Choice.objects.create(question=q2, text="Array", is_correct=False)
        Choice.objects.create(question=q2, text="Pointer", is_correct=False)
        Choice.objects.create(question=q2, text="Constant", is_correct=False)
        print(f"Added Question: {q2_text}")

    q3_text = "How do you create a comment in Python?"
    q3, created = Question.objects.get_or_create(lesson=lesson, text=q3_text)
    if created:
        Choice.objects.create(question=q3, text="# Comment", is_correct=True)
        Choice.objects.create(question=q3, text="// Comment", is_correct=False)
        Choice.objects.create(question=q3, text="/* Comment */", is_correct=False)
        Choice.objects.create(question=q3, text="-- Comment", is_correct=False)
        print(f"Added Question: {q3_text}")

    print("Database population complete!")

if __name__ == '__main__':
    populate()
