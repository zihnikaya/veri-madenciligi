from scipy.spatial import distance
hasan = [30, 4000]
ali = [28, 3500]
mahmut = [59, 12000]
ha_oklid_mesafesi = distance.euclidean(hasan, ali)
hm_oklid_mesafesi = distance.euclidean(hasan, mahmut)
am_oklid_mesafesi = distance.euclidean(ali, mahmut)
print("Hasan ile Ali arasındaki uzaklık:{} \nHasan ile Mahmut arasındaki uzaklık:{}"
"\nALi ile Mahmut arasındaki uzaklık:{}\n".format(ha_oklid_mesafesi,hm_oklid_mesafesi,am_oklid_mesafesi))
