if __name__ == '__main__':
    name_lst = []
    # score_lst = []
    # nest_lst = []
    for i in range(int(input())):
        # name_lst.append(name)        
        # score_lst.append(score)
        # name_lst[i].append(score)
        # lst = [name,score])
        name = input()
        score = float(input())
        name_lst.append([name,score])  
    # count = 0
    # for n in name_lst:
    # count+=1
    sl_score = sorted(set(s[1] for s in name_lst))
    for i in sorted(name_lst):
        if i[1] == sl_score[1]:
            print(i[0])
    # print(sl_score)
        
