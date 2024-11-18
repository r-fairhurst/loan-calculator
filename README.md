# loan-calculator
This program will calculate how long it will take for a loan to be paid off based on the input of a monthly payment, interest rate, and loan amount.

## Request a loan calculation by sending a message over zeromq

```python
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# montlhy payment, interest rate, loan amount
print("Sending...")
socket.send_string("50 .1 200")
```

## Receive the amount of months it will take to pay it off back

```python
reply = socket.recv_string()
print("Received reply: %s" % reply)
socket.send_string("exit")
print("sent")
socket.close()
```

## The loan calculator will receive the message and return the months as a string, but is really an int
```python
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
```

# Communication Contract

A.  This microservice is for Kylan Jagels

B.  This microservice is fully finished

C. N/A

D. Microservice should be ran locally, however it can receive messages from anywhere as long as it communicates to the correct port/IP address, you just have to change them

E. If my teammates cannot access or call my microservice they should reach out over discord if any issues show up, I will try and troubleshoot/fix/address them that same day

F. Preferably as soon as they find an issue, and lets just say by the end of November for the latest

G. The only thing I worry about is the port-port connection, I just have it hardcoded as 5555 for now, this can be easily changed later


# UML Sequence diagram

