**Created Trie Data Structure and implemented Insert, Search, Delete and ShowList functions** 

on these set of test cases: 


**Implemented : for test cases**

**Test case 1** 
**['apple','app', 'bat', 'batter', 'ban']**


trie1.showData() # prints : app  apple  bat  batter  ban 

trie1.search('apple') # Tells it contains 'apple' 

trie1.delete('app') # deletes the word
trie1.showData()    # 'app' not shown in the list  
                    # apple  bat  batter  ban

trie1.search('banana')  # tells it does not exist when searched
trie1.delete('banana')  # tells it does not exist to be deleted 
trie1.delete('random')  # 'random' does not exist to be deleted 


**Test case 2**
**['app', 'apron', 'ronan', 'nancy']**

trie2.showData()       # prints:  app  apron  ronan  nancy
trie2.search('app')    # Trie contains  app

trie2.delete('apron') 

trie2.showData()  # prints: app  ronan  nancy

trie2.delete('apple') #  apple  does not exist to be deleted
