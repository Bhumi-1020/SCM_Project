import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
        self.currencies = self.data['rates']
        
def convert(self, from_currency, to_currency, amount): 
    initial_amount = amount 
    #first convert it into USD if it is not in USD.
    # because our base currency is USD
    if from_currency != 'USD' : 
        amount = amount / self.currencies[from_currency] 
  
    # limiting the precision to 4 decimal places 
    amount = round(amount * self.currencies[to_currency], 4) 
    return amount
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)
print(converter.convert('INR','USD',100))

def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title = 'Currency Converter'
    self.currency_converter = converter
    
    self.geometry("500x200")

#Label
self.intro_label = Label(self, text = 'Welcome to Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
self.intro_label.config(font = ('Courier',15,'bold'))

self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)

self.intro_label.place(x = 10 , y = 5)
self.date_label.place(x = 170, y= 50)
