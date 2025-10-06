# Organizing our Python code

```
chai_shop/
    run.py -> start the app
    chai.py -> all the functional part of the code
    processing/
        more files
    utils/
        __init__.py -> What do we write inside this files?
        Actually nothing. This file is empty. It's just the
        name of the file which matters and which actually
        differentiates this `processing` with the `utils`

So we do have first name known as `module or modules`, so this `modules`
every single file that you have, like this `run.py` and this `chai.py`
all these files are known as `modules`

Another word that you are gonna see a lot in the world of python is known
as `package or packages` whatever you want to call them. Any folder which
has this init underscore py `__init__.py` this is known as `package`.
And yes that's the difference, any folder which has underscore underscore
init underscore underscore dot py empty file is called as package. But the
`processing` folder since it does not have this file is not going to be
called as `packages` and that's it.

Now inside these files like chai.py we have classes or functions

Just always keep in mind this is organization structure. Again it could have
been different name like `source`, `controllers` whatnot, whatever you want
to call them. That's not the problem. Just remember few things that hey,
these are my `modules` like normal `Python` files. If a folder has a `__init__.py`
that means it's a `package` it's a `Python` vocabulary and then rest of the
folders are just programs or files and folders just like that we don't have
a specific name for them
```

# PEP 8

There is something known as in the `Python` world which is `PEP8`
This `PEP8` is the style guideline for `Python` code. We don't kow
right now how to write the `Python` code that is ok, but there is
a guideline by the man himself who created the `Python` and it's
a very simple guideline, there is no too much included in it.

In the whole `PEP8` they mentioned a lot of points and don't worry, as
we write the code i will automatically incorporate these habits into you.
But some of the things like always use `four spaces` your editor does it
for you automatically. But this says always use `four space` never tabs.
So although tab also does `four space`, but they actually avoids it
because sometimes the tabs are configured for `two tabs` or `two spaces`
but again they say explicitly use `four spaces`.

Another things, it's just a way of writing the code, use better meaningful
names for your methods and functions and classes and all of that. So
call it as `chai` not `c1` `f` or `g`, use better names that is always a
good idea.

And then they also mentioned that use formatters, formatters like `black`
`rough`, `flakate` whatever you want to use, what formatter does, it
automatically makes your code more beautiful, more pep way, it does it
automatically, we don't wan to go into that.

# Zen of Python

One last thing that i wanted to show you is a `Zen of Python` This is known as
a `Pythonic` way of writing the code. So what's the `PEP8`, `PEP8` is also
the same but they have this nice interesting thing. So we can actually go a
head and see this in terminal, Just open up the terminal, doesn't need to be
virtual environment anything is fine, if you are on mac just write python3 or
if you are on windows just write python on terminal and hit enter
and just write `import this` as soon as you do this, this actually gives
you the `Zen of Python`, it's like a poem but again it is just basics.
The whole point is write your code as simple as possible. That is the whole
this poem is saying about it.

Once we are comfortable with `Python` then explore the `PEP8` documentation.
