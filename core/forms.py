from django.forms import ModelForm
from .models import Course, Category, Boiler


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Category name'
        }


# class participantForm(ModelForm):
#     class Meta:
#         model = participant
#         fields = '__all__'
#         labels = {
#             'name': 'Participant name'
#         }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'desc': 'Description'
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "click here to select the topic"


class BoilerForm(ModelForm):
    class Meta:
        model = Boiler
        fields = '__all__'
        labels = {
            'host': 'Username'
        }

    def __init__(self, *args, **kwargs):
        super(BoilerForm, self).__init__(*args, **kwargs)
        self.fields['host'].empty_label = "click here to select the User"
        # self.fields['participant'].empty_label = "click here to select the Participant"
        self.fields['Course'].empty_label = "click here to select the Course"
