from Domain.cardClient import Card


class CardService:
    """
    Manage card logic
    """
    def __init__(self, repository, validator):
        """
        Creates a card service
        """
        self.__repository = repository
        self.__validator = validator

    def add_card(self, id_card, first_name, second_name, cnp, birth_date, signup_date):
        """
        Adds a card
        :param id_card: int, the card id
        :param first_name: string, the first name
        :param second_name: string, the second name
        :param cnp: int, the cnp of the person
        :param birth_date: date, the birth date of the person
        :param signup_date: date, the signup of the person
        """

        card = Card(id_card, first_name, second_name, cnp, birth_date, signup_date)
        self.__validator.validate(card)
        self.__repository.create(card)

    def remove_card(self, id_card):
        """
        Deletes a card
        :param id_card: id of the card that need to be deleted
        """
        self.__repository.delete(id_card)

    def update_card(self, id_card, first_name, second_name, cnp, birth_date, signup_date):
        """
        Updates a card
        :param id_card: int, the card id
        :param first_name: string, the first name
        :param second_name: string, the second name
        :param cnp: int, the cnp of the person
        :param birth_date: date, the birth date of the person
        :param signup_date: date, the signup of the person
        """
        card = Card(id_card, first_name, second_name, cnp, birth_date, signup_date)
        self.__validator.validate(card)
        self.__repository.update(card)

    def get_all(self):
        """
        :return: list of all the drugs
        """
        return self.__repository.read()

    def search_card(self, id_card, first_name, second_name, cnp, birth_date, signup_date):
        list_cards = self.get_all()
        for card in list_cards:
            if card.id_entity == id_card and card.name == first_name and card.second_name == second_name and\
                    card.cnp == cnp and card.birth_date == birth_date and card.signup_date == signup_date:
                return card

