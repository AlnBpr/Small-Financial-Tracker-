# big=max(list)
# print(big)

#Tracking the best value
# def find_largest(numbers):
#     largest=numbers[0]
#     second_largest=None

#     for i in range(len(numbers)):
#         if numbers[i] > largest:
#             second_largest = largest
#             largest = numbers[i]
#         elif second_largest is None or numbers[i] > second_largest:
#                 second_largest = numbers[i]
        
#     return largest, second_largest

# list=[4,7,2,9,1]
# big_number=find_largest(list)
# print(big_number)


#tracking how many times something happens
# def count_target(numbers, target):
#      count=0
#      for i in range(len(numbers)):
#           if numbers[i] == target:
#             count+=1
#      return count
       

# list=[4,7,2,7,9,7,1]
# num=7
# n= count_target(list, num)
# print(f"{num} appears {n} times")


#adding only even numbers
# def total_even_numbers(numbers):
#     total=0
#     for i in range(len(numbers)):
#         if numbers[i] % 2==0:
#             total+=numbers[i]
#     return total

# list = [4,7,2,9,6,11]
# print(total_even_numbers(list))


#Searching for a target in a list #Linear seach #Worst case you have to check every item in the list. 
#Time complexity is O(n)

# def search_target(numbers, target):
#     for i in range (len(numbers)):
#         if numbers[i] == target:
#             return True
        
#     return False

# list = [4,7,2,9,6,11]
# num = 9
# print(search_target(list,num))


#FInd the index of a target 
# def find_index(numbers, target):
#     for i in range(len(numbers)):
#         if numbers[i]==target:
#             return i
#     return -1

# list=[4,7,2,9,6,11]
# num=5
# print(find_index(list,num))


#sets and removing duplicates.

# def unique_numbers(numbers):
#     seen=set()
#     result=[]
#     for i in range(len(numbers)):
#         if numbers[i] not in seen:
#             seen.add(numbers[i])
#             result.append(numbers[i])
#     return seen,result
    

# list_numbers=[4,7,2,7,9,4,1]
# num=(unique_numbers(list_numbers))
# print(f"The list Seen is: {num[0]}, the list Result is {num[1]}")


#count how many times each number appears.
#and return the most frequent number

# def appearing_numbers(numbers):
#     dict_num={}
#     for i in range(len(numbers)):
#         if numbers[i] in dict_num:
#             dict_num[numbers[i]]+=1
#         else:
#             dict_num[numbers[i]]=1
#     return dict_num

# list_of_numbers=[4,7,2,7,9,4,7]
# print(appearing_numbers(list_of_numbers))


#WRONG
# def appearing_numbers(numbers):
#     dict_num={}
#     for i in range(len(numbers)):
#         if numbers[i] in dict_num:
#             dict_num[numbers[i]]+=1
#         else:
#             dict_num[numbers[i]]=1
#     return dict_num

# def most_frequent_number(dict): #here needs to have a dictionary 
#     most_frequent=dict.keys(0)
#     highest_count=dict.values(0)
#     for i in range(len(dict)):
#         if dict.values(i) > highest_count:
#             highest_count = dict.values(i)
#             most_frequent=dict.keys(i)
#     return most_frequent

# list_of_numbers=[4,7,2,7,9,4,7]
# dictionary=appearing_numbers(list_of_numbers)
# print(dictionary)
# value=most_frequent_number(dictionary)
# print(f"The most frequent number that appear in the list is {value}")


#accessing through the keys and values 
# def appearing_numbers(numbers):
#     dict_num={}
#     for i in range(len(numbers)):
#         if numbers[i] in dict_num:
#             dict_num[numbers[i]]+=1
#         else:
#             dict_num[numbers[i]]=1
#     return dict_num

# def most_frequent_number(dict): 
#     most_frequent= None
#     highest_count=0
#     for i in dict:
#         if dict[i] > highest_count:
#             highest_count=dict[i]
#             most_frequent=i
#     return most_frequent    
        
