#!/usr/bin/env python3

from teacher import Teacher
from user import User

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast"
]

my_teacher = Teacher("My", "Teacher", knowledge)

class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Teacher.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        assert((my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher"))

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        assert(isinstance(my_teacher.knowledge, list) and len(my_teacher.knowledge) > 0)

    def test_can_teach(self):
        '''teaches from list of knowledge.'''
        assert(my_teacher.teach() in my_teacher.knowledge)

