# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:06:54 2021

@author: Dewald
"""
import requests 
import json

x = 0

SPrice = 1595   #Basalt price for deal
S1Price = 3190   #7.1 Basalt
S2Price = 6380   #7.2 Basalt
S3Price = 12760   #7.3 Basalt
SBPrice = 3676  #Basalt Block price for deal

BPrice = 5032   #Basalt price for deal
B1Price = 10064   #7.1 Basalt
B2Price = 20128   #7.2 Basalt
B3Price = 40256   #7.3 Basalt
BBPrice = 14000  #Basalt Block price for deal

MPrice = 16937 #Marble Price for deal
M1Price = 33874 
M2Price = 67748
M3Price = 135496
MBPrice = 46848 #Marble Block price for deal
       
def Slate():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T6_ROCK?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Slateprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('Slateprice.json') as f:
   data = json.load(f)
   S = ''  
   S = data
   #print(S[0:6])
   Bridgewatch = S[0]
   Lymhurst = S[3]
   FortSterling = S[2]
   Martlock = S[4]
   Carleon = S[1]
   Thetford = S[-1]
   
   City = [Carleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock]
   for x in City:
      #Rockprice = str(x["city"])+"\n Min:"+str(x["sell_price_min"])+" Max:"+ str(x["sell_price_max"])+'\n'
      #print("Rockprices "+ str(Rockprice))
      if int(x["sell_price_min"]) <= SPrice:
          print("Buy Slate in "+str(x["city"])+" for: " + str(x["sell_price_min"]))
Slate()

def Slate1():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T6_ROCK1@1?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Slateprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('Slateprice.json') as f:
   data = json.load(f)
   S = ''  
   S = data
   #print(S[0:6])
   Bridgewatch = S[0]
   Lymhurst = S[3]
   FortSterling = S[2]
   Martlock = S[4]
   Carleon = S[1]
   Thetford = S[-1]
   
   City = [Carleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock]
   for x in City:
      #Rockprice = str(x["city"])+"\n Min:"+str(x["sell_price_min"])+" Max:"+ str(x["sell_price_max"])+'\n'
      #print("Rockprices "+ str(Rockprice))
      if int(x["sell_price_min"]) <= SPrice:
          print("Buy Slate1 in "+str(x["city"])+" for: " + str(x["sell_price_min"]))
Slate1()