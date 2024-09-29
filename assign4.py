import re

def validate(check_type, check_string):
    PATTERN_NAME = re.compile(r"[A-Za-z]+(?:[ '-][A-Za-z]+){0,3}$")
    PATTERN_MOBILE = re.compile(r'^[789]\d{9}$')
    PATTERN_PAN = re.compile(r'^[A-Z]{5}\d{4}[A-Z]$')
    PATTERN_AADHAAR = re.compile(r'^2+(\d{4}[- ].?){3}$')

    validation_types = {
    'name': {"pattern": PATTERN_NAME,
             "success": "Name is valid.",
             "failure": "Name is not valid!"},

    'mobile': {"pattern": PATTERN_MOBILE,
               "success": "Mobile number is valid.",
               "failure": "Mobile number is not valid!"},

    'pan': {"pattern": PATTERN_PAN,
            "success": "PAN number is valid.",
            "failure": "PAN number is not valid!"},

    'aadhaar': {"pattern": PATTERN_AADHAAR,
                "success": "Aadhaar number is valid.",
                "failure": "Aadhaar number is not valid!"}
    }
    
    validation = validation_types[check_type]["pattern"]
    

    if re.match(validation,check_string):
        return validation_types[check_type]['success']
    else:
        return validation_types[check_type]['failure']


choice = int(input("Do you want to enter information 1/0?"))

while choice == 1:
        
    print("Validate Name")
    print(validate("name", input("Name: ")))


    print("Validate PAN")
    print(validate("pan", input("PAN: ")))


    print("Validate Aadhaar Number")
    print(validate("aadhaar", input("Aadhaar Number: ")))

    choice = int(input("Do you want to enter information 1/0?"))

        
           
        
