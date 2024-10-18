import requests
req = requests.get("https://archive.ics.uci.edu/static/public/880/data.csv")
url_content = req.content
csv_file = open('data.csv', 'wb')
csv_file.write(url_content)
csv_file.close()