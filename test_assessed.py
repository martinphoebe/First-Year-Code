#testing document
import pytest
from assessed_lab_exercises import *

pytest.main()

#1_calculator.py
def test_calculator():
    #additon testing
    assert calculator(10, 5, "+")  == 15 # 15
    assert calculator(100, 5, "+")  == 105 # 105
    assert calculator(-1, 5, "+")  == 4 # 4

    #subtraction testing
    assert calculator(10, 5, "-")  == 5 # 5
    assert calculator(0, 5, "-")  == -5 # -5
    assert calculator(100, 20, "-")  == 80 # 5

    #multiplication testing
    assert calculator(10, 5, "*")  == 50  # 50
    assert calculator(10, 10, "*")  == 100  # 100
    assert calculator(-2, 5, "*")  == -10  # -10

    #division testing
    assert calculator(10, 0, "/")  == "Cannot divide by zero!" # "Cannot divide by zero!"
    assert calculator(10, 5, "/")  == 2.0 # 2.0

    #greater than testing
    assert calculator(10, 5, ">")  == True # True
    assert calculator(1, 5, ">")  == False # False

    #greater than or equal to testing
    assert calculator(5, 5, ">=")  == True # True

    #less than testing
    assert calculator(12, 5, "<") == False # False
    assert calculator(1, 5, "<=") == True # True

    #less than or equal to testing
    assert calculator(10, 5, "<=") == False # False
    assert calculator(10, 10, "<=") == True # True

    #invalid testing
    assert calculator(10, 5, "$")  == "Invalid Operator!" # "Invalid operator!"



#2_max_of_three.py
def test_max_of_three():
    assert max_of_three(10, 20, 30) == 30 # Output: 30
    assert max_of_three(5, 12, 8) == 12 # Output: 12



#3_winning_numbers.py
def test_winning_numbers():
    assert winning_numbers([5, 14, 17], [5, 14, 6]) == "Second" # Expected: "Second"
    assert winning_numbers([1, 2, 3], [1, 2, 3]) == "First" # Expected: "First"
    assert winning_numbers([4, 7, 9], [0, 7, 2]) == "Third" # Expected: "Third"
    assert winning_numbers([10, 20, 30], [0, 0, 0]) == "No" # Expected: "No"



#4_sum_of_evens.py
def test_sum_of_evens():
    assert sum_of_evens(12, 21) == 80
    assert sum_of_evens(11, 39) == 120
    #assert sum_of_evens(30, 100) == 2340



#5_calculate_average
def test_calculate_average():
    assert calculate_average([1, 4, 5, 6]) == 4
    assert calculate_average([1, 8, 9]) == 6



#6_calculate_weekly
def test_calculate_weekly_pay():
    assert calcualte_weekly_pay(30) == 360
    assert calcualte_weekly_pay(36) == 438



#7_is_prime
def test_is_prime():
    assert is_prime(21) == False
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(41) == True



#8_are_anagrams
def test_are_anagrams():
    assert are_anagrams("HEART" , "EARTH") == True
    assert are_anagrams("HELP" , "SELF") == False
    assert are_anagrams("LITTLE" , "LITLE") == False
    assert are_anagrams("heart" , "EARTH") == True
    assert are_anagrams("HEART" , "earth") == True



#9_count_vowels
def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Programming is interesting") == 8
    assert count_vowels("Are you okay?") == 6



#10_sort_list
def test_sort_list():
    assert sort_list([5, 6, 9, 0]) == [0, 5, 6, 9]
    assert sort_list([1, 2, 1]) == [1, 1, 2]
    assert sort_list([-1, 9, -10]) == [-10, -1, 9]



#11_sum_of_digits
def test_sum_of_digits():
    assert sum_of_digits(123) == 6 # 6 (1 + 2 + 3)
    assert sum_of_digits(4567) == 22 # 22 (4 + 5 + 6 + 7)
    assert sum_of_digits(0) == 0 # 0



#12_is_paildrome
    
#13_password_strength
    
#14_letter_grade
def test_letter_grade():

    data_input = [
    {"subject": "Math", "score": 90, "credits": 40},
    {"subject": "History", "score": 75, "credits": 20},
    {"subject": "English", "score": 60, "credits": 20},
    {"subject": "Science", "score": 85, "credits": 40},
    {"subject": "Art", "score": 50, "credits": 40}
    ]

    average, grade = letter_grade(data_input)

    assert average == 73.125 # Expected output: 73.125
    assert grade == "B" # Expected output: B



#15_maximum_gap
def test_maximum_gap():
    assert maximum_gap([1,5 ,600], [100 ,7, 3 , 29, 39]) == 597 #returns 597
    assert maximum_gap([1,5 ,600], [100 ,7, 3 , 602, 39]) == 601 # returns 601


#16_cipher_text
def test_cipher_text():

    text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
    key = 3

    assert cipher_text(text, key) == "Each error you make in programming is an opportunity to become a better developer!"



#17_net_annual_income
def test_net_annual_income():
    assert net_annual_income(60000) == 48568



#18_my_split
def test_my_split():
    assert my_split("apple,banana,orange", ",") == ["apple", "banana", "orange"]



#19_longest_repitition
def test_longest_repitition():
    assert longest_repetition("aaabbcaaa") == ('a', 3)
    assert longest_repetition("hellooooo") == ('o', 5)
    assert longest_repetition("banana") == ('b', 1)
    assert longest_repetition("abc") == ('a', 1)



#20_closest_pair_under_budget
def test_closest_pair_under_budget():
    items = [("tv", 300), ("mobile phone", 800), ("laptop", 600), ("headphones", 200)]
    budget1 = 1000
    
    assert closest_pair_under_budget(items, budget1) == ['mobile phone', 'headphones']

