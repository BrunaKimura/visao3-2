import pickle
import dicionario
import matplotlib.pyplot as plt
import cv2
import argparse

dic_ori = dicionario.a
dic_id = pickle.load( open( "dict.p", "rb" ) )

parser = argparse.ArgumentParser(description = 'objeto buscado')
parser.add_argument(action='store', dest='simple_value',
                    help='Store a simple value')
results = parser.parse_args()

term = results.simple_value

def achaid():
    lista_id=[]
    lista_name = []
    for id_item, name in dic_ori.items(): 
        if term in name:
            lista_id.append(id_item)
            lista_name.append(name)
    return lista_id, lista_name

def achaididentico():
    lista_id=[]
    lista_name = []
    for id_item, name in dic_ori.items(): 
        if term == name:
            lista_id.append(id_item)
            lista_name.append(name)
    return lista_id, lista_name

find = 0
indice = 0
id_itens, lista_name = achaid()
for id_atual in id_itens:
    for key in dic_id:
        if key == id_atual:
            max_porc = sorted(dic_id[key], reverse=True)
            max_porc5 = max_porc[:5]
            find =1
    
        
    if find == 1:
        b = [el[1] for el in max_porc5]
        index = 1
        
        for i in b:
            img = cv2.imread(i)
            new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            plt.subplot(2,3,index)
            plt.imshow(new_img)
            index+=1
        print(lista_name)
        plt.suptitle(lista_name[indice])
        plt.show()
    else:
        print("termo não encontrado")
    indice+=1