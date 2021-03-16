from Domain.drug_validator import DrugValidator
from Domain.card_validator import CardValidator
from Domain.transaction_validator import TransactionValidator
from Repository.generic_repository import GenericFileRepository
from Service.drug_service import DrugService
from Service.card_service import CardService
from Service.transaction_service import TransactionService
from UI.user_interface import Console

drug_repository = GenericFileRepository("medicamente.txt")
card_repository = GenericFileRepository("carduri_clienti.txt")
transaction_repository = GenericFileRepository("tranzactii.txt")

drug_validator = DrugValidator()
card_validator = CardValidator()
transaction_validator = TransactionValidator

drug_repository.read()
card_repository.read()
transaction_repository.read()

drug_service = DrugService(drug_repository,transaction_repository, drug_validator)
card_service = CardService(card_repository, card_validator)
transaction_service = TransactionService(transaction_repository, drug_repository, card_repository, transaction_validator)
console = Console(drug_service, card_service, transaction_service)
console.run_console()
