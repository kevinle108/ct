from traceback import print_tb
from nbformat import read
import pandas as pd

def len_val(dict):
  count = 0
  for k,v in dict.items():
    count += len(v)
  return count

root_path = 'data/raw/counties/ct_county_*.csv'
files = [
  'fairfield',
  'hartford',
  'litchfield',
  'middlesex',
  'newhaven',
  'newlondon',
  'tolland',
  'windham'
]

all_munis = pd.read_csv('data/raw/municipalities/ct_muni_all.csv')['Name'].tolist()

alltowns = []
nottowns = []
townsCount = 0
countyMap = {}
# df = pd.read_csv(input_path.replace('*'))
for file in files:
  file_path = root_path.replace('*', file)
  df = pd.read_csv(file_path)
  towns = df['Town']
  outKey = file
  outVal = []
  for town in towns:   
    if town not in all_munis:
      print(f'\t***unknown town:{town}***')
      nottowns.append(town) 
    else: 
      outVal.append(town)
  countyMap[outKey] = outVal

for k, v in countyMap.items():
  print(k)
  print(f'\t{len(v)}')
  townsCount += len(v)



print(f'townCount {townsCount}')

# for county,towns in countyMap.items():
#   print(county)
#   no_dups = [town for town in towns if towns.count(town) == 1]
#   dups = {county:town for town in towns if towns.count(town) > 1}
#   countyMap[county] = no_dups
#   if dups.get(county):
#     print(dups)

print(len_val(countyMap))
  