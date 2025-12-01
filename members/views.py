from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MemberForm
from django.db.models import Q
from .models import Member
from django.contrib.auth import login
from .forms import RegisterForm

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def search_view(request):
    query = request.GET.get('q', '')  # get the search text (or empty if none)
    results = None

    if query:
        # Search in firstname OR lastname (case-insensitive)
        results = Member.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query)
        ).values()  # .values() if you prefer dictionaries

        # Or simple version (only firstname):
        # results = Member.objects.filter(firstname__icontains=query)

    return render(request, "search.html", {
        'results': results,
        'query': query
    })
    
@login_required
def members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'all_members.html', {'mymembers': mymembers})

@login_required
def search_view(request):
    query = request.GET.get('q', '').strip()
    
    if query.isdigit():
        member = Member.objects.filter(id=int(query)).first()
        if member:
            return redirect('member_detail', member_id=member.id)

    results = None
    if query:
        results = Member.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query)
        )

    return render(request, "search.html", {'results': results, 'query': query})

@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()                  # saves to database!
            return redirect('members-list')  # go back to list
    else:
        form = MemberForm()

    return render(request, 'add_member.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                  # auto login after register
            return redirect('members-list')       # go to home page
    else:
        form = RegisterForm()

    return render(request, 'members/register.html', {'form': form})