#take input from user

messages = int(input("What are the total number of messages?"))
normal = int(input("What are the total number of normal messages?"))
spam = int(input("What are the total number of spam messages?"))


#probability = desired/total

prob_normal = normal/messages
prob_spam = spam/messages


#type your message you want to find if it is a spam or is normal

message = input("What is the message you want to type?")

#function defined for total desired output

def prob(m):
    
    #split sentences into words
    
    w = m.split()

    #To introduce pseudocounts and to make sure that the probability is never zero 
    #we intialize the number of letters of each word to one.
    #then we start to add the number of words actually found in the training data set.
    
    #initial data for normal
    
    n = {
        'Dear':1+8,
        'Friend':1+5,
        'Lunch':1+3,
        'Money':1+1,
    }
    sum_n = 0
    for x in n:
        sum_n = sum_n + n[x]
    
    #initial data for spam
    
    s = {
        'Dear':1+2,
        'Friend':1+1,
        'Lunch':1+0,
        'Money':1+4,
    }
    sum_s = 0
    for y in s:
        sum_s = sum_s + s[y]
    
    #initializing a dictionary to all zeros because initially all words found are zero
    
    f = {
        'Dear':0,
        'Friend':0,
        'Lunch':0,
        'Money':0,
    }
    
    #finding the number of words in the message and updating the intialized dictionary
    
    for i in w:
        f[i] = f[i] + 1
    
    #calculating the probability of the normal
    
    probability_normal = prob_normal
    
    for j in f:
        probability_normal = probability_normal*pow(n[j]/sum_n,f[j])
    
    #calculating the probability of spam
    
    probability_spam = prob_spam
    
    for k in f:
        probability_spam = probability_spam*pow(s[k]/sum_s,f[k])
    
    #printing calculated probabilities 
    
    print("Your probability of normal message is ",probability_normal)
    print("Your probability of spam message is ",probability_spam)
    
    #comparing probabilities and returning the final result
    
    if probability_spam>probability_normal:
        return "Spam"
    elif probability_spam<probability_normal:
        return "Normal"
    else:
        return "Mail"

#calling function for output

print(prob(message))