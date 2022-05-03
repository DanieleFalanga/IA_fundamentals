import pandas

#GLOBAL
df = pandas.read_csv('/home/dans/Documents/university/Fondamenti_IA/Decision_Three/restaurant_waiting.csv')
dict_results = {}


def decision_list(examples):
    return 

def main():
    data_set = df.to_dict('index')

    rest_list = []
    for i in range(0,len(data_set)):
        rest_list.append(i)

    attr_list = []
    for i in df.columns: 
        attr_list.append(i)
    attr_list.remove("Wait")

    




if __name__ == '__main__':
    main()