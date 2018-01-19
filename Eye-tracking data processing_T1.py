import os
import csv
import sys
import pandas as pd
import numpy as np

os.chdir('C:/Users/Christina/Dropbox/Dissertation/Data/9-21-17 analysis/')

f = open('summary-2017-09-20_clean.csv', 'r')

input_mapping_dictionary = {}

header_row = f.readline()
split_header_row = header_row.split(',')
for i in range(0,len(split_header_row)):
    input_mapping_dictionary[split_header_row[i]] = i



print input_mapping_dictionary


across_subject_dict = {}

for line in f:
    linearray = line.split(',')
    if (linearray[input_mapping_dictionary['TIMEPOINT']] == '1' and int(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']]) > 0):
        if not(linearray[input_mapping_dictionary['CID']] in across_subject_dict):
            subject_dictionary =  {}
            subject_dictionary['CID'] = [0,0]
            subject_dictionary['SLPropFace'] = [0,0]
            subject_dictionary['SLPropTarget'] = [0,0]
            subject_dictionary['SLPropDistracter'] = [0,0]
            subject_dictionary['SRPropFace'] = [0,0]
            subject_dictionary['SRPropTarget'] = [0,0]
            subject_dictionary['SRPropDistracter'] = [0,0]
            subject_dictionary['STest1PropTarget'] = [0,0]
            subject_dictionary['STest1PropDistracter'] = [0,0]
            subject_dictionary['STest2PropTarget'] = [0,0]
            subject_dictionary['STest2PropDistracter'] = [0,0]
            subject_dictionary['STest3PropTarget'] = [0,0]
            subject_dictionary['STest3PropDistracter'] = [0,0]
            subject_dictionary['NSLPropFace'] = [0,0]
            subject_dictionary['NSLPropTarget'] = [0,0]
            subject_dictionary['NSLPropDistracter'] = [0,0]
            subject_dictionary['NSRPropFace'] = [0,0]
            subject_dictionary['NSRPropTarget'] = [0,0]
            subject_dictionary['NSRPropDistracter'] = [0,0]
            subject_dictionary['NSTest1PropTarget'] = [0,0]
            subject_dictionary['NSTest1PropDistracter'] = [0,0]
            subject_dictionary['NSTest2PropTarget'] = [0,0]
            subject_dictionary['NSTest2PropDistracter'] = [0,0]
            subject_dictionary['NSTest3PropTarget'] = [0,0]
            subject_dictionary['NSTest3PropDistracter'] = [0,0]
            across_subject_dict[linearray[input_mapping_dictionary['CID']]] = subject_dictionary
        if linearray[input_mapping_dictionary['blocktype']] == 'NS':
            blocktype = 'NS'
            if linearray[input_mapping_dictionary['trialtype']] == 'L':
                trialtype = 'L'
            elif linearray[input_mapping_dictionary['trialtype']] == 'R':
                trialtype = 'R'
            elif linearray[input_mapping_dictionary['trialtype']] == 'target':
                trialtype = 'Test1'
            elif linearray[input_mapping_dictionary['trialtype']] == 'distracter':
                trialtype = 'Test2'
            elif linearray[input_mapping_dictionary['trialtype']] == 'target2':
                trialtype = 'Test3'
        elif linearray[input_mapping_dictionary['blocktype']] == 'S':
            blocktype = 'S'
            if linearray[input_mapping_dictionary['trialtype']] == 'L':
                trialtype = 'L'
            elif linearray[input_mapping_dictionary['trialtype']] == 'R':
                trialtype = 'R'
            elif linearray[input_mapping_dictionary['trialtype']] == 'target':
                trialtype = 'Test1'
            elif linearray[input_mapping_dictionary['trialtype']] == 'distracter':
                trialtype = 'Test2'
            elif linearray[input_mapping_dictionary['trialtype']] == 'target2':
                trialtype = 'Test3'
        
        targetval = 0
        distval = 0
        if trialtype in ['L', 'R']:
           if trialtype == 'L':
               targetval = linearray[input_mapping_dictionary['leftObject']]
               distval = linearray[input_mapping_dictionary['rightObject']]
           else:
               targetval = linearray[input_mapping_dictionary['rightObject']]
               distval = linearray[input_mapping_dictionary['leftObject']]
           across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropFace'][0] += float(linearray[input_mapping_dictionary['face']])/float(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']])
           across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropFace'][1] += 1
        elif trialtype in ['Test1', 'Test2', 'Test3']:
            targetval = linearray[input_mapping_dictionary['LEFT_IA']]
            distval = linearray[input_mapping_dictionary['RIGHT_IA']]
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropTarget'][0] += float(targetval)/float(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']])
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropTarget'][1] += 1
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropDistracter'][0] += float(distval)/float(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']])
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropDistracter'][1] += 1

f.close()

f = open('WugLife_processed_9-20-17.csv', 'w')
    
writeString = 'CID,SLPropFace,SLPropTarget,SLPropDistracter,SRPropFace,SRPropTarget,SRPropDistracter,STest1PropTarget,STest1PropDistracter,STest2PropTarget,STest2PropDistracter,STest3PropTarget,STest3PropDistracter,NSLPropFace,NSLPropTarget,NSLPropDistracter,NSRPropFace,NSRPropTarget,NSRPropDistracter,NSTest1PropTarget,NSTest1PropDistracter,NSTest2PropTarget,NSTest2PropDistracter,NSTest3PropTarget,NSTest3PropDistracter'
writeString += '\n'
f.write(writeString) 

for CID in across_subject_dict:

    writeString = ''
    writeString += str(CID)
    keyArray = ['SLPropFace','SLPropTarget','SLPropDistracter','SRPropFace','SRPropTarget','SRPropDistracter','STest1PropTarget','STest1PropDistracter','STest2PropTarget','STest2PropDistracter','STest3PropTarget','STest3PropDistracter','NSLPropFace','NSLPropTarget','NSLPropDistracter','NSRPropFace','NSRPropTarget','NSRPropDistracter','NSTest1PropTarget','NSTest1PropDistracter','NSTest2PropTarget','NSTest2PropDistracter','NSTest3PropTarget','NSTest3PropDistracter']
    for key in keyArray:
        try:
            mean = across_subject_dict[CID][key][0]/across_subject_dict[CID][key][1]
        except ZeroDivisionError:
            mean = -1
        writeString += ','
        writeString += str(mean)
    writeString += '\n'
    f.write(writeString)

f.close()