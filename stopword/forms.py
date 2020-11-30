from django import forms
from .models import StopWord

class AddStopWordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = StopWord
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            qs = StopWord.objects.filter(name=name)
            if qs.exists():
                raise forms.ValidationError('이미 존재하는 금지어입니다.')
        return name