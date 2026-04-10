from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'{self.course.name} - {self.title}'


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Submission(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='submissions', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    selected_choices = models.ManyToManyField(Choice, blank=True)
    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student_name} - {self.lesson.title}'


class Exam(models.Model):
    lesson = models.OneToOneField(Lesson, related_name='exam', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.full_name
