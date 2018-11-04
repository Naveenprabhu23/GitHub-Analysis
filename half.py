#Date:
#Authors: A.Suraj Kumar and Naveen N Prabhu
#Roll No: 181046037 and 181046017
#Data Retrival from GitHub on particular date


import requests
import random
import json
import csv
#from github import Github
#file_url = "http://data.gharchive.org/2018-09-17-18.json.gz"
count=0
user_data = []
for i in range(10):
	rand=random.randint(240000,250000)
	#print(rand)
	#username='suraj19'
	#token1='9d98deacd0b4b3b3efdfb254c6af5c931ec237c5'
	#token2='808fd391c6908d19ceca268a311f3cb53a92b4e0'
	#Naveen's token: '19d3613f87d6be4b31d6480ac9aa6692aa47cd47'
	#Naveen's new token: '8103f0da6d0cd4dda76ba3960fd635ad82a74e34'
	#Vivek's Token: '0d494f03e8aeab180598b9f6cfd6c53ee56b9190'
	#Suraj New Token: 'bcda4a9669f4c0bba564f7d8d90bdbe6be90ef3d'
	headers = {'Authorization': '9d98deacd0b4b3b3efdfb254c6af5c931ec237c5 %s'}
	file_url1="https://api.github.com/user/"+str(rand)+":id"
	response1 = requests.get(file_url1, headers=headers)
	jsonToPython = response1.json()	#coverting json response to a python string
	#r= request.get(file_ural, stream = True)
	user_data.append(jsonToPython)
	#print(user_data)
	#columns=["login","id","public_repos","repos_url","followers","location","created_at"]
	user_list=[]
	#user_list.append(columns)
	for url in user_data:
		#print(url['repos_url'])
		'''repos_data=[]
		repo_link = url['repos_url']
		#file_url2="repo_link"user_data
		response2 = requests.get(repo_link, headers=headers)
		jsonToDict = response2.json()	#coverting json response to a python string
		repos_data.append(jsonToDict)'''
		temp=[]
		temp.append(url["login"])
		temp.append(url["id"])
		temp.append(url["public_repos"])
		temp.append(url["repos_url"])
		temp.append(url["followers"])
		temp.append(url["location"])
		temp.append(url["created_at"])
		user_list.append(temp)
		with open("UserData.csv","a",newline="") as f:
			writer=csv.writer(f)
			writer.writerows(user_list)
			#print('User Data is Downloaded')
	count+=1
	print('Number of user Data downloaded: ',count)
