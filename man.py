#importation des différents modules
import math
import csv
import networkx as nx
import matplotlib.pyplot as plt
 
#préparation du graph
G=nx.Graph()
nx.draw(G)  # networkx draw(), dessin
plt.draw()  # pyplot draw(), dessin

#traitement du csv
with open('VOIES_NM.csv') as csvfile:
	reader = csv.DictReader(csvfile)	#lecture
	i = 0
	#lecture jusqu'au bout du fichier
	for row in reader:
		i = i + 1	#incrémentation
		#print(row['LIBELLE'], row['TENANT'], row['ABOUTISSANT'], row['BI_MAX'])
		rue = row['COMMUNE'] + " " + row['LIBELLE'] #la rue
		tenant = row['TENANT']	#le tenant
		aboutissant = row['ABOUTISSANT']	#l'aboutissant
		points = row['BI_MAX']	#les points (donc le poids de la route
		statut = row['STATUT']  #le status (est-ce que c'est grave d'utiliser les voies privée en toutes circonstance ?)
		#if statut == "PRIVEE":
		#	print("privee !!!")
		#else:
		#	print("rue")
		if tenant != "" and aboutissant != "":
			print (tenant + " -> " + aboutissant)
			G.add_edge(tenant,aboutissant, axe=rue)			

nx.draw_circular(G)	#dessin du graph
#nx.draw_random(G)
plt.show()	#affichage

#recupération de toutes les routes possibles
def find_path(graph, start, end, path=[]):
	path = path + [start] #ajout de passage
        if start == end: #arrivée
            return path
        if not graph.has_key(start): #problème
            return None
        for node in graph[start]:	#bouclage de la fonction sur elle même
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

find_path(G, tenant, aboutissant) #lancement de la découverte