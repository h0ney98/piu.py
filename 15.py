# # выводим года
# # e=1900
# # while e <= 2022:
# #     print(e)
# #     e=e+1
#
#
# l1 = [1,2,3,'hello', ['test',10], 'word', True]
#
# l2 = list ('hello')
#
# l3=list((1,2,3))
#
#
#
# l4= [i for i in 'hello']
#
# l5= [i for i in 'hello World' if i  not in [' ', 'a','e','i','o','u']]
#
#
# print(l1,l2,l3,l4,l5, sep='\n')


for i in range (1,10) :
    for k in range (2,10):
        print (f'{i}*{k}={i*k}\t',end=' ')
    print('')

else:
    print ('well done')
