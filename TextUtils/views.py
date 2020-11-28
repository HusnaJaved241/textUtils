# This file is made by me...Husna Javed
# hmara viw ek http response deta hai ni dy to error ata rehta hai
from django.http import HttpResponse
from django.shortcuts import render
# Following is the code for using html in httpResponse String
# def index(request): #yahan ye argument lazmi dena prta hai ni to ye error de deta hai
#     return HttpResponse('''<h1>hello husna javed</h1> <a href="https://www.youtube.com/watch?v=6_PIRbXlELw"> Tiemtable by Dhattarwal</a>  <h1>Hello others</h1> <a href = "https://classroom.google.com/u/1/h ">Google classroom</a>'''); #hum isky ander html syntax me code likh skty hen

# def about(request): #yahan ye argument lazmi dena prta hai ni to ye error de deta hai
#     return HttpResponse("about husna javed");
def index(request):
  
    return render(request, 'index.html')

def analyze(request):
    # getting the text which user is entering in textarea
    djText = request.POST.get('text', 'default')

    # Cheeck checkbox values
    removepunc = request.POST.get('removePunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # Checking which chexkbox is on
    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djText = analyzed


    if (fullcaps == "on"):
        analyzed = ""
        for char in djText:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djText = analyzed
        
   
    if newlineremover=="on":
        analyzed=""
        for char in djText:
            if char!="\n" and char != "\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djText = analyzed


    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djText):
            if not(djText[index] == " " and djText[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djText = analyzed


    if(charactercounter=="on"):
        result = 0
        for char in djText:
            result += 1

        params = {'purpose': 'No. of Characters in text', 'analyzed_text': result}
        djText = analyzed


    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on"):
        return HttpResponse("Error!!!.Pleae elect the operationa and try again by entering your text agian.")

    return render(request, 'analyze.html', params)



