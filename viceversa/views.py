from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def reverse(request):
	get_text = request.GET['usertext']
	reversed_text = get_text[::-1]
	return render(request, 'reverse.html', {'usertext':reversed_text})