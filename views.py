from django.shortcuts import render, redirect, get_object_or_404

from .models import Questionnaire

from .forms import QuestionnaireForm


def questionnaire_list(request):

    data = Questionnaire.objects.all()

    return render(request, 'questionnaire/list.html', {'data': data})


def questionnaire_create(request):

    form = QuestionnaireForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()

        return redirect('/questionnaires/')

    return render(request, 'questionnaire/create.html', {'form': form})


def questionnaire_update(request, id):

    obj = get_object_or_404(Questionnaire, id=id)

    form = QuestionnaireForm(
        request.POST or None,
        request.FILES or None,
        instance=obj
    )

    if form.is_valid():

        form.save()

        return redirect('/questionnaires/')

    return render(request, 'questionnaire/update.html', {'form': form})


def questionnaire_delete(request, id):

    obj = get_object_or_404(Questionnaire, id=id)

    obj.delete()

    return redirect('/questionnaires/')