# list_of_numbers=[4,7,2,7,9,4,7]
# dictionary=appearing_numbers(list_of_numbers)
# value=most_frequent_number(dictionary)
# print(f"The most frequent number that appear in the list is {value}")


#iterating 
# list=[10,20,30]

# it=iter(list)
# print(next(it))
# print(next(it))


#Numbers that appear more than once 
# def appearing_numbers(numbers):
#     dict_num={}
#     for i in range(len(numbers)):
#         if numbers[i] in dict_num:
#             dict_num[numbers[i]]+=1
#         else:
#             dict_num[numbers[i]]=1
#     return dict_num

# def most_frequent_number(dict): 
#     most_frequent= None
#     highest_count=0
#     for i in dict:
#         if dict[i] > highest_count:
#             highest_count=dict[i]
#             most_frequent=i
#     return most_frequent    

# def more_appearing_numbers(dict_num):
#     numbers=[]
#     for i in dict_num:
#         if dict_num[i]>1:
#             numbers.append(i)
#     return numbers
        
# list_of_numbers=[4,7,2,7,9,4,7]
# dictionary=appearing_numbers(list_of_numbers)
# value=most_frequent_number(dictionary)
# # print(f"The most frequent number that appear in the list is {value}")

# many_numbers=(more_appearing_numbers(dictionary))
# print(many_numbers)


#how many times a character appear 

# def character_appear(word):
#     l={}
#     for i in range(len(word)):
#         if word[i] in l:
#             l[word[i]]+=1
#         else:
#             l[word[i]]=1
#     return l

# text="programming"

# count=character_appear(text)
# print(count)


#how many vowels are in a string 

# def numbers_of_vowels(word):
#     vowels_list=["a","e","i","o","u"]
#     counter=0
#     for i in range(len(word)):
#         if word[i] in vowels_list:
#             counter+=1
#     return counter

# text="hello world"
# print(numbers_of_vowels(text))



#return string reversed 

# def return_string(word):
#     reversed_text=""
#     for i in range(len(word)-1,-1,-1):
#         reversed_text+=word[i]
#     return reversed_text

# text="computer"

# print(return_string(text))


#returning only unique numbers. SET topic 

# def return_unique_numbers(numbers):
#     set_numbers=set()
#     for i in range(len(numbers)):
#         set_numbers.add(numbers[i])
#     return set_numbers

# list_num=[4,7,2,7,9,4,2]

# print(return_unique_numbers(list_num))


#STACK
# def stack_numbers(numbers):
#     stack=[]
#     result=[]
#     for i in range(len(numbers)):
#         stack.append(numbers[i])
#     for i in range(len(stack)):
#         value=stack.pop()
#         result.append(value)
#     return result

# list_num=[4,7,2]
# print(stack_numbers(list_num))


#QUEUE

# def queue_numbers(numbers):
#     queue=[]
#     result=[]
#     for i in range(len(numbers)):
#         queue.append(numbers[i])
#     for i in range(len(queue)):
#         value=queue.pop(0)
#         result.append(value)
#     return result

# list_num=[4,7,2]
# print(queue_numbers(list_num))

#sorting without sort() or sorted()

# def sort_numbers(numbers):
#     working=numbers.copy()
#     sorted_list=[]

#     for _ in range(len(working)):
#         smallest=working[0]
#         for number in working:
#             if number<smallest:
#                 smallest=number
#         sorted_list.append(smallest)
#         working.remove(smallest)
        
#     return sorted_list


# original=[7,2,9,4,1]
# print(sort_numbers(original))


#opposite sorting 

# def opposite_sorted(numbers):
#     working=numbers.copy()
#     sorted_list=[]

#     for _ in range(len(working)):
#         largest=working[0]

#         for number in working:
#             if number>largest:
#                 largest=number
#         sorted_list.append(largest)
#         working.remove(largest)
#     return sorted_list

# original=[7,2,9,4,1]
# print(opposite_sorted(original))


#find whether two numbers in a list add up to a target.

# def find_target(numbers,num):

#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i]+numbers[j]==num:
#                 return [numbers[i], numbers[j]]

# list_num=[4,2,7,9]
# target=11
# print(find_target(list_num,target))


