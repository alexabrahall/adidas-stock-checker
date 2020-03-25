import requests,json,time
print (('''         ADIDAS STOCK CHECKER

         Made By @Alex#0002 
         
         
         ''' ))

def check():
    sku= input ("Input the desired SKU here: ") #Adidas sku will go here (E.g. EF2099)  
    Region = input ("Please state the region you would like (E.g. UK, US, NL): ").upper() #not case sensitive
    ending = "co.uk" #Adidas UK is the default here

    if Region == "UK": #specific region configurations go here
        ending = "co.uk"
    elif Region!= "UK":
        ending = Region
    elif Region =="US":
        ending="com"
    else:
        print("Invalid region!")
        check()
    
    headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }


    r = requests.get("https://www.adidas."+ending+"/api/products/"+sku+"/availability",headers=headers)
    stock= json.loads(r.text)
    print("\n")
    try:
        if stock["message"] == "not found":
            print("Invalid SKU!")
            check()
    except:
        for item in stock["variation_list"]:
            #print(item)
            print ("Size "+str(item["size"])+" = "+ str(item["availability"])+" stock left")
    
    repeat = input("Do you want to check stock on another item?  Y/N ")
    if repeat.lower() == "y":
        check()
    else:
        time.sleep(10)

check()
                


