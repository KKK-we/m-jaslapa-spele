def ierakstīt(teksts):
    fails = open("teksts.txt","w",encoding='utf-8')
    fails.write(teksts)
    fails.write('\n')#\n tas parāda ka nākamajā rindā raksta 
    fails.close()

#ierakstīt("man iet labi")

def klat(teksts):
    fails = open("teksts.txt", "a" , encoding="utf-8")
    fails.write(teksts)
    fails.write('\n')#\n tas parāda ka nākamajā rindā raksta 
    fails.close(teksts)

#klat("man arī")    

def nolasit():
    fails = open("teksts.txt", "r", encoding="utf-8")
    viss = fails.read
    print(viss[0])

#nolasit()    

def uztaisit_vienu_spamu(vards, vecums, dz):
    if dz == "s":
        galotne = "usi"
    else:
        galotne = "is"    
    teksts = f"sveiki, {vards}!\nJūs esat laimēj{galotne} {int(vecums)*10} EUR!"
    with open(f"spams/{vards}.txt", "w", encoding= "utf-8") as f:
        f.write(teksts)

uztaisit_vienu_spamu("laima", 23, "s")    

def viss_spams():
    with open ("vardi.txt", "r", encoding="utf-8") as f :
        visi = f.readlines()
        for viens in visi:
            info = viens.split()
            print (info)
            uztaisit_vienu_spamu(info[0], info[1], info[2])
viss_spams()