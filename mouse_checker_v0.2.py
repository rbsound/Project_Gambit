# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "Probably got a Mouse"
    
    elif answers == 2:
        print "Maybe got a Mouse"
    
    elif answers == 3:
        print "Sometimes have a Mouse"
    
    elif answers == 4:
        print "Most likely have a Mouse"
    
    elif answers == 5:
        print "Mouse is hiding but there"
    
    elif answers == 6:
        print "Mouse Mouse Mouse"
    
    elif answers == 7:
        print "Yep you got a Mouse"
    
    elif answers == 8:
        print "you have so many Mouses"
