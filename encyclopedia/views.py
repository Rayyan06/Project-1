import random

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from . import util
from .forms import CreateEntryForm, EditEntryForm



def index(request):
    """
    Index View
    Returns all entries
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, TITLE):
    """
    Entry detail view

    Returns Title and Content of Entry formatted as HTML
    """
    entry_md = util.get_entry(TITLE)
    entry_html = util.convert_markdown_to_html(entry_md)

    return render(request, "encyclopedia/entry.html", {
        "entry": entry_html,
        "title": TITLE,
    })


def create(request):
    """
    Entry Create View
    Return
    """
    if request.method=="POST":
        form = CreateEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            util.save_entry(title, content)
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form
            })
    


    return render(request, "encyclopedia/create.html", {
        "form": CreateEntryForm()
    })



def edit(request, TITLE):
    content = util.get_entry(TITLE)
    form = EditEntryForm({'content': content})
    
    if request.method=='POST':
        form = EditEntryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            util.save_entry(TITLE, content)

            return HttpResponseRedirect(reverse("index"))
        else: 
            print(form.errors)
            return render(request, "encyclopedia/edit.html", {
                "title": TITLE,
                "form": form,
            })

    



    return render(request, "encyclopedia/edit.html", {
        "title": TITLE,
        "form": form
    })
    

def search(request):
    try:
        q = request.POST["q"]
    except:
        raise Http404("<h1>Invalid Query</h1>")


    search_result = util.get_entry(q)
    if search_result:
        return HttpResponseRedirect(f"/wiki/{q}")
    else:
        search_results = []
        for entry in util.list_entries():
            if q in entry:
                search_results.append(entry)
                print(search_results)

        return render(request, "encyclopedia/search_results.html", {
            "search_results": search_results
        })


def random_view(request):

    random_entry = random.choice(util.list_entries())

    return HttpResponseRedirect(f"/wiki/{random_entry}")