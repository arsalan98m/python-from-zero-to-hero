"""
static methods

static methods are helpful when u want utility functions grouped with your classes
without depending on any instance.
"""


class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " water , milk  , ginger, honey "

result = ChaiUtils.clean_ingredients(raw)
print(result)
