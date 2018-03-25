import csv

ini_csv = ['outTime', 'inTime', 'Speed', 'Size','Lane']
list1 = [[111461.35, 110994.21666666667, 64.22149279292162, 4160.5, 2], [112862.75, 112328.88333333333, 56.19380619380599, 4816.0, 2], [114130.68333333333, 113663.55, 64.22149279292162, 52160.0, 2], [117000.21666666667, 116533.08333333333, 64.22149279291963, 4951.5, 2], [123273.15000000001, 122806.01666666666, 64.22149279291963, 4429.0, 2], [131548.08333333334, 131014.21666666667, 56.19380619380599, 4978.5, 2], [133349.88333333333, 132816.01666666666, 56.19380619380599, 5676.5, 3], [159175.68333333335, 158775.28333333333, 74.92507492507056, 1204.5, 3], [162045.21666666667, 161578.08333333334, 64.22149279292162, 3935.5, 2], [168251.41666666666, 167784.28333333333, 64.22149279292162, 4765.5, 1], [169519.35, 168985.48333333334, 56.19380619380599, 17609.0, 3], [172989.48333333334, 172589.08333333334, 74.925074925076, 5128.5, 1]]
path = './output.csv'

with open(path, 'w') as csvfile:
    
    wr = csv.writer(csvfile, quoting = csv.QUOTE_ALL )
    wr.writerow(ini_csv)
    for ele in list1:
        wr.writerow(ele)

print("ended well")        