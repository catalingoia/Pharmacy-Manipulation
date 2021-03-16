from Domain.drug import Drug


class DrugService:
    """
    Manage drug logic
    """
    def __init__(self, repository, repository_t, validator):
        """
        Creates a drug service
        """
        self.__repository = repository
        self.__repository_t = repository_t
        self.__validator = validator

    def add_drug(self, id_drug, name, producer, price, recipe):
        """
        Adds a drug
        :param id_drug: int, the drug id
        :param name: string, the name
        :param producer: string, the producer
        :param price: int, the price of the drug(positive)
        :param recipe: bool
        """
        if recipe == "da":
            recipe = True
        else:
            recipe = False
        drug = Drug(id_drug, name, producer, price, recipe)
        self.__validator.validate(drug)
        self.__repository.create(drug)

    def remove_drug(self, id_drug):
        """
        Deletes a drug
        :param id_drug: id of the drug that need to be deleted
        """
        self.__repository.delete(id_drug)

    def update_drug(self, id_drug, name, producer, price, recipe):
        """
        Updates a drug
        :param id_drug:
        :param name:
        :param producer:
        :param price:
        :param recipe:
        :return:
        """
        if recipe == "da":
            recipe = True
        else:
            recipe = False
        drug = Drug(id_drug, name, producer, price, recipe)
        self.__validator.validate(drug)
        self.__repository.update(drug)

    def get_all(self):
        """
        :return: list of all the drugs
        """
        return self.__repository.read()

    def price_increase(self, percentage, val):
        list_drugs = self.get_all()
        for drug in list_drugs:
            if drug.price > val:
                drug.price = drug.price + drug.price*percentage/100
                self.__repository.update(drug)


    def sort_drugs_by_sales(self):
        list_drugs = self.get_all()
        x = self.number_of_sales()
        return list_drugs
