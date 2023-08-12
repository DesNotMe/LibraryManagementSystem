import re
import os
import csv
import atexit

# Manage customer request


class Books:
    def sort(self):
        displaymenu()


class Customer:
    customer_count = 0  # Class variable to keep track of customer IDs

    def __init__(self, name, email, gender, age, tier, points):
        self.name = name
        self.email = email
        self.gender = gender
        self.age = age
        self.tier = tier
        self.points = points

        Customer.customer_count += 1
        self.customer_id = f"\033[91mS{Customer.customer_count}\033[0m"

    def sort(self):
        main2()


class CustomerRequest():
    def __init__(self, customer_id, request_description):
        self.customer_id = customer_id
        self.request_description = request_description


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None


records2 = [{"Customer_ID": 'S111',
             "Name": "Johnny", "Email": "jtan@gmail.com", "Gender": "M", "Age": 13, "Tier": "C", "Points": 2000},
            {"Customer_ID": 'S222',
             "Name": "Rachel", "Email": "rwong@gmail.com", "Gender": "F", "Age": 17, "Tier": "B", "Points": 4000},
            {"Customer_ID": 'S333',
             "Name": "Mervyn", "Email": "mlee@gmail.com", "Gender": "M", "Age": 50, "Tier": "A", "Points": 100},
            {"Customer_ID": 'S444',
             "Name": "Matthew", "Email": "mkhoo@gmail.com", "Gender": "M", "Age": 24, "Tier": "D", "Points": 3000},]


customer_requests = Queue()


def main():
    total_requests = 0

    while True:
        print("\nCustomer Request Page:")
        print("1. Input customer request")
        print("2. View number of request")
        print("3. Service next request in menu")
        print("0. Return to main menu")
        choice2 = input("Please select one: ")

        if choice2 == '1':
            add_customer_request(customer_requests, records2)
            total_requests += 1
            continue

        elif choice2 == '2':
            print(
                f"Number of customer requests in the queue: {total_requests}")
            continue

        elif choice2 == '3':
            total_requests -= 1
            service_next_request()

        elif choice2 == '0':
            othermain()
            break


def add_customer_request(queue, records2):
    while True:
        customer_id = input("Enter Customer ID: ")
        for record in records2:
            if record["Customer_ID"] == customer_id:  # Duplicate accept
                request_description = input("Enter Request Description: ")
                request = CustomerRequest(customer_id, request_description)
                queue.enqueue(request)
                print("Request added successfully.")
                return
        print("Customer ID does not exist. Please try again.")


def service_next_request():
    if customer_requests.is_empty():
        print("No customer requests in the queue.")
    else:
        next_request = customer_requests.dequeue()
        customer = get_customer_by_id(next_request.customer_id)
        print("\nServicing Next Request:")
        print("-"*100)
        print(f"Customer ID: {customer['Customer_ID']}")
        print(f"Customer Name: {customer['Name']}")
        print(f"Customer Email: {customer['Email']}")
        print(f"Customer Gender: {customer['Gender']}")
        print(f"Customer Age: {customer['Age']}")
        print(f"Customer Tier: {customer['Tier']}")
        print(f"Customer Points: {customer['Points']}")
        print("-"*100)
        print(f"Request Description: {next_request.request_description}")
        num_remaining_requests = customer_requests.size()
        print(
            f"\nNumber of remaining requests in the queue: {num_remaining_requests}")


def get_customer_by_id(customer_id):
    for customer in records2:
        if customer["Customer_ID"] == customer_id:
            return customer


records = [{'ISBN (PK)': 2, 'Title': 'Python Cookbook ', 'Category': 'Education', 'Publisher': 'Denise',
            'Year_Published': 2014},
           {'ISBN (PK)': 3, 'Title': 'Adventures in Python', 'Category': 'Adventure', 'Publisher': 'Wiley',
            'Year_Published': 2000},
           {'ISBN (PK)': 4, 'Title': 'FizzBuzz', 'Category': 'Python', 'Publisher': 'Johnson',
            'Year_Published': 2016},
           {'ISBN (PK)': 1, 'Title': 'Java Cookbook ', 'Category': 'Education', 'Publisher': 'Denise',
            'Year_Published': 2014},
           {'ISBN (PK)': 90, 'Title': 'Me Cookbook ', 'Category': 'Education', 'Publisher': 'Denise',
            'Year_Published': 2014},
           ]

# Manage customers


