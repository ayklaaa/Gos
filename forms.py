# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# # from .models import Profile
# from django.core.exceptions import ValidationError
# from django.urls import reverse_lazy



from django import forms
from .models import MAppointments, MInstitutions, MService, MStaatus
#
# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = MAppointments
#         fields = ['organizations', 'service', 'date', 'time', 'status']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'time': forms.TimeInput(attrs={'type': 'time'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['service'].queryset = MService.objects.none()
#
#         if 'organizations' in self.data:
#             try:
#                 institution_id = int(self.data.get('organizations'))
#                 self.fields['service'].queryset = MService.objects.filter(учреждение_id=institution_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk:
#             self.fields['service'].queryset = self.instance.organizations.mservice_set.order_by('name')



# class RegisterForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Buyer
#
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'middle_name']




class AppointmentForm(forms.ModelForm):
    class Meta:
        model = MAppointments
        fields = ['organizations','service', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    # Поле для выбора учреждения
    organizations = forms.ModelChoiceField(queryset=MInstitutions.objects.all(), empty_label="Выберите учреждение",
                                           label="Учреждение")

    # Поле для выбора услуги
    service = forms.ModelChoiceField(queryset=MService.objects.all(), empty_label="Выберите услугу", label="Услуга")


    # Дата и время будут встроены через widgets
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Дата")
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Время")

