from django.shortcuts import render, redirect

# Create your views here.
from .models import PG
from .forms import PGForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages



def pg_list(request):

    query = request.GET.get('q') # Get the search query from the request

    if query:
        pgs=PG.objects.filter(
            Q(city__icontains=query) | Q(name__icontains=query) # Filter PGs based on the search query (case-insensitive)
             
             # Filter PGs based on the search query (case-insensitive)
        )


    else:
        pgs = PG.objects.all() # Retrieve all PGs if no search query is provided
    
    return render(request, 'pg_list.html', {'pgs': pgs})



def pg_detail(request, id):
    
    pg=PG.objects.get(id=id)

    context = {
        'pg':pg
    }

    return render(request, 'pg_detail.html', {'pg': pg})

@login_required
def add_pg(request):

    if request.method == 'POST':

        form = PGForm(request.POST, request.FILES)

        if form.is_valid():

            pg = form.save(commit=False)

            pg.owner = request.user

            pg.save()

            messages.success(request, "PG Added successfully!")

            return redirect('pg_list')

    else:

        form = PGForm()

    return render(request, 'add_pg.html', {'form': form})



#    following code is use for the updating the pg details

@login_required
def update_pg(request, id):

    pg=PG.objects.get(id=id)

    if request.user != pg.owner:

        return HttpResponse("you are not allowed to edit this PG details")

    if request.method == 'POST':

        form = PGForm(request.POST, request.FILES, instance=pg)

        if form.is_valid():

            form.save()

            messages.success(request, "PG details update successfully!")

            return redirect('pg_list')
        
    else:

        form = PGForm(instance=pg)

    context = {
            'form':form
        }

    return render(request, 'update_pg.html', context)

@login_required
def delete_pg(request, id):

    pg=PG.objects.get(id=id)

    if request.user != pg.owner:

        return HttpResponse("You are not allowed to delete this PG")

    if request.method == 'POST':

        pg.delete()

        return redirect('pg_list')
    
    context = {
        'pg': pg
    }

    messages.success(request, "PG deleted successfully!")
    
    return render(request, 'delete_pg.html', context)


# following code is use for the review and rating of the pg

@login_required
def add_review(request, pg_id):

    pg=PG.objects.get(id=pg_id)
    if request.method=='POST':

        form=ReviewForm(request.POST)
        if form.is_valid():

            review=form.save(commit=False)
            review.user=request.user
            review.pg=pg
            review.save()
            messages.success(request, "REVIEW ADDDED SUCCESSFULLY!")
            return redirect('pg_detail', id=pg_id)
    else:
        form=ReviewForm()

    return render(request, 'add_review.html', {'form': form})