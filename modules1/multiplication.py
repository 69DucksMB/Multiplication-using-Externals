# ==========================
# multiplication.py
# Mark Balagtas
# 6/4/2021
# Multiplication funcs
# ==========================

# ========== funcs ============

def multiply(n1,n2): # multiplication func lol
    return str(n1 * n2)

def ask(n1,n2):
    print("\nWhat is", n1, 'x', n2, "? ") # multiply quest
    return (input('> ')) 

def score(score,fn,sn):
    return ((score + 100) + (len(range(fn,sn))*2)) #calculates score
    
# ======================

