# doc string needs to be very first line of the function other wise it will return None inside __doc__

def chai_flavour(flavour="masala"):
    """Return the flavour of chai."""
    chai = "ginger"
    return flavour


print(chai_flavour.__doc__)
print(chai_flavour.__name__)

help(len)


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa.

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: Total bill
    """
    return (chai * 10) + (samosa * 15)


print(generate_bill(2, 3))
