import pandas
from numpy import log2

df = pandas.read_csv('/home/dans/Documents/Università/Fondamenti_IA/Decision_Three/restaurant_waiting.csv')
attr_dict = {}

def probability(examples):
    pk = 0
    nk = 0
    for j in examples:
        if df.get("Wait")[j] == "Yes":
            pk += 1
        else: 
            nk += 1
    return pk / (pk+nk)

def gain (examples, attribute):
    return entropy(probability(examples)) - remainder(examples, attribute)

def remainder(examples, attribute):
    ret = 0
    for i in attr_dict[attribute]:
        pk = 0
        nk = 0
        for j in examples:
            if i == df.get(attribute)[j]:
                if df.get("Wait")[j] == "Yes":
                    pk += 1
                else: 
                    nk += 1
        ret += ((pk+nk)/len(examples)) * entropy(pk / (pk+nk))
    return ret 
        

def entropy(q):
    ret = -(q*log2(q) + (1-q)*log2(1-q))
    return ret  

def split_attribute(attribute, attr_value, list):
  list_remained=[]
  for i in list:
    if df.get(attribute)[int(i)]==attr_value:
      list_remained.append(i)
  return list_remained    


def Learn_Decision_Tree(list_attributes, restaurants, parent_restaurants):
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

      gain_i=Gain(i, restaurants)
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








def main():
    data_set = df.to_dict('index')
    
    rest_list = []
    for i in range(0,len(data_set)):
        rest_list.append(i)
    
    attr_list = []
    for i in df.columns: 
        attr_list.append(i)
    attr_list.remove("Wait")

    for i in df.columns:
        if i not in attr_dict:
            attr_dict[i] = []
            for j in df.get(i):
                if j not in attr_dict[i]:
                    attr_dict[i].append(j)

    print(remainder(rest_list, "Hun"))
    









if __name__ == '__main__':
    main()