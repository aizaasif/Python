with open("practice.txt","r") as f:
   data=f.read()

word="aiza"

if data.find(word)!=-1:
    print("Word Found")
   
else:
   print("Not found")

   


# new_data=data.replace("java","python")

# with open("practice.txt","w") as f:
#    f.write(new_data)