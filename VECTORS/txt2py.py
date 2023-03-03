y_auto = []
with open("C:/Users/rapha/Desktop/Projet_long/eclairage_normalise_auto.txt","r") as f :
    lignes = f.readlines()


for l in lignes :
    nums = l.strip().split('\t')
    nums[:] = list(map(float, nums))
    y_auto.append(nums)
    
y = []
with open("C:/Users/rapha/Desktop/Projet_long/eclairage_auto.txt","r") as f :
    lignes = f.readlines()


for l in lignes :
    nums = l.strip().split('\t')
    nums[:] = list(map(float, nums))
    y.append(nums)
