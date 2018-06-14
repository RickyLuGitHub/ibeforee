#!python 3

# the 'i before e except after c' rule
def rule(prompt):
    if ('ei' in prompt):
        if ('cei' not in prompt):
            return False
    if ('ie' in prompt):
        if ('cie' not in prompt):
            return True
    else:
        return True

def check_word(prompt):
    if ('ie' not in prompt) and ('ei' not in prompt):
        return True
        print('$$$')
    else:
        return  rule(prompt)
    
def list_check():
    count = 0
    with open("list.txt", 'r') as words:
        for l in words:
            if not check_word(l):
                count += 1
    return count

# driver program
def main():
    prompt = input("Enter word to check the \" i before e \" rule:\n>> ")
    if prompt == "check list":
        print(list_check())
    elif check_word(prompt):
        print ("true")
    else:
        print ("false")

if __name__ == '__main__': 
    main()

