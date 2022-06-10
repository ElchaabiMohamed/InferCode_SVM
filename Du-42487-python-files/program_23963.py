class Employee(object):
	def __init__(self,name,number):
		self.name = name
		self.number = number

	def __str__(self):
		return "Name: {}\nNumber: {}\n".format(self.name,self.number)

	def wages(self):
		pass

class Manager(Employee):
	pass

class AssemblyWorker(Employee):#no comments
	def __init__(self,name,number,rate=0,hours=0):
		super().__init__(name,number)
		self.rate = rate
		self.hours

	def wages(self):
		pass

def main():
	print("Don't want to overwrite ca117 ver")
	p1 = Employee("Jake",1)
	p2 = AssemblyWorker("Nasus", 2)

	print(p1)
	while True:pass
if __name__ == "__main__":
	main()