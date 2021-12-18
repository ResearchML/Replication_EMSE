import csv
import pandas as pd
from src.quantum.codeanalyser.v2.TOKENS import get_tokens
import urllib.request
import json
class GitURL:
    def __init__(self, url, ct):
        self.ct = ct
        self.url = url
    def getResponse(self):
        jsonData = None
        try:
            if self.ct == len(get_tokens()):
                self.ct = 0
            reqr = urllib.request.Request(self.url)
            reqr.add_header('Authorization', 'token %s' % get_tokens()[self.ct])
            opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            content = opener.open(reqr).read()
            self.ct += 1
            jsonData = json.loads(content)
            #return jsonData, self.ct
        except Exception as e:
            pass
            #print(e)
        return jsonData, self.ct
    def url_header(self):
        jsonData = None
        try:
            if self.ct == len(get_tokens()):
                self.ct = 0
            reqr = urllib.request.Request(self.url)
            reqr.add_header('Accept', 'application/vnd.github.mercy-preview+json')
            reqr.add_header('Authorization', 'token %s' % get_tokens()[self.ct])
            opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            content = opener.open(reqr).read()
            self.ct += 1
            jsonData = json.loads(content)

        except Exception as e:
            pass
            #print(e)
        return jsonData, self.ct

class GitHubMeta:
    def __init__(self, repo, ct):
        self.ct = ct
        self.repo = repo

    def commit_(self, data_writer):
        p = 1
        total_contrib = 0
        while True:
            url2 = 'https://api.github.com/repos/' + self.repo + '/commits?page=' + str(p) + '&per_page=100'
            com_arrays, self.ct = GitURL(url2, self.ct).getResponse()
            p += 1
            if com_arrays != None:
                if len(com_arrays) == 0:
                    break
                total_contrib += len(com_arrays)
                if total_contrib % 500 == 0:
                    print(' ---- commits: ', total_contrib)
                for obj in com_arrays:
                    autho_name = obj['commit']['author']['name']
                    author_email = obj['commit']['author']['email']
                    author_date = obj['commit']['author']['date']
                    commiter_name = obj['commit']['committer']['name']
                    commiter_email = obj['commit']['committer']['email']
                    commiter_date = obj['commit']['committer']['date']
                    message = obj['commit']['message']

                    url = 'https://api.github.com/repos/' + self.repo + '/commits/'+str(obj['sha'])+''
                    shaa_obj, self.ct = GitURL(url, self.ct).getResponse()

                    cloc = 0
                    added = 0
                    removed = 0
                    try:
                        cloc = shaa_obj['stats']['total']
                        added = shaa_obj['stats']['additions']
                        removed = shaa_obj['stats']['deletions']
                    except:
                        pass
                    if shaa_obj != None:
                        for fOBJ in shaa_obj['files']:
                            filename = fOBJ['filename']
                            #if '.java' in str(filename) or '.c' in str(filename) or '.cc' in str(filename) or '.cpp' in str(filename) or '.h' in str(filename):
                            data_writer.writerow(
                                ['', filename, obj['sha'], autho_name, author_date, author_email, commiter_name,
                                 commiter_date, commiter_email, cloc, added, removed, message])

            else:
                break
        return self.ct

def main():
    path = '/Users/mosesopenja/Documents/Winter2020/Mouna-Revised/V2/'
    path_out = '/Users/mosesopenja/Documents/summer2021/mouna/File-all/'

    df_data = pd.read_csv(path + 'Repos-JNI.csv')
    Repos = df_data.Repos.values.tolist()
    ct = 0
    for i in range(0,len(Repos)):
        repo = Repos[i].split('/')[1]
        data_file = open(path_out + 'Repos_File_'+str(repo)+'.csv', mode='w', newline='', encoding='utf-8')
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['Repo', 'FileName', 'Hash', 'author', 'author_date', 'author_email', 'commiter',
                              "commiter_date", 'commiter_email', 'cloc', 'added', 'removed', 'message'])


        print(i, Repos[i])
        data_writer.writerow([Repos[i], '', '', '', '', '', '',
                              '', '', '', '', ''])
        ct = GitHubMeta(Repos[i], ct).commit_(data_writer)
        data_file.close()
if __name__ == '__main__':
    main()
