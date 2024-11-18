import zmq

def main():
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://*:5555")
	
	print("Receiver started. Waiting for message...")

	while True:
		message = socket.recv_string()
		if message == "exit":
			print("Exiting...")
			break
		print("Received message: %s" % message)
		# assuming the messages are received in the order: monthly payment, interest rate, loan amount

		monthly_payment, interest_rate, loan_amount = message.split(" ")
		months = loan_calculator(float(monthly_payment), float(interest_rate), float(loan_amount))
		print("Months needed to pay off the loan: %d" % months)
		socket.send_string(str(months))

	socket.close()


# calculate the number of months needed to pay off a loan, based on the monthly payment, interest rate, and loan amount
def loan_calculator(monthly_payment, interest_rate, loan_amount):
	months = 0
	remaining_amount = loan_amount
	while remaining_amount > 0:
		interest = remaining_amount * interest_rate
		remaining_amount = remaining_amount + interest - monthly_payment 
		months += 1
		if remaining_amount > loan_amount: # handle error case where loan amount is too low to pay off, it will return -1
			months = -1
			break
	return months
	



if __name__ == "__main__":
	main()