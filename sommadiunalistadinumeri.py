#1) definisco una funzione sum_list
def sum_list(the_list):
    s = 0 #da dove partiremo per mettere la nostra somma 
    for item in the_list:
        s += item # ogni item oggeto che trovo verrà messo dentro s formando quindi la nostra somma
    return s #ricordati di rimanere all'interno del for per l'indentazione altrimenti esco dal "blocco"

#creo adesso una lista a parte come voglio
l1 = [1,2,3,4,5,6,8,9] #la lista si forma con una parentesi quadra e gli elementi sono separati semplicemente da virgole

#stampiamo la nostra somma: ricorda bene print no printF

print("Sum list: {}". format(sum_list(l1)))
      

