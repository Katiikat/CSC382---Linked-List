#This program is written in Python, and therefore it is duct typed, which means that the coder doesn't have to specify a data type...the language figures it out automagically. In comparison with other languages, this program would be considered templated, since the language can determine the type itself. 

#The program is simple. In its current state, the numbers to be put into the list are hard-coded. To update this program, the code will need to be accept user input, and be able to find, delete, and return the minimum and maximum of all the numbers entered into the list. Shouldn't be to difficult. 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    #initializing of the list, there is no node in the list
    def __init__(self):
        self.head = None
        
    #insert -- add to the end of list    
    def insert(self, data):
        #add a node to beginning of list, or head, if no node exists
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            #if a node currently exists, create a new node
            #set cur, or current, to the head pointer
            #go through the list until a node that points to none is found (last element)
            #one the last node is found, set the next pointer to the new node
            #set the new nodes previous to current
            #then set the new nodes next step to none
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
                
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
            
    #prepend -- add number to the front of list
    def prepend(self,data):
        #adds number to beginning of list, or head
        #then set the previous pointer to none, or null
        #and the next to none
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            # if a number is already in the list
            #create a new node, set the current heads previous step to the new node
            #set the head tag to the new node
            #the set the new nodes previous to none
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            
    def __iter__(self):
        """Magic stuff"""
        cur = self.head
        yield cur
        while cur.next is not None:
            cur = cur.next
            yield cur

    def items(self):
        """Gets the data of stuff"""
        for item in self:
            yield item.data
    
    def find(self, data):
        """Finds stuff"""
        if data in self.items():
	        return (f'Data found: {data}')

        return "Data not found."

    def delete(self, data):
        """Deletes stuff"""
        cur = self.head
        while cur.next:
            if cur.data == data:
                prev_node = cur.prev
                next_node = cur.next
                
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                if self.head is cur:
                    self.head = next_node

                break
            cur = cur.next
        return f'\nDeleted: {data}'
                
    #simply prints the list out
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    
dllist = DoublyLinkedList()
print("Current List:")
#prepend -- add number to the front of list
dllist.prepend(0.0)
dllist.insert(1.5)
dllist.insert(2.9)
dllist.insert(3.3)
dllist.insert(4.7)
dllist.prepend(5.0)

for item in dllist.items():
    print(item)

con = True

while con:
    print("\nChoose any of the below options: \n")
    print("1. Find Number \n2: Add Number \n3: Delete Number")
    print("4: Find maximum \n5: Find Minimum")

    choice = input("Type a number: ")
    
    if int(choice) == 1:
        find = input("What number would you like to find?\n")
        print(f'{dllist.find(float(find))}\n')
    
    if int(choice) == 2:
        toAdd = input("What number would you like to add?\n")
        dllist.insert(float(toAdd))
        print("\nNew List:")
        for item in dllist.items():
            print(item)
        
    if int(choice) == 3:
        numDel = input("What number would you like to delete?\n")
        print(dllist.delete(float(numDel)))
        print("\nNew List:")
        dllist.print_list()
        print()
    
    if int(choice) == 4:
        print(f'Max: {max(dllist.items())}\n')
    
    if int(choice) == 5:
        print(f'Min: {min(dllist.items())}\n')
        
    ans = input ("Would like to choose another option? Y/N\n")
    
    if ans == "N" or ans == "n":
        con = False







































