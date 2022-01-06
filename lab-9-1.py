# Author: CMOB 1/6/2022

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]



for row in rows:
   for names in row:
        lennam = len(names)
        if names[lennam - 1] == "s":
            names = names +"'"
        else:
            names = names +"'s"
        print(names)
