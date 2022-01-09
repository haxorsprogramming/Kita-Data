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
maxFisika = max(nFisika)
maxBiologi = max(nBiologi)

# normalisasi
konvMatematika = []
konvFisika = []
konvBiologi = []

for x in nMatematika:
    nKonv = int(x) / int(maxMatematika)
    konvMatematika.append(nKonv)

for x in nFisika:
    nKonv = int(x) / int(maxFisika)
    konvFisika.append(nKonv)

for x in nBiologi:
    nKonv = int(x) / int(maxBiologi)
    konvBiologi.append(nKonv)

# perhitungan nilai prefrensi 
bbMatematika = 0.3
bbFisika = 0.5
bbBiologi = 0.2
pMatematika = []
pFisika = []
pBiologi = []

for x in konvMatematika:
    nP = x * bbMatematika
    pMatematika.append(nP)

for x in konvMatematika:
    nP = x * bbFisika
    pFisika.append(nP)

for x in konvBiologi:
    nP = x * bbBiologi
    pBiologi.append(nP)

tAdit = []
tAdit.append(pMatematika[0])
tAdit.append(pFisika[0])
tAdit.append(pBiologi[0])

totalAdit = sum(tAdit)

print(totalAdit)



