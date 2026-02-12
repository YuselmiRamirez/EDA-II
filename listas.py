def double(arr):
    return [x*2 for x in arr]

def maximum(arr):
    if not arr:
        return None
    return max(arr)

def average(arr):
    if not arr: 
        return 0
    total = 0
    for x in arr:
        total+=x
        return total/len(arr)
    
def main():
    listas = [
        [5, 6, 7, 7, 3],
        [-4, -17, -3],
        [10, 50, 36],
        []
    ]
    for lista in listas:
        print("Main List:", lista)
        print("Double: ", double(lista))
        print("Maximum: ", maximum(lista))
        print("Average: ", average(lista))
        print()

if __name__ == "__main__":
    main()
