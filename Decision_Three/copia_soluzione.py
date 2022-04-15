def Learn_Decision_Tree(list_attributes, restaurants, parent_restaurants):
  #print(list_attributes)
  #print(restaurants)
  aux=[]
  for i in restaurants:
    aux.append(dict_restaurants_result[i])

  if 'Yes' not in aux:
    print('Same classification: label NO')
    print('.........FOGLIA..........')
    print()
    return
  elif 'No' not in aux:
    print('Same classification: label YES')
    print('.........FOGLIA..........')
    print()
    return
  elif len(restaurants)==0:
    print('Plurality Value: label ', Plurality_value(parent_restaurants))
    print('........FOGLIA..........')
    print()
    return

  elif len(list_attributes)==0:
    print('Plurality Value: label ', Plurality_value(restaurants))
    print('........FOGLIA..........')
    print()
    return
  else: 
    print()
    gain=0
    attr_gain=''
    
    for i in list_attributes:
     # print(i)
  
#      if(i=='Price'):
#        pdb.set_trace()
  
      gain_i=Gain(i, restaurants)
      #print(gain_i)
      if gain_i >= gain:
        gain=gain_i
        attr_gain=i
    
    list_attributes.remove(attr_gain)
    copia_attr=list_attributes.copy()
    for i in attr_dict[attr_gain]:
      copia_parent_restaurants=restaurants.copy()
      restaurants_remained=split_attribute(attr_gain, i, restaurants)
  
      print('Attributo scelto: '+attr_gain+'    con gain: '+str(gain))
      print()
      print('al valore dell\'attributo: '+i+' sono associati i ristoranti: ')
      print(restaurants_remained)
      print()
      print()

      print('al valore dell\'attributo: '+i+' sono associati gli attributi: ')
      print(list_attributes)

      print()
      print()
      Learn_Decision_Tree(list_attributes, restaurants_remained, copia_parent_restaurants)
      list_attributes=copia_attr
#da correggere: manca l'attributo ALT nella seconda chiamata di HUN
#da controllare: se un nodo figlio ha entropia maggiore del padre, che fare???

(Learn_Decision_Tree(list_attributes, partecipants, partecipants))
