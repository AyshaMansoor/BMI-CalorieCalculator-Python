# CALCULATE BMI, DAILY CALORIES REQUIRED. SUGGEST DIETARY AND EXERCISE OPTIONS.

print("Calculate your BMI and calorie intake, let's get started.")
gender = input("Please state your gender: ")
age = int(input("Enter your age in numbers: "))
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kg: "))            # Taking user input
bmi = weight/(height)**2
result = round(bmi,2)
print("Your body mass index(BMI) is: ", result)                # Calculating BMI
if result <= 18.9:
  print("Your BMI is below the normal range, you need to gain weight!")
elif result >= 24.9:
  print("Your BMI is above the normnal range, you need to lose weight")
else:
  print("Your BMI is within the normal range!")  # Calculating range of BMI( Normal, Underweight, Overweight)

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

image = mpimg.imread("bmi.jpg")
plt.imshow(image)                   # Displaying the image ( BMI Index chart)
ax = plt.subplot(111)         


# Hide the right and top spines
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)
ax.spines.left.set_visible(False)

# Hiding the ticks
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks(color='w')
plt.yticks(color='w')
a = plt.gca()
xax = a.axes.get_xaxis()
xax = xax.set_visible(False)
yax = a.axes.get_yaxis()
yax = yax.set_visible(False)

# Closing the figure once the user presses the close button(clicks cross) 
plt.show(block=False)
plt.waitforbuttonpress(0) 

plt.close('all')


print("Based on your BMI, Let's now calculate how much calorie intake do you need per day.You will have to choose a level of activity for this.")
activity = ['sedentary', 'little active', 'active', 'very active']
print("Different levels of activity are: ",', '.join(activity))                                       # Selecting level of activity from a list
select = input("Please select an option from the above: ").lower()
select == activity[0] or select == activity[1] or select == activity[2] or select == activity[3]
bmrw = 655.1 + (9.563 * float(weight)) + (0.01850 * float(height)) - (4.676 * float(age))             # Calculating BMR (basal metabolic rate) 
bmrm = 66.47 + (13.75 * float(weight)) + (0.05003 * float(height)) - (6.755 * float(age))
if gender.lower() == "female"  and  select == activity[0]:
  amr = float(bmrw) * 1.2
  amr_round = round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
elif gender.lower() == "female" and select == activity[1]:
  amr = float(bmrw) * 1.375
  amr_round = round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
elif str(gender.lower()) == "female" and select == activity[2]:
  amr = float(bmrw) * 1.55
  amr_round =round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
elif str(gender.lower()) == "female" and select == activity[3]:      # Based on gender and level of activity, calculating calories using the BMR 
  amr = float(bmrw) * 1.725
  amr_round = round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
if gender.lower() == "male"  and  select == activity[0]:
  amr = float(bmrm) * 1.2
  amr_round = round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
elif gender.lower() == "male" and select == activity[1]:
  amr = float(bmrm) * 1.375
  amr_round = round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
elif str(gender.lower()) == "male" and select == activity[2]:
  amr = float(bmrm) * 1.55
  amr_round =round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
elif str(gender.lower()) == "male" and select == activity[3]:
  amr = float(bmrm) * 1.725
  amr_round = round(amr,2)
  print("Your daily calorie requirement is: ", amr_round)
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
  
  bmi1 = float(input("Enter your BMI: "))

  if bmi1 <= 18.9:
    p= Diet(bmi1)
    p.gainweight()                   # Displaying output(dietary suggestions) by creating object instance of the Diet Class using the gain and lose weight methods/functions
  elif bmi1 >= 24.9:
     p = Diet(bmi1) 
     p.loseweight()
  else:
    print("Congrats! You are doing great with maintaining a healthy weight. Continue eating healthy and don't forget to exercise daily!") 
if diet.lower() =="no":
  print("Okay! Wish you good health :)")
