def add_time(start, duration, day =""):
  #split into time and pm/am 
  new_time=0
  next_day = False
  next_day_counter = 0

  #Get time and duration from input string
  time, pm_am = start.split(" ")
  start_hour, start_minutes = time.split(":")
  duration_hours, duration_minutes = duration.split(":")
  pm_am = pm_am.strip()
  start_hour = start_hour.strip()
  start_minutes = start_minutes.strip()

  '''print(start_hour)
  print(start_minutes)
  print(duration_hours)
  print(duration_minutes)
  print(pm_am + "\n")'''

  if(pm_am == "PM"):
    new_minutes = int(start_minutes) + int(duration_minutes)
    new_hour = int(start_hour) + int(duration_hours)
    while(new_minutes >= 60):
      new_minutes = new_minutes - 60
      new_hour = new_hour + 1
    while(new_hour >= 12):
      new_hour = new_hour - 12
      if(pm_am == "PM"):
        pm_am = "AM"
      else:
        pm_am= "PM"

    '''print(new_hour)
    print(new_minutes)
    print(pm_am + "\n")'''

  elif(pm_am == "AM"):
    new_minutes = int(start_minutes) + int(duration_minutes)
    new_hour = int(start_hour) + int(duration_hours)
    while(new_minutes >= 60):
      new_minutes = new_minutes - 60
      new_hour = new_hour + 1
    while(new_hour >= 12):
      new_hour = new_hour - 12
      pm_am = "PM"

  #rewrite 0 AM/PM to 12AM/PM
  if(new_hour == 0):
    new_hour = 12

  '''
  print(new_hour)
  print(new_minutes)
  print(pm_am + "\n")
  '''

  #formating the output time
  if(len(str(new_hour))<2 and len(str(new_minutes))==2):
    new_time = "0" + str(new_hour) + ":" + str(new_minutes) + " " + pm_am
    
  elif(len(str(new_hour))<2 and len(str(new_minutes))<2):
    new_time = "0" + str(new_hour) + ":" + "0" + str(new_minutes) + " " + pm_am
  
  elif(len(str(new_hour))==2 and len(str(new_minutes))<2):
    new_time = str(new_hour) + ":" + "0" + str(new_minutes) + " " + pm_am

  elif(len(str(new_hour))==2 and len(str(new_minutes))==2):
    new_time = str(new_hour) + ":" + str(new_minutes) + " " + pm_am

  #Add weekday to output if specified
  if(day != ""):
    new_time += ", " + day

  return new_time