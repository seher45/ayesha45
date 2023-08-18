min_age_at_school =4
ayesha_age = input ("how old is ayesha?")
ayesha_age = int (ayesha_age)
#can hammad go to school?
if (ayesha_age == min_age_at_school):
    print ("yes, she can go to school")

elif (ayesha_age>6):
    print ("she must go to heigher school")

elif(ayesha_age<=2):
     print("no one should be allowed in his age group!")


else:
    print("no, she cannot go to school")