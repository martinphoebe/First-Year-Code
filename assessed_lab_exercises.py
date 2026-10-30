#1_calculator.py

def calculator(num1,num2,operator):

    if(type(num1) != int | type(num2) != int):
        print("Invalid input.")
    else:
        #addition
        if operator == "+":
            result = (num1+num2)
            return result

        #subtraction
        elif operator == "-":
            result = (num1-num2)
            return result

        #multiplicaiton
        elif operator == "*":
            result = (num1*num2)
            return result

        #division
        elif operator == "/":
            if num2 == 0:
                return "Cannot divide by zero!"
            else:
                result = (num1/num2)
            return result

        #modulo
        elif operator == "%":
            result = (num1%num2)
            return result

        #greater than
        elif operator == ">":
            if num1 > num2:
                return True
            else:
                return False

        #greater than or equal to
        elif operator == ">=":
            if num1 >= num2:
                return True
            else:
                return False

        #less than
        elif operator == "<":
            if num1 < num2:
                return True
            else:
                return False
        #less than or equal to
        elif operator == "<=":
            if num1 <= num2:
                return True
            else:
                return False
        else:
            return "Invalid Operator!"


'''print(calculator(10, 5, "+"))   # 15
print(calculator(10, 5, "-"))   # 5
print(calculator(10, 5, "*"))   # 50
print(calculator(10, 0, "/"))   # "Cannot divide by zero!"
print(calculator(10, 5, "/"))   # 2.0
print(calculator(10, 5, ">"))   # True
print(calculator(10, 5, "<="))  # False
print(calculator(10, 5, "$"))   # "Invalid operator!"'''



#2_max_of_three.py

def max_of_three(num1,num2,num3):

    if (type(num1) != int | type(num2) != int | type(num3) != int):
        print("Invalid Input.")
    else:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        elif num3 > num1 and num3 > num2:
            return num3
    

'''print(max_of_three(10, 20, 30))# Output: 30
print(max_of_three(5, 12, 8)) # Output: 12'''


#3_winning_numbers.py

def winning_numbers(winning_list, guessed_list):
    
    count = 0

    #checks to see if input is equal to a winning list
    if guessed_list[0] == winning_list[0]:
        count = count + 1
    if guessed_list[1] == winning_list[1]:
        count = count + 1
    if guessed_list[2] == winning_list[2]:
        count = count + 1

    if count == 1:
        return"Third"
    elif count == 2:
        return"Second"
    elif count == 3:
        return"First"
    elif count == 0:
        return"No"

'''print(winning_numbers([5, 14, 17], [5, 14, 6])) # Expected: "Second"
print(winning_numbers([1, 2, 3], [1, 2, 3])) # Expected: "First"
print(winning_numbers([4, 7, 9], [0, 7, 2])) # Expected: "Third"
print(winning_numbers([10, 20, 30], [0, 0, 0])) # Expected: "No"'''



#4_sum_of_evens.py

def sum_of_evens(min_num, max_num):

    if (type(min_num) != int | type(max_num) != int):
        print("Invalid input.")
    else:
        total = 0

        for i in range(min_num, max_num +1 ):
            if i % 2 == 0:
                total = total + i

        return total




#5_calculate_average.py

def calculate_average(list_average):

    total = 0
    average = 0 
    counter = 0

    for i in list_average:
        total += int(i)
        counter += 1
        
    average = total / counter

    return average



#6_calculate_weekly_pay.py

def calcualte_weekly_pay(number_of_hours_worked):

    if (type(number_of_hours_worked) != int):
        print("Invalid input.")
    else:
        #constant values
        base_hours = 35
        base_pay = 12
        overtime_pay = 18
        
        #checks to see if hours worked <= base hours
        if number_of_hours_worked <= base_hours:
            total = number_of_hours_worked * base_pay
        elif number_of_hours_worked > base_hours:
            overtime = (number_of_hours_worked - base_hours) * overtime_pay
            total = (base_hours * base_pay) + overtime

        return(total)




#7_is_prime.py

def is_prime(number):

    if (type(number) != int):
        return("Invalid Input.")
    else:
        #positive number only
        if number <= 1:
            return(False)
        
        else:
            is_prime = True

            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    is_prime = False
            return(is_prime)




#8_are_anagrams.py

def are_anagrams(word1 , word2):

    if (type(word1) != str | type(word2) != str):
        return("Invalid Input.")
    else:
        #converts user input to be lowercase so the words can be compared
        input1 = word1.lower()
        input2 = word2.lower()

        #checks to see if words have same letters
        if sorted(input1) == sorted(input2):
            return(True)
        else:
            return(False)



#9_count_vowels.py

def count_vowels(word):

    if (type(word) != str):
        print("Invalid Input.")
    else:
        text = word.lower()
        
        count = 0

        #check for vowels, adds 1 to counter if vowel found
        for i in text:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count += 1

        if count == 0:
            return("There are no vowels.")
        else:
            return(count)




#10_sort_list.py

def sort_list(user_list):

    #converts input to integer
    user_list = [int(i) for i in user_list]

    number = len(user_list)

    #bubble sort
    for i in range(number-1):
        for j in range(number-i-1):
            if user_list[j] > user_list[j+1]:
                user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
    return(user_list)
                                                                                                                       



