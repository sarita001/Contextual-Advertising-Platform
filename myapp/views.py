from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Tag,Advert
import requests
from rake_nltk import Rake
import nltk
import collections
import difflib
nltk.download('punkt')
nltk.download('stopwords')

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        #print(url)
        response = requests.get(url=url)
        #print(response.content)
        soup = BeautifulSoup(response.content,'html.parser')
        #print(soup)
        all_text =''
        for para in soup.find_all('p'):
            #print(para.get_text())
            all_text+=str(para.get_text())
        #print(all_text)
        rake_var = Rake()
        rake_var.extract_keywords_from_text(all_text)
        keywords_extracted = rake_var.get_ranked_phrases()
        #print(keywords_extracted)

        adtags =[]
        tags = Tag.objects.all()
        for tag in tags:
            adtags.append(tag.tagname)
        seta = set(keywords_extracted)
        setb = set(adtags)
        commonwords =[]
        if (seta & setb):
            commonwords = list(seta & setb)
        #print(commonwords)

        relevantads = []
        for advert in Advert.objects.all():
            for tag in advert.tags.all():
                if tag.tagname in commonwords:
                    relevantads.append(advert)
                    relevantads = set(relevantads)
                    relevantads = list(relevantads)
        print(relevantads)
        context={
            'relevantads':relevantads,
            'commonwords':commonwords
        }

        return render(request,'myapp/index.html',context)
          

        
    return render(request,'myapp/index.html')