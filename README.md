# Webscraping YallKora
---

This is a program that is designed to fetch football match data from https://www.yallakora.com/
The program uses BeautifulSoup to webscrape https://www.yallakora.com/ for the required data
The program then returns the output in a csv file

## Steps of implementation
- First, the user is prompted for a date in the format (MM/DD/YYYY). The program will keep prompting the user for input until the user enters a valid date.
- The program then sends a request using `request.get()` to the website using the user's chosen date.
- The content of the web page is then parsed using `BeautifulSoup` with `lxml` parser.
- Data are then scraped using their CSS classes, and cleaned before being stored into lists.
- User is then again prompted for a file path to export the `csv` file.
- Using `csv` module, data are exported to a `.csv` file named "Yallkora_MM_DD_YYYY.csv" where MM_DD_YYYY represents the user's chosen date

---
Feel free to contact me via LinkedIn or email!
