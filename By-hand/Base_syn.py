# Base syntax for str

#def base_syn(name):
  #  print('I am ',name)
  #  #result= 'I am '+name
  #  #return result

#base_syn('zhanghy')




#def base_syn(P1):
 #   result = 'I am '+' '+P1
 #   return result
#emm= base_syn('zhy')
#print(emm)
#a=base_syn('xiaoming')
#print(a)
#b=base_syn('xiaohong')
#print(b)



def base_syn(a='aaa',b='bbb',c='ccc'):
    emm = c+b+a
    print(emm)

base_syn()
#位置传递参数  a=groot b='bbb',c='ccc'
base_syn('groot ','am ','I ')
#关键字传递参数
base_syn(a='groot ',c='I')