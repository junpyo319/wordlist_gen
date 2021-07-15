from itertools import product

print('''

\033[93m☆\033[95m˚″´·.wordlist_gen..

''')

def get_len() :
  len_opt = input('1.\t\tset length.. e.g. 4:8..\t')
  return len_opt.split(':')

def get_chrset() :
  if input('2.\t\tDo you want to include alphabets into the set? (y/n)\t') == 'y' :
    if input('2-1.\tDo you want specify alphabets? (y/n)\t') == 'y' :
      chrset_tmp1 = input('\t\tinput alphabets.. e.g. abcd\t')
    else :
      chrset_tmp1 = 'abcdefghijklmnopqrstuvwxyz'
    if input('2-2.\tDo you want include upper alphabets? (y/n)\t') == 'y' :
      chrset_tmp1 = ''.join([chrset_tmp1, chrset_tmp1.upper()])
  else :
    chrset_tmp1 = ''

  if input('3.\t\tDo you want to include numeric chars into the set? (y/n)\t') == 'y' :
    if input('3-1.\tDo you want to specify nemeric chars? (y/n)\t') :
      chrset_tmp2 = input('\t\tinput numeric chars.. e.g. 1234\t')
    else :
      chrset_tmp2 = '0123456789'
    if input('3-2.\tDo you want include special chars? (y/n)\t') == 'y' :
      chrset_tmp2 = ''.join([chrset_tmp2, '!\][/?.,~-=";:><@#$%&*()_+\''])
  else :
    chrset_tmp2 = ''

  chrset = ''.join([chrset_tmp1, chrset_tmp2])
  
  print('chrset : ' + chrset)

  if not chrset :
    print('chrset is empty...')
    return get_chrset()
  elif chrset:
    return [chr for chr in chrset]

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

print('done...·´″˚\033[93m☆\033[95m')
