import os
import subprocess
# Execute the script in pathToScript for each file which will be find in dirWithData
# All the files produced by the script will be saved in pathToStoreResults
class EnvClass:
    def __init__(self):
       self.dirWithData = "/Users/s2462766/Data/BCTvsActiveNem/Res/"
       self.pathToScript = "/Users/s2462766/Data/MPCD/analysisScripts/VelAndOrientationAnimated.py"
       #self.pathToScript = "/home/dewerf/Documents/PhDBacterial/MPCD/analysisScripts/orientationField2Danimated.py"
       #self.pathToScript = "/home/dewerf/Documents/PhDBacterial/MPCD/analysisScripts/flowFieldAnimated.py"
       self.pathToStoreResults = "/Users/s2462766/Data/BCTvsActiveNem/Res/Videos/"
       self.dataFilesList = []
       self.popsFromData = set()
       self.actsFromData = set()
       self.sizesFromData = set()
       self.bssFromData = set()
       self.dampFromData = set()
       self.repFromData = set()
      
    def createListOfFolders(self):
        for files in os.listdir(self.dirWithData):
           #if (files.startswith("coarsegrain") or files.startswith("polarfield")) and files.endswith(".dat"):
           if files.startswith("coarsegrain") and files.endswith(".dat"):
           #if files.startswith("polarfield") and files.endswith(".dat"):
           #if files.startswith("directorfield") and files.endswith(".dat"):
           #if files.startswith("flowfield") and files.endswith(".dat"):
              self.dataFilesList.append(os.path.join(self.dirWithData, files))

    def runGeneral(self):
       self.createListOfFolders()
       for data in self.dataFilesList:
         fileName = data.split("/")[-1]
         dens = data.split("pop-")[1].split("-act")[0]
         act = data.split("act-")[1].split("-bs")[0]
         bs = data.split("bs-")[1].split("-rep")[0]
         rep = data.split("rep-")[1].split("-size")[0]
         size = data.split("size-")[1].split("-damp")[0]
         damp = data.split("damp-")[1].split(".dat")[0]
         if act == "0.0":
            continue
         if size != "100":
            continue
         if bs != "0.005":
            continue
         if "coarsegrain" in fileName or "polarfield" in fileName:
            process = subprocess.Popen(["python3", self.pathToScript, data, self.dirWithData+'/inputgrav-0.0-pop-'+str(dens)+'-act-'+str(act)+'-bs-'+str(bs)+'-rep-'+str(rep)+'-size-'+str(size)+'-damp-'+str(damp)+'.json', '0', '9999', 'z', '0', '-a', 'equal'], cwd=self.pathToStoreResults)
         elif "directorfield" in fileName or "flowfield" in fileName:
            process = subprocess.Popen(["python3", self.pathToScript, data, self.dirWithData+'/inputgrav-0.0-pop-'+str(dens)+'-act-'+str(act)+'-bs-'+str(bs)+'-rep-'+str(rep)+'-size-'+str(size)+'-damp-'+str(damp)+'.json', '0', '9999', 'z', '-a', 'equal'], cwd=self.pathToStoreResults) #directorField, flowfield
         else:
            print("Unknown file error")
            exit()
         process.wait()
         name='2Ddens_z0.mp4'
         if "directorfield" in fileName:
            name='2Dorientation_animation.mp4'
         elif "flowfield" in fileName:
            name='2Dvelocity_animation.mp4'
         for files in os.listdir(self.pathToStoreResults):
            if files == name:
               if "coarsegrain" in fileName:
                   os.rename(os.path.join(self.pathToStoreResults, name), os.path.join(self.pathToStoreResults, "coarsegrainDens"+str(dens)+"act"+str(act)+"bs"+str(bs)+"rep"+str(rep)+"size"+str(size)+"damp"+str(damp)+".mp4"))
               elif "polarfield" in fileName:
                   os.rename(os.path.join(self.pathToStoreResults, name), os.path.join(self.pathToStoreResults, "polarfieldDens"+str(dens)+"act"+str(act)+"bs"+str(bs)+"rep"+str(rep)+"size"+str(size)+"damp"+str(damp)+".mp4"))
               elif "directorfield" in fileName:
                   os.rename(os.path.join(self.pathToStoreResults, name), os.path.join(self.pathToStoreResults, "directorfieldDens"+str(dens)+"act"+str(act)+"bs"+str(bs)+"rep"+str(rep)+"size"+str(size)+"damp"+str(damp)+".mp4"))
               else:
                   os.rename(os.path.join(self.pathToStoreResults, name), os.path.join(self.pathToStoreResults, "flowfieldDens"+str(dens)+"act"+str(act)+"bs"+str(bs)+"rep"+str(rep)+"size"+str(size)+"damp"+str(damp)+".mp4"))
               break

    def runCombinePolarAndVel(self):
        for velFile in os.listdir(self.dirWithData):
           if velFile.startswith("coarsegrain") and velFile.endswith(".dat"):
              grav = velFile.split("coarsegrain-")[1].split("-pop")[0]
              dens = velFile.split("pop-")[1].split("-act")[0]
              act = velFile.split("act-")[1].split("-bs")[0]
              bs = velFile.split("bs-")[1].split("-rep")[0]
              rep = velFile.split("rep-")[1].split("-size")[0]
              size = velFile.split("size-")[1].split("-damp")[0]
              damp = velFile.split("damp-")[1].split(".dat")[0]
              polarFile = "polarfieldgrav-{}-pop-{}-act-{}-bs-{}-rep-{}-size-{}-damp-{}.dat".format(grav, dens, act, bs, rep, size, damp)
              if polarFile in os.listdir(self.dirWithData) and size != '200':
                 jsonFile = "inputgrav-{}-pop-{}-act-{}-bs-{}-rep-{}-size-{}-damp-{}.json".format(grav, dens, act, bs, rep, size, damp)
                 process = subprocess.Popen(["python3", self.pathToScript, os.path.join(self.dirWithData, velFile), os.path.join(self.dirWithData, polarFile), os.path.join(self.dirWithData, jsonFile)], cwd=self.pathToStoreResults)
                 process.wait()


if __name__ == "__main__":
  obj = EnvClass()
  #obj.runGeneral()
  obj.runCombinePolarAndVel()
