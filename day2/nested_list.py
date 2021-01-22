if __name__ == '__main__':
    marks_list=[]
    arr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr1=[name,score]
        marks_list.append(score)
        arr.append(arr1)
    
    marks_list=sorted(set(marks_list))
    arr=sorted(arr)
    for a in arr:
        if a[1]==marks_list[1]:
            print(a[0])
        
        
        
        
        