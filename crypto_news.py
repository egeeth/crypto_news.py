import feedparser

# CoinDesk RSS feed URL
RSS_URL = "https://www.coindesk.com/arc/outboundfeeds/rss/"

def get_news():
    feed = feedparser.parse(RSS_URL)
    print("\n📰 Güncel Kripto Haberleri (CoinDesk)\n")
    
    for i, entry in enumerate(feed.entries[:10], start=1):  # sadece ilk 10 haber
        print(f"{i}. {entry.title}")
        print(f"   {entry.link}\n")

if __name__ == "__main__":
    get_news()
