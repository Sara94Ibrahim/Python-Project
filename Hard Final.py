with open('stu_19.dat') as f:  #Reading all lines
    line = f.readlines()
    loc = []                   #Identifying the starting position for each query position
    SampleA, SampleB = '', ''  #Variables to Extract sampleA and sampleB sequence
    loc_all, SampleAs, SampleBs = [], [], []  #Creating lists for all starting positions and mutations
    for pos, val in enumerate(line):
        if 'Query_' in val:
            loc.append(line[pos].split()[1])
            SampleA += (line[pos+1].split())[2]
            SampleB += (line[pos+2].split())[2]
        if 'Matrix' in val:     # Keywork indicating Identifying the last line for each patient's data 
            loc_all.append(loc[0])
            SampleAs.append(SampleA)
            SampleBs.append(SampleB)
            SampleA, SampleB, loc = '', '', []

#print(loc_all)
#print (SampleAs)
#print (SampleBs)
#mutation positions: T134A, A443G, G769C, G955C, A990C, G1051A, G1078T, T1941A, T2138C, G2638T and A3003T
#Now, I want to test each sample to find the number and location of each mutation, so I will create a definition

#sample= SampleAs or SampleBs
#location = location of the entire file

def Mutation(number, sample, location): #Defining the function of the mutation testing
    mutation = []  #empty list to be appended 
    
    for pos, val in enumerate(sample): 
        posnum = int(location[pos]) #position number
        if val[number-posnum] != '.': #if statement to find the mutation
            mutation.append(pos)   #filling the empty list from before with the values 
    
    return mutation

#Ending the function    
#The last patient starts from 61
#no difference from the reference is 0
#heterozygous (only appearing in one allele/hap) is 1, homozygous (both alleles) is 2
print (f"{' ':^4}\t{'T134A': ^4}\t{'A443G': ^4}\t{'G769C': ^4}\t{'G955C': ^4}\t{'A990C': ^4}\t{'G1051A': ^4}\t{'G1078T': ^4}\t{'T1941A': ^4}\t{'T2138C': ^4}\t{'G2638T': ^4}\t{'A3003T': ^4}")

Mutnum_lst = [134, 443, 769, 955, 990, 1051, 1078, 1941, 2138, 2638, 3003] #muation number list
for patient in range(len(SampleAs)):
    lst =[]
    r = 0
    for m in Mutnum_lst:
        if patient in Mutation(Mutnum_lst[r], SampleAs, loc_all) and patient in Mutation(Mutnum_lst[r], SampleBs, loc_all):
                         lst.append('2')
        elif patient in Mutation(Mutnum_lst[r], SampleAs, loc_all) or patient in Mutation(Mutnum_lst[r], SampleBs, loc_all):
                         lst.append('1')
        else:
                         lst.append('0')
        r += 1
    print(f'pat{patient+1:02d}\t{lst[0]}\t{lst[1]}\t{lst[2]}\t{lst[3]}\t{lst[4]}\t{lst[5]}\t{lst[6]}\t{lst[7]}\t{lst[8]}\t{lst[9]}\t{lst[10]}') 
#identify the number of the patients in the file and print them
