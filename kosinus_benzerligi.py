from scipy.spatial import distance
a_vektoru = (3,4)
b_vektoru = (4,2)
a_b_uzaklik = distance.cosine(a_vektoru,b_vektoru)
a_b_benzerlik = 1-a_b_uzaklik;
print ("a ve b vektörleri arasındaki benzerlik:",a_b_benzerlik)
