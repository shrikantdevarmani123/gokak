class string1:
     def reverse_names(name):
        mylist = name.split(" ")
        new_name=""
        for i in mylist:
                    # print(i)
                    rever_name=""
                    for a in i:
                         # print(a)
                        rever_name=a+rever_name
                    new_name=new_name+" "+rever_name
        print(new_name)

string1.reverse_names("radisys com shiv nikh")
         



