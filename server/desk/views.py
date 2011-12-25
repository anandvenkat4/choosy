from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.http import require_POST

from gym.models import Exercise
from desk.forms import ExerciseForm

def index(request):
    exes = Exercise.objects.all()
    return render_to_response('desk/templates/index.html', {'exes': exes})

def show(request, exid):
    exercise = get_object_or_404(Exercise, pk=exid)
    ctx = RequestContext(request)
    ctx['ex'] = exercise
    return render_to_response('desk/templates/show_exercise.html', ctx)

def edit(request, exid=None):
    if exid:
        exercise = get_object_or_404(Exercise, pk=exid)
    else:
        exercise = None
    form = ExerciseForm(request.POST or None, instance=exercise)
    if form.is_valid():
        exercise = form.save()
        return redirect('desk_show_exercise', exercise.id)

    ctx = RequestContext(request)
    ctx['form'] = form
    return render_to_response('desk/templates/edit_exercise.html', ctx)

def yaml(request, exid):
    """Deliver the exercise as a YAML file."""
    exercise = get_object_or_404(Exercise, pk=exid)
    response = HttpResponse(exercise.as_yaml(), mimetype="text/yaml") 
    response['Content-Disposition'] = 'attachment; filename=ex_%d.yaml' % exercise.id
    return response
