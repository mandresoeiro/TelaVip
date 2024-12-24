from django import forms
from cine.models import Cine

#TODO # from cine.models import Genre, streaming, Actor, Director, Producer

# class CineForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="")
#     streaming = forms.ModelChoiceField(queryset=streaming.objects.all(), empty_label="")
#     debut_year = forms.IntegerField()
#     actor = forms.ModelChoiceField(queryset=Actor.objects.all(), empty_label="")    
#     director = forms.ModelChoiceField(queryset=Director.objects.all(), empty_label="")    
#     producers = forms.ModelChoiceField(queryset=Producer.objects.all(), empty_label="")
#     original_writer = forms.CharField(max_length=255)
#     value = forms.IntegerField()
#     resume = forms.CharField(max_length=255)
   


# TODO OPÇÃO DE ALTERAR O FORMULARIO


class CineModelForm(forms.ModelForm):
    class Meta:
        model = Cine
        fields = '__all__'


#    def clean_value(self) -> Any:
#         value = self.cleaned_data.get('value')
#         if value < 20000:
#            self.add_error('value', 'O Valor deve ser maior que R$ 20.000')
#         return value
    
    def clean_debut_year(self):
        debut_year = self.cleaned_data.get('debut_year')
        if debut_year < 1935:
            self.add_error('debut_year', 'O Ano deve ser maior que 1935')
        return debut_year
    
    