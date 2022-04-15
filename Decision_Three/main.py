import pandas
from numpy import log2

#GLOBAL VARIABLES
df = pandas.read_csv('/home/dans/Documents/university/Fondamenti_IA/Decision_Three/restaurant_waiting.csv')
attr_dict = {}
restaurants_wait={}


def probability(examples):
    pk = 0
    nk = 0
    for j in examples:
        if df.get('Wait')[j] == 'Yes':
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
        if (pk != 0 and nk != 0):
          ret += ((pk+nk)/len(examples)) * entropy(pk / (pk+nk))
    return ret 
        

def entropy(q):
    ret = -(q*log2(q) + (1-q)*log2(1-q))
    if not ret:
        return 0
    return ret  

def split_attribute(attribute, attr_value, list):
  list_remained=[]
  for i in list:
    if df.get(attribute)[int(i)]==attr_value:
      list_remained.append(i)
  return list_remained    

def Plurality_value(list_restaurants):
  elem_yes=0
  elem_no=0
  for i in list_restaurants:
    if restaurants_wait[i]=='Yes':
      elem_yes+=1
    else:
      elem_no+=1
  if elem_yes>elem_no:
    return 'YES'
  else:
    return 'NO'

def Learn_Decision_Tree(list_attributes, restaurants, parent_restaurants):
  #for i in list_attributes:
  #  print(gain(restaurants, i))
  
  aux=[]
  for i in restaurants:
    aux.append(restaurants_wait[i])
  #print(aux)


  if len(restaurants)==0:
    print('Plurality Value: on parent restaurants ', Plurality_value(parent_restaurants))
    print('<<<<<LEAF>>>>>')
    print()
    return

  elif len(list_attributes)==0:
    print('Plurality Value: on restaurants ', Plurality_value(restaurants))
    print('<<<<<LEAF>>>>>')
    print()
    return
  elif 'Yes' not in aux:
    print('All red restaurants')
    print('<<<<<LEAF>>>>>')
    print()
    return
  elif 'No' not in aux:
    print('All green restaurants')
    print('<<<<<LEAF>>>>>')
    print()
    return
  else: 
    print()
    _gain=0
    attr_gain=''
    
    for i in list_attributes:

      gain_i=gain(restaurants, i)
      if gain_i >= _gain:
        _gain=gain_i
        attr_gain=i
    
    list_attributes.remove(attr_gain)
    attr_copy=list_attributes.copy()
    for i in attr_dict[attr_gain]:
      parent_restaurant_copy=restaurants.copy()
      restaurants_remained=split_attribute(attr_gain, i, restaurants)
  
      print('Chosen Attribute:'+''+attr_gain)
      print() 
      print('Attribute\'s value: '+i+'\nRemained restaurants: ')
      print(restaurants_remained)
      print()
      print()

      print('Attribute\'s value: '+i+'\nRemained attributes: ')
      print(list_attributes)

      print()
      print()
      Learn_Decision_Tree(list_attributes, restaurants_remained, parent_restaurant_copy)
      list_attributes=attr_copy.copy()


def main():
    data_set = df.to_dict('index')
    
    rest_list = []
    for i in range(0,len(data_set)):
        rest_list.append(i)
    #print(rest_list)
    attr_list = []
    for i in df.columns: 
        attr_list.append(i)
    attr_list.remove("Wait")
    #print(attr_list)
    for i in range(0, len(df.get(df.columns[0]))):
      restaurants_wait[i]=df.get(df.columns[len(df.columns)-1])[i]
    #print(restaurants_wait)
    
    for i in df.columns:
        if i not in attr_dict:
            attr_dict[i] = []
            for j in df.get(i):
                if j not in attr_dict[i]:
                    attr_dict[i].append(j)
    #print(attr_dict)
    Learn_Decision_Tree(attr_list, rest_list, rest_list)



if __name__ == '__main__':
    main()