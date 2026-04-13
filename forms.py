from django.forms import ModelForm
from .models import Questionnaire


class QuestionnaireForm(ModelForm):

    class Meta:
        model = Questionnaire
        fields = '__all__'