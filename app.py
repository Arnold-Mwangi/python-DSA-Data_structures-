def is_balanced(expression):
    opening = []
    condition = True

    if len(expression) % 2 != 0:
        return False

    for char in expression:
        if condition:
            if char in "[{(":
                opening.append(char)
            elif char in "]})": 
                last = opening.pop()           
                if char == "}":
                    condition = last == '{'
                    
                elif char == "]":
                    condition = last == '['
                elif char == ")":
                    condition = last == '('
            
    return condition

expression1 = "()]{}"
expression2 = "([)??]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 



def  remove_duplicates(sequence):
    list = []

    for num in sequence:
        if list.count(num) < 1:
            list.append(num)
    return list
sequence = [1,1,2,3,3,3,3,4,4,5]
print(remove_duplicates(sequence))


def word_frequency(sentence):
    words = sentence.split()
    result =[ word.strip(".?,") for word in words]

    return {word: result.count(word) for word in result}



sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


