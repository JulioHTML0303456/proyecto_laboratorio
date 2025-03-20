def CountWords(list):
    i=0
    count=0
    while i<len(list):
        if type(list[i]) == str:
            count+=1
        i+=1
    return count

print(CountWords(["hjvhhg",'ghtvyjtb',5,'tttbbnb',6,'ihbby']))    