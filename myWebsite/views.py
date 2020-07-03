from django.http import HttpResponse
from django.shortcuts import render

#method view

def index(request):
	context = {
		'judul' : 'Selamat Datang | Wasis Waluyo',
		'deskripsi' : 'Website ini dibagun menggunakan Django',
		'banner' : 'img/profile1.png',
	}
	return render(request, 'index.html', context)