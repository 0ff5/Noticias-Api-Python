import requests
from requests.exceptions import HTTPError
import webbrowser
from termcolor import colored
import colorama
import random

# Colorama
colorama.init()

# lista de colores
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

while True:
    try:
        url = ('https://newsapi.org/v2/top-headlines?country=ar&apiKey=64ab2a7e7aa040ccb9852a25c3330576')
        response = requests.get(url)
        articles = response.json()['articles']
        for i, article in enumerate(articles):
            # Elige un color
            title_color = random.choice(colors)
            title = colored(f"{i+1}. {article['title'].split('-')[0].strip()}", title_color)
            print(f"{title}.")
        
        choice = input("Escriba un numero para leer la noticia entera o escriba cerrar para salir del programa: ")
        if choice.lower() == 'cerrar':
            break
        elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(articles):
            print(colored("Numero incorrecto , porfavor escriba un numero correcto", 'magenta'))
        else:
            article_url = articles[int(choice)-1]['url']
            print(colored(f"Abriendo articulo: {article_url}", 'green'))
            webbrowser.open_new(article_url)
            
    except HTTPError as http_err:
        print(colored(f'ERROR HTTP: {http_err}', 'red'))
    except Exception as err:
        print(colored(f'Un error ocurrio: {err}', 'red'))