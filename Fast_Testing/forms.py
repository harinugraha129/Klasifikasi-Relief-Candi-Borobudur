from django import forms
# from .models import Dataset

class DataTestForm(forms.Form):
	image = forms.FileField()
	nilai_k = forms.IntegerField(required=True)
	# point = forms.IntegerField(required=True)
	# radius = forms.IntegerField(required=True)
		# label = "Radius LBP",
	 #    widget = forms.IntegerField(
  #           attrs={
  #               'placeholder':'Nama label dari gambar',

  #           }
	 #    )
	# )

























	