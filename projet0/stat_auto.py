import requests
from bs4 import BeautifulSoup
import datetime
#--------------	--------------------------------------------------------------------------------------------------------------------
#calcule et convertion de la date du jour precedant
date1 = datetime.date.today() - datetime.timedelta(days=1)
new_date = date1.strftime("%d/%m/%Y")
#----------------------------------------------------------------------------------------------------------------------------------
#fonction qui retourne le nombre de voiture
def scrapeadd(adresse):
	requete1 = requests.get("https://deals.jumia.ci/voitures")
	charge1= requete1.content
	exploit1 = BeautifulSoup(charge1, 'html.parser')
	vo1 = exploit1.find_all("span",{"class":"price"})
	return(len(vo1))


#----------------------------------------------------------------------------------------------------------------------------------

#fonction qui retourne les balises de prix a filtré
def scrape(adresse):
	requete2 = requests.get(adresse)
	charge2= requete2.content
	exploit2 = BeautifulSoup(charge2, 'html.parser')
	vo2 = exploit2.find_all("span",{"class":"price"})
	return (vo2)
#----------------------------------------------------------------------------------------------------------------------------------

#fonction qui affiche uniquement que des prix
def aff(vo2):
	for prix in vo2:	
		print(prix.text)


#recuperation de toutes les valeurs
val1 = scrapeadd("https://deals.jumia.ci/voitures-neuves")
val2 = scrapeadd("https://deals.jumia.ci/location-de-voiture")
val3 = scrapeadd("https://deals.jumia.ci/voitures")

list1 = scrape("https://deals.jumia.ci/voitures-neuves")
list2 = scrape("https://deals.jumia.ci/location-de-voiture")
list3 = scrape("https://deals.jumia.ci/voitures")
#----------------------------------------------------------------------------------------------------------------------------

#la liste uniquement des prix a exploiter
aff(list1)
aff(list3)
aff(list1)



#affichage des informations
ensemble = val1 + val2 + val3
print("================================================================================")
print("Hier : ", new_date)
print("il y a eu", ensemble ,"voiture(s) postée(s) sur jumia Deals")


