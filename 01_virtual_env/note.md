# Virtual Environment

It's like safeguarding your application from other version's and don't clutter your operating
system and also so that your program actually moves safely in other environment as well on
`Linux` or `Mac` or other people's computer

# Creating Virtual environment in Mac using Traditional Way

```bash
python3 -m venv `name_of_venv`

# usually people call it also `venv` the same name or some people call it as a `.venv`
# just to make sure that it's hidden, you can call it superman no problem at there

python3 -m venv .venv

# Now after running this command, there is a new folder exits in our project which is .env
# and now we have the whole virtual environment folder, this actually creates a separate
# version of the python itself. Now this is just created it, it's not activated. Currently
# we are using python version 3 which is installed in my whole computer, not the small box
# here, to activate it, there are actually two commands, one for mac and another for windows

.venv\Scripts\activate # this is how we activate virtual environment in windows

source .venv/bin/activate # this is for mac

# Now after running this command we are not in our computers python, but you are into
# the virtual environment. This is where you can install and bring third party and
# it will not effect anything that you are bringing in one.

# to deactivate virtual environment run this command
deactivate
```

There is also a new way of installing the python, so the traditional way says
that you always go a head and use `venv` but there is a new way as well. And
new way actually uses more tools of the python which is `uv`. This is actually
much much powerful and a lot of people are loving this.
