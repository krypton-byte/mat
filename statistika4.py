#!/usr/bin/env python3
import numpy as np
from math import sqrt as root
from prettytable import PrettyTable
def materi():
    print("""
1. Membaca & Menyajikan
2. Ukuran Pemusatan
3. Ukuran Letak
4. Ukuran Penyebaran
    - Nilai yang menyatakan seberapa jauh data dari pusat data
    - Materi : - Jangkauan/Range
                 pengertian: Selisih antara data dengan nilai yang terbesar dengan data dengan nilai yg terkecil pada
                             Data Tunggal:
                                R = X{max}-X{min} 
                                contoh: [3], 5, 6, 8, 9, [10]
                                    R = 10 - 3
                                    R = 7
                            Data Kelompok:
                                Sesilish Tiktik tengah kelas tertingi dengan titik tengah terendah
                                kelas   |  Titik Tengah | fi |
                                13, 15  |    [14]       |  5 |
                                16, 18  |     17        |  7 | R = 23 - 14
                                19, 21  |     20        |  2 | R = 9
                                22, 24  |    [23]       | 20 |
                                ------------------------------
                                            Jumlah      | 20 |
               - Jangkauan Antar Kuartil/Hamparan
                    - Selish antara kuartil ketiga dengan kuartil pertama
                    H = Q3 - Q1
               - Simpangan Quartil
                    - Setengah Jangkauan antar quartil
                    Qd = 1/2 H
               - Simpangan Rata-Rata
                    - Merupakan penyebaran nilai dari nilai rata rata dari suatu data
                    Data Tunggal:
                        - Jumlah harga mutlak selisih setiap nilai data xi dengan nilai rata-rata  x̄ di bagi banyak dat
                        SR=(Σn|xi-x̄|)/n
                        Contoh:
                            Tentukanlah Simpangan rata-rata dari data 3, 4, 5, 6, 7
                    Data Kelompok:
                        SR = (Σk fi|xi-x̄|)/Σk fi
                        Tentukan Simpangan rata rata dari
                        | Berat Badan (Kg)|Frekuensi|           |  f1 | x1 | f1 * x1 | [xi-x̄] | fi[xi-x̄] |
                        |     50, 54      |    3    |           |  3  | 52 |   156   |   13   |    39    |
                        |     55, 59      |    4    |  ----\    |  4  | 57 |   228   |    8   |    32    |
                        |     60, 64      |    5    |       \   |  5  | 62 |   310   |    3   |    15    |
                        |     65, 59      |    2    |       /   |  2  | 67 |   134   |    2   |    4     |
                        |     70, 74      |    2    |  ----/    |  2  | 72 |   144   |    7   |    14    |
                        |     75, 79      |    4    |           |  4  | 77 |   308   |    12  |    48    |               ----------------------------            ----------------------
                                                                   Σ     20   1.300                152

                        x̄ = Σ f1*x1/Σf
                        x̄ = 1300/20
                        x̄ = 65

                        SR = Σ f1|x1-x̄|/Σf
                        SR = 152/20
                        SR = 7.6
               - Ragam / Variasi
                    Ukuran Seberapa Jauh Sebuah kumpulan bilangan tersebar
                    Data Tunggal:
                        S^2 = Σn(x1-x̄)^2/n
                        Tentukan Ragam dari data [3, 4, 5, 6, 7]
                        x̄ = (3+4+5+6+7)/5
                        x̄ = 5
                        S^2 = ((3-5)^2+(4-5)^2+(5-5)^2+(6-5)^2+(7-5)^2)/5
                        S^2 = (4+1+0+1+4)/5
                        S^2 = 10/5
                        S^2 = 2
                    Data Kelompok:
                        S2 = (Σfi(x1-x̄)^2)/Σfi
               - Simpangan Baku
                    Merupakan Salah satu teknik statistik yang digunakan untuk menjelaskan homogenitas dari sebuah kelompok.
                    Fungsi: -Untuk menjelaskan bagaimana sebaran data dalam sampel
                            -Menyatakan Hubungan Antara Titik individu dan mean atau rata rata nilai data dari sampel
                    S = √S^2
""")
x_bar_p = lambda n:sum(n)/n.__len__()
Range_tunggal = lambda n:max(n)-min(n)
def range_kelompok(data=[[1, 3], [4, 6], [8, 10]], frekuensi=[], isprint=False):
    tengah=[median(range(x, y+1)) for x, y in data]
    if isprint:
        table = PrettyTable()
        table.add_column("Data", data)
        table.add_column("Titik Tengah", tengah)
        if frekuensi.__len__() == data.__len__():
            table.add_column("fi", frekuensi)
        print(table)
        print(f"R = {max(tengah)}-{min(tengah)}")
        print(f"R = {max(tengah)-min(tengah)}")
    return max(tengah)-min(tengah)
