import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # montlhy payment, interest rate, loan amount

    print("Sending...")
    socket.send_string("50 .1 200")
    
    reply = socket.recv_string()
    
    print("Received reply: %s" % reply)

    socket.send_string("exit")
    print("sent")
    socket.close()

if __name__ == "__main__":
    main()
