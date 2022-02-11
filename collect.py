from selenium import webdriver
import time
import datetime
from datetime import date
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import os
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Google Trends Scraper')
# root.iconbitmap('./')
root.geometry('300x300')

e =Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, 'Number of days')
# e.bind(sequence, func)

os.environ['WDM_LOG_LEVEL'] = '0'
today = date.today()

def collect():
    global days
    while True:
        try:
            days = int(e.get())
        except ValueError:
            messagebox.showerror('Wrong Input', 'Kindly key in a number')
            break
        if days == 0:
            messagebox.showwarning('Wrong Input', 'Your response must be greater than zero')
            break
        else:
            break

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://trends.google.com/trends/trendingsearches/daily?geo=AU')

    init_day = 0
    data = []
    fdate = []

    while init_day < days:
        element  = driver.find_elements_by_css_selector('div.feed-list-wrapper')[init_day]
        date = str(element.find_element_by_css_selector('div.content-header-title').text)

        for i in range(5):
            title = element.find_elements_by_css_selector('div.details-top')[i].text
            count = element.find_elements_by_css_selector('div.search-count-title')[i].text
            
            data.append((date, title, count))

        fdate.append(datetime.datetime.strptime(date.split(',')[-1].strip() + date.split(',')[1], "%Y %B %d").strftime('%Y-%m-%d'))

        time.sleep(2)        
        driver.find_element_by_css_selector('body > div.trends-wrapper > div:nth-child(2) > div > div.feed-content > div > div.feed-load-more-button').click()
        Label(root, text='Clicked').grid(row=init_day+3, column=0)
        time.sleep(2)
        init_day += 1

    time.sleep(2)
    driver.quit()


    df = pd.DataFrame(data, columns=['date', 'title', 'count'])
    df.to_csv(f'Google_Trends_{today}_{fdate[-1]}.csv')


Button(root, text='Collect', command=collect).grid(row=2, column=1, padx=10, pady=5)

root.mainloop()