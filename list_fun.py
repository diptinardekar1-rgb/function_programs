Mi_2025=["Naman Dhir", "Ryan Rickelton","Sherfane Rutherford","Rohit Sharma","Suryakumar Yadav", "Raj Bawa","Corbin Bosch","Will Jacks","Hardik Pandya"
"Mitchell Santner","Tilak Varma", "Jasprit Bumrah"]
 


Rcb_2025=["Virat Kohli","Rajat Patidar","Josh Hazlewood","Yash Dayal","Swapnil Singh","Swastik ChikarTim David","Bhuvneshwar Kumar","Jitesh Sharma","Liam Livingstone"
"Nuwan Thushara"]



pbks_2025=["Aaron Hardie","Arshdeep Singh","Azmatullah Omarzai","Glenn Maxwell","Harnoor Singh","Harpreet Brar","Josh Inglis","Kuldeep Sen",
"Kyle Jamieson","Lockie Ferguson","Marco Jansen"]


Gt_2025=["Shubman Gill","Anuj Rawat", "Arshad Khan","Gurnoor Brar","Ishant Sharma","Jayant Yadav","Jos Buttler","Kagiso Rabada","Kumar Kushagra",
"Manav Suthar","Mohammed Siraj"]


print(Mi_2025,Rcb_2025,pbks_2025,Gt_2025)

def add_ipl_teams(team1, team2):
    ipl_teams = []
    ipl_teams.append(team1)
    ipl_teams.append(team2)
    return ipl_teams

# Function call
teams = add_ipl_teams("Mi_2025", "Rcb_2025")
print(teams)





       
def print_s_players(Mi_2025):
    for player in Mi_2025:
        if player.lower().startswith('s'):
            print(player)                                   #Sherfane Rutherford
                                                            Suryakumar Yadav
            
            
print_s_players(Mi_2025) 



def len_plyar(Mi_2025)
    for i in range(0,len(Mi_2025)):
        if i%2 ==1:
            print(i,"------>",Mi_2025[i])
            
len_plyar(Mi_2025)                             #1 ------> Ryan Rickelton
                                               3 ------> Rohit Sharma
                                                5 ------> Raj Bawa
                                                7 ------> Will Jacks
                                                9 ------> Tilak Varma


def pop(listname,index):
    bin = listname.pop(index)
    return bin

a =pop(Rcb_2025,0)
print(f"popped element : {a}")                #virat Kohli

def append(listname,plyar):
    listname.append(plyar)
    return listname

b = append(Mi_2025,"sarthak patil")
print(b)




 
         