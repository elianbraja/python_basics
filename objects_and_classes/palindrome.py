class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self._processed_content() == reverse(self._processed_content())

    def _processed_content(self):
        """Process content for palindrome testing."""
        return self.content.lower()


class TranslatedPhrase(Phrase):
    """A class to represent phrases with translation."""

    def __init__(self, content, translation):
        super().__init__(content)
        self.translation = translation

    def _processed_content(self):
        """Override superclass method to use translation instead of content ."""
        return self.translation.lower()


def reverse(string):
    """Reverse a string"""
    return "".join(reversed(string))

# Ki parasysh qe Python nuk ka nje menyre per te definuar metoda private te nje klase.
# Ne fakt perdoret konvente qe kur emri i methodes eshte _method_name, athere do te thote
# qe kjo metode duhet te konsiderohet si private. Gjithsesi nese tenton ta therrasesh eshte
# po njesoj si nje methode normale. Eshte thjesht mnyra Pythonic qe duhet respektuar.

# Gjithashtu eshte dhe nje menyre tjeter me dy underscore, __method_name. Kjo metode nuk
# mund te thirret drejtperdrejt dhe sjell error, por gjithsesi dhe kjo mund te thirret nese
# thirret si _classname__method_name


# import palindrome
# phrase = palindrome.Phrase("Racecar")
# phrase.ispalindrome()

# import palindrome
# phrase = palindrome.TranslatedPhrase("MakineGarash", "Racecar")
# phrase.ispalindrome()



