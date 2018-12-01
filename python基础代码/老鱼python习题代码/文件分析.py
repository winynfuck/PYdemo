# -*- coding: UTF-8 -*-


import linecache
import json
from collections import Counter
'''

@编码思路：
step1：获取文件中一行的数据构造一个字典
step2: 将所有行的字典组成一个列表。

@吐槽：逻辑一定要清晰，不然很难搞

@总结：原来linecache真的有用。


'''
def f_dict(content):
	'由每一行的数据构造一个字典'
	
	dict_content = {}
	dict_content_content = content#content值的序列
	
	fields='bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url'
	dict_content_keys = fields.split(',')#键的序列
	# print('键值的索引数是:',len(dict_content_keys))
	for i in range(len(content)):
		dict_content[dict_content_keys[i]] = dict_content_content[i]
	return dict_content
	
	
def remove_yinhao(a):
	'去除列表中每一个元素的单引号字符串内的双引号，并将结果整合以列表输出'
	g = str.maketrans('"',' ')
	b = []
	for each in a:
		each =each.translate(g).strip()
		b.append(each)
	return b
	

with open('twitter数据挖掘片段.txt','r',encoding = 'utf-8') as f:
	dict_sum = []
	count = 0  
	#获取行数
	while True:  
		buffer = f.read(1024 * 8192)  
		if not buffer:  
			break  
		count += buffer.count('\n')
	print('该文本行数是：',count)
	for i in range(1,count+1):
		f_content = linecache.getline('twitter数据挖掘片段.txt',i).split('","')
		# print('文件中一行数据的第一次索引数是:',len(f_content))
		# print(f_content)
		f_content =remove_yinhao(f_content)#重构一行的数据列表
		# print(f_content)
		# print('第%d行'%i)
		# print('文件中一行数据的第二次索引数是:',len(f_content))
		dict1 = f_dict(f_content)
		dict_sum.append(dict1)
		#print(dict_sum)
		#print(len(dict_sum))

'''

@解题思路：（该题的思路，请用1，2，3步骤描述该题思路）
@吐槽：（如果你还有更好的办法，请不吝啬地写在这里吧。）
@我真的不懂啊/我不喜欢去温习旧知识：（把不懂的地方写在这里）


'''
# usernames = []
# for each in dict_sum:
	# usernames.append(each['username'])
# usernames =list(set(usernames))

# user_file ='用户名文件.json'
# with open(user_file,'w') as username_json:
	# json.dump(usernames,username_json)
	

# print('该文本每一个用户的名字构成的列表： ',usernames)
# times = []
# count =0
# for each in dict_sum:
	# if '2012-11' in each['time']:
		# count += 1
	# times.append(each['time'][:10])
# print(list(set(times)))
# hours = []
# for eachhour in dict_sum:
	# hours.append(eachhour['time'][11:13])
# hour_count ={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0 ,
# '09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0 ,
# '17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'24':0 
# }
# # print(hour_count.keys())
# for eachhour in hours:
	# if eachhour in hour_count.keys():
		# hour_count[eachhour] += 1
# hour_count_max =sorted(hour_count.items(),key = lambda item : item[1],reverse = True)
# print(hour_count_max[0][0])
# count = 0
# for each in dict_sum:
	# if "https://twitter.com/umiushi_no_uta" in each['rt_v_url']:
		# count += 1
# print(count)
# content_max = 0
# content_max_uid = ''
# for each in dict_sum:
	# if len(each['content']) >= content_max:
		# content_max_uid = each['uid']
		# content_max = len(each['content']) 
# print(content_max_uid)
# uids = []
# for each in dict_sum:
	# uids.append(each['uid'])
# uids =list(set(uids))
# def weibo_cishu(a):
	# '此函数输入一个uid列表，用于检测发微博数最多的用户'
	# cishu = dict.fromkeys(a,0)
	# for each in dict_sum:
		# cishu[each['uid']] += 1
	# max =sorted(cishu.items(),key = lambda item: item[1],reverse = True)
	# max_uid =[]
	# for i in range(len(a)):
		# if max [i][1] == max[0][1]:
			# max_uid.append(max[i][0])
	# return max_uid
# print(weibo_cishu(uids))

# laiyuan =[]
# for each in dict_sum:
	# laiyuan.append(each['source'])
# laiyuan = list(set(laiyuan))
# laiyuan_cishu = dict.fromkeys(laiyuan , 0)
# for each in dict_sum:
	# laiyuan_cishu[each['source']] += 1
# keys =laiyuan_cishu.keys()
# values =laiyuan_cishu.values()
# print(list(zip(keys,values)))
# url_cisu = dict.fromkeys(uids,0)
# for each in dict_sum:
	# if each['rt_v_url'] != '':
		# url_cisu[each['uid']] += 1
# url_cisu = sorted(url_cisu.items(),key = lambda item :item[1],reverse =True)
# print(url_cisu)
# max_uid2 = []
# for i in range(len(url_cisu)):
	# if url_cisu[i][1] == url_cisu[0][1]:
		# max_uid2.append(url_cisu[i][0])
# print(max_uid2)			
	
# _11user=[]
# for each in dict_sum:
	# if each['time'][11:13] == '11':
		# _11user.append(each['uid'])
# def all_list(arr):
	# result = {}
	# for i in set(arr):
		# result[i] = arr.count(i)
	# return result
# uidmax = sorted(all_list(_11user).items(),key = lambda item :item[1],reverse =True)
# max_uid3 = []
# for i in range(len(uidmax)):
	# if uidmax[i][1] == uidmax[0][1]:
		# max_uid3.append(uidmax[i][0])
# print(max_uid3)
# user =dict.fromkeys(uids,0)
# for each in dict_sum:
	# if each['v_url'] != '':
		# user[each['uid']] += 1
# user = sorted(user.items(),key = lambda item :item[1],reverse =True)
# print(user[0][0])
# def all_list(arr):
		# result = {}
		# for i in set(arr):
			# result[i] = arr.count(i)
		# return result
# def tweets(day):
	# usernames=[]
	# for each in dict_sum:
		# if each['time'][:10] == day:
			# usernames.append(each['username'])
	# user_max =all_list(usernames)
	# user_max =sorted(user_max.items(),key = lambda item :item[1],reverse =True)
	# return user_max[0][0]
# day =[]
# for each in dict_sum:
	# day.append(each['time'][:10])
# day =list(set(day))


# max =[]
# for i in range(len(day)):
	# max.append(tweets(day[i]))
# result = dict(list(zip(day,max)))
# print(result)
# a =[]
# def all_list(arr):
		# result = {}
		# for i in set(arr):
			# result[i] = arr.count(i)
		# return result
# for each in dict_sum:
	# a.append(each['time'][11:13])
# a= all_list(a)
# keys_a =a.keys()
# vals_a =a.values()
# zipped =list(zip(keys_a,vals_a))
# print(zipped)

	

		