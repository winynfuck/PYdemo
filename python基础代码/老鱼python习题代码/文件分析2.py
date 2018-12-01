#coding=UTF-8
#Author:Winyn
import linecache,time
'''
文件的数据准备。数据结构，一个大列表中包含每一行数据构成的小列表。

'''
starttime =time.time()
#打开文件，把所有行的数据放到一个列表中，列表中每一个元素是每一行的内容
lines = linecache.getlines('twitter数据挖掘片段.txt')

#把每一行的内容切分成小列表，再把所有的小列表构建成一个大列表。
f_lines = []
for line in lines:
	line =line[1:-2].split('","')#因为linecache获取的每行数据后面有\n，因此切分到-2
	f_lines.append(line)


'''
构建每一行数据对应字段的名称与在id的字典关系。


'''
fields = 'bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url'
fields = fields.split(',')

key={x:fields.index(x) for x in fields}


'''
获取该文本中的用户数

'''
user_num = len(set([line[key['uid']] for line in f_lines ]))

'''
获取该文本中，每一个用户的名字，输出一个list。

'''
user_name = list(set([line[key['username']] for line in f_lines ]))


'''
获取该文本中，在2012年11月发布的tweets数

'''
tweets_2012_11_num =len(list(filter(lambda x:x[key['time']][:7]=='2012-11',f_lines)))
#上面的方法要开辟很大空间新建一个列表，不好。
# tweets_2012_11_num = 0
# for line in f_lines:
	# if line[key['time']][:7]=='2012-11':
		# tweets_2012_11_num +=1

		
'''
统计该文本中有哪几天的数据，返回一个list

'''
date =list(set([line[key['time']][:10] for line in f_lines ]))

'''
统计该文本中，哪个小时发布的数据最多


'''
#构建一个计数字典
hour = dict.fromkeys(list(range(0,24)),0)

#获取小时数据
hour_list = [int(line[key['time']][11:13]) for line in f_lines ]

#进行计数
for each in hour_list:
	hour[each] += 1
#进行排序
hour_max = sorted(hour.items(),key = lambda x: x[1], reverse =True)[0][0]

'''
获取文本中，每一天发表tweets最多的用户。输出一个字典。

'''
#构建一个计数字典，格式{日期：{用户名：发表的tweets数}}

tweets_max ={day:{} for day in date}


#遍历文本的每一行数据进行计数，添加到大字典里面的小字典里去。
for line in f_lines:
	day_day =line[key['time']][:10]
	if line[key['username']] not in tweets_max[day_day].keys():
		tweets_max[day_day][line[key['username']]] = 1
	else:
		tweets_max[day_day][line[key['username']]] += 1
#进行排序
#这里没有很直接的二维字典排序方法，不过可以变通一下
for k,v in tweets_max.items():
	#对解析下的一维字典进行排序
	v = sorted(v.items(),key = lambda x: x[1],reverse =True)[0][0]
	tweets_max[k] = v
	
	
'''
获取2012-11-03这天每小时发布tweets的频率


'''
#先过滤得到在2012-11-03号这天发布的数据
list_2012_11_03 = list(filter(lambda x:x[key['time']].split(' ')[0] =='2012-11-03',f_lines))

#构建一个计数字典
dict_2012_11_03_hours = dict.fromkeys(list(range(0,24)),0)

#获取小时数据
hour_2012_11_03_list = [int(each[key['time']][11:13]) for each in list_2012_11_03 ]

#进行计数
for each in hour_2012_11_03_list:
	dict_2012_11_03_hours[each] += 1
list_f = [(x,y)for x,y in dict_2012_11_03_hours.items()]


'''
统计文本中，来源的相关信息和次数

'''

#获取来源的相关信息数据
source_list = [each[key['source']] for each in f_lines ]

#构建一个计数字典
dict_source= dict.fromkeys(source_list,0)
#进行计数
for each in source_list:
	dict_source[each] += 1
list_source = [(x,y)for x,y in dict_source.items()]


'''
计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个

'''
url_num =len(list(filter(lambda x :x[key['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'), f_lines)))



'''
 UID为573638104的用户 发了多少个微博

'''
uid_573638104_num =len(list(filter(lambda x :x[key['uid']]=='573638104', f_lines)))




'''
定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid


'''
def tweets_max_uid(*args):
	if args =='' :
		return 'null'
	else:
		args =list(args)
	#构建一个计数字典
	dict_args= dict.fromkeys(args,0)
	#进行计数
	for each in f_lines:
		u=int(each[key['uid']])
		if u in args:
			dict_args[u] += 1
	return sorted(dict_args.items(),key = lambda x: x[1], reverse =True)[0][0]
assert tweets_max_uid(28803555,72047320,573638104,612489475)==28803555


'''
统计该文本中发微博内容长度最长的用户的uid


'''

def get_len_max_uid():
	len_max =0
	len_max_uid =''
	for line in f_lines:
		length =len(line[key['content']])
		if length >= len_max:
			len_max =length
			len_max_uid = line[key['uid']]
	return len_max_uid
	
assert get_len_max_uid()=='111503549'


'''
该文本中转发URL最多次数的用户的uid

'''
#获取包含所有uid的列表
all_uid = [line[key['uid']] for line in f_lines]

#构建一个计数字典
dict_uid= dict.fromkeys(all_uid,0)

#进行计数
for each in f_lines:
	if each[key['rt_v_url']] != '':
		dict_uid[each[key['uid']]] += 1
		
#进行排序
uid_max_result = sorted(dict_uid.items(),key = lambda x: x[1], reverse =True)[0][0]

assert uid_max_result == '28803555'


'''
获取该文本中，在11点钟，谁发的微博次数最多


'''
#先过滤得到11点中的数据
list_hour_11 = list(filter(lambda x:x[key['time']][11:13] =='11',f_lines))	

#获取包含所有符合条件uid的列表
all_11_uid = [line[key['uid']] for line in list_hour_11]

#构建一个计数字典
dict_uid_11= dict.fromkeys(all_11_uid,0)

#进行计数
for each in list_hour_11:
		dict_uid_11[each[key['uid']]] += 1
		
#进行排序
uid_max_11_result = sorted(dict_uid_11.items(),key = lambda x: x[1], reverse =True)[0][0]
assert uid_max_11_result == '110736303'		

'''
获取该文本中哪个用户的远微博URL次数最多

'''

#构建一个计数字典
dict_uid2= dict.fromkeys(all_uid,0)

#进行计数
for each in f_lines:
	if each[key['v_url']] != '':
		dict_uid2[each[key['uid']]] += 1
		
#进行排序
v_url_max = sorted(dict_uid2.items(),key = lambda x: x[1], reverse =True)[0][0]
assert v_url_max=='17814581'
	
	
'''
总结：
一、要熟练使用列表生成式
二、要熟练使用filter过滤器对原始数据进行过滤，常常对应着一些对数据进行限制的条件。
三、条例一定要清晰，先做什么，后作什么，事先用注释写好



'''
stoptime = time.time()
print('程序运行的时间是：%.2f s'%(stoptime -starttime))

