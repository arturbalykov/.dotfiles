config.load_autoconfig()

config.set("content.headers.user_agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36", "https://accounts.google.com/*")

c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "g": "https://www.google.com/search?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "gh": "https://github.com/search?q={}",
    "wiki": "https://en.wikipedia.org/wiki/Special:Search?search={}",
    "r": "https://www.reddit.com/search/?q={}",
    "ya": "https://yandex.ru/search?text={}",
}
