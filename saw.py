import numpy as np

dataUji = np.array([['matematika', 'fisika', 'biologi'],['aditia', 'adam', 'diana'], [10,4,32], [12,78,33], [13,11,23]])

matkul = dataUji[0]
mhs = dataUji[1]

j = 2
for x in mhs:
    m = 0
    t_nilai = np.array([])
    tmpK = []
    totalNilai = 0
    print("----- "+x+" -------")
    for k in matkul:
        print("Nilai " + k + " = " + dataUji[j,m])
        tmpK.append(dataUji[j, m])
        totalNilai = totalNilai + int(dataUji[j,m])
        m += 1
    rataRata = totalNilai / 3
    t_nilai = np.append(t_nilai, tmpK)
    print("Total nilai : " + str(totalNilai))
    print("Rata rata : " + str(rataRata))
    print("------------------------------")
    j += 1

print("----------------------------")

nMatematika =  []
nFisika = []
nBiologi = []
mo = 2
fo = 2
bo = 2

for x in range(3):
    nMatematika.append(dataUji[mo, 0])
    mo += 1

for x in range(3):
    nFisika.append(dataUji[fo, 1])
    fo += 1

for x in range(3):
    nBiologi.append(dataUji[bo, 2])
    bo += 1

maxMatematika = max(nMatematika)

print(maxMatematika)
