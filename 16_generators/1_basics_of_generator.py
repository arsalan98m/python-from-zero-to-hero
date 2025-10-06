"""
Generator or Generators

Generator is a very interesting concept in python. It's relatively easy, you just have
to train your brain that what's the difference between a regular function as well as a 
generator. Now whenever there's generator, always remember one thing which is we are 
`generating things`, in the `regular function` or in the `loop` we just get the results 
immediately. So everything is loaded up in the memory, in the `loops` or `other functions`.
But when you design generators, you get one value at a time. So it's very memory optimized,
it doesn't do all the things at once. It's actually very optimized in certain cases.
But this doesn't mean we are going to to replace the whole functions with the generators.
They do have their need and sometimes they are super helpful, super useful and especially
if you are working with fastAPI or anything like that it's very helpful but not always.

Whenever we are talking about the generators, a couple of things you are going to see
as special terms but one of the most common term that we see all around the places is `yield`.
This is a keyword. Just like we have a `for` keyword but generators are always always 
going to come up with the `yield` as a keyword. Now the most important part that you 
should always remember about generators is first of all `you save memory`. Another part
is some times `you don't want the results immediately` and the most important part is
`lazy evaluation`. These are the three most important keyword points of generators, but
not the only one there are other use-cases as well but these are the more than enough for 
us to understand and remember that how it works. 


OR 

🧠 What is a Generator?
A generator is a special type of function that generates values one at a time using the `yield` keyword.

Unlike regular functions that return everything at once (and store it all in memory), a generator gives you
just one value at a time, only when you ask for it.

✅ Why Use Generators?
- Memory Efficiency: Instead of storing a big list in memory, you get one item at a time.
- Lazy Evaluation: It doesn't compute everything immediately — it waits until you ask (like “on demand”).

- Great for Big Data or Streams: When you're working with a lot of data (like reading large files, APIs, 
or streaming content), you don't want to load everything into memory at once.


Now let's see how we can create a generator.
"""


# ⚙️ Generator Function
def serve_chai():
    """
    - Returns one item at a time.
    - More memory-friendly.
    - Can pause and resume between yields.
    """
    yield "Cup 1: Masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"


stall = serve_chai()  # Creates a generator

for cup in stall:
    # Inside here Python automatically calls the next() function for you behind the scenes on the iterator object until it raises StopIteration.
    # The for loop handles that for you.
    print("🧋", cup)


# Normal Function
def get_chai_list():
    """
    - Returns the full list at once.
    - Uses more memory.
    - You can't pause and resume it.
    """
    return ["Cup 1: Masala chai", "Cup 2: Ginger chai", "Cup 3: Elaichi chai"]

# ⚙️ Generator Function


def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_gen()

# 🔄 Using next() with Generators
print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
print(next(chai))  # ❌ Error: StopIteration (No more cups!)
