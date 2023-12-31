from django.shortcuts import render, redirect
from random import randrange
from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def error_page(request):
    return render(request, 'encyclopedia/404.html')


def search_page(request):
    value = request.GET['q']

    entries = util.list_entries()

    if value in entries:
        return redirect(f"/wiki/{value}")
    else:
        coincidences = [i for i in entries if value in i]
        print(coincidences)
        if coincidences:
            return render(request, 'encyclopedia/result.html', {"entries":coincidences})
        else:
            return render(request, 'encyclopedia/404.html',{"message": "No matches found"})

def entry(request, title):
    entry = util.get_entry(title)

    if (entry == None):
        return render(request, "encyclopedia/404.html", { "message": "Entry not found" })
    markdowner = Markdown()

    content = markdowner.convert(entry)

    return render(request, "encyclopedia/entry.html", { "name": title, "content": content })


def new_page(request):
    if request.method == 'GET':
        return render(request, 'encyclopedia/new-page.html')
    else:
        title = request.POST['title']
        content = request.POST['content']

        entries = util.list_entries()

        print(entries)

        if (title in entries):
            print('---------')
            return render(request, 'encyclopedia/new-page.html', {"error" : "This encyclopedia already exists."})
        else:
            util.save_entry(title, content)
            return redirect(f"/wiki/{title}")
        

def edit_page(request, title):
    if request.method == 'GET':
        entry = util.get_entry(title)
        print(entry)
        return render(request, 'encyclopedia/edit-page.html', {"title": title, "content": entry})
    else:
        content = request.POST['content']

        util.save_entry(title, content)
        return redirect(f"/wiki/{title}")
    

def random_page(request):

    entries = util.list_entries()

    random_number = randrange(0, entries.__len__())

    entry = util.get_entry(entries[random_number])

    return redirect(f"/wiki/{entries[random_number]}")