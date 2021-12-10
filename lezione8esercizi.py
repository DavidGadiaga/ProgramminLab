
def incremento_modello(args):

    incremento = 0
    media = 0
    args = list(args)
    t = 60

    for i in range(1,len(args)):
        print(i)
        #if args[i] == None:
            #continue
        incremento += args[i] - args[i-1]
    

    media = incremento/(len(args)-1)
    t = t+media

    return t

print(incremento_modello(50,52,60))