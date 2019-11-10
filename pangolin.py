import sys
import typing

class Node(object):
    def __init__(self, text : str, parent):
        self.text   = text
        self.parent = parent
        self.yes    = None
        self.no     = None

    def set_yes_answer(child):
        self.yes = child

    def set_no_answer(child):
        self.no = child

    def is_leaf(self) -> bool:
        if not self.yes and not self.no:
            return True
        else:
            return False


def print_node(node: Node, id : str):
    print("===============================")
    print("= Node text: ({}) {}".format(id, node.text))
    if not node.parent:
        print("= Parent: None")
    else:
        print("= Parent: {}".format(node.parent.text))
        if node == node.parent.yes:
            print("= Relationship: yes")
        elif node == node.parent.no:
            print("= Relationship: no")
        else:
            print("= Relationship: unknown")
    if node.yes:
        print("= yes node defined")
    elif node.no:
        print("= no node defined")
    else:
        print("= This is a leaf node")
   

def print_tree(node: Node, id : str):
    print_node(node, id)
    if node.yes:
        print_tree(node.yes, "yes")
    elif node.no:
        print_tree(node.no, "no")
    


def guess(node : Node) -> Node:
    if not node:
        return None;

    print("--- START OF TREE DUMP ----")
    print_tree(root, "root")
    print("--- END  OF TREE DUMP ----")

   # print_node(node, "guess")
    if(not node.is_leaf()):
        print("{} [y/n]: ".format(node.text))
        yesno = sys.stdin.readline().strip().lower()
        if yesno == "y" and node.yes:
                return guess(node.yes)
        if yesno == "n" and node.no:
                return guess(node.no)
    return node

def add_negative_node(question : str, answer: str, current_node : Node) -> Node:
    question_node = Node(question, current_node)
    if current_node: # Root node case
        current_node.no = question_node
    question_node.yes = Node(answer, question_node)
    return question_node

root = None
done = False
points = 0

while not done:
    print("Think of an animal...")
    # this will return None or a leaf node
    leaf = guess(root)
    if leaf and leaf.is_leaf():
        print_node(leaf, "END")
        print("Oh! Oh! I think I know what it is. Did you think of a {} ? [y/n]".format(leaf.text))
        yesno = sys.stdin.readline().strip()
        if yesno == "y":
            points = points + 1
            print("1 extra point for me! I now have {} points.".format(points))
            continue


    print("I give up! What is it???")
    new_animal_str = sys.stdin.readline().strip()

    print('Please type a question for which the answer would be: {}'.format(new_animal_str))
    question = sys.stdin.readline().strip()

    # is it the first question?
    if not leaf:
        root = add_negative_node(question, new_animal_str, None)
    else:
        add_negative_node(question, new_animal_str, leaf.parent)

    print("I will try to remember a {}".format(new_animal_str))

    print ("Would you like to go again? [y/n]:")
    ans = sys.stdin.readline().strip()
    if ans == "n":
        done = True

print("Thanks for playing!")
