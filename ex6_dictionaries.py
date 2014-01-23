__author__ = 'sakkas'


#Sözlükler key ve valuedan oluşurlar.
# Örnek
# key 06 value Ankara
# key 35 value İzmir

cities = {"06":"Ankara", "34":"İstanbul", "35":"İzmir"}
print(cities["06"])#Ankara

#Sözlüğe eleman ekleme
cities["01"] = "Adana"
print(cities["01"])#Adana


#Sözlükten eleman çıkarma
cities.__delitem__("34")

print(cities)