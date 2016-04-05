# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Володимир',
         'last_name': u'Рибак',
         'ticket': 235,
         'image': 'img/image1.jpg'},
        {'id': 2,
         'first_name': u'Гриць',
         'last_name': u'Борода',
         'ticket': 2123,
         'image': 'img/image2.jpg'},
		{'id': 3,
         'first_name': u'Павло',
         'last_name': u'Непийпиво',
         'ticket': 221,
         'image': 'img/image3.jpg'},
    )
    return render(request, 'students/students_list.html',
        {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
