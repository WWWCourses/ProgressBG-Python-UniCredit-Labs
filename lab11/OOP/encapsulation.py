class BankAccount:
	def __init__(self, owner, balance) :
		self.__balance = 0
		self.owner = owner

	def validate_balance(self, balance):
		if( balance>=0 ):
			return True
		else:
			return False

	# implent balance setter
	@property
	def balance(self):
		print('balance is get')
		return self.__balance

	# implent balance setter
	@balance.setter
	def balance(self, balance):
		if self.validate_balance(balance):
			self.__balance = balance
		else:
			self.__balance = 0

	def __repr__(self):
		return f'owner:{self.owner}\nbalance:{self.__balance}'


maria_account = BankAccount("Maria", 1_300)
print(maria_account)

# maria_account.balance = -1_000_000
# maria_account.set_balance(-1_000_000)
maria_account.balance = -1_000_000
print( maria_account )

# print( maria_account.get_balance())
print( maria_account.balance )


# maria_account._BankAccount__balance = -9999999999
# print(maria_account._BankAccount__balance)

maria_account.__balance = 88888888;

print(maria_account.__dict__)
print(dir(maria_account))


# owner:Maria
# balance:0