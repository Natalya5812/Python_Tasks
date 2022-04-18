
   
#7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
import os
os.system("cls")


X = [True, False]
Y = [True, False]
Z = [True, False]


for i in range(0,2):
    for j in range (0,2):
        for k in range (0,2):
            if (not(X[i] or Y[j] or Z[k])) == (not X[i] and not Y[j] and not Z[k]):
                print (f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - True')
            else:
                print (f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - False')