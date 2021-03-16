from datetime import datetime

class Console:
    def __init__(self, drug_service, card_service, transaction_service):
        self.__drug_service = drug_service
        self.__card_service = card_service
        self.__transaction_service = transaction_service

    def __show_menu(self):
        print("1.Medicamente")
        print("2.Card Client")
        print("3.Tranzactii")
        print("x.Exit")

    def run_console(self):
        while True:
            self.__show_menu()
            op = input("Optiune:")
            if op == '1':
                self.__show_drugs()
            if op == '2':
                self.__show_cards()
            if op == '3':
                self.__show_transactions()
            elif op == 'x':
                break
            else:
                print("Comanda invalida")

    def __show_drugs(self):
        while True:
            self.__show_menu_drugs()
            op1 = input("Optiune:")
            if op1 == "1":
                self.__handle_drug_add()
            elif op1 == "2":
                self.__handle_drug_delete()
            elif op1 == "3":
                self.__handle_drug_update()
            elif op1 == "4":
               self.__handle_sort_drugs_by_sales()
            elif op1 == "5":
                self.__handle_drug_increase()
            elif op1 == "6":
                print(self.__handle_drug_search())
            elif op1 == "7":
                print(self.__drug_service.number_of_sales())
            elif op1 == "a":
                self.__show_list(self.__drug_service.get_all())
            elif op1 == 'b':
                break
            else:
                print("Comanda invalida")

    def __show_cards(self):
        while True:
            self.__show_menu_cards()
            op1 = input("Optiune:")
            if op1 == "1":
                self.__handle_card_add()
            elif op1 == "2":
                self.__handle_card_delete()
            elif op1 == "3":
                self.__handle_card_update()
            elif op1 == "4":
                print(self.__handle_card_search())
            elif op1 == "a":
                self.__show_list(self.__card_service.get_all())
            elif op1 == 'b':
                break
            else:
                print("Comanda invalida")

    def __show_transactions(self):
        while True:
            self.__show_menu_transactions()
            op1 = input("Optiune:")
            if op1 == "1":
                self.__handle_transaction_add()
            elif op1 == "2":
                self.__handle_transaction_delete()
            elif op1 == "3":
                self.__handle_transaction_update()
            elif op1 == "4":
                print(self.__handle_card_search())
            elif op1 == "5":
                print(self.__handle_transaction_all_by_days())
            elif op1 == "6:":
                self.__handle_transaction_del_days()
            elif op1 == "a":
                self.__show_list(self.__transaction_service.get_all())
            elif op1 == 'b':
                break
            else:
                print("Comanda invalida")


    def __show_menu_drugs(self):
        print('MEDICAMENTE')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Afisare medicamente dupa vanzari')
        print("5. Scumpire medicament cu un procentaj dat")
        print("6. Cautare medicament")
        print('a. Afisare')
        print('b. Back')

    def __show_menu_cards(self):
        print('CARDURI CLIENTI')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('a. Afisare')
        print('b. Back')

    def __show_menu_transactions(self):
        print('TRANZACTII')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare')
        print('5. Afisarea tranzactilor dintr-un interval dat de zile')
        print("6. Stergerea tuturor tranzactiilor dintr-un interval de zile dat")
        print('a. Afisare')
        print('b. Back')

    def __handle_transaction_del_days(self):
        try:
            day1 = datetime.strptime(input("Intervalul sa inceapa din :"),
                                   "%d-%m-%Y")
            day2 = datetime.strptime(input("Si sa se termine in:"),
                                     "%d-%m-%Y")
            self.__transaction_service.del_days(day1, day2)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)

    def __handle_drug_add(self):
        try:
            id_drug = int(input("ID-ul:"))
            name = input("Numele:")
            producer = input("Producatorul:")
            price = int(input("Pretul:"))
            recipe = input("Reteta (da sau nu):")
            self.__drug_service.add_drug(id_drug, name, producer, price, recipe)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Medicament adaugat cu succes")

    def __handle_drug_delete(self):
        try:
            id_drug = int(input("ID-ul medicamentului de sters:"))
            self.__drug_service.remove_drug(id_drug)
        except ValueError as ve:
            print("Erori")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Medicament sters cu succes")

    def __handle_drug_update(self):
        try:
            id_drug = int(input("ID-ul medicamentului de modificat:"))
            name = input("Noul nume:")
            producer = input("Noul producator:")
            price = float(input("Noul pret:"))
            recipe = input("Noua reteta (da sau nu):")
            self.__drug_service.update_drug(id_drug, name, producer, price, recipe)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Medicament modificat cu succes")

    def __handle_drug_search(self):
        try:
            id_drug = int(input("ID-ul:"))
            name = input("Numele:")
            producer = input("Producatorul:")
            price = float(input("Pretul:"))
            recipe = input("Reteta (da sau nu):")
            return self.__drug_service.search_drug(id_drug, name, producer, price, recipe)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)

    def __handle_card_search(self):
        try:
            id_card = int(input("ID-ul:"))
            first_name = input("Nume:")
            second_name = input("Prenume:")
            cnp = int(input("CNP:"))
            birth_date = input("Data nasterii:")
            signup_date = input("Data inregistrare:")
            self.__card_service.search_card(id_card, first_name, second_name, cnp, birth_date, signup_date)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)

    def __handle_drug_increase(self):
        try:
            percentage = int(input("Procentajul dorit pentru scumpire: "))
            val = int(input("Pretul minim al medicamentelor :"))
            self.__drug_service.price_increase(percentage, val)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Medicamente scumpite cu succes")

    def __handle_sort_drugs_by_sales(self):
        self.__drug_service.sort_drugs_by_sales()

    def __handle_card_add(self):
        try:
            id_card = int(input("ID-ul:"))
            first_name = input("Nume:")
            second_name = input("Prenume:")
            cnp = int(input("CNP:"))
            birth_date = input("Data nasterii:")
            signup_date = input("Data inregistrare:")
            self.__card_service.add_card(id_card, first_name, second_name, cnp, birth_date, signup_date)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Card adaugat cu succes")

    def __handle_card_delete(self):
        try:
            id_card = int(input("ID-ul cardului de sters:"))
            self.__card_service.remove_card(id_card)
        except ValueError as ve:
            print("Erori")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Card sters cu succes")

    def __handle_card_update(self):
        try:
            id_card = int(input("ID-ul cardului de modificat:"))
            first_name = input("Noul nume:")
            second_name = input("Noul prenume:")
            cnp = int(input("Noul CNP:"))
            birth_date = input("Noua data de nastere:")
            signup_date = input("Noua data de inregistrare")
            self.__card_service.update_card(id_card, first_name, second_name, cnp, birth_date, signup_date)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Medicament modificat cu succes")

    def __handle_transaction_add(self):
        try:
            id_transaction = int(input("ID-ul:"))
            id_drug = int(input("ID medicament:"))
            id_card = input("ID card:")
            quantity = int(input("Numar bucati:"))
            date = input("Data inregistrare:")
            self.__transaction_service.add_transaction(id_transaction, id_drug, id_card, quantity, date)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Tranzactie adaugat cu succes")

    def __handle_transaction_delete(self):
        try:
            id_transaction = int(input("ID-ul tranzictiei de sters:"))
            self.__transaction_service.remove_transaction(id_transaction)
        except ValueError as ve:
            print("Erori")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Tranzactie sters cu succes")

    def __handle_transaction_update(self):
        try:
            id_transaction = int(input("ID-ul tranzactiei de modificat:"))
            id_drug = int(input("ID medicament:"))
            id_card = int(input("ID card:"))
            quantity = input("Numar bucati:")
            date = input("Data inregistrare:")
            self.__transaction_service.update_transaction(id_transaction, id_drug, id_card, quantity, date)
        except ValueError as ve:
            print("Erori:")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Medicament modificat cu succes")

    def __handle_transaction_all_by_days(self):
        try:
            day1 = datetime.strptime(input("Intervalul sa inceapa din :"),
                                     "%d-%m-%Y")
            day2 = datetime.strptime(input("Si sa se termine in:"),
                                     "%d-%m-%Y")
            self.__transaction_service.all_by_days(day1, day2)
        except ValueError as ve:
            print("Erori")
            for error in ve.args[0]:
                print(error)
        finally:
            print("Comanda realizata cu succes")

    def __show_list(self, objects):
        for object in objects:
            print(object)




