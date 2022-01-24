#BankAccount:
# owner: string
# balance: float
# withdraw
# deposit

class BankAccount:
	def __init__(self,owner,balance,product):
		self.owner = owner
		self.__balance = balance
		self.product = product

	# decorators will be discussed in next topics, but
	# what we do here is telling python that balance()
	# method is a "getter", i.e. when using obj.balance
	# the method balance() will be called
	@property
	def balance(self):
		return self.__balance

	def withdraw(self,amount):
		# log in database when the balance is changed
		self.__balance -= amount

	def deposit(self, amount):
		# log in database when the balance is changed
		self.__balance += amount

	def __str__(self):
		return f"""BankAccount:
		 owner = {self.owner}
		 balance = {self.__balance}
		"""


# instantiate objects:
maria_account = BankAccount("Maria", 1_300, 'current')
pesho_account = BankAccount("Pesho", 100, 'deposit')

print(maria_account.balance)
print(maria_account)

# use objects:
maria_account.withdraw(1000)
print(maria_account.balance)

# change directly maria's balance:
# maria_account.__balance = 2_000_000;
# maria_account._BankAccount__balance = 1_000_000;
print(maria_account)


print(dir(maria_account))
print('~'*30)
print(maria_account.__dict__)

print(id(maria_account))
print(id(pesho_account))
print(id(BankAccount))

