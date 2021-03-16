from Domain.transaction import Transaction
import datetime


class TransactionService:
    """
    Manage drug logic
    """
    def __init__(self, transaction_repository, drug_repository, card_repository, validator):
        """
        Creates a drug service
        """
        self.__transaction_repository = transaction_repository
        self.__drug_repository = drug_repository
        self.__card_repository = card_repository
        self.__validator = validator

    def add_transaction(self, id_transaction, id_drug, id_card, quantity, date):
        """
        Adds a drug
        :param id_transaction: int, the drug id
        :param id_drug: string, the name
        :param id_card: string, the producer
        :param quantity: int, the price of the drug(positive)
        :param date: bool
        """
        if self.__drug_repository.read() is None:
            raise ValueError('Nu exista niciun medicament cu id-ul: ' + id_drug)
        drug = self.__drug_repository.read(id_drug)
        price = drug.price
        print(price)
        if self.__card_repository.read(id_transaction):
            if drug.price is True:
                price = drug.price + drug.price * 15 / 100
            else:
                price = drug.price + drug.price * 15 / 100
        price = price*quantity

        print("Pretul Transactiei este de " + str(price))

        transaction = Transaction(id_transaction, id_drug, id_card, quantity, date)
        self.__transaction_repository.create(transaction)

    def remove_transaction(self, id_transaction):
        """
        Deletes a drug
        :param id_transaction: id of the drug that need to be deleted
        """
        self.__transaction_repository.delete(id_transaction)

    def update_transaction(self, id_transaction, id_drug, id_card, quantity, date):
        """
        Updates a drug
        :param id_transaction:
        :param id_drug:
        :param id_card:
        :param quantity:
        :param date:
        :return:
        """
        transaction = Transaction(id_transaction, id_drug, id_card, quantity, date)
        self.__transaction_repository.update(transaction)

    def get_all(self):
        """
        :return: list of all the drugs
        """
        return self.__transaction_repository.read()

    def all_by_days(self, day1, day2):
        trans_to_print = []
        date_list = [day1 + datetime.timedelta(days=x) for x in range(0, (day2-day1).days)]
        transactions = self.get_all()
        for day in date_list:
            for transaction in transactions:
                if transaction.date == day:
                    trans_to_print.append(transaction)
        return trans_to_print

    def del_days(self, day1, day2):
        for transaction in self.get_all():
            date = datetime.strptime(transaction.date, "%d-%m-%Y")
            if day1 <= date <= day2:
                self.__transaction_repository.delete(transaction.id_entity)
