from django import forms
from Djangoku.models import Karyawan

class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = ['nik', 'nama', 'alamat']
        widgets = { 'nik': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'nama': forms.TextInput(attrs={ 'class': 'form-control' }),
            'alamat': forms.TextInput(attrs={ 'class': 'form-control' }),
    	}