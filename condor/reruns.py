import os,sys,subprocess,fnmatch
from pathlib import Path

logdir = Path(sys.argv[1]).resolve()
resubmit = False
if len(sys.argv) > 2:
    resubmit = bool(eval(sys.argv[2]))

deletefakes = False
killdisconnect = False
splitjobs = True
nsplit = 2 #-1

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

reruns = []
killandrerun = {}
fakes = []
mem = []
time = []
rm = []
crashed = []
running = []

Njobs = 0
Nsubmitted = 0
Nsuccess = 0
for file in findfiles(logdir, '*.job'):
    Njobs += 1
    hasout = True
    hasFinished = 0
    hasCopied = 0
    isrunning = True
    disconnected = False
    started = 0
    fakejob = 0
    outname = file.replace('.job','.out')
    logname = outname.replace('.out','.log')
    if os.path.exists(logname):
        Nsubmitted += 1
    if not os.path.exists(outname):
        hasout = False
    else:
        command = 'grep "Done analyzing!" '+outname+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')
        digits = out.find(' ')
        hasFinished = int("".join(out[0:digits]))

        if not hasFinished:
            command = 'grep "Analysis End" '+outname+' | wc'
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            (out, err) = proc.communicate()
            out = out.strip()
            out = out.decode('utf-8')
            digits = out.find(' ')
            hasFinished = int("".join(out[0:digits]))

        command = 'grep "fully done through copying" '+outname+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')
        digits = out.find(' ')
        hasCopied = int("".join(out[0:digits]))

        command = 'grep "Number of Entries: 0" '+outname+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')
        digits = out.find(' ')
        fakeJob = int("".join(out[0:digits]))

    if hasFinished and hasCopied:
        Nsuccess += 1
        isrunning = False
        
    command = 'tail -2 '+logname
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.strip()
    out = out.decode('utf-8')

    memkill = False
    timekill = False
    rmkill = False
    crash = False
    if (not hasFinished or not hasCopied) and 'TimeSlotBusy' in out:
        crash = True
        isrunning = False
    if 'SYSTEM_PERIODIC_REMOVE' in out or 'terminated' in out or 'condor_rm' in out or 'exceeding requested memory' in out or 'wall time exceeded' in out:
        isrunning = False
        if 'exceeding requested memory' in out:
            memkill = True
        elif 'job running for more than 2 days' in out:
            timekill = True
        elif 'condor_rm' in out:
            rmkill = True
        elif 'exit-code 0' not in out:
            crash = True
    if 'Can not reconnect' in out:
        disconnected = True
    if 'attempting to reconnect' in out or 'rying to reconnect' in out:
        disconnected = True

    command = 'grep "executing on host" '+logname+' | wc'
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.strip()
    out = out.decode('utf-8')
    digits = out.find(' ')
    started = int("".join(out[0:digits]))

    if isrunning and disconnected == True:  #started == 0 # seems like logs update late...
        command = 'tail -4 '+logname
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')

        jobnum = ((out.split(" ")[1]).split(".")[0])[1:]
        killandrerun[outname] = jobnum


    if isrunning:
        running.append(outname)
    if not isrunning and (not hasFinished or not hasCopied or not hasout):
        if fakeJob > 0:
            fakes.append(outname)
        else:            
            reruns.append(outname)
            if memkill:
                mem.append(outname)
            elif timekill:
                time.append(outname)
            elif rmkill:
                rm.append(outname)
            else:
                crashed.append(outname)

print('Jobs existing:',Njobs,', and submitted:',Nsubmitted)
print('Jobs successfully complete:',Nsuccess)

print('Jobs still running:',len(running))
for i in range(len(running)):
    print(running[i])

print('Jobs that are disconnected:',len(killandrerun))
print(killandrerun)

print('Fake jobs:',len(fakes))
print(fakes)
if deletefakes:
    print('Deleting the fakes...')
    for fake in fakes:
        os.system('rm '+fake)
        os.system('rm '+fake.replace('out','err'))
        os.system('rm '+fake.replace('out','log'))
        os.system('rm '+fake.replace('_RDF','').replace('out','job'))

print('Over memory jobs:',len(mem))
print(mem)

print('Over time jobs:',len(time))
for i in range(len(time)):
    print(time[i])

print('Removed jobs:',len(rm))
print(rm)

print('Crashed jobs:',len(crashed))
for i in range(len(crashed)):
    print(crashed[i])


#print('Found several jobs that failed:',len(reruns))
# for ijob in reruns:
#     print(ijob)

resubs = {}

