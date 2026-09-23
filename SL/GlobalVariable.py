Gvar = "I am a global variable"
print(Gvar)

def MyFunction():
    global Gvar # Declare Gvar as global. Python normally assumes Gvar is a local variable inside the function.
    Gvar = "I am a global variable still"
    Lvar = "I am a local variable"
    print(Gvar)
    print(Lvar)


MyFunction()

print(Lvar)  # This will raise an error because Lvar is not defined in this scope
print(Gvar)  # This will print "I am a global variable still" because Gvar was modified inside the function and declared as global.