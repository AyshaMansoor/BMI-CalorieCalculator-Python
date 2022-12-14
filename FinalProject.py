# CALCULATE BMI, DAILY CALORIES REQUIRED. SUGGEST DIETARY AND EXERCISE OPTIONS.

print("Calculate your BMI and calorie intake, let's get started.")

a = 1
gender = 0
while a:
  gender = input("Please state your gender- male/female: ").lower()
  if gender == 'male' or gender == 'female':
    a =0
  else:  
    print("Wrong input")

b =1
age = 0
while b:
  age = input("Enter your age in numbers: ")                        # Taking user inputs of age, height, weight and gender through a while loop to make sure the user
  if age.isalpha() == False and int(age) <= 120:                                          # gets to re-enter the correct form of inputs. The right data type/input is necessary to proceed with the calculations and 
    b =0                                                               # program execution
  else:  
   print("Please enter a proper and numeral age value")

c= 1
height = 0
while c:
  height = input("Enter your height in metres: ")
  if height.isalpha() ==False:
    c =0
  else:
    print("Please enter a numeral value")


d = 1
weight = 0
while d:
  weight = input("Enter your weight in kg: ")        
  if weight.isalpha() == False:
    d =0
  else:
    print("Enter a numeral value")


bmi = float(weight)/(float(height))**2
result = round(bmi,2)
print("Your body mass index(BMI) is: ", result)                          # Calculating BMI
if result <= 18.9:
  print("Your BMI is below the normal range.")
elif result >= 24.9:
  print("Your BMI is above the normal range.")
else:
  print("Your BMI is within the normal range.")                         # Calculating range of BMI( Normal, Underweight, Overweight)

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

image = mpimg.imread("bmi.jpg")
plt.axis('off')  
plt.imshow(image)                                                 # Displaying the image ( BMI Index chart)
plt.show(block=False)
plt.waitforbuttonpress(0) 
plt.close('all')                                                 # Closing the figure once the user presses the close button(clicks cross)
 
                

print("Based on your BMI, Let's now calculate how much calorie intake do you need per day.You will have to choose a level of activity for this.")
 
bmrw = 655.1 + (9.563 * float(weight)) + (0.01850 * float(height)) - (4.676 * float(age))             # Calculating BMR (basal metabolic rate) 
bmrm = 66.47 + (13.75 * float(weight)) + (0.05003 * float(height)) - (6.755 * float(age))
activity = ['sedentary', 'little active', 'active', 'very active']
print("Different levels of activity are: ",', '.join(activity))                                       # Giving users the levels of activity

i = 1
select = 0

while i :                                                                                                        # Using while loop to calculate select activity and calculate calories. 
  select == activity[0] or select == activity[1] or select == activity[2] or select == activity[3]               #The user will get to re-enter inputs in case it is wrongly done. 
  
  select = input("Please select your level of activity from the 'four options' given above: ").lower()
  
  if gender.lower() == "female"  and  select == activity[0]:
    
   amr = float(bmrw) * 1.2
   amr_round = round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
     
          
  elif gender.lower() == "female" and select == activity[1]:
   amr = float(bmrw) * 1.375
   amr_round = round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
   
  elif str(gender.lower()) == "female" and select == activity[2]:
   amr = float(bmrw) * 1.55
   amr_round =round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
  elif str(gender.lower()) == "female" and select == activity[3]:      # Based on gender and level of activity, calculating calories using the BMR 
   amr = float(bmrw) * 1.725
   amr_round = round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
    
  elif gender.lower() == "male"  and  select == activity[0]:
    
   amr = float(bmrm) * 1.2
   amr_round = round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
     
          
  elif gender.lower() == "male" and select == activity[1]:
   amr = float(bmrm) * 1.375
   amr_round = round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
   
  elif str(gender.lower()) == "male" and select == activity[2]:
   amr = float(bmrm) * 1.55
   amr_round =round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0
  elif str(gender.lower()) == "male" and select == activity[3]:      # Based on gender and level of activity, calculating calories using the BMR 
   amr = float(bmrm) * 1.725
   amr_round = round(amr,2)
   print("Your daily calorie requirement is: ", amr_round)
   i=0

  elif select != activity[0] and select != activity[1] and select != activity[2] and select != activity[3]:
    print("Invalid input, please enter again")


    
class Diet():
  def __init__(self,bmi):                                # Using a Class and functions(lose and gain weight) importing a .txt file to display the dietary suggestions.
    self.bmi = bmi
  def gainweight(self):
    my_file_handle=open("/Users/ayshamansoor/Desktop/gainweight.txt")
    txt = my_file_handle.read()
    print(txt)
      
  def loseweight(self):
    my_file_handle=open("/Users/ayshamansoor/Desktop/loseweight.txt")
    txt=my_file_handle.read()
    print(txt)
      
diet = input("Do you want dietary and exercise suggestions?")   # Taking user input to see if dietary suggestions needed.

                                                                 
if diet.lower() == "yes":
  print("Suggesting options based on your BMI which was: " , result)
  
  bmi1 = result

  if bmi1 <= 18.9:
    p= Diet(bmi1)
    print("Since your BMI is below the normal range, you need to gain weight")
    p.gainweight()                                         # Displaying output(dietary suggestions) by creating object instance of the Diet Class using the gain and lose weight methods/functions
  elif bmi1 >= 24.9:
     p = Diet(bmi1)
     print("Since your BMI is above the normal range, you need to lose weight")
     p.loseweight()
  else:
    
    print("Congrats! Your BMI is within the normal range.You are doing great with maintaining a healthy weight. Continue eating healthy and don't forget to exercise daily!") 
if diet.lower() =="no":
  print("Okay! Wish you good health :)")
