countries = {
    "USA":{"California":{"Los Angeles":4000000,"Sanfrancisco":8700000}},
    "Canada":{"Ontario":{"Toronto":2930000,"Ottawa":994837}}
}
#country = input("Enter the country: ")
#State = input("Enter the state: ")
for county in countries.items():
   # if county in countries[country]["California"]:
       # if county in countries[country]["Canada"]:
            print(county)
for city in countries["USA"].items():
       print(city)