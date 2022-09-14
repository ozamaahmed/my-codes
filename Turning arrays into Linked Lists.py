#lemme first create two LLs based on arrays

# this is a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# we are inserting the nodes at the back. were maintaing an end pointer
# instead of traversing each time
def insert(head,end,data):
    temp = Node(data)
    if head==None:
        head = temp
        end = temp
    else:
        end.next = temp
        end = temp
    return head,end
    
# to display the data
def display(head):
    node = head
    while node!= None:
        print(node.data)
        node = node.next
        
# here we call the function insert n times and end is a new node everytime
def put(arr):
    head = None
    end = None
    for i in arr:
        head,end = insert(head,end,i)
    display(head)
    return head
list1 = [1,2,4]
list2 = [1,3,4]

head1 = put(list1)
head2 = put(list2)

#now head1 and head2 are pointing to the head of the both linked lists
#we have created