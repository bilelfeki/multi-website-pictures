import os

def getExtension(imageName:str):
     return  imageName.split('.')[len(imageName.split('.'))-1]

def getInsideDirectory(directoryName:str):
     return os.listdir('./'+ str(directoryName))

def filterOnlyDirectories(elementsInsideDirectory:list):
     for file in elementsInsideDirectory:
          directoryList=[]
          if(os.path.isdir('./'+ str(file))):
               directoryList.append(file)
          return directoryList

directories = filterOnlyDirectories(os.listdir('./'))
            
for directory in directories: 
     subdirectories= getInsideDirectory(directory)
     for subdirectory in subdirectories: 
          images=entries = os.listdir('./'+directory +'/'+subdirectory)
          for index, image in enumerate(images):
               extension=getExtension(image)
               currentImageName='./'+directory +'/'+subdirectory+'/'+image
               replacementImageName='./'+directory +'/'+subdirectory+'/'+'b-'+str(index)+'.'+extension
               try:
                    os.rename(currentImageName,replacementImageName)
               except:
                    print('file renamed successfully')