import os
import csv
import sys
import pandas as pd
import numpy as np

os.chdir('C:/Users/Christina/Dropbox/Dissertation/Data')

f = open('summary-2017-09-25_T2_clean.csv', 'r')

input_mapping_dictionary = {}

header_row = f.readline()
split_header_row = header_row.split(',')
for i in range(0,len(split_header_row)):
    input_mapping_dictionary[split_header_row[i]] = i



print input_mapping_dictionary


across_subject_dict = {}

for line in f:
    linearray = line.split(',')
    if (linearray[input_mapping_dictionary['TIMEPOINT']] == '2' and int(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']]) > 0):
        if not(linearray[input_mapping_dictionary['CID']] in across_subject_dict):
            subject_dictionary =  {}
            subject_dictionary['CID'] = [0,0]
            subject_dictionary['SLPropFace2'] = [0,0]
            subject_dictionary['SLPropTarget2'] = [0,0]
            subject_dictionary['SLPropDistracter2'] = [0,0]
            subject_dictionary['SRPropFace2'] = [0,0]
            subject_dictionary['SRPropTarget2'] = [0,0]
            subject_dictionary['SRPropDistracter2'] = [0,0]
            subject_dictionary['STest1PropTarget2'] = [0,0]
            subject_dictionary['STest1PropDistracter2'] = [0,0]
            subject_dictionary['STest2PropTarget2'] = [0,0]
            subject_dictionary['STest2PropDistracter2'] = [0,0]
            subject_dictionary['STest3PropTarget2'] = [0,0]
            subject_dictionary['STest3PropDistracter2'] = [0,0]
            subject_dictionary['NSLPropFace2'] = [0,0]
            subject_dictionary['NSLPropTarget2'] = [0,0]
            subject_dictionary['NSLPropDistracter2'] = [0,0]
            subject_dictionary['NSRPropFace2'] = [0,0]
            subject_dictionary['NSRPropTarget2'] = [0,0]
            subject_dictionary['NSRPropDistracter2'] = [0,0]
            subject_dictionary['NSTest1PropTarget2'] = [0,0]
            subject_dictionary['NSTest1PropDistracter2'] = [0,0]
            subject_dictionary['NSTest2PropTarget2'] = [0,0]
            subject_dictionary['NSTest2PropDistracter2'] = [0,0]
            subject_dictionary['NSTest3PropTarget2'] = [0,0]
            subject_dictionary['NSTest3PropDistracter2'] = [0,0]
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
           across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropFace2'][0] += float(linearray[input_mapping_dictionary['face']])/float(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']])
           across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropFace2'][1] += 1
        elif trialtype in ['Test1', 'Test2', 'Test3']:
            targetval = linearray[input_mapping_dictionary['LEFT_IA']]
            distval = linearray[input_mapping_dictionary['RIGHT_IA']]
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropTarget2'][0] += float(targetval)/float(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']])
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropTarget2'][1] += 1
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropDistracter2'][0] += float(distval)/float(linearray[input_mapping_dictionary['TRIAL_DWELL_TIME']])
        across_subject_dict[linearray[input_mapping_dictionary['CID']]][blocktype+trialtype+'PropDistracter2'][1] += 1

f.close()

f = open('WugLife_processed_9-25-17_T2.csv', 'w')
    
writeString = 'CID,SLPropFace2,SLPropTarget2,SLPropDistracter2,SRPropFace2,SRPropTarget2,SRPropDistracter2,STest1PropTarget2,STest1PropDistracter2,STest2PropTarget2,STest2PropDistracter2,STest3PropTarget2,STest3PropDistracter2,NSLPropFace2,NSLPropTarget2,NSLPropDistracter2,NSRPropFace2,NSRPropTarget2,NSRPropDistracter2,NSTest1PropTarget2,NSTest1PropDistracter2,NSTest2PropTarget2,NSTest2PropDistracter2,NSTest3PropTarget2,NSTest3PropDistracter2'
writeString += '\n'
f.write(writeString) 

for CID in across_subject_dict:

    writeString = ''
    writeString += str(CID)
    keyArray = ['SLPropFace2','SLPropTarget2','SLPropDistracter2','SRPropFace2','SRPropTarget2','SRPropDistracter2','STest1PropTarget2','STest1PropDistracter2','STest2PropTarget2','STest2PropDistracter2','STest3PropTarget2','STest3PropDistracter2','NSLPropFace2','NSLPropTarget2','NSLPropDistracter2','NSRPropFace2','NSRPropTarget2','NSRPropDistracter2','NSTest1PropTarget2','NSTest1PropDistracter2','NSTest2PropTarget2','NSTest2PropDistracter2','NSTest3PropTarget2','NSTest3PropDistracter2']
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