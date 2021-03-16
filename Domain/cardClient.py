from Domain.entity import Entity


class Card(Entity):
    """
    Card Client object
    """
    def __init__(self, id_card, first_name, second_name, cnp, birth_date, signup_date):
        """
        Creates a card
        :param id_card: int, the card id
        :param first_name: string, the first_name
        :param second_name: string, the second_name
        :param cnp: int, the cnp of the person(unique)
        :param birth_date: datetime, the birth date of the person
        :param signup_date: datetime, the signup date of the person
        """
        super(Card, self).__init__(id_card)
        self.__first_name = first_name
        self.__second_name = second_name
        self.__cnp = cnp
        self.__birth_date = birth_date
        self.__signup_date = signup_date

    def __str__(self):
        return "{}/{}/{}/{}/{}/{}".format(self.id_entity, self.__first_name, self.__second_name, self.__cnp,
                                          self.__birth_date, self.__signup_date)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @property
    def second_name(self):
        return self.__second_name

    @second_name.setter
    def second_name(self, new_second_name):
        self.__second_name = new_second_name

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, new_cnp):
        self.__cnp = new_cnp

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date

    @property
    def signup_date(self):
        return self.__signup_date

    @signup_date.setter
    def signup_date(self, new_birth_date):
        self.__signup_date = new_birth_date