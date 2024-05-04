info_messages = {
      "staticAttributeMsg": "this is a static attribute from Super class",
      'instanceAttributeMsg': 'this is an instance attribute from Super class',
      'methodMsg': 'this is a method from Super class',
      'exampleNumberValue': 1,
      'exampleNullValue': None,  
   }

def get_info_messages(class_name):
    info_messages = {
      "staticAttributeMsg": f"this is a static attribute from {class_name} class",
      'instanceAttributeMsg': f'this is an instance attribute from {class_name} class',
      'methodMsg': f'this is a method from {class_name} class',
      'exampleNumberValue': 1,
      'exampleNullValue': None,     
   }
    
    return info_messages