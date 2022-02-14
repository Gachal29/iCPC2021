from django.shortcuts import render, HttpResponse

def test_view(request):
  params = {
    'page_title': 'Test Page.',
    'message': 'This page for testing.'
  }

  return render(request, 'testpage.html', params)
