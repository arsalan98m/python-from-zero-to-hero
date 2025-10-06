# ********** String **********

"""
One more thing about string is, which we will use quite a lot and a lot times 
these strings we are writing all the English strings, but it's not always that
you'll be writing English scripts sometimes maybe you want to write Hindi, maybe
you want to write Chinese, you want to write Japanese, you want to write Korean
whatever the language that you want to write they have own characters. Like 
for example in the Spanish you might have seen if you press long `a` there
are tilde over the a so if you want to use these kind of things, there is a 
special way to do that.
"""

# now é is not an ordinary character that we are working with and this can actually
# create a problem for us. So for these kind of things when you have these special
# characters or special symbols, we actually use encoded string.
label_text = "Chai Spécial"

# Behind the scene, this one has the guarantee that all of your characters are truly
# encoded and all these special meanings actually carry on.
encoded_label = label_text.encode("utf-8")
print("Non encoded label: ", label_text)
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print("Decoded label: ", decoded_label)
