##Nama : Bayu Yudha Bhakti
##NIM : L200170010
##Kelas : A

##Nomor 1

class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

c0 = MhsTIF('Ika', 10, 'Magetan','L200180048')
c1 = MhsTIF('Budi', 51, 'Sukoharjo','L200180028')
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 'L200180018')
c3 = MhsTIF('Chandra', 18, 'Surakarta','L200180012')
c4 = MhsTIF('Eka', 4, 'Boyolali','L200180132')
c5 = MhsTIF('Fandi', 31, 'Salatiga','L200180042')
c6 = MhsTIF('Deni', 13, 'Klaten', 'L200180088')
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 'L200180014')
c8 = MhsTIF('Janto', 23, 'Klaten', 'L200180022')
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 'L200180124')
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 'L200180089')


Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)

##Nomor 2

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [1,3,5,2,4,8,12,18,14,22]
B = [19,7,9,17,11,16,13,20,15]
C = []
C.extend(A)
C.extend(B)
print ('Nilai C' , C)

##N0m0r 3

from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[q]= A[q]
    A[q]= tmp
    
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil   

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion:%g detik' %(ak-aw));
