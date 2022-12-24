# Contextual-Advertising-Platform

Django Project 2

## Description
1) Contextual advertising is a technology that finds our relevant ads from a given blog article to maximise a blog or websites revenue.
2) Contextual advertising is the reason why you see an ad for nike shoes on a fitness related article.
3) In this project I have build a contextual advertising platform which reads data from any blog who's URL we pass in, find relevant keywords on that blog and find ads which are relevant to them and all of this is done automatically.
3) First we create a basic Django app that could accept a blog URL, then read all the data on that blog page using the requests library and parse the data using BeautifulSoup.
4) We then feed the parsed data to the rake library which then finds the most relevant and prominent keywords in that blog article and save them.
5) These relevant keywords are then matched with the ads present in our database and gives us back the ads which are most relevant to the blog post.
6) Also using Tailwind to style up the web app.

## Technologies Used
1) Python : Programming language.
2) Django : For web app.
3) Requests: For making HTTP request to blog pages.
4) BeautifulSoup: To parse webpages
5) RakeNLTK : To find relevant keywords

## Installation
1) Python x.x < 3.9
2) Django 

```bash
  pip install django==3.2
```
3) requests (Python library for making HTTP requests)

```bash
  pip install requests
```
4) BeautifulSoup (Python library for for extracting data from HTML and XML documents. beautifulsoup 4 is the lastest version)

```bash
  pip install beautifulsoup4
```
5) RAKE --Rapid Automatic Keyword Extraction (Its is an NLP tool), RAKE is implemented in the Python Natural Language Toolkit (NLTK) library. 

```bash
  pip install rake-nltk
```
6) Node.js (In order to set-up and install Tailwind), NPM for tailwind
--> a) https://nodejs.org/en/  (download the LTS version), after installsation check if it is installed by running command (node --version)
--> b) tailwind 

```bash
  npm install tailwindcss@2.2.16
```

## SCREENSHOTS

1) Homepage  

![image](https://user-images.githubusercontent.com/102078863/209398280-f8fb4bbf-5784-4476-9b98-50abebaec2e4.png)


2) Providing a link for demo and clicking on sumbit.

![image](https://user-images.githubusercontent.com/102078863/209398332-b82224ca-17e8-4c9b-852f-280a8222cd61.png)


3) Relevant keywords are then matched with the ads present in our database and gives us back the ads which are most relevant to the blog post. 
 
![screencapture-127-0-0-1-8000-2022-12-24-01_00_40](https://user-images.githubusercontent.com/102078863/209398397-7ff0f61d-6b1d-4599-9aca-f5ba0082ea2a.png)


## KEY CONCEPTS 
### requests (Python Library)
* requests is a Python library for making HTTP requests. It provides a simple and easy-to-use interface for sending HTTP requests and receiving HTTP responses.
* With requests, you can send various types of HTTP requests, including GET, POST, PUT, DELETE, and more. 
* We can also send requests with different HTTP headers and parameters, and you can handle responses with different HTTP status codes.

### Beautiful Soup (Python library)
* Beautiful Soup is a Python library for extracting data from HTML and XML documents. 
* It provides a simple and efficient way to parse and navigate documents, and to extract data from them.
* Beautiful Soup converts an HTML or XML document into a tree-like structure, with each element in the document represented as a node in the tree. 
* We can use the various methods provided by Beautiful Soup to navigate and search the tree, extract data, and modify the document.

Some of the features of Beautiful Soup include:  
--> Support for parsing HTML and XML documents.  
--> Support for searching and navigating the document tree using various search criteria.  
--> Support for extracting data from the document using tag names, attribute values, and CSS classes.  
--> Support for modifying the document tree and writing the modified document back to a file.  

* Important function of BeautifulSoup library used in the project 

1)  find_all()   
--> The find_all() function is a method of the BeautifulSoup object that allows you to search for all occurrences of a particular HTML or XML element in the document.  
--> It returns a list of elements that match the search criteria.  

2) get_text()  
--> The get_text() method is a method of the Tag object in Beautiful Soup that allows you to extract the text contents of the tag.   
--> It returns a string containing the text of the tag, including any text contained within child tags.  

### RAKE (Rapid Automatic Keyword Extraction)
* RAKE is a natural language processing (NLP) tool that is used to extract keywords and phrases from a text document.  
* It is based on the idea of identifying candidate keywords by analyzing the co-occurrence of words in the document and scoring them based on their frequency and distinctiveness.  
* RAKE is implemented in the Python Natural Language Toolkit (NLTK) library. 
* To use RAKE in a Python project, you will need to install the NLTK library and import the RAKE module.
