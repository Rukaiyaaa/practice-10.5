from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author': "rukaiya", 'age': 24, 'list': ['python', 'is', 'best'], 'null': "", 'a': 21, 'b': 123456789, 'num':[1, 2, 3], 'publication_date': '2024-09-10 12:00:00', 'value': "I'm in Dhaka", 'birthday': datetime.datetime.now(), 'courses': [
        {
            'id': 1,
            'name': "python",
            'fee': 5000
        },
        {
            'id': 2,
            'name': "Django",
            'fee': 6000
        },
        {
            'id': 3,
            'name': "c++",
            'fee': 7000
        }
    ]}
    return render(request, 'home.html', d)
