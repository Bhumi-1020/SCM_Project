import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(https://api.exchangerate-api.com/v4/latest/USD).json()
        self.currencies = self.data['rates']