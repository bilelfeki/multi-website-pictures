from PIL import Image
import os

def resizePerfectly(inittialSize,targetSize):
    coefInitialSize=inittialSize[0]/ inittialSize[1]
    return getEnhancedTargetSize(targetSize,coefInitialSize)


def getEnhancedTargetSize(targetSize,coef):
  return (targetSize[0],int(targetSize[0]/coef)) 

def getExtension(imageName:str):
     return  imageName.split('.')[len(imageName.split('.'))-1]

def getInsideDirectory(directoryName:str):
     return os.listdir('./'+ str(directoryName))

def filterOnlyDirectories(elementsInsideDirectory:list):
    directoryList=[]
    for file in elementsInsideDirectory:
          if(os.path.isdir('./'+ str(file))):
               directoryList.append(file)
    return directoryList

directories = filterOnlyDirectories(os.listdir('./'))
print(directories)

#Electronic Parapharmacie ...
for directory in directories: 
    #Coverture - products
    subdirectories= getInsideDirectory(directory)
    index=0
    for subdirectory in subdirectories:
        print(subdirectory)
        if(subdirectory=='products'):
            enhancedSize=(500,300)
        else:
            enhancedSize=(1800,737)
        print(enhancedSize)
        #every image inside the folder
        repoImagesPath='./'+directory +'/'+subdirectory
        os.makedirs('enhanced/'+directory+'/'+subdirectory)
        for image in getInsideDirectory(repoImagesPath): 
            print(image)
            referenceImage = Image.open(repoImagesPath+'/'+image)
            enhancedSize=resizePerfectly(referenceImage.size,enhancedSize)
            enhancedImage = referenceImage.resize(enhancedSize)
            enhancedImage.save('enhanced/'+directory+'/'+subdirectory+'/'+image)
    
    