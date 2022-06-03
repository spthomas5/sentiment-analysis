import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import datetime

dates = []
presidents = []
polarities = []
subjectivities = []

with open('transcripts.json', 'r', encoding='latin-1') as file:
    f = file.read()
    data = json.loads(f)
    for i in data:
        date = i['date']
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        dates.append(parsed_date)

        presidents.append(i['president'])
        b = TextBlob(i['transcript'])
        polarities.append(b.sentiment[0])
        subjectivities.append(b.sentiment[1])

# Display polarities

# plt.scatter(dates, polarities, c=polarities, cmap='YlGn', edgecolors='grey')
# plt.title("Polarities of SOTU Addresses, 1860 - 2018")
# plt.xlabel("Years")
# plt.ylabel("Polarities")
# plt.xticks(rotation=90)
# plt.show()

# Display subjectivities

plt.scatter(dates, subjectivities, c=subjectivities, cmap='YlGn', edgecolors='grey')
plt.title("Subjectivities of SOTU Addresses, 1860 - 2018")
plt.xlabel("Years")
plt.ylabel("Subjectivities")
plt.xticks(rotation=90)
plt.show()






