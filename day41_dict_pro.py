website_info = input("please input website info:")
website_info = website_info.split(" ")

website_dict = {"website_name":website_info[0],"website_url":website_info[1],"website_descrip":website_info[2],"website_rate":website_info[3]}

for key,value in website_dict.items():
    print(key,value)