# Augment the increase_balance function with log functionality
def log_decorator(f):
	def foo():
		print('logging')
		f()

	return foo


@log_decorator
def increase_balance():
	print('balance is increased')


# increase_balance = log_decorator(increase_balance)

increase_balance()
increase_balance()
increase_balance()


# 'logging'
# 'balance is increased'