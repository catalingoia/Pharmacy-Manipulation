from Domain.entity import Entity


class Transaction(Entity):
    """
    Transaction object
    """
    def __init__(self, id_transaction, id_drug, id_card, quantity, date):
        """
        Creates a Transaction
        :param id_transaction: int, the transaction id
        :param id_drug: int, the drug id
        :param id_card: int, the card id
        :param quantity: int, the quantity of the drug
        :param date: datetime,
        """
        super(Transaction, self).__init__(id_transaction)
        self.__id_drug = id_drug
        self.__id_card = id_card
        self.__quantity = quantity
        self.__date = date

    def __str__(self):
        return "{}/{}/{}/{}/{}".format(self.id_entity, self.__id_drug, self.__id_card,
                                                   self.__quantity, self.__date)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity

    @property
    def id_drug(self):
        return self.__id_drug

    @id_drug.setter
    def id_drug(self, new_id_drug):
        self.__id_drug = new_id_drug

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, new_id_card):
        self.__id_card = new_id_card

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date
