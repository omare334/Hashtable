class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):

        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

            def __init__(self):
                self.data = {}





    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(1000)

# insert some values


import pandas as pd
L=input("Enter the file name with type e.g all_data.csv : ")
df=pd.read_csv(f'{L}')


def add_to_hash_table(key, value):
    hash_table.set_val(key, value)

df.apply(lambda x: add_to_hash_table(x['hash'], x['national_insurance_number']), axis=1)

def search_hash_table():
    for key in lst:
       hashed = int(key)
       print(hash_table.get_val(hashed))


# accept user integer input and search for the value in the hash table
A=input("do you have a list (seperated by spaces) or need to make one (yes/no) \
or do you have a positional argument (other): ")
if A=="yes":
    input_string = input('Enter elements of a list separated by space ')
    print("\n")
    user_list = input_string.split()
    print('list: ', user_list)
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    for key in user_list:
       hashed = int(key)
       print(hash_table.get_val(hashed))
elif A=="no":
    lst = []
    n = int(input("Enter number of elements in your list: "))
    for i in range(0, n):
        ele = ele = int(input("enter hash number: "))
        lst.append(ele)  # adding the element
    search_hash_table()
elif A=="other":
    w=int(input("Enter the position of first hash as it appears in excel : "))
    w=int(w-2)
    z=int(input("Enter the position of last hash as it appears in excel: "))
    z=int(z-1)
    D=(df.iloc[w:z, df.columns.get_loc('hash')])
    result = [hash_table.get_val(x) for x in D]
    G = list(range(w, z))
    df3 = pd.DataFrame(result, index=[G], columns=['national'])
    file_name = input("what name would you like the file to be saved as (please add .csv at the end): ")
    df3.to_csv(file_name, index=True)
    print(df3)
else:
    print("invalid input")

A=input("do you have another postional argument (Y/N);")
while A=="Y":
    w=int(input("Enter the position of first hash as it appears in excel : "))
    w=int(w-2)
    z=int(input("Enter the position of last hash as it appears in excel: "))
    z=int(z-1)
    D=(df.iloc[w:z, df.columns.get_loc('hash')])
    result = [hash_table.get_val(x) for x in D]
    G = list(range(w, z))
    df3 = pd.DataFrame(result, index=[G], columns=['national'])
    file_name = input("what name would you like the file to be saved as (please add .csv at the end): ")
    df3.to_csv(file_name, index=True)
    print(df3)
    A=input("do you have another postional argument (Y/N);")
    if A=="N":
        print("Thanks, your csv files have been created")
        break

input("Press enter to exit;")













