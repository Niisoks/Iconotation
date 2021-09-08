from PIL import Image
import os

extension = '.png'

imageDict = {}
imageList = ['1','2','3','4','NULL','6','7','8','9',
             '>','+','a','b','c','d','[','j','*',
             'h','v','r','x']


def open_images_into_dictionary(imageList, imageDict):
    for x in range(len(imageList)):
        currentMove = imageList[x]
        imageDict[currentMove] = Image.open(path + str(x + 1) + extension)
        print('opening:' + path + str(x + 1) + extension)

def generate_image(userInput):
    dst = Image.new('RGB', (len(userInput[0]) * 20, len(userInput) * 30)) 
    for i in range(len(userInput)):
        for z in range(len(userInput[i])):
            dst.paste(imageDict[userInput[i][z]],(20 * z , 30 * i))

    dst = dst.resize((dst.width * 2, dst.height * 2), resample=None, box=None, reducing_gap=None)
    dst.save(path + 'output.png')
    

def generate_valid_inputs(userInput):
    emptyList = []
    for i in range(len(userInput)):
        if userInput[i] in imageDict:
            emptyList.append(userInput[i])
        else:
            print('command ' + userInput[i] + ' not recognised - removing')

    return emptyList

def chunks(L, n): return [L[x: x+n] for x in range(0, len(L), n)]

while True:
    try:
        path = input('input path to images e.g /home/usr/images/ :  ')
        open_images_into_dictionary(imageList, imageDict)
    except FileNotFoundError:
        print('No PNGs in stated directory (make sure you have a / at the end)')
        continue
    break

userInput = list(input('insert combo').lower())
userInput = generate_valid_inputs(userInput)
userInput = chunks(userInput, 30)
print(userInput)
generate_image(userInput)
