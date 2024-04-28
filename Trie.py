class Node:
    def __init__(self):
        self.child = {} # for storing alphabetic characters in a manner of key value pairs
        self.iscomplete = False # for checking if this is the end of a word


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root              # direct to the root always check if the characters in the word are already present in the root
        for char in word:               #iterating through each character in the word
            if char not in node.child:      #if character not found 
                node.child[char] = Node()   # a new node for the character is created
            node = node.child[char]     # if found then it moves forward to the next character / node 
        node.iscomplete = True          # shows that a word is complete 
    
    def search(self, word):
        node = self.root       # start from the root always
        for char in word:       #iterating through each character in the word
            if char not in node.child: # checking if the char is not in the node, vause if not 
               print("\n", word," does not exist")
               return False            # then we do not need to check further 
            node = node.child[char]     # if found move to the next character
        if node.iscomplete:
            print("\nTrie contains ",word)
        

    
    def delete(self, word):
        node = self.root        # start from the root 

        for char in word:       
            if char in node.child:     # if character found, move to the next node 
                node = node.child[char]    # checking if the char is not in the node, if all the character was iterated then, the word was present in Trie
            else:       # ie, if char in node.child does not exist then
                print("\n",word," does not exist to be deleted")
                return            # exit the function or else it will print again in the next condition check          
        if not node.iscomplete:             # if iscomeplete is still True after all the character in the word is iterated then it means the word does not exist
            print("\n",word," does not exist to be deleted") # for checking if a word that has no common char with the word on the list
        node.iscomplete = False         # then changed the "end of word" to false -> showcasing that a word does not end here 
        return                          # hence removing the word from the dictionary    
                                         # checks if word does not exist in the Trie

 


    def dfsTrie(self, node, curword):  # depth first search for iterating through the Trie DS and print out the words present in it
        if node.iscomplete:             # checks if iscomplete is True, if a word is complete 
            print(curword," ",end="")       # if so then prints it
        for char in node.child.keys():      # checks the key of the node ie, the character stored in the dictionary
            childNode = node.child[char]    # if present then the next childnode made the root node for the dfsTrie function to be called again 
            self.dfsTrie(childNode, curword+char) # recursively appends the character it comes across until iscomplete is True and the word is printed


    def showlist(self):                 # for printing the updated list 
        self.dfsTrie(self.root, "")
                


trie1 = Trie()

words = ['apple','app', 'bat', 'batter', 'ban']

# inserting words in the Trie DS
for word in words:
    trie1.insert(word)

trie1.showlist()

trie1.search('apple') # Tells it contains 'apple' 


trie1.delete('app') # deletes the word
trie1.showlist()    # 'app' not shown in the list 

trie1.search('banana')  # tells it does not exist
trie1.delete('banana')  # tells it does not exist to be deleted 
trie1.delete('random')

#################################################################################

trie2 = Trie()

words2 = ['app', 'apron', 'ronan', 'nancy']

for i in words2:
    trie2.insert(i)

print('\n')
trie2.showlist()
trie2.search('app')

trie2.delete('apron')

trie2.showlist()