def median(data):
    data=list(data)
    data.sort()
    if data.__len__()%2:
        return data[int((len(data)+1)/2)-1]
    else:
        return sum(data[int(len(data)/2)-1:int(len(data)/2)+1])/2


def SimpanganRataRata_tunggal(data=[3, 4, 5, 6, 7 ]):
    data = np.array(data)
    data.sort()
    SR_ = data-x_bar_p(data)
    SR_[SR_< 0] = -SR_[SR_< 0]
    return SR_.sum()/x_bar_p(data)


def SimpanganRataRata_kelompok(data = [[1, 3], [4, 6], [7, 9], [10, 12], [13, 15]], frekuensi = [4, 5, 6, 3, 2], isprint=False):
    assert data.__len__() == frekuensi.__len__()
    x1 = np.array([median(range(x, y+1)) for x, y in data])
    fi_xi = np.array(frekuensi)*x1
    x_bar = fi_xi.sum() / sum(frekuensi)
    xi_min_xbar =  x1-x_bar
    xi_min_xbar[xi_min_xbar<0]=-xi_min_xbar[xi_min_xbar<0]
    fi_xi_min_xbar = np.array(frekuensi)*xi_min_xbar
    if isprint:
        table = PrettyTable()
        table.add_column("Data", data)
        table.add_column("Frekuensi", frekuensi)
        table.add_column("xi", x1)
        table.add_column("fi*xi",fi_xi)
        table.add_column("[xi-x̄]", xi_min_xbar)
        table.add_column("fi[xi-x̄]", fi_xi_min_xbar)
        table.add_row(["Σ", sum(frekuensi).__str__(), " ", fi_xi.sum().__str__(), " ", fi_xi_min_xbar.sum().__str__()])
        print(table)
        print(f"SR = {fi_xi_min_xbar.sum()}/{sum(frekuensi)}\nSR = {fi_xi_min_xbar.sum()/sum(frekuensi)}")
    return fi_xi_min_xbar.sum()/sum(frekuensi)


def RAGAM_kelompok(data=[[19, 21], [22, 24], [25, 27], [28,30]], frekuensi=[9, 4, 5, 2], isprint=False):
    assert data.__len__() == frekuensi.__len__()
    xi = np.array([median(range(x, y+1)) for x, y in data])
    fi_xi = np.array(frekuensi)*xi
    x_bar = fi_xi.sum()/sum(frekuensi)
    xi_min_xbar = xi-x_bar
    xi_min_xbar[xi_min_xbar<0] = -xi_min_xbar[xi_min_xbar<0]
    fi_xi_min_xbar_quadrat = (xi_min_xbar**2)*np.array(frekuensi)
    if isprint:
        table = PrettyTable()
        table.add_column("Data", data)
        table.add_column("Frekuensi", frekuensi)
        table.add_column("xi", xi)
        table.add_column("fi*xi", fi_xi)
        table.add_column("[xi-x̄]", xi_min_xbar)
        table.add_column("f(xi-x̄)^2", fi_xi_min_xbar_quadrat)
        table.add_row(["Σ", sum(frekuensi).__str__(), " ", fi_xi.sum().__str__(), " ", fi_xi_min_xbar_quadrat.sum().__str__()])
        print(table)
        print(f"S^2 = {fi_xi_min_xbar_quadrat.sum()}/{sum(frekuensi)}\nS^2 = {fi_xi_min_xbar_quadrat.sum()/sum(frekuensi)}")
    return fi_xi_min_xbar_quadrat.sum()/sum(frekuensi)


def RAGAM_tunggal(data=[3, 4, 5, 6, 7 ]):
    x_bar = x_bar_p(data)
    S2 = sum((np.array(data)-x_bar)**2)/data.__len__()
    return S2


def SimpanganBaku_tunggal(data=[3, 4, 5, 6, 7]):
    return round(root(RAGAM_tunggal(data)), 3)


def SimpanganBaku_kelompok(data=[[19, 21], [22, 24], [25, 27], [28,30]], frekuensi=[9, 4, 5, 2], isprint=False):
    assert data.__len__() == frekuensi.__len__()
    ragam = RAGAM_kelompok(data=data, frekuensi=frekuensi, isprint=isprint)
    hasil = round(root(ragam),2)
    if isprint:
        print(f"S = √{ragam}\nS = {hasil}")
    return hasil

