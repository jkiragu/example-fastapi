import pytest
from app.calculations import add, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def non_zero_bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected",[
    (3,2,5),
    (7,1,8),
    (12,4,16)
] )
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected


def test_bank_set_initial_amount(non_zero_bank_account):
    # bank_account = BankAccount(50)
    assert non_zero_bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    assert zero_bank_account.balance == 0

def test_withdrawal():
    bank_account = BankAccount(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50

def test_deposit():
    bank_account = BankAccount(80)
    bank_account.deposit(50)
    assert bank_account.balance == 130

def test_collect_interest():
    bank_account = BankAccount(100)
    bank_account.collect_interest()
    assert round(bank_account.balance) == 110

@pytest.mark.parametrize("deposited, withdrew, expected",[
    (200,100,100),
    (50,10,40),
    (1200,200,1000)
] )
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(non_zero_bank_account):
    with pytest.raises(InsufficientFunds):
        non_zero_bank_account.withdraw(200)