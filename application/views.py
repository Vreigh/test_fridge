from django.shortcuts import render

# Create your views here.
from application.models import Note


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_notes = Note.objects.all().count()
    notes = Note.objects.all()

    context = {
        'num_notes': num_notes,
        'notes': notes
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
