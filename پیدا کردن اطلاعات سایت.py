import requests

def get_titles(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        html = response.text

        titles = []
        start = 0

        while True:
            position = html.find('title="', start)

            if position == -1:
                break
            start_title = position + len('title="')
            end_title = html.find('"', start_title)

            if end_title == -1:
                break
            title = html[start_title:end_title]
            title = title.strip()
            if title and title not in titles:
                titles.append(title)
            start = end_title + 1

        return titles

    except requests.exceptions.RequestException:
        print("False!")
        return []
url = input("Enter the website URL")
titles = get_titles(url)
print("Extracted Information:", len(titles))
print()

for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")