import os
import git
def clone(path, project):
    filename = "{}/{}".format(path,project.split("/")[1])
    if checkFile(filename) is False:
        try:
            git.Git(path).clone("https://github.com/{}.git".format(project))
            print("Cloning {} completed successful!".format(project))
        except:
            print("Error while clonning: {} ".format(project))
            pass
    else:
        print("File already exist!!!!")

def checkFile(filename):
    return os.path.exists(filename)
path = "/Users/mosesopenja/Documents/Winter2020/Mouna-Revised/clones/";
project = "luben/zstd-jni"
clone(path,project)