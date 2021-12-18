from os import listdir
from os.path import isfile, join
import csv
import pandas as pd
import os

def main():
    path = '/Users/mosesopenja/Documents/Winter2020/Mouna-Revised/smells/Smells_results/'
    path_output = '/Users/mosesopenja/Documents/Winter2020/Mouna-Revised/V2/CombinedStats4/'
    excelPath = '/Users/mosesopenja/Documents/Winter2020/Mouna-Revised/reviced/output4/'
    folders = ['rocksdb', 'realm-java', 'pljava', 'javacpp', 'conscrypt', 'jna', 'frostwire', 'OpenDDS']
    path_all = '/Users/mosesopenja/Documents/Winter2020/Mouna-Revised/V2/file_schema2/all/'

    for folder in folders:
        onlyfiles = [f for f in listdir(path + folder) if isfile(join(path + folder, f))]
        xl1 = pd.ExcelFile(excelPath + 'SnapshotsDetailsJNI.xlsx')
        # xl2 = pd.ExcelFile(excelPath + file_inducing)
        # print(xl.sheet_names)
        df_bugs = xl1.parse(folder)

        # print(folder)
        # ID = df_bugs.Project.values.tolist()
        FileName = df_bugs.FileName.values.tolist()
        snapshotName = df_bugs.snapshotName.values.tolist()
        startDate = df_bugs.startDate.values.tolist()
        endDate = df_bugs.endDate.values.tolist()
        inducing = df_bugs.inducing.values.tolist()
        Fixing = df_bugs.Fixing.values.tolist()
        InducingFlag = df_bugs.InducingFlag.values.tolist()
        FixingFlag = df_bugs.FixingFlag.values.tolist()

        CLOC_Inducing = df_bugs.CLOC_Inducing.values.tolist()
        AddedInducing = df_bugs.AddedInducing.values.tolist()
        RemovedInducing = df_bugs.RemovedInducing.values.tolist()
        prev_inducing = df_bugs.prev_inducing.values.tolist()
        prev_fixing = df_bugs.prev_fixing.values.tolist()
        cum_inducing = df_bugs.cum_inducing.values.tolist()
        cum_fixing = df_bugs.cum_fixing.values.tolist()
        Message_induce = df_bugs.Message_induce.values.tolist()
        Message_fix = df_bugs.Message_fix.values.tolist()

        InducingDates = df_bugs.InducingDates.values.tolist()
        FixingDates = df_bugs.FixingDates.values.tolist()

        dev_induce = df_bugs.DevEmailinduc.values.tolist()
        dev_fix = df_bugs.DevEmailfixing.values.tolist()

        LOC_All = df_bugs.LOC_All.values.tolist()
        Time = df_bugs.Time.values.tolist()

        map_data = pd.read_csv(path_all + folder + ".csv")
        # Read and Convert to list
        Map_Id = map_data.Id.values.tolist()
        Map_File = map_data.FileName.values.tolist()

        CreatedAt = map_data.CreatedAt.values.tolist()
        RenamedFrom = map_data.RenamedFrom.values.tolist()
        RenamedTo = map_data.RenamedTo.values.tolist()

        RenamedAt = map_data.RenamedAt.values.tolist()
        RemovedDate = map_data.RemovedDate.values.tolist()
        status = map_data.status.values.tolist()

        Modifications = map_data.modifications.values.tolist()
        LastModifiedHash = map_data.LastModifiedHash.values.tolist()
        LastModifiedAt = map_data.LastModifiedAt.values.tolist()
        # df.head()

        rows = ["Id_db", "File", "System", "Version", "Package", "Release", "Class", "ExcessiveInterlangCommunication",
                "Toomuchclustring", "ToomuchScattering", "UnusedMethodDeclaration",
                "UnusedMethodImplementation", "UnusedParameter", 'AssumingSafeReturnValue', 'ExcessiveObjects',
                'NotHandlingExceptions', 'NotCachingObjects', 'NotSecuringLibraries',
                'HardCodingLibraries', 'NotUsingRelativePath', 'MemoryManagementMismatch', 'LocalReferencesAbuse',
                'FilePath', 'inducing', 'fixing', 'inducingflag', 'fixingFlag', 'Smelly', 'LOC', 'Time', 'CLOC', 'LOC_inducing',
                'prev_inducing', 'prev_fixing', 'cum_inducing', 'cum_fixing', 'Message_induce', 'Message_fix', 'dev-inducing',
                'dev-fixing', 'CreatedAt', 'RenamedFrom', 'RenamedTo', 'RenamedAt', 'RemovedDate', 'InducingDates', 'FixingDates',
                'status', 'modifications', 'LastModifiedAt', 'LastModifiedHash']

        fileCSV = open(path_output + folder + "_merged2.csv", 'w+')
        writer = csv.writer(fileCSV)
        writer.writerow(rows)
        dic_merged_files = {}
        for file in onlyfiles:
            print(file)
            df_data = pd.read_csv(path + folder + "/" + file)
            # Read and Convert to list
            Id_db = df_data.Id_db.values.tolist()
            File = df_data.File.values.tolist()
            System = df_data.System.values.tolist()
            Version = df_data.Version.values.tolist()
            Package = df_data.Package.values.tolist()
            Class = df_data.Class.values.tolist()
            ExcessiveInterlangCommunication = df_data.ExcessiveInterlangCommunication.values.tolist()
            Toomuchclustring = df_data.iloc[:, 8].values.tolist()
            ToomuchScattering = df_data.iloc[:, 9].values.tolist()
            UnusedMethodDeclaration = df_data.UnusedMethodDeclaration.values.tolist()
            UnusedMethodImplementation = df_data.UnusedMethodImplementation.values.tolist()
            UnusedParameter = df_data.UnusedParameter.values.tolist()
            AssumingSafeReturnValue = df_data.AssumingSafeReturnValue.values.tolist()
            ExcessiveObjects = df_data.ExcessiveObjects.values.tolist()
            NotHandlingExceptions = df_data.NotHandlingExceptions.values.tolist()
            NotCachingObjects = df_data.NotCachingObjects.values.tolist()
            NotSecuringLibraries = df_data.NotSecuringLibraries.values.tolist()
            HardCodingLibraries = df_data.HardCodingLibraries.values.tolist()
            NotUsingRelativePath = df_data.NotUsingRelativePath.values.tolist()
            MemoryManagementMismatch = df_data.MemoryManagementMismatch.values.tolist()
            LocalReferencesAbuse = df_data.LocalReferencesAbuse.values.tolist()
            FilePath = df_data.FilePath.values.tolist()

            for j in range(1, len(FileName)):
                # print(str(FileName[j]),path_)
                # print(rename_version,snapshotName[j])
                index_i = 0
                flag = 0
                if FileName[j] in Map_File:
                    map_index = Map_File.index(FileName[j])
                    ID_ = Map_Id[map_index]
                    list_package = []
                    for i in range(0, len(File)):
                        rename_version = file.replace('format.csv', '')
                        path_ = '/'.join(str(FilePath[i]).split('\\'))
                        if str(FileName[j]) in path_ and str(snapshotName[j]) in path_:
                            # if File[i] in FileName[j] and rename_version == snapshotName[j]:
                            index_i = i
                            flag += 1
                            break
                    class_ = ''
                    if '.java' in FileName[j]:
                        class_ = FileName[j].split("/")[len(FileName[j].split("/")) - 1].split(".")[0]
                    # if not str(FileName[j])+"/"+str(snapshotName[j])+"/"+str(ID_) in list_all_files:
                    if flag > 0:
                        smelly = 0
                        if ExcessiveInterlangCommunication[index_i] > 0 or Toomuchclustring[index_i] > 0 or \
                                ToomuchScattering[index_i] > 0 or UnusedMethodDeclaration[index_i] > 0 or \
                                UnusedMethodImplementation[index_i] > 0 or UnusedParameter[index_i] > 0 or \
                                AssumingSafeReturnValue[index_i] > 0 or ExcessiveObjects[index_i] > 0 or \
                                NotHandlingExceptions[index_i] > 0 or NotCachingObjects[index_i] > 0 or \
                                NotSecuringLibraries[index_i] > 0 or HardCodingLibraries[index_i] > 0 or \
                                NotUsingRelativePath[index_i] > 0 or MemoryManagementMismatch[index_i] > 0:
                            smelly = 1

                        rows = [ID_, File[index_i], System[index_i], snapshotName[j], Package[index_i], startDate[j],
                                Class[index_i],
                                ExcessiveInterlangCommunication[i], Toomuchclustring[index_i],
                                ToomuchScattering[index_i],
                                UnusedMethodDeclaration[index_i],
                                UnusedMethodImplementation[index_i], UnusedParameter[index_i],
                                AssumingSafeReturnValue[index_i],
                                ExcessiveObjects[index_i], NotHandlingExceptions[index_i], NotCachingObjects[index_i],
                                NotSecuringLibraries[index_i],
                                HardCodingLibraries[index_i], NotUsingRelativePath[index_i],
                                MemoryManagementMismatch[index_i],
                                LocalReferencesAbuse[index_i], str(FileName[j]),
                                inducing[j], Fixing[j], InducingFlag[j], FixingFlag[j], smelly, LOC_All[j], Time[j],
                                CLOC_Inducing[j], AddedInducing[j] + RemovedInducing[j], prev_inducing[j],
                                prev_fixing[j], cum_inducing[j], cum_fixing[j], Message_induce[j], Message_fix[j],
                                dev_induce[j], dev_fix[j], CreatedAt[map_index], RenamedFrom[map_index],
                                RenamedTo[map_index], RenamedAt[map_index], RemovedDate[map_index], InducingDates[j],
                                FixingDates[j], status[map_index],
                                Modifications[map_index], LastModifiedAt[map_index], LastModifiedHash[map_index]]
                        # writer.writerow(rows)
                        dic_merged_files[str(ID_) + "/" + str(FileName[j]) + "/" + str(snapshotName[j])] = rows
            print(" ----- snapshot: {} ".format(rename_version))
        untract = 0
        for j in range(1, len(FileName)):
            if FileName[j] in Map_File:
                map_index = Map_File.index(FileName[j])
                ID_ = Map_Id[map_index]
                rows = dic_merged_files.get(str(ID_) + "/" + str(FileName[j]) + "/" + str(snapshotName[j]))
                if rows == None:
                    smelly = 0
                    rows = [ID_, FileName[j].split("/")[len(FileName[j].split("/")) - 1], snapshotName[j].split("_")[0],
                            snapshotName[j], "", startDate[j], "",
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, str(FileName[j]),
                            inducing[j], Fixing[j], InducingFlag[j], FixingFlag[j], smelly, LOC_All[j], Time[j],
                            CLOC_Inducing[j], AddedInducing[j] + RemovedInducing[j], prev_inducing[j],
                            prev_fixing[j], cum_inducing[j], cum_fixing[j], Message_induce[j], Message_fix[j],
                            dev_induce[j], dev_fix[j], CreatedAt[map_index], RenamedFrom[map_index],
                            RenamedTo[map_index], RenamedAt[map_index], RemovedDate[map_index], InducingDates[j],
                            FixingDates[j], status[map_index],
                            Modifications[map_index], LastModifiedAt[map_index], LastModifiedHash[map_index]]
                writer.writerow(rows)
            else:
                untract += 1
        print("untracted files: {}".format(untract))
        fileCSV.close()


if __name__ == '__main__':
    main()