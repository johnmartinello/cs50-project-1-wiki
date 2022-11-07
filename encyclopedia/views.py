from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import Markdown
from . import util
from django.urls import reverse
from .forms import NameForm
from django import forms
import random



from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def htmlToMd(title):
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        return Markdown().convert(content)
   
   
#for entries typed directly in the url
def entry(request, title):
    htmlContent= htmlToMd(title)
    if htmlContent != None:
        return render(request, "encyclopedia/entries.html",{
            "title": title,
            "content": htmlContent
        })
        
    else:
        return render(request, "encyclopedia/error.html",{
            "title": title,
        })

def search(request):
    if request.method == "POST":
        entrySearch = request.POST['q']
        htmlContent = htmlToMd(entrySearch)
        
        if htmlContent != None:
            return render(request, "encyclopedia/entries.html",{
            "title": entrySearch,
            "content": htmlContent,
            })

        else:
            entries = util.list_entries()
            relatedPages = []
            
            for entry in entries:
                if entrySearch.lower() in entry.lower():
                    relatedPages.append(entry)
            
            return render(request,"encyclopedia/search.html",{
                "entry": entrySearch,
                "relatedPages": relatedPages
            })
            
def newPage(request):
    if request.method == "GET":
        return render(request,"encyclopedia/newpage.html")
    
    else:
        title = request.POST['title']
        content = request.POST['content']
        
        titleExist = util.get_entry(title)
        
        if titleExist:
            return render(request, "encyclopedia\errorExist.html",{
                "title": title
            })
        
        else:
            htmlContent = util.save_entry(title, content)
            page = htmlToMd(htmlContent)
            return render(request, "encyclopedia/entries.html",{
                "title": title,
                "content": content,
            })
            
def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
        "title": title,
        "content": content,
        })
        
def saveEdit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        
        htmlContent = htmlToMd(title)
        
        return render(request,"encyclopedia/entries.html",{
            "content": htmlContent,
            "title": title
        } )

def randomPage(request):
    pages = util.list_entries()
    randomPage = random.choice(pages)
    
    htmlContent = htmlToMd(randomPage)
    
    return render(request, "encyclopedia/entries.html",{
        "title": randomPage,
        "content": htmlContent
    })