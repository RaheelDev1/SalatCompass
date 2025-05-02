from flask import Flask, render_template, request, redirect, session, url_for
import os
from config import WEATHER_API_KEY, PRAYER_API_BASE_URL
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')