import json
import sys
import subprocess
import os
# Used together with launchScript.sh
class EnvClass:
    def __init__(self):
        self.plotName = "VcmMag"
        self.myMap = None
        self.jsonInputFile = None
        self.jsonResultsFile = None
        self.pwd = os.getcwd()
        self.indexValue = float(sys.argv[2])
        self.gravValue = float(sys.argv[3])
        self.popValue = float(sys.argv[4])
        self.sizeValue = int(sys.argv[5])
        self.actValue = float(sys.argv[6])
        self.bsValue = float(sys.argv[7])
        self.dampValue = float(sys.argv[8])
        self.dataFile = os.path.join(self.pwd, 'MPCD/sampleInputs/myExp/Exp'+sys.argv[2]+'/input.json')

        # Const
        self.fileToRun = os.path.join(self.pwd, 'MPCD/mpcd.out')
        self.directoryToRunFrom = os.path.join(self.pwd, sys.argv[1])
        print("Initialization finished")


    def loadInputJson(self):
        f = open(self.dataFile)
        self.jsonInputFile = json.load(f)
        print(json)
        f.close()

    def loadResultsJson(self):
        f = open(self.jsonWithResults)
        self.jsonResultsFile = json.load(f)
        f.close()

    def changeJsonValue(self, actData, densData, sizeData, gravData, bsData, dampData):
        self.loadInputJson()
        self.jsonInputFile['domain'] = [sizeData, sizeData]
        self.jsonInputFile['species'][0]['dens'] = densData
        self.jsonInputFile['species'][0]['act'] = actData
        self.jsonInputFile['species'][0]['bs'] = bsData
        #self.jsonInputFile['BC'][0]['DN'] = sizeData
        #self.jsonInputFile['BC'][1]['DN'] = sizeData
        #self.jsonInputFile['BC'][1]['Q'] = [sizeData, 0, 0]
        #self.jsonInputFile['BC'][3]['Q'] = [0, sizeData, 0]
        self.jsonInputFile['grav'] = [0, gravData, 0]
        self.jsonInputFile['species'][0]['damp'] = dampData
        if "BC" in self.jsonInputFile:
            self.jsonInputFile["BC"][0]["Q"] = [sizeData/2, sizeData/2, 0]
            self.jsonInputFile["BC"][0]["R"] = sizeData/2 - 1


        with open(self.dataFile, 'w') as f:
            json.dump(self.jsonInputFile, f,indent=4)

    def run(self):
        self.changeJsonValue(actData=self.actValue, densData=self.popValue, sizeData=self.sizeValue, gravData=self.gravValue, bsData=self.bsValue, dampData=self.dampValue)
        process = subprocess.Popen([self.fileToRun, "-i", self.dataFile, "-o", "./"], cwd=self.directoryToRunFrom)
        process.wait()

if __name__ == "__main__":
    obj = EnvClass()
    obj.run()
