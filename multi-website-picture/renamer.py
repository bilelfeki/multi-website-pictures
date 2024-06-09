import os

def getExtension(imageName:str):
     return  imageName.split('.')[len(imageName.split('.'))-1]

def getInsideDirectory(directoryName:str):
     return os.listdir('./'+ str(directoryName))

def filterOnlyDirectories(elementsInsideDirectory:list):
     for file in elementsInsideDirectory:
          if(os.path.isfile('./'+ str(file))):
               elementsInsideDirectory.remove(file)
          return elementsInsideDirectory

directories = filterOnlyDirectories(os.listdir('./'))
            
for directory in directories: 
     subdirectories= getInsideDirectory(directory)
     for subdirectory in subdirectories: 
          images=entries = os.listdir('./'+directory +'/'+subdirectory)
          for index, image in enumerate(images):
               extension=getExtension(image)
               currentImageName='./'+directory +'/'+subdirectory+'/'+image
               replacementImageName='./'+directory +'/'+subdirectory+'/'+'b-'+str(index)+'.'+extension
               os.rename(currentImageName,replacementImageName)
