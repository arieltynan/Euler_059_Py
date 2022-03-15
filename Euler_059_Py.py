#Ariel Tynan
#Euler Problem 059, XOR decryption, solved in Python
#Started 14 March 2022, solved 15 March 2022 (1am)

#Read in file
with open('p059_cipher.txt') as f:
    if open:
        print("File has opened successfully.")
    output = str(f.read().replace(',',' '))
    #output = output.replace(" ","")
str_list = output.split()
code = []
for i in str_list:
    code.append(int(i))

#Encription key is 3 lower case characters
total = 0 #sum of all ascii values for answer
for i in range(97,123): #a-97, z-122
    #print("First element:",i)
    for j in range(97,123):
        for k in range(97,123):
            cipher = [i,j,k]
            shift = 0 #shifting between elements of key
            #temp = code #reset code
            ans = [None]*len(code) #reset answer
            for x in range(0,len(code)): #shifting between 3 elements in key
                if shift == 0:
                    ans[x] = code[x] ^ cipher[0] #XOR gate ^
                    shift = 1
                elif shift == 1:
                    ans[x] = code[x] ^ cipher[1]
                    shift = 2
                elif shift == 2:
                    ans[x] = code[x] ^ cipher[2]
                    shift = 0
                if ans[x] < 0:
                    ans[x] = ans[x] + 127

            OF = THE = AND = EULER = 0 #setting vars
            for m in range(0,len(ans)-5):
                if ans[m] == 32 and ans[m+1] == 116 and ans[m+2] == 104 and ans[m + 3] == 101: #" the"
                    #print("THE found at", cipher)
                    THE = 1
                if ans[m] == 32 and ans[m+1] == 97 and ans[m+2] == 110 and ans[m + 3] == 100: #" and"
                    #print("AND found at", cipher)
                    AND = 1
                if ans[m] == 32 and ans[m+1] == 69 and ans[m+2] == 117 and ans[m + 3] == 108 and ans[m + 4] == 101 and ans[m + 5] == 114 : #" Euler"
                    #print("EULER found at", cipher)
                    Euler = 1
                if ans[m] == 32 and ans[m+1] == 111 and ans[m+2] == 102: #" of"
                    #print("OF found at", cipher)
                    OF = 1
            #Found high frequency of use of the above words, including the only instance of "Euler"
            if THE == 1 and AND == 1 and Euler == 1 and OF == 1: #cipher == [101,120,112]:
                for k in ans: #sums all ints/ascii nums
                    #print(chr(k)) #print for message
                    total = total + k
                print(total) #answer
                    
                
