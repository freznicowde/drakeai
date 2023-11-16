import os
from rimes import rimes
import random as r

def generation(word,risk,nwords):
    def get_couplet(arg):
        arg=arg.split(" ")
        return arg




    text=open("Drake.txt",'rb').read().decode(encoding='utf-8')

    text=text.lower()
    text=text.replace(".","").replace(":","").replace(",","").replace("?","").replace('"',"").replace("'","").replace(";","").replace("\n"," ").replace("!","").replace("-","").replace("\n"," ")
    text=text.split(" ")
    print(text)
    def gen(word):
        i=0
        phrase=[]
        posibilities=[]

        while i != len(text):
        
            if text[i]==word:
            
                posibilities.append(text[i+1])
            
            
            i=i+1
        r.shuffle(posibilities)
    
    # Liste de mots
# Créez un dictionnaire pour stocker la fréquence de chaque mot
        frequence_des_mots = {}
        liste_de_mots=posibilities
# Comptez la fréquence de chaque mot dans la liste
        for mot in liste_de_mots:
            if mot in frequence_des_mots:
                frequence_des_mots[mot] += 1
            else:
                frequence_des_mots[mot] = 1
# Triez le dictionnaire par fréquence décroissante
        mots_plus_frequents = sorted(frequence_des_mots.items(), key=lambda x: x[1], reverse=True)
# Affichez les mots les plus fréquents
        
        long=len(mots_plus_frequents)-1
        if long < risk:
            word=phrase.append(mots_plus_frequents[r.randint(0, long )][0])
        else:
            word=phrase.append(mots_plus_frequents[r.randint(0, risk )][0])
        return(phrase[0])
    n=int(nwords)
    repet=0
    word=word
    l=[]
    l.append(word + " ")
    while repet != n:
        mot=gen(word)
        print(mot)
        l.append(mot + " ")
        word=mot
        repet=repet+1
    
    phrase=''.join(l)
    print(phrase)
    phrase=rimes(phrase)
    print(phrase)
    return phrase


# Nom du dossier de destination
    destination_folder = "saves"

# Crée le dossier s'il n'existe pas déjà
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

# Contenu à enregistrer dans le fichier
    file_content = phrase

# Nom du fichier à enregistrer
    file_name = f"MySave{word},{n}.txt"

# Chemin complet du fichier
    file_path = os.path.join(destination_folder, file_name)

# Enregistre le contenu dans le fichier en utilisant le codage UTF-8
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)