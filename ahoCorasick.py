'''
Implementation of AhoCorasick search for python (2.7)

example of usage:

tree = searchTree()
for word in ['word1', 'word2', 'word4'] :
   tree.add(word)
tree.make()
tree.search('This is the text you want to search in')


Deposited to pastebin
billbaggins@gmail.com for questions
'''
import collections

#http://crazyhottommy.blogspot.com/2013/10/python-code-for-getting-reverse.html
def simpleReverseCompliment(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join([seq_dict[base] for base in reversed(seq)])
 
class acNode :
    def __init__(self, ch) :
        self.char = ch
        self.transitions = []
        self.results = []
        self.fail = None
 
class searchTree :
    def __init__(self) :
        self.terms = []
        self.root = None
        self.maxLength = 0
 
    def add(self, term) :
        self.terms.append(term)
        self.maxLength = max(self.maxLength,len(term))
 
    def make(self) :
        # Create the root node and queue for failure paths
        root = acNode(None)
        root.fail = root
        queue = collections.deque([root])
 
        # Create the initial tree
        for keyword in self.terms :
            current_node = root
            for ch in keyword :
                new_node = None
                for transition in current_node.transitions:
                    if transition.char == ch:
                        new_node = transition
                        break
 
                if new_node is None:
                    new_node = acNode(ch)
                    current_node.transitions.append(new_node)
                    if current_node is root:
                        new_node.fail = root
 
                current_node = new_node
            current_node.results.append(keyword)
 
        # Create failure paths
        while queue:
            current_node = queue.popleft()
            for node in current_node.transitions:
                queue.append(node)
                fail_state_node = current_node.fail
                while not any(x for x in fail_state_node.transitions if node.char == x.char) and fail_state_node is not root:
                    fail_state_node = fail_state_node.fail
                node.fail = next((x for x in fail_state_node.transitions if node.char == x.char and x is not node), root)
 
        # tree has been built! return it
        self.root = root
 
    def initHits(self):
        hits = {}
        for term in self.terms:
            hits[term]=[]
        return hits


    def search(self, text,findStart=True,verbose=False) :
        hits=self.initHits()
        currentNode = self.root
 
        # Loop through characters
        textPos=0
        nChar=len(text)
        for c in text :
            if verbose and nChar> 1000000 and textPos%1000000==0: print(textPos,"/",nChar)
            # Find next state (if no transition exists, fail function is used)
            # walks through tree until transition is found or root is reached
            trans = None
            while trans == None :
                # trans=currentNode.GetTransition(text[index])
                for x in currentNode.transitions :
                    if x.char == c :
                        trans = x
                if currentNode == self.root : break
                if trans==None : currentNode=currentNode.fail
               
            if trans != None : currentNode=trans
            # Add results from node to output arrays and move to next character
            for result in currentNode.results :
                thisPosition=textPos
                if(findStart): thisPosition=thisPosition-len(result)+1
                hits[result].append(thisPosition)
            textPos+=1
 
        return hits

    def reverseComplimentTree(self):
        tree=searchTree()
        for term in self.terms:
            tree.add(simpleReverseCompliment(term))
        tree.make()
        return tree
    #could implement a line by line search, being smart at new line transitions but not sure it's necessary. one chr should fit in memory ok. save for later
    #def searchFile(self,fileHandle):
         
