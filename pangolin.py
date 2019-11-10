import sys
import typing


class Node(object):
    def __init__(self, text: str, parent):
        self.text = text
        self.parent = parent
        self.yes = None
        self.no = None

    def is_leaf(self) -> bool:
        if  self.yes == None  and self.no == None:
            return True
        else:
            return False

    def __str__(self):
        return self.text

def get_yes_no_answer(question : str) -> str:
    while True:
        print("{} [y/n] ".format(question))
        ans = sys.stdin.readline().strip()
        if ans == "t":
            print_tree(root)
        if ans == "y" or ans == "n":
            return ans

def print_node(node: Node, tag: str):
    print("===============================")
    print("= Node text: ({}) {}".format(tag, node.text))
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


def print_tree(node: Node, tag: str):
    print_node(node, tag)
    if node.yes:
        print_tree(node.yes, "yes")
    elif node.no:
        print_tree(node.no, "no")


def guess(node: Node) -> Node:
    if not node:
        return None;

    if node.is_leaf():
        return node

    # print_node(node, "guess")
    yesno = get_yes_no_answer(node.text)
    if yesno == "y" and node.yes:
        return guess(node.yes)
    if yesno == "n" and node.no:
        return guess(node.no)

    # else return the current node, not this may not be a leaf node
    return node


def handle_give_up(question: str, answer: str, current_node: Node) -> Node:
    question_node = Node(question, current_node)
    current_node.no = question_node
    question_node.yes = Node(answer, question_node)
    return question_node


# here we want to insert a new node between the parent and the current node
# the current node needs to become the negative answer to the
# new question.
def handle_wrong_guess(question: str, answer: str, current_node: Node) -> Node:
    parent = current_node.parent

    new_question_node = Node(question, parent)

    # save old yes answer
    old_yes = parent.yes

    parent.yes = new_question_node

    new_question_node.no = old_yes
    new_question_node.yes =  Node(answer, new_question_node)
    return new_question_node



root = None
done = False
points = 0

# bootstrap the model cause I'm too lazy to handle the empty case
root = Node("is it a mammal?", None)
dog = Node("dog", root)
root.yes = dog
handle_wrong_guess("does it live in the ocean?", "dolphin", dog)


while not done:
    get_yes_no_answer("Think of an animal... Are you ready?")
    node = guess(root)
    if node.is_leaf():
        print("Oh! Oh! I think I know what it is. Did you think of a {} ? [y/n]".format(node.text))
        yesno = sys.stdin.readline().strip()
        if yesno == "y":
            points = points + 1
            print("1 extra point for me! I now have {} points.".format(points))
            continue

    print("I give up! What is it???")
    new_animal_str = sys.stdin.readline().strip()

    print('Give me a yes/no type question for which the answer would be yes for {}'.format(new_animal_str))
    question = sys.stdin.readline().strip()

    if node.is_leaf():
        handle_wrong_guess(question, new_animal_str, node)
    else:
        handle_give_up(question, new_animal_str, node)

    print("I will try to remember a {}.".format(new_animal_str))

    print("Would you like to go again? [y/n]:")
    ans = sys.stdin.readline().strip()
    if ans == "n":
        done = True

print("Thanks for playing!")
