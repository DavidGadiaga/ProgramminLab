def prodotto(my_list):
  p = 1
  for item in my_list:
    p *= item
  return p

l1= [1,2,3,4,5]
print("Prodotto: {}". format(prodotto(l1)))