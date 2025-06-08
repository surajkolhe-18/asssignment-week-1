from itertools import combinations

n = int(input())  
letters = input().split()  
k = int(input())  

all_combos = list(combinations(letters, k))

favorable = [combo for combo in all_combos if 'a' in combo]

probability = len(favorable) / len(all_combos)

print(f"{probability:.4f}")