class CustomerLinkedList:
    def __init__(self):
        self.head = None

    def add_customer(self, customer):
        new_customer_node = CustomerNode(customer)
        if self.head is None:
            self.head = new_customer_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_customer_node

    def display_customers(self):
        current = self.head
        while current is not None:
            print(f"Name: {current.customer.name}")
            print(f"Email: {current.customer.email}")
            print(f"Gender: {current.customer.gender}")
            print(f"Age: {current.customer.age}")
            print(f"Tier: {current.customer.tier}")
            print(f"Points: {current.customer.points}")
            print(f"Customer ID: {current.customer.customer_id}")
            print("--------------------")
            current = current.next

    def count_customers(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def get_customers(self):
        customers = []
        current = self.head
        while current is not None:
            customers.append(current.customer)
            current = current.next
        return customers


class CustomerNode:
    def __init__(self, customer):
        self.customer = customer
        self.next = None


def add_new_customer(customer_list):
    customer_id = input("Enter Customer ID: ")
    existing_customer_id = []
    for customer in records2:
        existing_customer_id.append(customer['Customer_ID'])

    while customer_id in existing_customer_id:
        print("Customer ID already exists. ")
        customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    email = input("Enter Customer Email: ")
    while '@' not in email:
        print('Invalid email. Email should contain @. Try again.')
        email = input('Enter Email: ')

    while True:
        gender = input("Enter Customer Gender (M/F): ")
        if gender.upper() in ['M', 'F']:
            break
        else:
            print("Invalid gender. Please enter 'M' for Male or 'F' for Female.")
    while True:
        age = int(input("Enter Customer Age: "))
        if age >= 12:
            break
        else:
            print("Invalid age. Minimum 12 years old to create member.")
    tier = input("Enter Customer Tier: ")
    points = int(input("Enter Customer Points: "))
    customer = Customer(name, email, gender, age, tier, points)
    customer_list.add_customer(customer)

    new_records = {
        'Customer_ID': customer_id,
        'Name': name,
        'Email': email,
        'Age': age,
        'Gender': gender.upper(),
        'Tier': tier.upper(),
        'Points': points
    }
    records2.append(new_records)
    print("Customer added successfully.")


# Display sorted customers
def insertion_sort_customers():
    for i in range(1, len(records2)):
        value_to_sort = records2[i]
        j = i - 1

        while j >= 0 and records2[j]['Name'] > value_to_sort['Name']:
            records2[j + 1] = records2[j]
            j -= 1

        records2[j + 1] = value_to_sort

    print("\nRecords have been sorted by Name in ascending order.")


def display_customers_sorted():
    for y in records2:
        print("Customer ID:", y['Customer_ID'])
        print("Name:", y['Name'])
        print("Email:", y['Email'])
        print("Gender: ", y['Gender'])
        print("Age: ", y['Age'])
        print("Tier:", y['Tier'])
        print("Points:", y['Points'])
        print()


def deletecustomer():
    deleted_customer = None
    remaining_customers = []

    while deleted_customer is None:
        deleted_customer_id = input(
            "Please key in the Customer ID of the customer you want to delete: ")

        for each in records2:
            if each['Customer_ID'] == deleted_customer_id:
                deleted_customer = each
            else:
                remaining_customers.append(each)

        if deleted_customer:
            print(
                f"Customer with Customer ID {deleted_customer_id} has been deleted.")
            records2.clear()
            records2.extend(remaining_customers)
            print("\nRemaining customers:")
            try:
                for each in remaining_customers:
                    print(
                        f"Customer ID: {each['Customer_ID']} \nName: {each['Name']} \nEmail: {each['Email']} \nGender: {each['Gender']} \nAge: {each['Age']} \nTier: {each['Tier']} \nPoints: {each['Points']}\n")
            except (TypeError, ValueError, AttributeError):
                print("Error occurred while accessing customer details.")
        else:
            print(f"No customer with ID {deleted_customer_id} found.")

    return remaining_customers


def update_customer_details():
    while True:
        customer_id = input(
            "Enter the Customer ID you want to update (or 'q' to quit): ")

        if customer_id == 'q':
            print("Exiting update process.\n")
            return

        found_customer = False

        for index, customer in enumerate(records2):
            if customer['Customer_ID'] == customer_id:
                found_customer = True
                print("Updating details for Customer:", customer['Name'])

                updated_name = input(
                    f"Enter new Name (current: {customer['Name']}, 'q' to quit): ")
                if updated_name != 'q':
                    records2[index]['Name'] = updated_name

                updated_email = input(
                    f"Enter new Email (current: {customer['Email']}, 'q' to quit): ")
                if updated_email != 'q':
                    records2[index]['Email'] = updated_email

                updated_gender = input(
                    f"Enter new Gender (current: {customer['Gender']}, 'q' to quit): ")
                if updated_gender != 'q':
                    records2[index]['Gender'] = updated_gender

                updated_age = input(
                    f"Enter new Age (current: {customer['Age']}, 'q' to quit): ")
                if updated_age != 'q':
                    records2[index]['Age'] = int(updated_age)

                updated_tier = input(
                    f"Enter new Tier (current: {customer['Tier']}, 'q' to quit): ")
                if updated_tier != 'q':
                    records2[index]['Tier'] = updated_tier

                updated_points = input(
                    f"Enter new Points (current: {customer['Points']}, 'q' to quit): ")
                if updated_points != 'q':
                    records2[index]['Points'] = int(updated_points)

                print(f"Details updated for Customer ID: {customer_id}")
                break

        if not found_customer:
            print(
                f"No customer with ID {customer_id} found. Please enter a valid ID.")


customer_list = CustomerLinkedList()


def main2():
    while True:
        print("\nManage Members Page")
        print("1. Add new members")
        print(
            "2. Sort members by their name using Insertion sort and display the outcome in ascending order")
        print("3. Delete members based on customer id")
        print('4. Update members based on customer id')
        print("0. Return to main menu")
        choice3 = input("Please select one: ")
        if choice3 == '1':
            add_new_customer(customer_list)
        elif choice3 == '2':
            insertion_sort_customers()
            display_customers_sorted()
        elif choice3 == '3':
            deletecustomer()
        elif choice3 == '4':
            update_customer_details()
            for customer in records2:
                print(
                    "\n".join([f"{key}: {value}" for key, value in customer.items()]))
                print("=" * 30)
        elif choice3 == '0':
            othermain()
            break


def displaymenu():
    print("\n****** Book Management System ******")
    menu = ["1. Display of all the books' records",
            "2. Add a new book",
            "3. Sort books by their Category in ascending order using Bubble sort and display the outcome",
            "4. Sort the Publisher in descending order using only Selection sort and display outcome",
            "5. Delete a book based on ISBN(PK)",
            "6. Sort books by Title in ascending order using Insertion sort and display the outcome",
            "7. Sort books by Year published and then by ISBN in ascending order using Merge sort and display the outcome",
            "8. Manage customer request",
            "9. Manage members"]
    print(*menu, sep='\n')


def deleteisbn():
    deleted_book = None
    remaining_books = []

    while True:
        isbn = input("Please key in the ISBN of the book you want to delete: ")
        if isbn.isdigit():
            break
        print('Enter a valid value')

    isbn = int(isbn)  # Convert the input to integer for comparison

    for book in records:
        if book['ISBN (PK)'] == isbn:
            deleted_book = book
        else:
            remaining_books.append(book)

    if deleted_book:
        print(f"Book with ISBN {isbn} has been deleted.")
        records.clear()
        records.extend(remaining_books)
        print("Remaining books:")
        try:
            for book in remaining_books:
                print(
                    f"ISBN (PK): {book['ISBN (PK)']}, Title: {book['Title']}, Category: {book['Category']}, Publisher: {book['Publisher']}, Year Published: {book['Year_Published']}")
        except (TypeError, ValueError, AttributeError):
            print("Error occurred while accessing book details.")
    else:
        print(f"No book with ISBN {isbn} found.")

    return remaining_books


def AllRecords():
    for x in records:
        print("\nTitle:", x['Title'])
        print("Category:", x['Category'])
        print("Publisher:", x['Publisher'])
        print("Number of ISBN (PK):", x['ISBN (PK)'])
        print("Year_Published: Year {}".format(x['Year_Published']), '\n')


def BubbleSort():
    length = len(records)

    for i in range(length - 1, 0, -1):
        for j in range(i):
            if records[j]['Category'] > records[j + 1]['Category']:
                tmp = records[j]
                records[j] = records[j + 1]
                records[j + 1] = tmp
    print("\nRecords have been sorted by Category")


def InsertionSort():
    indexing_length = range(1, len(records))
    for i in indexing_length:
        value_to_sort = records[i]

        while i > 0 and records[i-1]['Title'] > value_to_sort['Title']:
            records[i], records[i-1] = records[i-1], records[i]
            i = i - 1

    print("\nRecords have been sorted by Title in ascending order.")


def MergeSort():
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            merge_sort(left_arr)
            merge_sort(right_arr)

            y = 0
            x = 0
            i = 0

            while y < len(left_arr) and x < len(right_arr):
                if left_arr[y]['Year_Published'] < right_arr[x]['Year_Published']:
                    arr[i] = left_arr[y]
                    y += 1
                elif left_arr[y]['Year_Published'] == right_arr[x]['Year_Published'] and left_arr[y]['ISBN (PK)'] < right_arr[x]['ISBN (PK)']:
                    arr[i] = left_arr[y]
                    y += 1
                else:
                    arr[i] = right_arr[x]
                    x += 1
                i += 1

            while y < len(left_arr):
                arr[i] = left_arr[y]
                y += 1
                i += 1

            while x < len(right_arr):
                arr[i] = right_arr[x]
                x += 1
                i += 1

    merge_sort(records)
    print("\nRecords have been sorted by Year Published and then by ISBN number in ascending order.")


def SelectionSort():
    length = len(records)

    for i in range(length - 1):
        smallNdx = i
        for j in range(i + 1, length):
            if records[j]['Publisher'] > records[smallNdx]['Publisher']:
                smallNdx = j
        if smallNdx != i:
            tmp = records[i]
            records[i] = records[smallNdx]
            records[smallNdx] = tmp
    print("\nRecords have been sorted by Publisher in descending order")


def listingrecords():
    Year_Published = []
    checkforrecords = False
    for x in records:
        Year_Published.append(x['Year_Published'])
    Year_Published = list(dict.fromkeys(Year_Published))
    length = len(Year_Published)
    listing = True
    while listing:
        min = input("Please key in the minimum Year_Published: ")
        if min.isdigit():
            min = int(min)
            if min < 0:
                print("Please enter a valid value.")
                continue
            else:
                max = int(input("Please key in the maximum Year_Published: "))
                if max <= 0 or max < min:
                    print("Please enter a valid value")
                    continue
                if max == min:
                    print("Please enter a value more than the minimum value")
                    continue
                else:
                    for c in range(length):
                        for l in range(len(records)):
                            if Year_Published[c] > min and Year_Published[c] < max:
                                checkforrecords = True
                                if Year_Published[c] == records[l]['Year_Published']:
                                    print("\nCategory: ",
                                          records[l]['Category'])
                                    print("Publisher: ",
                                          records[l]['Publisher'])
                                    print("ISBN (PK): ",
                                          records[l]['ISBN (PK)'])
                                    print("Year_Published: ",
                                          records[l]['Year_Published'])
                    if (checkforrecords == False):
                        print("There are no records in Year_Published range Year {0} to Year {1}. Try Again".format(min,
                                                                                                                    max))
                        continue
                    break
        else:
            print("Please key a valid value.")


def addnew():
    try:
        while True:
            PK = input("Please enter the PK of the book: ")
            if not PK:
                print("PK cannot be empty. Please enter a valid PK.")
                continue
            elif not PK.isdigit():
                print("PK must be a numeric value. Please enter a valid PK.")
                continue
            elif int(PK) < 0:
                print("PK cannot be a negative value. Please enter a valid PK.")
                continue

            PK = int(PK)
            existing_PKs = [record['ISBN (PK)'] for record in records]
            if PK in existing_PKs:
                print("PK already exists. Please enter a new PK.")
            else:
                break

        Title = input("Please enter the Title of the book: ")
        while not Title:
            print("Title cannot be empty. Please enter a valid Title.")
            Title = input("Please enter the Title of the book: ")

        Category = input("Please enter the Category of the book: ")
        while not Category:
            print("Category cannot be empty. Please enter a valid Category.")
            Category = input("Please enter the Category of the book: ")

        Publisher = input("Please enter the Publisher of the book: ")
        while not Publisher:
            print("Publisher cannot be empty. Please enter a valid Publisher.")
            Publisher = input("Please enter the Publisher of the book: ")

        while True:
            try:
                Year = int(input("Please enter the Year of the book: "))
                if Year < 1000 or Year > 2023:
                    print("That's not a valid year. Please enter a correct year.")
                else:
                    break
            except ValueError:
                print("That's not a valid year. Please enter a number.")

        new_book = {
            'ISBN (PK)': PK,
            'Title': Title,
            'Category': Category,
            'Publisher': Publisher,
            'Year_Published': Year
        }

        records.append(new_book)
        print("Book has been added.")

    except (ValueError, AttributeError) as e:
        print(e)
        addnew()


def othermain():
    while True:
        displaymenu()
        choice = input("Please choose from the above selection (Q to quit): ")
        choice.upper()
        if choice == '1':
            AllRecords()
            continue
        if choice == '2':
            addnew()
            continue
        elif choice == '3':
            BubbleSort()
            AllRecords()
            continue
        elif choice == '4':
            SelectionSort()
            AllRecords()
            continue
        elif choice == "5":
            deleteisbn()
            continue
        elif choice == "6":
            InsertionSort()
            AllRecords()
            continue
        elif choice == "7":
            MergeSort()
            AllRecords()
            continue
        elif choice == "8":
            main()
        elif choice == '9':
            main2()
        elif choice == 'Q' or choice == 'q':
            print("\nExiting application. Goodbye!")
            break
        else:
            print("Please enter a valid value")


while True:
    othermain()
