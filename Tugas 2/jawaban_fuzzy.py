'''
    PROGRAM     solving_fuzzy
    CREATED BY  Enki Probo Sidhi
'''

'''
     Problem Summary:
        - There are two input variables ie. 'Emosi' and 'Provokasi'
        - Both variables have crisp value as follow [0,100]

        - There is an output variable ie. 'Hoax'
        - 'Hoax' variable can have two crisp value and that is Ya or Tidak
'''

'''
    Solution Plan:
        - Input variable Emosi will have <some level> fuzzy set value and that is <it,et,ot>
        - Input variable Provokasi will have <some level> fuzzy set value and that is <it,et,ot>

        - For determining Emosi values, fuzzy membership function is defined as follow:
            - membership function for <it>
            - membership function for <et>
            - membership function for <ot>
        - For determining Provokasi values, fuzzy membership function is defined as follow:
            - membership function for <it>
            - membership function for <et>
            - membership function for <ot>

        - Inference rule that will be used is <this> (Inference Rule is Fuzzy Rule, number of member of rules is |number of level in Emosi|*|number of level in Provokasi|):

        - Value of degree of feasibility is [0,100] 
'''

import membership_function_factory as mff

def main(listOfCrispInput):

    print "Berita | Emosi | Provokasi | Hoax " 
    b = 0
    for crispInput in listOfCrispInput:

        # define a level of each fuzzy set
        numberOfEmosiLevel = 3 # kecil 0, sedang 1, besar 2
        mFunctionEmosi = [mff.trapesium, mff.trapesium, mff.trapesium]
        mParameterEmosi = []
        mParameterEmosi.append({"a":0,"b":0,"c":60,"d":70}) # untuk kecil 0
        mParameterEmosi.append({"a":65,"b":65,"c":72,"d":82}) # untuk sedang 1
        mParameterEmosi.append({"a":60,"b":85,"c":100,"d":100}) # untuk besar 2

        numberOfProvokasiLevel = 4 # kecil 0, menuju kecil 1, menuju besar 2, besar 3
        mFunctionProvokasi = [mff.trapesium for i in range(numberOfProvokasiLevel)]
        mParameterProvokasi = []
        mParameterProvokasi.append({"a":0,"b":0,"c":25,"d":30}) # untuk kecil 0
        mParameterProvokasi.append({"a":10,"b":30,"c":65,"d":75}) # untuk menuju kecil 1
        mParameterProvokasi.append({"a":73,"b":75,"c":80,"d":91}) # untuk menuju besar 2
        mParameterProvokasi.append({"a":85,"b":90,"c":100,"d":100}) # untuk besar 3

        numberOfHoaxLevel = 2 # level of fuzzy set in output, 0 for Tidak, 1 for Ya
        mFunctionHoax = [mff.trapesium for i in range(numberOfHoaxLevel)]
        mParameterHoax = []
        mParameterHoax.append({"a":0,"b":0,"c":70,"d":80}) # untuk Tidak
        mParameterHoax.append({"a":70,"b":85,"c":100,"d":100}) # untuk Ya

        # initiate the fuzzy set based on level exist
        fSEmosi = []
        fSProvokasi = []

        # crisp input
        xEmosi = crispInput[0]
        xProvokasi = crispInput[1]

        # FUZZIFICATION
        for i in range(numberOfEmosiLevel):
            fSEmosi.append(mff.membership_function(mFunctionEmosi[i], xEmosi, mParameterEmosi[i]))
        for i in range(numberOfProvokasiLevel):
            fSProvokasi.append(mff.membership_function(mFunctionProvokasi[i], xProvokasi, mParameterProvokasi[i]))

        # print fSEmosi
        # print fSProvokasi

        # INFERENCE
        tempHoax = [[] for i in range(numberOfHoaxLevel)]
        fSHoax = [[] for i in range(numberOfHoaxLevel)]

        for i in range(numberOfEmosiLevel):
            for j in range(numberOfProvokasiLevel):
                if i == 0 and j == 0:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 0 and j == 1:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 0 and j == 2:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 0 and j == 3:
                    tempHoax[1].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 1 and j == 0:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 1 and j == 1:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 1 and j == 2:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 1 and j == 3:
                    tempHoax[1].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 2 and j == 0:
                    tempHoax[0].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 2 and j == 1:
                    tempHoax[1].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 2 and j == 2:
                    tempHoax[1].append(min(fSEmosi[i], fSProvokasi[j]))
                elif i == 2 and j == 3:
                    tempHoax[1].append(min(fSEmosi[i], fSProvokasi[j]))

        fSHoax[0] = max(tempHoax[0])
        fSHoax[1] = max(tempHoax[1])

        # print fSHoax

        # DEFUZZIFICATION

        # menggunakan mamdani
        numberOfSplit = 10
        perSplit = 100/numberOfSplit

        nilaiAtas = []
        nilaiBawah = []

        for i in range(numberOfSplit):
            xHoax = perSplit*(i+1)

            nilai1 = mff.membership_function(mFunctionHoax[1], xHoax, mParameterHoax[1])
            pengali1 = min(fSHoax[1], nilai1)

            nilai2 = mff.membership_function(mFunctionHoax[0], xHoax, mParameterHoax[0])
            pengali2 = min(fSHoax[0], nilai2)

            pengaliA = max(pengali1,pengali2)

            nilaiAtas.append(xHoax*pengaliA)
            nilaiBawah.append(pengaliA)

        derajatHoax = sum(nilaiAtas)/sum(nilaiBawah)

        # print derajatHoax

        # PENENTUAN AKHIR
        apakahHoax = ""
        if derajatHoax<50:
            apakahHoax = "Tidak"
        else:
            apakahHoax = "Ya"

        # PRINT HASIL
        b += 1
        print "B"+str(b), "|", xEmosi, "|", xProvokasi, "|", apakahHoax

listOfCrispInput = [
    (97, 74),
    (36, 85),
    (63, 43),
    (82, 90),
    (71, 25),
    (79, 81),
    (55, 62),
    (57, 45),
    (40, 65),
    (57, 45), #10
    (77, 70),
    (68, 75),
    (60, 70),
    (82, 90),
    (40, 85),
    (80, 68),
    (60, 72),
    (50, 95),
    (100, 18),
    (11, 99)
]

main(listOfCrispInput)