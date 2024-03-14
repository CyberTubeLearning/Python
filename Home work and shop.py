# Store Bill system.

print("F square")
customer_name = input("customer name: ")
number_of_items = int(input("number of items :"))
birthday_month = input("enter your birthday month : ")
memebership = input("Do you have mambership card : ")
total =0
for i in range(number_of_items):
    product_name = input("product name : ")
    price = float(input("price of product:"))
    total +=price
print("total amount",total)

if birthday_month=="yes":
    print("your today discount is 2%")
    dic=total/100*2
    final_amount=total-dic
    print("final_amount is :",final_amount)
else:
    birthday_month=0
if  memebership =="yes":
    print("your today discount is 5%")
    dic=total/100*5
    final_amount=total-dic 
    print("final_amount is :",final_amount)   
else:
     memebership=0
if total>=4000:
    print("your  discount is 15%")
    dic = total/100*15
    final_amount = total-dic
    print("final_amount is:",final_amount)
else:
     total <=4000
     print("you can't get any discount") 
    

# Home making cost?
def Home_making_cost(h):
    h=0
bhk=int(input("how many bhk house are needed : "))
if bhk==1 and bhk<=2:
        land_cost=800000
        persquarefeet=800
        squarefeet=land_cost/persquarefeet
        basic_furniture_cost =90000
        electrical_applienece=40000
        labur_cost=80000
        row_material=250000
        total=(land_cost,basic_furniture_cost,electrical_applienece,labur_cost,row_material)
        total=sum(total)
        print("totalcost of home making is :",total)
elif bhk==2 and bhk<=3:
        land_cost=1200000
        persquarefeet=800
        squarefeet=land_cost/persquarefeet
        basic_furniture_cost=100000
        electrical_applienece=45000
        labur_cost=90000
        row_material=320000
        total=(land_cost,basic_furniture_cost,electrical_applienece,land_cost,row_material)
        total=sum(total)
        print("total cost of home making is :",total)

Home_making_cost(0)
def home_making_cost(h):
     furniture=input("do you want fully furnished:")
     if furniture=="yes":
          fully_furnished=250000
          total_cost=total+fully_furnished
          print("total cost of home making and fully furnished:",total_cost)
     else:
          furniture=="no"
          no_furniture=0
          total_cost=total+no_furniture
          print("total cost of home making furnished:",total_cost)
home_making_cost(0)