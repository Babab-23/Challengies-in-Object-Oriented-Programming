class IntegerToRoman:
    def __init__(self, number: int):
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number
    
    def convert(self) -> str:
        num = self.number
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        roman_string = ""
        for value, symbol in roman_numerals:
            while num >= value:
                roman_string += symbol
                num -= value
        
        return roman_string
    
    def __str__(self):
        return self.convert()

# Example Usage
if __name__ == "__main__":
    number = 1994
    converter = IntegerToRoman(number)
    print(f"{number} in Roman numerals is: {converter}")
