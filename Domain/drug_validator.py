class DrugValidator:

    def validate(self, drug):

        errors = []
        if drug.price < 0:
            errors.append("Pretul trebuie sa fie un numar pozitiv")
        if drug.recipe not in [True, False]:
            errors.append("Retata trebuie sa fie una dintre: da, nu")
        if errors != []:
            raise ValueError(errors)
