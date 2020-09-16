import random as rand

class Monty:

    def __init__(self, arr):
        self.arr = arr

    def test(self, n):
        switched = 0
        stayed = 0
        for i in range(n):
            nopick = 999
            switchto = 999
            arr = self.arr
            rand.shuffle(arr)
            for i in range(1,3):
                if(arr[i]==0):
                    nopick=i
                    break
            for i in range(1,3):
                if(i!=nopick):
                    switchto=i


            if(arr[0]==1):
                stayed+=1
            else:
                switched+=1
        return {"stay":stayed, "switch":switched}

if __name__ == "__main__":
    arr = [0,0,1]
    m = Monty(arr)
    testResults = m.test(1000)
    stayRes=testResults.get("stay")
    switchRes=testResults.get("switch")
    print(stayRes,"/",switchRes,"",stayRes*100/(stayRes+switchRes),"%")