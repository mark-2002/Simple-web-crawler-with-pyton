from urllib import request
google_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1596462938&period2=1627998938&interval=1d&events=history&includeAdjustedClose=true'
def url_csv_downloader(url):
    file = request.urlopen(url)#takes url of a csv file and stores connection to  variable
    csv = file.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'#save in a raw string
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

url_csv_downloader(google_url)