
real = input("actual: PRESS ENTER ")
code = input("coded: ")

dict_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dict_alphabet2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def find_place(str, alphas):
    for i in range(len(alphas)):
        if str[0] == alphas[i]:
            return i
        else:
            continue

placement_real = find_place(real, dict_alphabet)
placement_code = find_place(code, dict_alphabet2)

num = placement_code - placement_real
print (num)
