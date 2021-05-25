 
def gender(response):
    for x in response['FaceDetails']:
        return('Person is ' + str(x['Gender']['Value']))
    
def age(response):
    for x in response['FaceDetails']:
        return('Person must be ' + str(x['AgeRange']['Low'])+" to "+str(x['AgeRange']['High'])+' years \n')
    
def Mustache(response):
    for x in response['FaceDetails']:
        if (str(x['Mustache']['Value'])=='True'):
            return("Person has Mustache\n")
        else:
            return("Person doesn't have Mustache\n")

def smile(response):
    for x in response['FaceDetails']:
        if (str(x['Smile']['Value'])=='True'):
            return("Person is smiling\n")
        else:
            return("Person doesn't seem smiling\n")
        
def Beard(response):
    for x in response['FaceDetails']:
        if (str(x['Beard']['Value'])=='True'):
            return("Person has Beard\n")
        else:
            return("Person doesn't have Beard\n")

def Glass(response):
    for x in response['FaceDetails']:
        if (str(x['Sunglasses']['Value'])=='True'):
            return("Person is wearing Sunglasses\n")
        else:
            return("Person isn't wearing Sunglasses\n")

        
def Emotion(response):
    for x in response['FaceDetails']:
        for emotion in x['Emotions']:
            return(str(emotion['Type']) + " by " + str(emotion['Confidence']) +" %")
    
