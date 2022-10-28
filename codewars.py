#CodeWars Python Base

#Exo 1, a -> est une liste 
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

#Exo 2, i -> est une liste de nombre à doubler 
def double_integer(i):
    sum = i * 2
    return sum

#Exo 3, basic_op est une fonction
def basic_op(operator, value1, value2):
    result = 0
    if operator == '+':
        result = value1 + value2
        return result
    
    if operator == '-':
        result = value1 - value2
        return result
    
    if operator == '*': 
        result = value1 * value2
        return result
    
    if operator == '/':
        result = value1 / value2
        return result

#Exo 4, double tout les nombre de la liste 
def maps(a):
    output = [2 * x for x in a]
    print(output)
    return output

#Exo 5 Convertisseur en milliseconde
def past(h, m, s):
    return(3600* h + 60 * m + 1000 * s)

#Exo 6 Dans une Liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] il doit me return [10, -65] 
# il compte le nombre de positif et le result des negatif
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    
    nb_positive = 0
    sum_negative = 0
    for x in arr: 
        if x > 0:
            nb_positive += 1
            print(nb_positive)

        if x < 0:
            sum_negative += x
            print(sum_negative)
    return [nb_positive, sum_negative]

#Exo 7 Voir dans une liste qui est le chiffre le plus grand et le plus petit (negatif compris)
def minimum(arr):
    mini = min(arr)
    print(mini)
    return mini
        
def maximum(arr):
    maxi = max(arr)
    print(maxi)
    return maxi
    
#Exo 8, remplacer des espaces 
def no_space(x):
    result = x.replace(" ","")
    print(result)
    return result

#Exo 9, Pierre Feuille Ciseaux (pas reussit à 100%)
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

#Exo 10 Mettre des nombres positif en negatif et vice versa 
def opposite(number):
  # your solution here
    if number > 0:
        opposite_pos = (number - (number + number))
        print(opposite_pos)
        return opposite_pos
    
    if number < 0:
        opposite_neg = (number - (number + number))
        print(opposite_neg)
        return opposite_neg
    
    if number == 0:
        return 0