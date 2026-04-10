from django.contrib import admin
from django.contrib.auth.models import Group
from .models import (
    Choice,
    Course,
    Exam,
    Lesson,
    Question,
    Student,
    Submission,
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'lesson')
    search_fields = ('text',)
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__name')
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'lesson', 'score', 'submitted_at')
    readonly_fields = ('submitted_at',)


admin.site.site_header = 'OnlineCourse Administration'
admin.site.site_title = 'OnlineCourse Admin'
admin.site.index_title = 'Authentication and Authorization'

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Exam)
admin.site.register(Student)
admin.site.unregister(Group)
