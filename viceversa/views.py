from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def countWords(a):
	word_list = a.split()
	return len(word_list)

def reverse(request):
	get_text = request.GET['usertext']
	reversed_text = get_text[::-1]
	count_words = countWords(reversed_text)
	return render(request, 'reverse.html', {'usertext':reversed_text,
		'resulting':count_words})