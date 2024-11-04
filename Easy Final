with open('stu_19.dat') as f_all:  #Read the original file to create a new file for only the first patient's data
    pat1 = []   #Extract data of first patient
    for line in f_all:
        pat1.append(line) 
        if 'Matrix' in line: break  #Keyword to indicate the finish line of the first patient's data
    f_pat1 = open('stu19_pat1.dat','w') #Create a new file
    f_pat1.write(''.join(pat1))
    f_pat1.close()

#Identify each line that holds query sequence
SampleA, SampleB = '', '' #Extract first line (SampleA) and second line (SampleB) Sequences
loc=[] #Identify starting positions for each query line.
with open ('stu19_pat1.dat') as fo:
    line = fo.readlines()
    for pos, val in enumerate(line):
        if 'Query_' in val:
            loc += line[pos].split()[1::4]
            SampleA += line[pos+1].split()[2]
            SampleB += line[pos+2].split()[2]
Sample_A= list(SampleA)
Sample_B = list(SampleB)
print(loc)

ASTR = '' #An empty string for all Sample A
BSTR =''  #An empty string for all Sample B
for i in range(len(Sample_A)):
    if "." not in Sample_A[i]:
        ASTR = ASTR +str(i+int(loc[0]))  +  ' '
for i in range(len(Sample_B)):  #Finding first line (SampleA) mutation positions
       if Sample_B[i] != '.':   #Finding second line (SampleB) mutation positions
            BSTR = BSTR + str( i+int(loc[0])) + ' '
print('Sample A:')         
print (ASTR)
print (' ')
print ('Sample B:')
print(BSTR)