if killdisconnect:
    for outname in killandrerun.keys():
        os.system('condor_rm '+killandrerun[outname])
        reruns.append(outname)


if not resubmit: exit()
print('resubmitting')

for rerun in reruns:
    os.chdir(logdir)
    rerun = rerun.replace('_RDF','').replace('.out','.job')
    command = 'grep "Arguments" '+rerun
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.decode('utf-8')
    jobnums = [int(out.split(" ")[4]),int(out.split(" ")[5])]
    
    print('\''+rerun+'\':'+str(jobnums))
    resubs[rerun] = jobnums
    #os.system('ls -l '+rerun.replace('_','_RDF_').replace('.job','.out'))
    #os.system('tail -20 '+rerun.replace('_','_RDF_').replace('.job','.err'))

for rerun in resubs.keys():
    folder = rerun.split('/')[-2]
    jobfile = rerun.split('/')[-1]

    #if 'TTWZ2022' in folder: continue # these are somehow NanoAODv11...don't have pNet btagging

    if splitjobs:
        if resubs[rerun][0] == resubs[rerun][1]:
            print('NOT SPLITTING THIS ONE, SINGLE FILE '+folder+'/'+jobfile)
            os.chdir(str(logdir)+'/'+folder)
            os.system('condor_submit '+jobfile)
            continue

        if nsplit == 2: 
            half = int(resubs[rerun][0] + (resubs[rerun][1] - resubs[rerun][0])/2.0)
            print(folder+': new ranges '+str(resubs[rerun][0])+' - '+str(half)+' , '+str(half+1)+' - '+str(resubs[rerun][1]))

            newjobfile = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(half+1))
            os.chdir(str(logdir)+'/'+folder)
            os.system('cp '+jobfile+' '+newjobfile)
            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(half)+' |" '+jobfile) # only change upper in original file
            os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(half+1)+' |" '+newjobfile) # only change lower in new file
            os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(half+1)+'\.|" '+newjobfile)
            
            os.system('condor_submit '+jobfile)
            os.system('sleep 0.5')
            os.system('condor_submit '+newjobfile)
            os.system('sleep 0.5')

        if nsplit == 3:
            third = int(resubs[rerun][0] + (resubs[rerun][1] - resubs[rerun][0])/3.0)
            third2 = int(resubs[rerun][0] + 2*(resubs[rerun][1] - resubs[rerun][0])/3.0)
            print(folder+': new ranges '+str(resubs[rerun][0])+' - '+str(third)+' , '+str(third+1)+' - '+str(third2)+', and '+str(third2+1)+' - '+str(resubs[rerun][1]))
    
            newjobfile = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(third+1))
            newjobfile2 = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(third2+1))
        
            os.chdir(str(logdir)+'/'+folder)
            os.system('cp '+jobfile+' '+newjobfile)
            os.system('cp '+jobfile+' '+newjobfile2)
            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(third)+' |" '+jobfile) # only change upper in original file

            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(third2)+' |" '+newjobfile) # change upper in middle file
            os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(third+1)+' |" '+newjobfile) # change lower in middle file
            os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(third+1)+'\.|" '+newjobfile)

            os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(third2+1)+' |" '+newjobfile2) # only change lower in last file
            os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(third2+1)+'\.|" '+newjobfile2)
            
            os.system('condor_submit '+jobfile)
            os.system('sleep 0.5')
            os.system('condor_submit '+newjobfile)
            os.system('sleep 0.5')
            os.system('condor_submit '+newjobfile2)
            os.system('sleep 0.5')

        if nsplit == -1:
            print(folder+': new ranges:')
            os.chdir(str(logdir)+'/'+folder)
            for ijob in range(resubs[rerun][0]+1,resubs[rerun][1]+1): # loop for everything past the first file
                newjobfile = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(ijob))
                print('\t ',ijob,' with file name ',newjobfile)
                os.system('cp '+jobfile+' '+newjobfile)
                os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(ijob)+' |" '+newjobfile)
                os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(ijob)+' |" '+newjobfile)
                os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(ijob)+'\.|" '+newjobfile)
                os.system('condor_submit '+newjobfile)
                os.system('sleep 0.5')


            print('\t ',resubs[rerun][0],' with file name ',jobfile)
            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(resubs[rerun][0])+' |" '+jobfile) # edit first file .job
            os.system('condor_submit '+jobfile)
            os.system('sleep 0.5')
            
            
    else:
        os.chdir(str(logdir)+'/'+folder)
        os.system('condor_submit '+jobfile)
            