#11_sum_of_digits

def sum_of_digits(num):
    if (type(num) != int):
        return("Invalid Input.")
    else:
        total = 0
        
        num = list(map(int, str(num)))

        return total




#12_is_palindrome

def is_palindrome(text):
    if (type(text) != str):
        return("Invalid Input.")
    else:
        i, j = 0, len(text) - 1

        palindrome = True

        #checks to see if the input is palindrome, compares letters from either end 
        while i < j:
            if text[i] != text[j]:
                palindrome = False

            i += 1
            j -= 1

        if palindrome:
            return("It is a palindrome")
        else:
            return("Not a palindrome")




#13_password_strength

def password_strength(password):

    #special character store
    special_characters = {'@' , '$', '£'}
    count_special = 0

    #upper character store
    upper_character = 0

    for i in password:
        if i in special_characters:
            count_special += 1 #checks to see if password contains a special character
        if i.isupper():
            upper_character += 1 #checks to see if password contains an uppercase
        
    if len(password) < 6 or count_special == 0 or upper_character == 0:
        return("Weak")
    elif 6 <= len(password) <= 10 and count_special >0 and upper_character >0:
        return("Medium")
    elif len(password) > 10 and count_special > 0 and upper_character > 0:
        return("Strong")



#14_letter_grade

def letter_grade(subjects):

    #counters
    total_score = 0
    total_credit = 0

    for subject in subjects:
        grade = subject["score"]
        credits = subject["credits"]
        total_score += grade * credits
        total_credit += credits

        
    #stops division by 0, 0 is automatically a fail
    if total_credit == 0:
        return ("F")

    average = total_score / total_credit

    if average < 50:
        grade_letter = "F"
    elif 50 <= average < 60:
        grade_letter = "D"
    elif 60 <= average < 70:
        grade_letter = "C"
    elif 70 <= average < 90:
        grade_letter = "B"
    else:
        grade_letter = "A"

    return (average, grade_letter)




#15_maximum_gap

def maximum_gap(list1, list2):

    max1 = max(list1)
    min1 = min(list1)

    max2 = max(list2)
    min2 = min(list2)

    gap1 = abs(max1 - min2)
    gap2 = abs(max2 - min1)

    return max(gap1, gap2)




#16_cipher_text

def cipher_text(cipher_text, key):

    #opens the string
    decrypted_code = ""

    for i in cipher_text:
        ascii_code = ord(i)
        changed_code = (ascii_code - key) % 256

        #concatenates the character to the end of the string
        decrypted_code += chr(changed_code)

    return decrypted_code



#17_net_annual_income

def net_annual_income(gross_salary):

    if (type(gross_salary) != int):
        return("Invalid Input.")
    else:
        #uk tax thresholds
        #limits show the next band i.e., basic limit goes into the next band of higher
        personal_allowance = 12750
        basic_rate_limit = 50270
        higher_rate_limit = 125140

        total_tax = 0

        #taxable income - income over personal allowance
        tax_income = max(0, gross_salary - personal_allowance)

        # 20% tax - basic band
        if gross_salary > personal_allowance:
            basic_band = min(tax_income, basic_rate_limit - personal_allowance)
            total_tax += basic_band * 0.20

        # 40% tax - higher band
        if gross_salary > basic_rate_limit:
            higher_band = min(tax_income - (basic_rate_limit - personal_allowance), higher_rate_limit - basic_rate_limit)
            total_tax += higher_band * 0.40

        # 45% tax - additional band
        if gross_salary > higher_rate_limit:
            additional_band = gross_salary - higher_rate_limit
            total_tax += additional_band *0.45

        net_income = gross_salary - total_tax 
        return(net_income)



#18_my_split

def my_split(s, sep):
   
    j = 0

    #opens output
    output = []

    #looks at whole input, first to last index
    for i in range (len(s)):
        if s[i] == sep:
            output.append(s[j:i])
            j = i + 1
    output.append(s[j:]) #looks at whole of output, no end index
    return output

'''print(my_split("apple,banana,orange", ","))'''


#19_longest_repitition

def longest_repetition(text):

    if (type(text) != str):
        return("Invalid Input.")
    else:
        #max letter repition count
        repititions = 1

        #letter most repeated
        letter = text[0]

        #current letter count
        count = 1


        for i in range (1, len(text)):
            if text[i] == text[i-1]: #checks whole length of text
                count += 1
                if count > repititions:
                    repititions = count
                    letter = text[i]

            else:
                count = 1

        return letter , repititions

'''print(longest_repetition("aaabbcaaa"))
print(longest_repetition("hellooooo"))
print(longest_repetition("banana"))
print(longest_repetition("abc"))'''



#20_closest_pair_under_budget

def closest_pair_under_budget(items, budget):

    pair = None
    within_budget_total = 0

    for i in range (len(items)):
        for j in range(i + 1, len(items)):
            total = items[i][1] + items[j][1]

            if total <= budget and total > within_budget_total:
                best_total = total
                pair = (items[i][0], items[j][0])

    return pair, within_budget_total

#budget = 1000
#items = [("tv", 300), ("mobile phone", 800), ("laptop", 600), ("headphones", 200)]
#print(closest_pair_under_budget(items, budget))
