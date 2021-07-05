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
        next_day = True
        next_day_counter+=1
      else:
        pm_am= "PM"

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

  #formating the output time
  if(len(str(new_hour))<2 and len(str(new_minutes))==2):
    new_time = "0" + str(new_hour) + ":" + str(new_minutes) + " " + pm_am
    
  elif(len(str(new_hour))<2 and len(str(new_minutes))<2):
    new_time = "0" + str(new_hour) + ":" + "0" + str(new_minutes) + " " + pm_am
  
  elif(len(str(new_hour))==2 and len(str(new_minutes))<2):
    new_time = str(new_hour) + ":" + "0" + str(new_minutes) + " " + pm_am

  elif(len(str(new_hour))==2 and len(str(new_minutes))==2):
    new_time = str(new_hour) + ":" + str(new_minutes) + " " + pm_am

  #Add weekday to output if specified and number of days later
  if(day != ""):
    new_time += ", " + day
  elif(day != "" and next_day ==True and next_day_counter != 1):
    new_time += ", " + day +"(" + next_day_counter + " days later)"
  elif(day != "" and next_day ==True and next_day_counter == 1):
    new_time += ", " + day +"(next day)"
  elif(next_day ==True and next_day_counter != 1):
    new_time += " (" + str(next_day_counter) + " days later)"
  elif(next_day ==True and next_day_counter == 1):
    new_time +=" (next day)"



  return new_time