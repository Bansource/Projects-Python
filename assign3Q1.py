"""
N = int(input("How many names: "))             # number of names

for i in range(N):
    person = input("Please enter a name: ")          # person
    print(f"Hi, {person}. Thank you for being a part of my program!")



Lines = int(input("How many lines? "))
Length = int(input("Length of the lines? "))
S = input("Enter a Symbol:")
print()

for i in range(Lines):
    print(S * Length)



# Write your program here
total_p = 330           # Total US Popualtion = 330 million
vac_p = 40              # Vaccinated Popualtion = 40 million
rate = 1.5              # "DAILY" Vaccination Rate = 1.5 million/day
#increment_Q = 40
#period = float(input("Target time period ( in weeks): "))
increment_Q = float(input("Enter the Percent Daily Increase Rate: "))

# Percentage of US Population Vaccinated at the end of the input period
# final = current + 100N + QN(N-1)/2
dvr = (vac_p + rate*(i*7) + rate * (increment_Q/100) *(i*7)* (((i*7)-1)/2))/total_p*100
perc_vac =  ((vac_p + rate * (i)) / total_p) * 100
"""
#increment_Q = 40
#period = float(input("Target time period ( in weeks): "))
increment_Q = float(input("Enter the Percent Daily Increase Rate: "))
for i in range(10,21):
    total_p = 330           # Total US Popualtion = 330 million
    vac_p = 40              # Vaccinated Popualtion = 40 million
    rate = 1.5              # "DAILY" Vaccination Rate = 1.5 million/day


# Percentage of US Population Vaccinated at the end of the input period
# final = current + 100N + QN(N-1)/2
    dvr = (vac_p + rate*(i) + rate * (increment_Q/100) *(i)* (((i)-1)/2))/total_p*100  # dvr from part b
    perc_vac =  ((vac_p + rate * (i)) / total_p) * 100
    dvrprob1 = float(((80*total_p/100)-vac_p)/(i)) # the dvr from part a
    print(f"On September {i}, {(rate + dvrprob1): .3f} million were vaccinated")
print()
print(f"By September {20}, {dvr: .3f} % of the population is vaccinated")