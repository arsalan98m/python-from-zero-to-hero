sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")
print(f"ID of sugar: {id(sugar_amount)}")

print("\n" + "=" * 50 + "\n")

# Now interestingly, what i want to share you about the `mutable` and `immutable` part which most people goes absolutely wrong
sugar_amount = 12  # Here sugar_amount is updated to 12
print(f"Second Initial sugar: {sugar_amount}")
print(f"ID of sugar after update: {id(sugar_amount)}")

"""
If i go and run this program, i will get the output as 2 and then 12.
The initial sugar is 2 and then the second initial sugar is 12.
Now here is a interesting part. Now this thing is here on line 4 what
we have done. The numbers are considered as `immutable` they do not 
change. But again the point is, hey, arsalan, this is just changed here.
We initially having the value of 2. Now we have a value of 12. So it 
definitely changed. How can you say that? This is immutable. This cannot
be changed. This is where a lot of people make it absolutely wrong in 
the python, as i mentioned, you never check it with the value. The
value definitely of the sugar_amount is getting changed but behind the
scene, this number `2` itself is actually immutable. This `2` never 
changed.

What Python did behind the scene for you is it took this number `2` and it
actually created a new number `12` this time it says, hey you want 12? ok
we'll give you 12. So a new number was created for you and this time instead
of pointing the `2` you are pointing actually to `12`. Yeah this is a little
bit of an interesting aspect of how python actually works. So instead
this time we simply go a head and say that, hey, we are pointing `12` not `2`
This `2` is still in memory, this is `immutable` you cannot change it. What
you are changing now is reference always remember what we are changing what
seems to be changing in the world of mutable is the reference, So you are
changing the reference, you are not changing the actual value itself. I'll
show you that. Yes, some of these values do get changed.

Now you might be asking what's the proof of it?
Yeah that's a good question, as i mentioned always check for identity, never 
for the value. Yeah our value got changed but i asked you, hey, not to track
with the values. There's a big `no` here. Now, what i want to do is change or
track based on identity. So how we can we find the identity of it?
It actually super easy.

"""
