import boto3
import base64
import json
import os


rekognition_client= boto3.client('rekognition')

file= open('katy.jpeg','rb').read()

response= rekognition_client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)

for face in response['FaceDetails']:

    if (int(face['AgeRange']['High'])< 24):
        if (face['Gender']['Value']=='Male'):
            print ('There is a young boy in the picture.')
        else:
            print('There is a young girl in the picture.')
    else:
        if(face['Gender']['Value']=='Male'):
            print('There is a man in the picture.')
        else:
            print('There is a women in the picture.')

    if (face['Gender']['Value']=='Male'):
        gender_pronoun= 'He'
        gender_possessive= 'His'
    else:
        gender_pronoun= 'She'
        gender_possessive = 'Her'

    print(str(gender_possessive) + ' age range looks between ' + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + ' years old.')
    

    if ( str(face['Smile']['Value']) == 'True'):
        print(str(gender_pronoun) + ' is smiling in the picture.')
    else:
        print(str(gender_pronoun) + ' is not smiling in the picture.')
    
    
    if(str(gender_pronoun) == 'He'):
        if (str(face['Beard']['Value']) == 'True'):
            print('He has a beard too.')
        else:
            print(' He doesnt have a beard.')

    if(str(face['Sunglasses']['Value']) == 'True') :
        print(gender_pronoun + ' is wearing a Sunglasses.' )
    else:
       print(gender_pronoun + ' is not wearing Sunglasses.' ) 

    max_conf= 0
    emotion = 'none'
    for key in face['Emotions']:
        # print (key['Confidence'])
        if key['Confidence'] > max_conf:
            max_conf = key['Confidence']
            emotion= key['Type'].lower()

    print(gender_pronoun + ' is looking very ' + emotion+ ' in the picture.')