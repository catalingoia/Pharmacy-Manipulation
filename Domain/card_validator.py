from Repository import generic_repository

class CardValidator:

    def validate(self, card):

        errors = []
        if card.cnp < 13:
            errors.append("CNP-ul a fost introdus incorect")
        if errors != []:
            raise ValueError(errors)
