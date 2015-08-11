import csv
from bs4 import BeautifulSoup
import urllib2 
import time
import os
import re

with open('test_faculty.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("Name", "Specialization", "Title", "E-mail"))
	my_writer.writeheader()
	addressDep='https://polisci.wustl.edu/faculty/specialization'
	webpageDep = urllib2.urlopen(addressDep)
	soupDep = BeautifulSoup(webpageDep.read())
	link = soupDep.find_all("a", {"class": "person-view-primary-field"})
	for i in link:
		page = i.get("href")
		addresspro = "https://polisci.wustl.edu" + page
		webpagepro = urllib2.urlopen(addresspro)
		souppro = BeautifulSoup(webpagepro.read())
		name = souppro.find_all("h1", {"class": "pane-title"})[0].text
		specialization = souppro.find_all("a", {"typeof": "skos:Concept"})[1].text
		title = souppro.find_all("div", {"class": "field field-name-field-person-titles field-type-text field-label-hidden"})
		title = re.sub(r'<[^>]+>', '', str(title))
		for a_tab in souppro.find_all("a"):
			try:
				if "mailto:" in a_tab["href"]:
					email = a_tab.text
					break
			except:
				pass
		my_writer.writerow({"Name": name, "Specialization": specialization, "Title": title, "E-mail": email})
	

# Butler
addressButler = "https://polisci.wustl.edu/faculty/daniel-butler"
webpageButler = urllib2.urlopen(addressButler)
soupButler = BeautifulSoup(webpageButler.read())
soupButler.find_all("div", {"class": "field field-name-field-person-titles field-type-text field-label-hidden"})
soupButler.find_all("a", {"typeof": "skos:Concept"})[1].text

# Brancati
addressBran = "https://polisci.wustl.edu/Dawn_Brancati"
webpageBran = urllib2.urlopen(addressBran)
soupBran = BeautifulSoup(webpageBran.read())
soupBran.find_all("a", {"typeof": "skos:Concept"})[1].text
soupBran.find_all("h1", {"class": "pane-title"})[0].text
soupBran.find_all("div", {"class": "soupButler.find_all("div", {"class": "field field-name-field-person-titles field-type-text field-label-hidden"})"})
soupBran.find_all("div", {"class": "field-item"})
for a_tab in soupBran.find_all("a"):
	try:
		if "mailto:" in a_tab["href"]:
			email = a_tab.text
			break
	except:
		pass

soupBran.find_all("div", {"class": "field field-name-field-person-titles field-type-text field-label-hidden"})


