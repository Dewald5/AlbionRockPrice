# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:09:50 2020

@author: Dewald
"""
#import webbrowser if you want it to output a textfile at the end of each run with all of the prices
import requests 
import json

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
   
   CarleonS = 'Flat Slate prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= SPrice:
       print("Buy Slate in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= SPrice:
       print("Buy Slate in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= SPrice:
       print("Buy Slate in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= SPrice:
       print("Buy Slate in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= SPrice:
       print("Buy Slate in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= SPrice:
       print("Buy Slate in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "w+")
   f.write(All)
   f.close()

def Slate1():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T6_ROCK_LEVEL1@1?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Slate1price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Slate1price.json') as f:
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

   CarleonS = '\nSlate .1 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'
   
   if int(Carleon["sell_price_min"]) <= S1Price:
       print("Buy Slate1 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= S1Price:
       print("Buy Slate1 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= S1Price:
       print("Buy Slate1 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= S1Price:
       print("Buy Slate1 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= S1Price:
       print("Buy Slate1 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= S1Price:
       print("Buy Slate1 in Martlock for: " + str(Martlock["sell_price_min"]))
   
   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def Slate2():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T6_ROCK_LEVEL2@2?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Slate2price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Slate2price.json') as f:
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

   CarleonS = '\nSlate .2 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= S2Price:
       print("Buy Slate2 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= S2Price:
       print("Buy Slate2 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= S2Price:
       print("Buy Slate2 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= S2Price:
       print("Buy Slate2 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= S2Price:
       print("Buy Slate2 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= S2Price:
       print("Buy Slate2 in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def Slate3():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T6_ROCK_LEVEL3@3?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Slate3price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Slate3price.json') as f:
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

   CarleonS = '\nSlate .3 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= S3Price:
       print("Buy Slate3 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= S3Price:
       print("Buy Slate3 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= S3Price:
       print("Buy Slate3 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= S3Price:
       print("Buy Slate3 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= S3Price:
       print("Buy Slate3 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= S3Price:
       print("Buy Slate3 in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def SlateBlock():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T6_STONEBLOCK?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('SlateBlockprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('SlateBlockprice.json') as f:
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

   CarleonS = '\nSlate Block prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= SBPrice:
       print("Buy SlateBlock in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= SBPrice:
       print("Buy SlateBlock in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= SBPrice:
       print("Buy SlateBlock in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= SBPrice:
       print("Buy SlateBlock in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= SBPrice:
       print("Buy SlateBlock in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= SBPrice:
       print("Buy SlateBlock in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def Basalt():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T7_ROCK?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Basaltprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('Basaltprice.json') as f:
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
   
   CarleonS = 'Flat Basalt prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= BPrice:
       print("Buy Basalt in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= BPrice:
       print("Buy Basalt in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= BPrice:
       print("Buy Basalt in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= BPrice:
       print("Buy Basalt in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= BPrice:
       print("Buy Basalt in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= BPrice:
       print("Buy Basalt in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def Basalt1():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T7_ROCK_LEVEL1@1?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Basalt1price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Basalt1price.json') as f:
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

   CarleonS = '\nBasalt .1 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'
   
   if int(Carleon["sell_price_min"]) <= B1Price:
       print("Buy Basalt1 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= B1Price:
       print("Buy Basalt1 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= B1Price:
       print("Buy Basalt1 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= B1Price:
       print("Buy Basalt1 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= B1Price:
       print("Buy Basalt1 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= B1Price:
       print("Buy Basalt1 in Martlock for: " + str(Martlock["sell_price_min"]))
   
   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def Basalt2():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T7_ROCK_LEVEL2@2?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Basalt2price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Basalt2price.json') as f:
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

   CarleonS = '\nBasalt .2 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= B2Price:
       print("Buy Basalt2 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= B2Price:
       print("Buy Basalt2 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= B2Price:
       print("Buy Basalt2 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= B2Price:
       print("Buy Basalt2 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= B2Price:
       print("Buy Basalt2 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= B2Price:
       print("Buy Basalt2 in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def Basalt3():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T7_ROCK_LEVEL3@3?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Basalt3price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Basalt3price.json') as f:
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

   CarleonS = '\nBasalt .3 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= B3Price:
       print("Buy Basalt3 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= B3Price:
       print("Buy Basalt3 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= B3Price:
       print("Buy Basalt3 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= B3Price:
       print("Buy Basalt3 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= B3Price:
       print("Buy Basalt3 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= B3Price:
       print("Buy Basalt3 in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

def BasaltBlock():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T7_STONEBLOCK?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('BasaltBlockprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('BasaltBlockprice.json') as f:
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

   CarleonS = '\nBasalt Block prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= BBPrice:
       print("Buy BasaltBlock in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= BBPrice:
       print("Buy BasaltBlock in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= BBPrice:
       print("Buy BasaltBlock in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= BBPrice:
       print("Buy BasaltBlock in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= BBPrice:
       print("Buy BasaltBlock in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= BBPrice:
       print("Buy BasaltBlock in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()



def Marble():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T8_ROCK?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Marbleprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('Marbleprice.json') as f:
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

   CarleonS = '\nFlat Marble prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= MPrice:
       print("Buy Marble in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= MPrice:
       print("Buy Marble in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= MPrice:
       print("Buy Marble in Lymhurst for: " + str(Lymhurst["sell_price_min"]))   
   if int(FortSterling["sell_price_min"]) <= MPrice:
       print("Buy Marble in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= MPrice:
       print("Buy Marble in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= MPrice:
       print("Buy Marble in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()
    
def Marble1():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T8_ROCK_LEVEL1@1?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Marble1price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Marble1price.json') as f:
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

   CarleonS = '\nMarble .1 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= M1Price:
       print("Buy Marble1 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= M1Price:
       print("Buy Marble1 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= M1Price:
       print("Buy Marble1 in Lymhurst for: " + str(Lymhurst["sell_price_min"])) 
   if int(FortSterling["sell_price_min"]) <= M1Price:
       print("Buy Marble1 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= M1Price:
       print("Buy Marble1 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= M1Price:
       print("Buy Marble1 in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()
   
def Marble2():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T8_ROCK_LEVEL2@2?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Marble2price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Marble2price.json') as f:
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

   CarleonS = '\nMarble .2 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'

   if int(Carleon["sell_price_min"]) <= M2Price:
       print("Buy Marble2 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= M2Price:
       print("Buy Marble2 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= M2Price:
       print("Buy Marble2 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= M2Price:
       print("Buy Marble2 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= M2Price:
       print("Buy Marble2 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= M2Price:
       print("Buy Marble2 in Martlock for: " + str(Martlock["sell_price_min"]))

   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()
   
def Marble3():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T8_ROCK_LEVEL3@3?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('Marble3price.json', 'wb') as outf:
    outf.write(response.content)

 with open('Marble3price.json') as f:
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

   CarleonS = '\nMarble .3 prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'
   
   if int(Carleon["sell_price_min"]) <= M3Price:
       print("Buy Marble3 in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= M3Price:
       print("Buy Marble3 in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= M3Price:
       print("Buy Marble3 in Lymhurst for: " + str(Lymhurst["sell_price_min"]))    
   if int(FortSterling["sell_price_min"]) <= M3Price:
       print("Buy Marble3 in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= M3Price:
       print("Buy Marble3 in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= M3Price:
       print("Buy Marble3 in Martlock for: " + str(Martlock["sell_price_min"]))
       
   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()
def MarbleBlock():
 response = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T8_STONEBLOCK?locations=Caerleon,Bridgewatch,Lymhurst,FortSterling,Thetford,Martlock&qualities=0")
 with open('MarbleBlockprice.json', 'wb') as outf:
    outf.write(response.content)

 with open('MarbleBlockprice.json') as f:
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

   CarleonS = '\nMarble Block prices:\n'+str(Carleon["city"])+"\n Min:"+str(Carleon["sell_price_min"])+" Max:"+ str(Carleon["sell_price_max"])+'\n'
   BridgewatchS = str(Bridgewatch["city"])+"\n Min:"+str(Bridgewatch["sell_price_min"])+" Max:"+ str(Bridgewatch["sell_price_max"])+'\n'
   LymhurstS = str(Lymhurst["city"])+"\n Min:"+str(Lymhurst["sell_price_min"])+" Max:"+ str(Lymhurst["sell_price_max"])+'\n'
   FortSterlingS = str(FortSterling["city"])+"\n Min:"+str(FortSterling["sell_price_min"])+" Max:"+ str(FortSterling["sell_price_max"])+'\n'
   ThetfordS = str(Thetford["city"])+"\n Min:"+str(Thetford["sell_price_min"])+" Max:"+ str(Thetford["sell_price_max"])+'\n'
   MartlockS = str(Martlock["city"])+"\n Min:"+str(Martlock["sell_price_min"])+" Max:"+ str(Martlock["sell_price_max"])+'\n'
   #list1 = ['Carleon','Bridgewatch'+'Lymhurst'+'FortSterling'+'Thetford'+'Martlock']  
   
   if int(Carleon["sell_price_min"]) <= MBPrice:
       print("Buy MarbleBlock in Carleon for: " + str(Carleon["sell_price_min"]))
   if int(Bridgewatch["sell_price_min"]) <= MBPrice:
       print("Buy MarbleBlock in Bridgewatch for: " + str(Bridgewatch["sell_price_min"]))
   if int(Lymhurst["sell_price_min"]) <= MBPrice:
       print("Buy MarbleBlock in Lymhurst for: " + str(Lymhurst["sell_price_min"]))   
   if int(FortSterling["sell_price_min"]) <= MBPrice:
       print("Buy MarbleBlock in FortSterling for: " + str(FortSterling["sell_price_min"]))
   if int(Thetford["sell_price_min"]) <= MBPrice:
       print("Buy MarbleBlock in Thetford for: " + str(Thetford["sell_price_min"]))
   if int(Martlock["sell_price_min"]) <= MBPrice:
       print("Buy MarbleBlock in Martlock for: " + str(Martlock["sell_price_min"]))
   
   All = CarleonS+BridgewatchS+LymhurstS+FortSterlingS+ThetfordS+MartlockS 
   f = open("Rockprices.txt", "a")
   f.write(All)
   f.close()

BuySlate = input("Do you want to Buy Slate Y/N\n").upper()
BuyBasalt = input("Do you want to Buy Basalt Y/N\n").upper()  
BuyMarble = input("Do you want to Marble Slate Y/N\n").upper()
print("\nProcessing... this may take some time\n")
if BuySlate == "Y":
 Slate()
 Slate1()
 Slate2()
 Slate3() 
 SlateBlock()  
 
if BuyBasalt == "Y":  
 Basalt()
 Basalt1()
 Basalt2()
 Basalt3()
 BasaltBlock()

if BuyMarble == "Y":
 Marble()
 Marble1()
 Marble2()
 Marble3()
 MarbleBlock()

#webbrowser.open("Rockprices.txt") to open the TEXTFILE with the cities and all their names
print('\n   Done!!!!!')