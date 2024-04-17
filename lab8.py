import tkinter as tk
import feedparser


def fetch_news(url):
    feed = feedparser.parse(url)
    return [f"{entry.title}: {entry.link}" for entry in feed.entries]


def display(news):
    listbox.delete(0, tk.END)
    for news_item in news:
        listbox.insert(tk.END, news_item)


def get_and_display():
    news = fetch_news('https://lenta.ru/rss/articles')
    display(news)


def compose(*functions):
    def composed_function(arg):
        result = arg
        for func in functions:
            result = func(result)
        return result

    return composed_function


root = tk.Tk()
root.title("News Aggregator")

label = tk.Label(root, text="Latest News:")
label.pack()

listbox = tk.Listbox(root, width=100, height=20)
listbox.pack()

fetch_button = tk.Button(root, text="Get News", command=get_and_display)
fetch_button.pack()

root.mainloop()
