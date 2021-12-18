import csv
import json
import sys
import os

# Class occurrence, crated per line
class Occurrence:
   
   def __init__(self, parsed_line):
       self.Id_Table = parsed_line[0]
       self.ID = parsed_line[1]
       self.Name = parsed_line[2]
       self.Variable = parsed_line[3]
       self.Method = parsed_line[4]
       self.Class = parsed_line[5]
       self.Package = parsed_line[6]
       self.File = parsed_line[7]
       self.FileName = parsed_line[8]
       self.System = parsed_line[9]
       self.Version = parsed_line[10]
       self.Release = parsed_line[11]

       self.ExcessiveInterlangCommunication = 0   #
       self.TooMuchClustering = 0                  #
       self.TooMuchScattering = 0                 #
       self.UnusedMethodDeclaration = 0           #
       self.UnusedMethodImplementation = 0        #
       self.UnusedParameter = 0                   #
       self.AssumingSafeReturnValue = 0           #
       self.ExcessiveObjects = 0                  #
       self.NotHandlingExceptions = 0             #
       self.NotCachingObjects = 0                 #
       self.NotSecuringLibraries = 0              #
       self.HardCodingLibraries = 0               #
       self.NotUsingRelativePath = 0              #
       self.MemoryManagementMismatch = 0
       self.LocalReferencesAbuse = 0              #
    
   # This is identifier if each occurrence, it should generate unique string for unique occurrence
   # Same identifier means there is same occurrence
   def identifier(self):
       # Used File, System, Version, Package, Release
       return self.File + "," + self.System + "," + self.Version + "," + self.Package + "," + self.Release + ","
       

if len(sys.argv)>2:

  occurences = {}
  c = 0
  for line in list(csv.reader(open(sys.argv[1], 'r'), delimiter=',')):
      if c>0:
          oc = Occurrence(line)
          #check occurrence is in dictionary
          if oc.identifier() in occurences:
              #print(oc.identifier())
              pass
          else:
              # add new occurrence if needed
              occurences[oc.identifier()] = oc

          # update class name, if still empty
          if occurences[oc.identifier()].Class == "":
             occurences[oc.identifier()].Class = oc.Class

          # increase counters
          if oc.Name == "AssumingSafeMultiLanguageReturnValues":
              occurences[oc.identifier()].AssumingSafeReturnValue = occurences[oc.identifier()].AssumingSafeReturnValue + 1
          if oc.Name == "NotHandlingExceptions":
              occurences[oc.identifier()].NotHandlingExceptions = occurences[oc.identifier()].NotHandlingExceptions + 1
          if oc.Name == "LocalReferencesAbuse":
              occurences[oc.identifier()].LocalReferencesAbuse = occurences[oc.identifier()].LocalReferencesAbuse + 1
          if oc.Name == "UnusedDeclaration":
              occurences[oc.identifier()].UnusedMethodDeclaration = occurences[oc.identifier()].UnusedMethodDeclaration + 1
          if oc.Name == "UnusedImplementation":
              occurences[oc.identifier()].UnusedMethodImplementation = occurences[oc.identifier()].UnusedMethodImplementation + 1
          if oc.Name == "UnusedParameters":
              occurences[oc.identifier()].UnusedParameter = occurences[oc.identifier()].UnusedParameter + 1
          if oc.Name == "NotSecuringLibraries":
              occurences[oc.identifier()].NotSecuringLibraries = occurences[oc.identifier()].NotSecuringLibraries + 1
          if oc.Name == "HardCodingLibraries":
              occurences[oc.identifier()].HardCodingLibraries = occurences[oc.identifier()].HardCodingLibraries + 1
          if oc.Name == "NotUsingRelativePath":
              occurences[oc.identifier()].NotUsingRelativePath = occurences[oc.identifier()].NotUsingRelativePath + 1
          if oc.Name == "NotCachingObjects":
              occurences[oc.identifier()].NotCachingObjects = occurences[oc.identifier()].NotCachingObjects + 1
          if oc.Name == "ExcessiveInterLanguageCommunication":
              occurences[oc.identifier()].ExcessiveInterlangCommunication = occurences[oc.identifier()].ExcessiveInterlangCommunication + 1
          if oc.Name == "ExcessiveObjects":
              occurences[oc.identifier()].ExcessiveObjects = occurences[oc.identifier()].ExcessiveObjects + 1
          if oc.Name == "TooMuchScattering":
              occurences[oc.identifier()].TooMuchScattering = occurences[oc.identifier()].TooMuchScattering + 1
          if oc.Name == "TooMuchClustering":
              occurences[oc.identifier()].TooMuchClustering = occurences[oc.identifier()].TooMuchClustering + 1
          if oc.Name == "NotUsingRelativePath":
              occurences[oc.identifier()].NotUsingRelativePath = occurences[oc.identifier()].NotUsingRelativePath + 1
          if oc.Name == "MemoryManagementMismatch":
              occurences[oc.identifier()].MemoryManagementMismatch = occurences[oc.identifier()].MemoryManagementMismatch + 1

      # row counter, it's used for skipping header row
      c = c + 1


  with open(sys.argv[2], 'w') as writer:  # writing file
      # Write Header
      writer.write("Id_db,File,System,Version,Package,Release,Class,ExcessiveInterlangCommunication,Too much clustring,Too much Scattering,UnusedMethodDeclaration,UnusedMethodImplementation,UnusedParameter,AssumingSafeReturnValue,ExcessiveObjects,NotHandlingExceptions,NotCachingObjects,NotSecuringLibraries,HardCodingLibraries,NotUsingRelativePath,MemoryManagementMismatch,LocalReferencesAbuse\n")
      # Erite lines
      for name in occurences.keys():  
          oc = occurences[name]

          writer.write("none,")
          writer.write(os.path.basename(oc.File))
          writer.write(",")
          writer.write(oc.System)
          writer.write(",")
          writer.write(oc.Version)
          writer.write(",")
          writer.write(oc.Package)
          writer.write(",")
          writer.write(oc.Release)
          writer.write(",")
          writer.write(oc.Class)
          writer.write(",")

          writer.write(str(oc.ExcessiveInterlangCommunication))
          writer.write(",")
          writer.write(str(oc.TooMuchClustering))
          writer.write(",")
          writer.write(str(oc.TooMuchScattering))
          writer.write(",")
          writer.write(str(oc.UnusedMethodDeclaration))
          writer.write(",")
          writer.write(str(oc.UnusedMethodImplementation))
          writer.write(",")
          writer.write(str(oc.UnusedParameter))
          writer.write(",")
          writer.write(str(oc.AssumingSafeReturnValue))
          writer.write(",")
          writer.write(str(oc.ExcessiveObjects))
          writer.write(",")
          writer.write(str(oc.NotHandlingExceptions))
          writer.write(",")
          writer.write(str(oc.NotCachingObjects))
          writer.write(",")
          writer.write(str(oc.NotSecuringLibraries))
          writer.write(",")
          writer.write(str(oc.HardCodingLibraries))
          writer.write(",")
          writer.write(str(oc.NotUsingRelativePath))
          writer.write(",")
          writer.write(str(oc.MemoryManagementMismatch))
          writer.write(",")
          writer.write(str(oc.LocalReferencesAbuse))
          writer.write(",")
          writer.write(oc.File)

          writer.write("\n");
  # 
      
else:
  print("Using:")
  print("python dwh.py <input csvfile> <output csvfile>")


