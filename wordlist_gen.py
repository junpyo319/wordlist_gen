import re
from itertools import product

header = 'wordlist_gen..'

def get_len() :
  len_opt = input('set length.. e.g. 4:8..\t')
  return re.split(':',len_opt)

def get_chrset() :
  chrset_opt1 = input('Do you want to include alphabet into the set? (y/n)\t')
  if chrset_opt1 == 'y' :
    chrset_opt1_1 = input('Do you want specify alphabet? (y/n)\t')
    if chrset_opt1_1 == 'y' :
      chrset_tmp1 = input('input char set.. e.g. abcd\t')
    elif chrset_opt1_1 == 'n' :
      chrset_tmp1 = 'abcdefghijklmnopqrstuvwxyz'
    else :
      get_chrset()
  elif chrset_opt1 == 'n' :
    chrset_tmp1 = ''
  else :
    get_chrset()

  chrset_opt2 = input('Do you want to include numeric char into the set? (y/n)\t')
  if chrset_opt2 == 'y' :
    chrset_opt2_1 = input('Do you want to specify nemeric char? (y/n)\t')
    if chrset_opt2_1 == 'y' :
      chrset_tmp2 = input('input numeric set.. e.g. 1234\t')
    elif chrset_opt2_1 == 'n' :
      chrset_tmp2 = '123456789'
  elif chrset_opt2 == 'n' :
    chrset_tmp2 = ''
  else :
    get_chrset()

  chrset_tmp = chrset_tmp1 + chrset_tmp2
  print('chrset : ' + chrset_tmp)

  if not chrset_tmp :
    print('chrset is empty...')
    get_chrset()
  elif chrset_tmp:
    return [chr for chr in chrset_tmp]

def print_list(len_opt, chrset) :
  i = int(len_opt[0])
  with open("wordlist.txt", 'w') as f :
    for i in range(int(len_opt[0]), int(len_opt[1]) + 1) :
      for j in product(chrset, repeat = i) :
        wd = ''.join(j)
        f.write(wd + '\n')

def duple(chrset) :
  chrset_len = len(chrset)
  for i in range(0, chrset_len) :
    for j in range(i + 1, chrset_len) :
      if chrset[i] == chrset[j] :
        chrset.remove(chrset[j])
        return duple(chrset)
      elif (i == chrset_len - 2) and (j == chrset_len - 1) :
        return chrset

len_opt = get_len()
chrset = get_chrset()
chrset = duple(chrset)
print_list(len_opt,chrset)
