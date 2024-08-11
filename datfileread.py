file =open("note.txt","r",encoding="utf-8")
file_content=file.read()
print(file_content)
print(file_content.find("Number of Announcements Played on SIP MS"))
# if file_content.find() =="Number of Announcements Played on SIP MS":
#     print(file_content)