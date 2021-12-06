import sys
import typing

# Use the Composite design pattern to maintain 
# a hierarchy of questions with answers as the leaf nodes.
class Node:
    def is_leaf(self) -> bool:
        return isinstance(self, Animal)

class Question(Node):
    def __init__(self, question: str):
        self.text = question
        self.children = []

    def getText(self):
        return self.text
    
    def add(self, node:Node):
        self.children.append(node)

    def getChild(self, i:int):
        if i < 0 or i > (len(self.children) - 1):
            raise IndexError()
        return self.children[i]

    def getNumChildren(self):
        return len(self.children)

    def print(self):
        print("Question: {}".format(self.text))
        for node in self.children:
            node.print()

    def __str__(self):
        return self.text


class Animal(Node):
    def __init__(self, animal:str):
        self.text = animal

    def getText(self):
        return self.text

    def print(self):
        print("Animal: {}".format(self.text))

    def __str__(self):
        return self.text

def prompt_yes_no_answer(question: str) -> str:
    while True:
        print("{} [y/n] ".format(question))
        ans = sys.stdin.readline().strip()
        if ans == "t":
            root.print()
        if ans == "y" or ans == "n":
            return ans



# There are possible outcomes:
# 1. we guess correctly
# 2. we guess wrong (the node arg is a Animal)
#    - we need to insert a new Question node between the Animal and its parent
# 3. we exhaust our questions (the node arg is Question)
#    - we need to add another question to the list in the current Node
#
# Depending on if the asnwer to the new question is yes or no, we'll either need
# to add the new animal as a child to the new question, or append the animal the
# the end of the children list of the current node.
def add_new_animal(node: Question, guessed_animal: Animal):
    
    print("What animal did you think of?")
    animal = Animal(sys.stdin.readline().strip())
    print("Can you give me a question that is more specific than:\n"
            " --  {}? --\n"
            "to which the answer -- {} -- would be true?".format(
                node, animal)
    )
    new_question = Question(sys.stdin.readline().strip().replace("?", ""))
    new_question.add(animal)
    node.add(new_question)
    print("-------------------------------------------------------------")
    print("I will try my best to remember a {}.".format(animal))
    print("-------------------------------------------------------------")

def guess(node: Node, parent: Node) -> Node:
    if not node:
        return None
       
    i = 0
    while i < node.getNumChildren():
        curnode = node.getChild(i)
        if isinstance(curnode, Question):
            yesno = prompt_yes_no_answer("{}?".format(curnode))
            if yesno == "y":
                return guess(curnode, node)
        if isinstance(curnode, Animal):
            yesno = prompt_yes_no_answer("Is it a {}?".format(curnode))
            if yesno == "y":
                return(curnode)
        i = i + 1

    # at this point we've exhausted the available questions
    print("I give up!")
    add_new_animal(node, None)
    return None

if __name__ == "__main__":

    root = None
    done = False
    points = 0

    # bootstrap the model with some basic cases
    root = Question("Is it an animal?")
    q1 = Question("Does it live in the sea?")
    q1.add(Animal("Tuna fish"))
    root.add(q1)   
    root.add(Question("Does it fly?").add(Animal("Cuckatoo")))
    root.add(Animal("pangolin"))

    while not done:
        if prompt_yes_no_answer("\n\nThink of an animal... Are you ready?") == "n":
            break
        node = guess(root, None)
        if node is not None:
            points = points + 1
            print("1 extra point for me! I now have {} points.".format(points))
            continue

        if prompt_yes_no_answer("Would you like to go again?") == "n":
            done = True

    print("Thanks for playing!")

