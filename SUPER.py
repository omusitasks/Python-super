
# A1B1.PY
class AList: # defining a class of FIXEDSIZE-Array-List

    def __init__(self, inSize=3): # constructor, default size=3
        self.pList=[None]*inSize  # new a Python List to hold data
        self.last = 0             # The position of the last element
        self.capacity = inSize  # The current capacity of the list

        #######STUDENT's WORK#######
        # simple comment HERE
        def insertL(self, elt, pos): # Insert element, pos start from 1
            pass # TO BE DONE BY STUDENT

        # simple comment HERE
        def appendL(self, elt):
            pass # TO BE DONE BY STUDENT

        # simple comment HERE
        def searchFirstL(self, elt):
            pass # TO BE DONE BY STUDENT

        # simple comment HERE
        def clearL(self):
            pass # TO BE DONE BY STUDENT

        ##### END of STUDENT's WORK#######

        def isEmpty(self): # check if the list is empty or not
            return self.sizeL()==0

        def isFullL(self): # check if the list is full or not
            return self.sizeL()==self.capacity

        def sizeL(self): # Return size of List (number of elements)
            return self.last

        def display(self):
            print(f'>>>AList Display(Head/Left), size/last<{self.last}>,', f'capacity<{self.capacity}>:')


# A1B2.py


class DLNode: # modelling a node with Doubly-Linked-List 
    def _init_(self, inValue=None, inPrev=None, inNext=None): # constructor
        self.value = inValue # the node data value, default None 
        self.prevN = inPrev # the previous node, default None
        self.nextN = inNext # the next node, default None

class DLList: # defining a class of Doubly-Linked-List 
    def _init_(self): # GIVEN: constructor 
        self.headN = None # the head Node 
        self.tailN = None # the tail Node

        ##STUDNET'S WORK #####
        # # #simple comment HERE
        def getNextFwDL(self, refElt): # Get & return (without remove) next element of reference refElt, in forward order 
            pass # TO BE DONE BY STUDENT

        # simple comment HERE
        def getPrevBwDL(self, refElt): # Get & return (without remove) previous element of reference refElt, in backward order
            pass # TO BE DONE BY STUDENT
        
        # simple comment HERE
        def removeNextFwDL(self, refElt): # REMOVE & return next element of reference refElt, in forward order 
            pass # TO BE DONE BY STUDENT 

        ####### END of STUDNET's WORK  #####
        def appendDL(self, elt): # GIVEN: append/insert a new node value, as the new tail
            if self.headN==None: # case of empty DLL 
                newTailN = DLNode(elt) # create new Node 
                self.headN = newTailN # link new (Tail) Node 
                self.tailN = self.headN
            else:
                newTailN = DLNode(elt, self.tailN) # create a new (Tail) Node, set its previous node as the current Tail 
                self.tailN.nextN = newTailN # current Tail. links next


# MA1B1.py


from A1B1 import AList

def main():
    print("=== A1B1, Fixed-Sized ArrayList, by <Student NAME><Student ID> ===\n")
    myL = AList(5)
    print(f"--- 0. new AL <CHECK> isFullL()?:{myL.isFullL()}, isEmptyL()?:{myL.isEmptyL()}")
    myL.displayL()
    print(f"--- 1. insertL <ABQCP>-R?")
    myL.insertL('A', 1); myL.insertL('B', 2); myL.insert('C', 3); 
    myL.insertL('P', 4); myL.insertL('Q', 3); myL.insertL('R', 2); 
    myL.displayL()
    
    myL.removeL (4); myL.removeL (4);
    print("\n---2. appendL: <ABQ,QA>-H? ") 
    myL.appendL('Q'); myL.appendL ('A'); myL.appendL('H'); 
    myL.displayL() 
    print("\n 3. <CHECK> search FirstL('Q'), pos:{myL.searchFirstL('Q')}")
    print("\n--- 3. removeL (myL.searchFirstL ('A')), elt:{myL.removeL (myL.searchFirstL('A'))}")
    myL.displayL()
    print(f"- <CHECK> searchFirstL('Q'), pos:{myL.searchFirstL('Q')}")
    print(f"--------- <CHECK> searchFirstL('H'), pos:{myL.searchFirstL('H')}")
    print (f"------<CHECK> searchFirstL('QA'), pos:{myL.searchFirstL('QA')}")
    print("\n=== Program ends ===\n")

main()

# MA1B2.py

from A1B2 import DLList

def main():
    print("====== A1B2, DLList program, by <Student NAME><Student ID>===")
    myL = DLList()
    myL.appendDL(20); myL.appendDL (30); myL.appendDL(40)
    myL.appendDL(50); myL.appendDL(60); myL.appendDL(70)
    print("\n--- 1. List with Insert items <20,30,40,50,60,70> ---")
    
    myL.displayDL()
    myL.displayBwDL()

    print(f" --- ------<CHECK> getNextFwDL(50), elt:{myL.getNextFwDL(50)}")
    print(f" -- <CHECK> getPrevBwDL(60), elt:{myL.getPrevBwDL(60)}")
    print(f"\n 2. <CHECK> removeNextFwDL (30), elt:{myL.removeNextFwDL(30)}")
    myL.displayDL()
    myL.displayBwDL()
    
    print("\n=== Program ends ===\n")

main() 