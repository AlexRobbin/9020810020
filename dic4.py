course = {
   "title" : "python learn",
    "teacher" : " davoud moghimi",
    "time" : 20,
    "videocount" : 30,
    "tag" : ["python", "python language", "python learn"],
    "py part" :[
    {
        "parts" : "part1",
        "time" : 5
    },
    {
        "parts" : "part2",
        "time" : 4
    },
    {
        "parts" : "part3",
        "time" : 6
    }
    
    
    
    ],
    "shotLink" : "@faradars",
    "relatedCourse" : [
        {
            "title" : "java",
            "teacher" : " reza irani",
            "time" : 15,
            "videocount" : 10,
            "tag" : ["java", "java language", "java learn"],
            "shotLink" : "@faradars"
            
        },
        {
            "title" : "c#",
            "teacher" : " amir gaemi",
            "time" : 10,
            "videocount" : 12,
            "tag" : ["c#", "c# language", "c# learn"],
            "shotLink" : "@faradars",
            
        }
    ]
}


for related in course["relatedCourse"]:
    print(related["title"])
    


print("------------------------")


totalplus = 0
for plustime in course["py part"]:
    totalplus += plustime["time"] 
print(totalplus)
    