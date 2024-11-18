import subprocess

def main():
	subprocess.Popen(["python.exe", "sender.py"])
	subprocess.Popen(["python.exe", "receiver.py"])

if __name__ == "__main__":
	main()