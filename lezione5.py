my_var = 'ciao'
print(my_var)

my_var_ = 'ciao'
print(my_var_)

#non mi fa salire l'errore: prova una cosa ma se non funzione fai questo
try:
    my_var = float(my_var)
except:
    print('non posso convertire "my var" a valore numerico!!!')
    #mi permette di usare un valore di default in caso ci siano errori e per evitarli
    print('uso valore di default "0.0" per my_var')
    my_var = 0.0
    #normalizzo parametri in input se mi dai il paramentro sbagliato vado avanti con un valore di default

    my__var = 'ciao'

    try:
        my__var = float(my__var)

    #salvo l'errore in 'e' e mi permette questo metodo di vedere bene il mio errore/eccezzione
    except Exception as e:
        print('Non posso convertire "my var" a valore numerico!')
        print('la variabile "my var" valeva: "{}"'.format(my__var))
        print('ed ho avuto questo errore: "{}"'.format(e))


    try:

        my___var = float(my___var)

    except ValueError:
        print('Non posso convertire "my var" a valore numerico!')
        print('Ho avuto un errore di VALORE. "my___var" valeva "{}".'.format(my___var))

    except TypeError:
        print('Non posso convertire "my var" a valore numerico!')
        print('Ho avuto un errore di TIPO. "my___var" valeva "{}".'.format(type(my___var)))

    except Exception as e:
        print('Non posso convertire "my var" a valore numerico!')
        print('Ho avuto un errore generico: {}".'.format(e))
#questo metodo non va bene con codici con molte righe perchè non ci permette di capire precisamente dov'è l'errore in aprticolare se nasconde il trace back cioè non so più quale sia la riga da dove viene l'errore. se lo faccio su grandi pezzi di codice perdo informazioni
#se ho ,olte righe di codice posso fare più righe try diverse o metto un try dentro al try

#se type errore è figlio di value error , se type error passa value error non passa mai il primo error, metto alla fine exception per catturare tutto quell che rimane

