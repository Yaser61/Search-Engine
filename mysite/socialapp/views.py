from django.shortcuts import render
from .agent import search_query  # Daha önce oluşturduğumuz agent.py dosyasını dahil ediyoruz

def home(request):
    query = request.GET.get('q', 'apple inc')  # Varsayılan sorgu "apple inc"
    results = search_query(query)
    return render(request, 'home.html', {'results': results})