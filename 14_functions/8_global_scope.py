chai_type = "Plain"


def front_desk():
    chai_type = "Masala"

    def kitchen():
        """
        instead of a global can i go and user nonlocal?
        What's happen that case?
        Then it's says hey `No binding for nonlocal 'chai_type' found` because it's looking just above the function

        - The nonlocal is designed specifically in such a way that it should be looking
          up just in this outer function, not the global scope. 
        - So global is a reference to global object from anywhere, you can access this anywhere.
           but if you want to access it just above in the function nonlocal is your friend.
        """
        global chai_type  # After this line, chai_type is no longer local, it's now global
        chai_type = "Irani"
    kitchen()
    print(f"After kitchen update: {chai_type}")


front_desk()
print(f"Global: {chai_type}")
