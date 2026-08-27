class FileCalculator:
    def __init__(self, filename):
        self.filename =filename

    def read_number(self):
        try:
            with open(self.filename, "r") as file:
               number = file.read().split()
            return  number
        except FileNotFoundError:
            print("file not found")
            return []

    def convert_to_integer(self, value):
        try:
            int(value)
        except ValueError:
            print("not a valid int value")
            return None

    def divide(self,num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print("can't divide by zero ")
            return None


    def run(self):

        # Read file
        values = self.read_number()

        if len(values) < 2:
            print("Need at least two numbers.")
            return

        # Convert values to integers
        num1 = self.convert_to_integer(values[0])
        num2 = self.convert_to_integer(values[1])

        if num1 is None or num2 is None:
            return

        # Divide
        result = self.divide(num1, num2)

        if result is not None:
            print("Result:", result)


calculator = FileCalculator("numbers.txt")

calculator.run()