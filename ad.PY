# python code to advertise 3 colleges in mcpherson university and their department

# dictionary showing colleges and their each department

mcpherson_university = {
    "College of Computing (COLCOM)":[
        "Software Engineering",
        "Cyber Security",
        "Data Science",
        "Information Technology"
    ],

    "College of Natural and Applied Science (COLNAS)":[
        "Microbiology",
        "Biochemistry",
        "Biotechnology"
    ],

    "College of Humanities, Social amd Management Sciences (COHSMAS)":[
        "Mass Communication",
        "International Relation",
        "Accounting",
        "Business Administration"
    ]
}


print("Welcome to Mcpherson University!")
for college, department in mcpherson_university.items():
    print(f"\n{college}")
    for i,department in enumerate(department,start=1):
        print(f"{i}.{department}")
    
