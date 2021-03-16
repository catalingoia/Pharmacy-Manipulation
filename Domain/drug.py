from Domain.entity import Entity


class Drug(Entity):
    """
    Drug object
    """
    def __init__(self, id_drug, name, producer, price, recipe):
        """
        Creates a drug
        :param id_drug: int, the drug id
        :param name: string, the name
        :param producer: string, the producer
        :param price: int, the price of the drug(positive)
        :param recipe: bool
        """
        super(Drug, self).__init__(id_drug)
        self.__name = name
        self.__producer = producer
        self.__price = price
        self.__recipe = recipe

    def __str__(self):
        return "{}/{}/{}/{}/{}".format(self.id_entity, self.__name, self.__producer, self.__price, self.__recipe)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def producer(self):
        return self.__producer

    @producer.setter
    def producer(self, new_producer):
        self.__producer = new_producer

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def recipe(self):
        return self.__recipe

    @recipe.setter
    def recipe(self, new_recipe):
        self.__recipe = new_recipe