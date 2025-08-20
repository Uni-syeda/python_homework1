# Write your code here.
#Task 1: Hello
#Write a hello function that takes no arguments and returns Hello!. 
#  Now, what matters here is what the function returns.  
# You can print() whatever you want for debugging purposes, 
# but the tests ignore that, and only check the return value.

print("********************TASK1**************")

def hello():
    print("Hello")

hello()


print("********************TASK2**************")
#Task 2: Greet with a Formatted String
#Write a greet function.  It takes one argument,
#  a name, and returns Hello, Name!. 
#  Use a formatted string.  Note that you have to return exactly the right string or the test fails -- 
# but PyTest tells you what didn't match.

def greet(name):
    print("Hello , " + name + "!")
greet("Shakera")

print("********************TASK3**************")
def calc(x, y, z="multiply"): 
    try:
        match z:
            case "add":
                result = x + y
                print("Addition: ", result)
                return result
            case"subtract":
                result = x - y
                print("Subtract: ", result)
                return result
            case "multiply":
                result = x * y
                print("Multiply: ", result)
                return result
            case "divide":
                result = x / y
                print("Divide: ", result)
                return result
            case "modulo":
                result = x % y
                print("Modulo: ", result)
                return result
            case "int_divide":
                result = x // y
                print("Int_divide: ", result)
                return result  
            case "power":
                result = x ** y
                print("Power: ", result)
                return result
            case _:
                print("Invalide operation")
                return "Invalid operation!"
    except ZeroDivisionError:
        print("You can't divide by 0!")
        return "You can't divide by 0!"
    except TypeError:
        print("You can't multiply those values!")
        return "You can't multiply those values!"

# Test calls
calc(5, 2, "add")
calc(12, 4, "subtract")
calc(2, 3, "multiply")
calc(10, 5, "divide")
calc(8, 3, "modulo")
calc(10, 3, "int_divide")
calc(2, 3, "power")
calc(10, 0, "divide")       # triggers ZeroDivisionError
calc(7, 0, "modulo")        # triggers ZeroDivisionError
calc(5, 2, "xyz")           # invalid operation
calc("hello", "world", "subtract")

print("********************TASK4**************")

def data_type_conversion(value, name):
    try:
        if name == "float":
            result = float(value)
            print(result)
            return result
        elif name == "str":
                result = str(value)
                print(result)
                return result
        elif name == "int":
                result = int(value)
                print(result)
                return result
        else:
             print("Invalid conversion!")
    except ValueError:
        print(f"You can't convert {value} into a {name}.")

        return f"You can't convert {value} into a {name}."

data_type_conversion("5", "int")
data_type_conversion("5", "float")
data_type_conversion("5", "str")
data_type_conversion("5", "abc")
data_type_conversion("nonsense", "float")


print("********************TASK5*************")

def grade(*args):
    try: 
        average = sum(args) / len(args)
        if average >=90:
            return "A grade"
        elif 80 <=average <89:
            return "B grade"
        elif 70 <=average <79:
            return "C grade"
        elif 60 <=average <69:
            return "D grade"
        else:
            return "F grade"
    except:
        return "Invalid data was provided."

print(grade(100, 90, 80))     # A
print(grade(85, 88, 82))      # B
print(grade(72, 70, 78))      # C
print(grade(65, 62, 68))      # D
print(grade(40, 55, 50))      # F
print(grade(50, "oops", 80))  # Invalid data was provided.

print("********************TASK6************")
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result
s1 = repeat("Manha ",5)
print(s1)

print("********************TASK7***********")
def student_scores(choice, **kwargs):
    if choice == "best":
        best_student = max(kwargs, key=kwargs.get)
        return f"{best_student} with score {kwargs[best_student]}"
    elif choice == "mean":
        mean_score = sum(kwargs.values()) / len(kwargs)
        return f"Average score is {mean_score:.2f}"
    else:
        return "Invalid choice"

print(student_scores("best", Ali=90, Sara=85, John=78))
print(student_scores("mean", Ali=90, Sara=85, John=78))

print("********************TASK8**********")
def titleize(input_string):
    # Define little words that shouldn't be capitalized (unless first or last)
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    # Split the input string into a list of words
    words = input_string.split()

    for i, word in enumerate(words):
        # Always capitalize the first and last word
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        else:
            # If the word is in little_words, keep it lowercase
            if word.lower() in little_words:
                words[i] = word.lower()
            else:
                words[i] = word.capitalize()

    return " ".join(words)


print(titleize("The Secret of Success is Hard Work"))

print("********************TASK9*********")
def hangman(secret,guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result

print(hangman("alphabet", "ab"))   
print(hangman("hangman", "aeiou")) 
print(hangman("python", "xyz"))   

print("********************TASK10**********")
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()  
    pig_words = []

    for word in words:
        # Case 1: word starts with a vowel
        if word[0] in vowels:
            pig_word = word + "ay"

        # Case 2: word starts with "qu"
        elif word[:2] == "qu":
            pig_word = word[2:] + "quay"

        # Case 3: word starts with consonant(s)
        else:
            # Find the index of the first vowel
            for i, char in enumerate(word):
                if char in vowels:
                    break
            # Move consonant cluster to the end and add "ay"
            pig_word = word[i:] + word[:i] + "ay"

        pig_words.append(pig_word)

    # Join the list of words back into a sentence
    return " ".join(pig_words)

print(pig_latin("apple"))            
print(pig_latin("hello"))            
print(pig_latin("quick brown fox")) 
