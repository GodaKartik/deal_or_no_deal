from random import shuffle
from time import sleep

def RMS(list):
    sq_sum=0
    for item in list:
        sq=item**2
        sq_sum+=sq
    sq_mean=sq_sum/len(list)
    rms=sq_mean**(1/2)
    return rms

def Sort(list):
    global str_to_nums
    str_to_nums=[]
    for string in list:
        str_to_nums.append(int(string))
    return sorted(str_to_nums)

cases=[str(num) for num in range(1,24)]
shuffle(cases)
values=[10,20,30,40,50,60,70,80,90,100,200,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,50000]
shuffle(values)
case_value={}
for i in range(len(cases)):
    case_value[cases[i]]=values[i]

start=input("DEAL OR NO DEAL\n\nTYPE START TO START THE GAME-  ")
print("\n\nGame starts in..")
for sec_1 in range(5,0,-1):
    print(f"{sec_1}", end="..")
    sleep(1)

print("\n\nPick You Case \n")
your_case=input("your case- ")
cases.remove(your_case)

for rounds in range(6,1,-1):
    print(" \n\n")
    print(f"PICK {rounds} CASES\n")
    for ind_round in range(rounds):
        case=input(f"\npick case number {ind_round+1}- ")
        for sec_2 in range(3,0,-1):
            print(f"{sec_2}", end="..")
            sleep(1)
        print("\n",case_value[case],"\n")
        values.remove(case_value[case])
        cases.remove(case)
        print(f"cases left: {Sort(cases)}")
        print(f"\n You still have {sorted(values)} left \n")
    sleep(2)
    print("\n Banker's Deal \n")
    banker_deal=round(RMS(values),2)
    print(f"your banker offers {banker_deal} \n")
    d_nd=input("deal or no deal? ")
    if d_nd=="deal":
        print("\n YOU WON {} !! CONGRATS !!!!".format(banker_deal))
        break
    sleep(3)

if d_nd=="deal":
    pass
else:
    case=input("\nPICK 1 CASE- ")
    for sec in range(3,0,-1):
        print(f"{sec}", end="..")
        sleep(1)
    print()
    print(case_value[case],"\n")
    values.remove(case_value[case])
    cases.remove(case)
    print(f"cases left: {Sort(cases)}")
    print(f"\n You still have {sorted(values)} left \n")
    
if d_nd=="deal":
    pass
else:
    swap=input(" DO you wanna open your case or swap cases? ")
    if swap=="my case":
        print(f"\nYOU WON {case_value[your_case]}!! CONGRATS!!")
    else:
        caseleft=cases[0]
        print(f"\nYOU WON {case_value[caseleft]}!! CONGRATS!!")   
