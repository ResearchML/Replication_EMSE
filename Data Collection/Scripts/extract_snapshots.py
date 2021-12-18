import csv
import os
import shutil
import subprocess
import urllib.request
import zipfile
from datetime import date
import time
import pandas as pd


def clone_git_repository(url, target_path):
    os.chdir(target_path)
    git_clone_command = "git clone " + url
    print("Cloning repository from :{} into {}".format(url, target_path))
    p = subprocess.Popen(git_clone_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    for line in p.stdout.readlines():
        output = output + str(line) + '\n'
    retval = p.wait()
    if retval == 0:
        print("Repository cloned successfully!")
    else:
        print("Error in cloning!")
        print(output)
    return retval


def extract_git_commit_logs(repo_path, log_path):
    os.chdir(repo_path)
    git_log_command = "git --no-pager log --pretty=format:\"%H|%ad|%an|%s\" --date=short >" + log_path
    # print(git_log_command)
    print("Extracting commit logs from repository in :{}".format(repo_path))
    p = subprocess.Popen(git_log_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    for line in p.stdout.readlines():
        output = output + str(line) + '\n'
    retval = p.wait()
    if retval == 0:
        print("Commit log extracted successfully!")
    else:
        print("Error in commit log extraction!")
        print(output)
    return retval


def list_git_commits(log_path):
    commit_list = []
    try:
        with open(log_path, "r", encoding='utf-8') as fp:
            text_lines = fp.readlines()
            for line in text_lines:
                try:
                    log_parts = line.split('|')
                    #print(log_parts)
                    csha = log_parts[0]
                    c_date = log_parts[1]
                    commit_list.append([csha, c_date])
                except:
                    pass
        fp.close()
        no_commit = len(commit_list)
        commit_list1 = []
        for i in range(no_commit - 1, -1, -1):
            commit_list1.append(commit_list[i])
    except FileNotFoundError:
        print("Error in file reading")
    return commit_list1


def get_date_days_diff(date1, date2):
    dy1, dm1, dd1 = date1.split('-')
    dy2, dm2, dd2 = date2.split('-')

    d1 = date(int(dy1), int(dm1), int(dd1))
    d2 = date(int(dy2), int(dm2), int(dd2))

    delta = d2 - d1
    no_days = delta.days
    # print(delta.days)
    return no_days


def get_next_commit(commits, ref_commit, cur_pos, day_threshold):
    next_commit = None
    new_pos = cur_pos
    no_commit = len(commits)
    for i in range(cur_pos, no_commit - 1):
        if get_date_days_diff(ref_commit[1], commits[i][1]) > day_threshold:
            new_pos = i
            break
    if new_pos != cur_pos and new_pos != no_commit:
        next_commit = commits[new_pos]

    return next_commit, new_pos


def select_git_snapshots(commits, start_pos=0, day_threshold=90):
    n_commits = len(commits)
    selected_commits = []
    c1 = commits[start_pos]
    cur_pos = start_pos
    selected_commits.append(c1)

    for i in range(start_pos, n_commits - 1):
        c2, pos = get_next_commit(commits=commits, ref_commit=c1, cur_pos=cur_pos, day_threshold=day_threshold)
        cur_pos = pos
        if c2 is not None:
            selected_commits.append(c2)
            c1 = c2
        else:
            break
    return selected_commits


def download_git_snapshotsV2(commits, git_url, download_folder, snapshot_folder, repo_name, index):
    no_snaps = len(commits)
    url_base = git_url.replace('.git', '')
    for i in range(no_snaps):
        try:
            commit_sha = commits[i][0]
            print('Downloading snapshot: #{}: {}'.format(i, commit_sha[:7]))

            download_url = url_base + '/archive/' + commit_sha[:7] + '.zip'
            print(download_url)
            target_zip_path = os.path.join(download_folder, repo_name + '_' + str(i) + '.zip')
            print(target_zip_path)
            urllib.request.urlretrieve(download_url, target_zip_path)
            print("Downloaded successfully")

            print('Extracting zipped snapshot: #{}: {}'.format(i, commit_sha[:7]))
            extract_path = snapshot_folder + "/" + repo_name + "_"+str(index)+ "_snapshots"
            print(extract_path)
            extract_zip(zip_path=target_zip_path, target_path=extract_path)
            print("ZIP extracted!")
            time.sleep(3)
            extracted_in = get_zip_extracted_folder_name(commits[i], repo_name)
            new_name = repo_name+"_"+str(i)
            print(extracted_in)
            os.chdir(extract_path)
            os.rename(extracted_in,new_name)
            print("Extracted snapshot renamed to:{}".format(new_name))
            os.chdir(snapshot_folder)
            os.remove(new_name+'.zip')
        except Exception as e:
            print(e)
            pass

        # if i >= 2:
        #     break
    return


def extract_zip(zip_path, target_path):
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(target_path)
    z.close()
    return


def get_zip_extracted_folder_name(commit, repo_name):
    c_sha = commit[0]
    folder_name = repo_name + '-' + c_sha
    return folder_name


def export_selected_log(commits, log_path):
    text = ''
    for i in range (len(commits)):
        text = text +"Snapshot {} : Commit {} : {}".format(i, commits[i][0][:7],commits[i][1]) +'\n'
    with open(log_path, 'w') as fp:
        fp.write(text)
    fp.close()
    return

def main():
    path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'
    output_path = '/Volumes/Cisco/Fall2021/Mona/Analysis/general/'
    Repos_Name = ['objectcomputing/OpenDDS', 'google/conscrypt', 'facebook/rocksdb', 'jMonkeyEngine/jmonkeyengine', 'sosy-lab/java-smt',
    'videolan/vlc', 'realm/realm-java', 'eclipse/openj9', 'frostwire/frostwire']
    repo_target_path_root = "/Users/mosesopenja/Documents/summer2020/Mona/v2/snapshots/all"

    data_file = open(output_path + 'snapshots_dates.csv', mode='w', newline='', encoding='utf-8')
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['Repos','PIndex','snapshot_id', 'snapshot_date', 'Hash'])
    for index in range(len(Repos_Name)):
        #if index in id_list:
        #if Language[index] == 'C':
        repo = Repos_Name[index]
        #if 'q-e_old' in repo:

        repository_url = "https://github.com/"+repo+".git"
        cloned = 0   # 0 if not cloned yet, else 1
        log_extracted = 0  # 0 if not log is not extracted yet, else 1
        repo_name_parts = repository_url.split('/')
        repo_name = repo_name_parts[len(repo_name_parts) - 1]
        repo_path = repo_target_path_root+'/'+repo_name
        log_path = output_path + 'snapshots/' + repo_name + "_"+str(index)+ '-commit-logs.txt'

        print(index, repo)

        if not os.path.exists(repo_root_path):
            clone = clone_git_repository(url=repository_url, target_path=repo_target_path_root)

        #if cloned == 1 and log_extracted == 0:
        extract_git_commit_logs(repo_path=repo_path, log_path=log_path)

        commit_list = list_git_commits(log_path)
        commit_sha_list = [x[0] for x in commit_list]
        # print(commit_sha_list[0])
        print("Commits listed: {}".format(len(commit_list)))
        # next_commit, pos = get_next_commit(commits=commit_list, ref_commit=commit_list[0], cur_pos=0, day_threshold=90)
        selected_commits = select_git_snapshots(commits=commit_list, start_pos=0, day_threshold=90)
        total = len(selected_commits)
        print('Selected Commits:', total)

        for i in range(len(selected_commits)):
            data_writer.writerow([repo, index,i, selected_commits[i][0],selected_commits[i][1]])

        download_git_snapshotsV2(commits=selected_commits,git_url=repository_url, download_folder=repo_target_path_root, snapshot_folder=repo_target_path_root, repo_name=repo_name, index=index)
        ## We can now delete the cloned repo to free spaces!
        try:
            shutil.rmtree(repo_root)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
    data_file.close()


if __name__ == '__main__':
    main()
