contacts = [
    {
        "name": "Raman",
        "phone": "9876532112",
        "Conversation":[
            "hi",
            "Hello",
            "This is awesome day",
            "lets go"
        ]
    },
     {
        "name": "Sanam",
        "phone": "9876543218",
        "Conversation":[
            "kese ho",
            "badiya",
            "kithe h",
            "ghare"
        ]
    },
      {
        "name": "mandeep",
        "phone": "98745612399",
        "Conversation":[
            "hor kida",
            "vadia tu ds",
            "kive chl rhe h python",
            "vadia"
        ]
    },
       {
        "name": "shivam",
        "phone": "7894561239",
        "Conversation":[
            "hiiii",
            "hello",
            "nice day",
            "thank you"
        ]
    }
]
search_keyword = input("enter keyword to search:")
print("search keyword", search_keyword)
for contact in contacts:
  #   if contact["name"].lower().startswith(search_keyword.lower()):
   #        if contact["name"].lower().__contains__(search_keyword.lower()):
        if contact["name"].lower().find(search_keyword.lower()) >= 0 \
              or contact["phone"].find(search_keyword.lower()) >= 0: 
                  print(contact)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
#implement search on conversation as well as

