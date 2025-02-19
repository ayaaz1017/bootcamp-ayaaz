import requests

API_KEY = "YOUR_API_KEY_HERE"
NYT_BESTSELLERS_URL = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={API_KEY}"

def fetch_nyt_best_sellers():
    response = requests.get(NYT_BESTSELLERS_URL)

    if response.status_code == 200:
        books = response.json().get("results", {}).get("books", [])
        
        print("📚 NYT Best Sellers - Hardcover Fiction 📚\n")
        for book in books[:10]:  # Show top 10 books
            print(f"📖 {book['title']} by {book['author']}")
            print("-" * 40)
    else:
        print("❌ Error fetching NYT Best Sellers list.")

fetch_nyt_best_sellers()