#BINARY

# def binary_target(numbers,num):
#     left=0
#     right=len(numbers)-1
#     while left <= right:
#         middle=(left+right)//2

#         if numbers[middle]==num:
#             return middle
#         elif num> numbers[middle]:
#             left=middle+1
#         else:
#             right=middle-1
        
#     return "target wasn't found"

# list_num=[1,2,4,7,9]
# target=7
# value=(binary_target(list_num,target))
# print(f"The number of the target is at index {value}")


#BASIC RECURSION 

# def count_down(number):
#     if number==0:
#         return
#     else:
#         print(number)
#         count_down(number-1)

# num=3
# count_down(num)

#BASIC RECURSION 2 

# def sum_count(n):
#     if n==0:
#         return 0
#     return n+sum_count(n-1)

# num=4
# print(sum_count(num))

#TASK 3 
from datetime import date
# from datetime import datetime
import json
# expenses=[]

def new_expense():
    while True:
        try:
            amount_spent=float(input("How much money you want to spend? Insert in numbers: "))
            break
        except ValueError:
            print(f"\n\nPlease only type in numbers.\n\n")
    category=input("What is the category? ")
    description=input("Description of the product? ")
    today= date.today()

    expense={}
    expense["Amount"]=amount_spent
    expense["Category"]=category.capitalize()
    expense["Description"]=description.capitalize()
    expense["Date"]=str(today)

    expenses.append(expense)

def view_expenses(expenses):
    for i in range(len(expenses)):
        print("-"*20)
        print(f"Expense {i+1}")
        for key in expenses[i]:
            print(f"{key}: {expenses[i][key]}")

def delete_expenses():
    if (len(expenses))==0:
        print(f"There are no expenses to delete.")
        return
    while True:
        while True:
            try:
                Number=int(input(f"\nWhat expense do you want to delete?\n{"-"*20}\n"))
                break
            except ValueError:
                print(f"\n\nPlease insert numbers between the existing expenses.\n\n")
        index=Number-1
        # for i in range(len(expenses)):
        if 0<=index<(len(expenses)):
            print("Found it!")
            print(f"\nRemoving...\n")
            print(f"Expense {Number}")
            for key in expenses[index]:
                print(f"{key}: {expenses[index][key]}")

            #expenses.remove(expenses[index])#or 
            expenses.pop(index)

            print(f"\nSuccesfully removed!\n")
            print(f"Remaining: {expenses}")
            break
        else:
            print(f"The number must be between 1 and {len(expenses)}.")

def calculate_spending():
    if len(expenses)==0:
        print("Nothing to show.")
        return

    total=0.0
    for index in range(len(expenses)):
        total+=expenses[index]["Amount"]
    print(f"Total amount spent is: {total}")

def edit_expense():
    if (len(expenses)) == 0:
        print("There are no expenses to edit.")
        return
    
    print(f"Remaining expenses: ")
    # for index in range (len(expenses)):
    #     print(f"Expense {index+1}")
    view_expenses(expenses)
    
    while True:
        try:
            answer=int(input(f"Choose what expenses to edit: "))
            number=answer-1
            if 0<=number<(len(expenses)):
                break
            else:
                print(f"Please insert a valid number among the remaining expenses.")
        except ValueError:
            print(f"Invalid input.")

    valid_field=["Amount","Category","Description"]
    while True:
        choice=input(f"Please choose what to edit: {', '.join(valid_field)}\n").capitalize()
        if choice in valid_field:
            break
        else:
            print("Not in the options listed.")
        
    if choice =="Amount":
        while True:
            try:
                change=float(input(f"Please enter the new amount: "))
                expenses[number][choice] = change
                break
            except ValueError:
                print(f"Incorrect or not recognized input.")
    else:
        change=input(f"Please enter the new information: ")
        expenses[number][choice] = change.capitalize()
    print(f"Change succesfully executed!")

