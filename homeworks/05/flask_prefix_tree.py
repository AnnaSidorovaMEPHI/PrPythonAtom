from flask import Flask, request, jsonify

app = Flask(__name__)

class PrefixTree:
    def __init__(self):
        self.root = [{}]

    def add(self, string, jsn, rating):
        
        if self.check(string):
            return
        wrk_dict = self.root
       # print(wrk_dict)
        for i in string:
            if i in wrk_dict[0]: 
                wrk_dict=wrk_dict[0][i] #опускаемся по строке по словарю
                if len(wrk_dict[2])<10:
                    wrk_dict[2][rating] = [string, jsn] #МОЖНОНЕСРАВНИВАТЬ, просто пихаем
                else:#ЕСЛИ НАБРАНО, то на место той минимальной частоты ставим новый 
                    if rating > wrk_dict[1]:#Если рейтинг б минимального
                        wrk_dict[2][wrk_dict[1]] = [string, jsn]  
                 
                wrk_dict[1]=min(wrk_dict[2].keys()) 
            else:#Если его нет в словаре, то по нему пока положим данное в топ
                wrk_dict[0][i] = [{}, rating, {rating: [string, jsn]}]
                wrk_dict = wrk_dict[0][i]
        wrk_dict.append(True)
        #TODO добавить строку
    def check(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        #print(len(wrk_dict))
        #print(wrk_dict)
        if len(wrk_dict) == 4:
            return True
        return False
        #TODO проверить наличие строки
    
    def check_part(self, string):
        wrk_dict = self.root
        for i in string:
            if i in wrk_dict[0]:
                wrk_dict = wrk_dict[0][i]
            else:
                return False
        return True

    def top(self, string):
        top=[]
        if not self.check_part(string):
            return []
        wrk_dict=self.root
        #print("Передалось")
        #print(wrk_dict)
        if self.check_part(string):
            for i in string:
                if i in wrk_dict[0]:
                    wrk_dict=wrk_dict[0][i]
            #print(wrk_dict)
            index=[]
            list=[]
            for i in wrk_dict[2]:#В него клала топ
                #print("***")
                index.append(int(i))
                list.append(wrk_dict[2][i])
            n=1
            while n<len(index):#Parallel BubbleSort:D
                for j in range(len(index)-n):
                    if index[j]>index[j+1]:
                        index[j],index[j+1]=index[j+1],index[j]
                        list[j],list[j+1]=list[j+1],list[j]
                    n+=1
        return list
            
    #TODO реализация класса prefix tree, методы как на лекции + метод дать топ 10 продолжений. Скажем на строку кросс выдаем кроссовки, кроссовочки итп. Как хранить топ? 
    #Решать вам. Можно, конечно, обходить все ноды, но это долго. Дешевле чуток проиграть по памяти, зато отдавать быстро (скажем можно взять кучу)
    #В терминальных (конечных) нодах может лежать json с топ актерами.
def init_prefix_tree(filename):
    with open(filename, 'r+') as f:
        for x in f:
        #x=f.read().strip()
            s = x.strip().split('/t')
            pr_tree.add(s[0],s[1],s[2])
        f.close()
pr_tree = PrefixTree()
init_prefix_tree('1.txt')    

@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    #TODO по запросу string вернуть json, c топ-10 саджестами, и значениями из нод
    
    json = jsonify(pr_tree.top(string))
    return json
@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    instr="Из файла загружаются данные. По введенному вами префиксу, вернется топ 10 популярных саджестов."
    return instr

if __name__ == "__main__":
    app.run()
