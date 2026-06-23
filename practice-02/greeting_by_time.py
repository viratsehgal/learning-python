def greeting_output(time_input):
  if time_input < 12:
      print("Good Morning")
  elif time_input < 18:
      print("Good Afternoon")
  elif  time_input < 24:
      print("Good Evening") 
  else:
      print("Error")
      

hour = int(input("Enter the time: "))
greeting_output(hour)