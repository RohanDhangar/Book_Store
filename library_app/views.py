from django.shortcuts import render

# Create your views here.

def home(request):
    book1 = {
        "title":"Book1",
        "author": "Author_1",
        "subject": "Fiction"
    }
    book2 = {
        "title":"Book2",
        "author": "Author_2",
        "subject": "Science"
    }
    book3 = {
        "title":"Book3",
        "author": "Author_3",
        "subject": "Maths"
    }
    book4 = {
        "title":"Book4",
        "author": "Author_4",
        "subject": "English"
    }
    
    context = {
        'book1': book1,
        'book2': book2,
        'book3': book3,  
        'book4': book4
    }
    return  render(request, 'home.html', context)

def about(request):
    return  render(request, 'about.html')

def contact(request):
    return  render(request, 'contact.html')

def books(request):
    books=[
    {
        'title':'Book1',
        'Author':'Author_1',
        'price':50,
        'availability':'Yes', 
        "subject": "Fiction",
        "rating": 4.5,
        'purchese': 'Yes'       
    },
    {
        'title':'Book2',
        'Author':'Author_2',
        'price':500,
        'availability':'Yes', 
        "subject": "Science", 
        "rating": 4.8,  
        'purchese': 'Yes'      
    },
    {
        'title':'Book3',
        'Author':'Author_3',
        'price':10,
        'availability':'Yes', 
        "subject": "Maths",
        "rating": 4.4,
        'purchese': 'Yes'        
    },
    {
        'title':'Book4',
        'Author':'Author_4',
        'price':5000,
        'availability':'Yes', 
        "subject": "English",
        "rating": 4.6,
        'purchese': 'Yes'         
    },
    {
        'title':'Book5',
        'Author':'Author_5',
        'price':10,
        'availability':'Yes', 
        "subject": "Maths-1",
        "rating": 4.4,
        'purchese': 'Yes'        
    },
    {
        'title':'Book6',
        'Author':'Author_6',
        'price':10,
        'availability':'Yes', 
        "subject": "SST",
        "rating": 4.4,
        'purchese': 'Yes'        
    },
    {
        'title':'Book7',
        'Author':'Author_7',
        'price':10,
        'availability':'Yes', 
        "subject": "Hindi",
        "rating": 4.4,
        'purchese': 'Yes'        
    },
    {
        'title':'Book8',
        'Author':'Author_8',
        'price':1000,
        'availability':'Yes', 
        "subject": "UPSC",
        "rating": 4.4,
        'purchese': 'Yes'        
    },
    {
        'title':'Book9',
        'Author':'Author_9',
        'price':20,
        'availability':'Yes', 
        "subject": "Law",
        "rating": 4.4,
        'purchese': 'Yes'        
    },
    {
        'title':'Book10',
        'Author':'Author_10',
        'price':100,
        'availability':'Yes', 
        "subject": "Computer application",
        "rating": 4.4,
        'purchese': 'Yes'        
    }
    ]
    return  render(request, 'books.html', {'books':books})
