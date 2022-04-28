'''This file is the main file for the application.'''
from flask import Flask, render_template
from data import get_data
import random

app = Flask(__name__)

@app.route('/')
def hello():
    '''This function is the main function for the application.'''
    info = get_data()

    '''Dua Lipa, Olivia Rodrigo, Ariana Grande'''
    artist_list = ['6M2wZ9GZgrQXHCFfjv46we', '1McMsnEElThX1knmY4oliG', '66CXWjxzNUsdJxJ2JdwvnR']

    rand = random.randint(0, len(artist_list) - 1)

    info = get_data(artist_list[rand])
    print(info)

    return render_template(
