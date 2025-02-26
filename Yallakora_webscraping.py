# import libraries
import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
import datetime

# fetch the link
while True:
        date = input("Enter desired date (MM/DD/YYYY): ")
        try:
            datetime.datetime.strptime(date, "%m/%d/%Y")
            break
        except ValueError:
            print("Please enter the date in the correct format: MM/DD/YYYY")

url = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#days")

# save page content
content = url.content

# parse content
soup = BeautifulSoup(content, "lxml")

# create empty lists
channel = []
time = []
team_A = []
score = []
team_B = []
status = []
details = []

# get data
channels = soup.find_all("div", {"class": "channel icon-channel"})
times = soup.find_all("span", {"class", "time"})
teams_A = soup.find_all("div", {"class": "teams teamA"})
scores = soup.find_all("div", {"class": "MResult"})
teams_B = soup.find_all("div", {"class": "teams teamB"})
statuses = soup.find_all("div", {"class": "matchStatus"})
match_details = soup.find_all("div", {"class": "date"})

# get scores
for result in scores:
    for unwanted in times:
        unwanted.extract()

# fill data lists
for i in range(len(channels)):
    channel.append(channels[i].text.strip())
    time.append(times[i].text.strip())
    team_A.append(teams_A[i].text.strip())
    score.append(" " + scores[i].text.strip().replace('\n', ''))
    team_B.append(teams_B[i].text.strip())
    status.append(statuses[i].text.strip())
    details.append(match_details[i].text.strip())

# write csv file
folder_path = input("Enter the folder path to save the file (e.g., F:/Courses/): ")
file_name = f"{folder_path}Yallakora_{date.replace('/', '_')}.csv"
file_list = [channel, time, team_A, score, team_B, status, details]
exported = zip_longest(*file_list)
with open(file_name, "w", newline = "") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["القناة", "التوقيت", "الفريق الأول", "النتيجة", "الفريق الثاني", "الحالة", "التفاصيل"])
    wr.writerows(exported)
