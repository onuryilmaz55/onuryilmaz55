def düzlestir(liste1):
    liste2=[]
    
    for i in liste1:
        if(type(i) is list):
            for a in i:
                liste2.append(a)
        else:
            liste2.append(i)
            
    return liste2

liste1=[10,15,[18,19],25,27,[30,35,37,98],107,"onur",["yılmaz,samsun"]]

print("eski liste",liste1)
print("yeni liste",düzlestir(liste1))