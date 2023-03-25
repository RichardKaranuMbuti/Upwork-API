from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def get_upwork_data(request):
    url = 'https://www.upwork.com/search/profiles/?q=python'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    # Extract relevant data from the HTML using BeautifulSoup
    for profile in soup.select('.freelancer-tile'):
        title = profile.select_one('.freelancer-tile-title a').text.strip()
        rate = profile.select_one('.rate').text.strip()
        data.append({
            'title': title,
            'rate': rate
        })

    return JsonResponse(data, safe=False)