def search_expenses():
    if (len(expenses))==0:
        print("There are no available expenses to search through.")
        return

    flag=False
    total=0.0
    word=input(f"Key to search: ").capitalize()
    for expense in expenses:
        if expense["Category"]==word:
            total=total + expense["Amount"]
            print(f"{"-"*20}")
            for key in expense:
                print(f"{key}: {expense[key]}")
            flag=True

    if flag:
        print(f"Total amount spent in this category is {total}")
    else:
        print("No results found.")
            
def save_file():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
def load_file():
    try:
        with open("expenses.json", "r") as file:
            load=json.load(file)
            return load
    except FileNotFoundError:
        print("No file available. Starting a new one.")
        return []

def monthly_statement():
    while True:
        year_date=input("Enter the year (YYYY): ")
        if year_date.isdigit() and len(year_date)==4:
            break
        print("Please insert a valid year.")
    while True:
        month_date=input("Enter the month in number (MM): ")
        if month_date.isdigit() and len(month_date)==2 and 1<=month_date<=12:
            break
        print("Please insert a valid month number.")

    total=0.0
    flag=False
    search_date=f"{year_date}-{month_date}"
    for expense in expenses:
        if expense["Date"][:7]==search_date:
            total+=expense["Amount"]
            flag=True
            print(f"{"-"*20}")
            for key in expense:
                print(f"{key}:{expense[key]}")

    if flag:
        print(f"\nResults amount for {search_date} is £{total}")
    else:
        print("\nResults not found")
            
def view_statistics():
    if len(expenses) == 0:
        print("There are no expenses to analyse.")
        return

    amounts=[]

    for expense in expenses:
        amounts.append(expense["Amount"])

    highest=max(amounts)
    lowest=min(amounts)
    total=sum(amounts)
    average=total/len(amounts)
    number=len(amounts)
    print(f"Highest expense among expenses is: £{highest:.2f},\nLowest amount among expenses is: £{lowest:.2f},\nTotal spending: £{total:.2f},\nAverage spent: £{average:.2f},\nQuantity of expenses: {number}")
    

expenses=load_file()

##MAIN
def main_start():
    while True:
        print(f"{"-"*20}\nWelcome\n{"-"*20} \nThis is the MENU section\n \n \n\n")
        while True:
            try:
                choice=int(input(f"Select the options:\n1.Add expense\n2.View expenses\n3.Delete expense\n4.Calculate total spending\n5.Editing expenses\n6.Searching expenses\n7.View monthly statement\n8.View statistics\n9.Exit\n{"-"*20}\n\n"))
                break
            except ValueError:
                print(f"\nPlease choose from the selection offered.\n\n{"-"*20}")
        if choice==1:
            print(f"\n\nYou chose 1.Add expense\n{"-"*20}")
            new_expense()
        elif choice==2:
            print(f"\n\nYou chose 2.View expenses\n{"-"*20}")
            view_expenses(expenses)
        elif choice==3:
            print(f"\n\nYou chose 3.Delete expense\n{"-"*20}")
            delete_expenses()
        elif choice==4:
            print(f"\n\nYou chose 4.Calculate total spending\n{"-"*20}")
            calculate_spending()
        elif choice==5:
            print(f"\nYou chose 5.Editing expenses\n{"-"*20}")
            edit_expense()
        elif choice==6:
            print(f"\nYou chose 6.Searching expenses\n{"-"*20}")
            search_expenses()
        elif choice==7:
            print(f"\nYou chose 7.View monthly statement\n{"-"*20}")
            monthly_statement()
        elif choice==8:
            print(f"\nYou chose 8.View statistics\n{"-"*20}")
            view_statistics()
        elif choice==9:
            save_file()
            print("\n\nExiting program...")
            break
        else:
            print(f"\n\nInvalid choice\n\n")
main_start()

# new_expense()
# view_expenses(expenses)
# print(expenses)



#My notes for understanding
# color=input("Color? ")
# expenses=[]
# expense={}
# expense["color"]=color
# expenses.append(expense)
# print(expenses)

# for i in range(len(expenses)):
#     print(f"Expense {i+1}")
#     for key in (expenses[i]):
#         print(f"{key}: {expenses[i][key]}")
