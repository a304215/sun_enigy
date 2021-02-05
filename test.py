from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.taipower.com.tw/d006/loadGraph/loadGraph/genshx_.html")
time.sleep(3)
soup = BeautifulSoup(driver.page_source, "html.parser")
result = soup.find_all('tr','group-item--a-name-wind-a-b-風力-wind-b-')
word = str(result[0])
print(word)
data_list = []
for i in result:
    word = str(i)
    split_list = word.split('<td class="">')
    title = split_list[1].split('</td>')[0]
    data1 = split_list[2].split('</td>')[0]
    data2 = split_list[3].split('</td>')[0]
    data3 = split_list[4].split('</td>')[0]
    data_list.append([title,data1,data2,data3])
result = soup.find_all('tr','group-item--a-name-solar-a-b-太陽能-solar-b-')
word = str(result[0])
print(word)
data_list.append(['太陽能'])
for i in result:
    word = str(i)
    split_list = word.split('<td class="">')
    title = split_list[1].split('</td>')[0]
    data1 = split_list[2].split('</td>')[0]
    data2 = split_list[3].split('</td>')[0]
    data3 = split_list[4].split('</td>')[0]
    data_list.append([title,data1,data2,data3])
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['機組名稱', '裝置容量', '淨發電量','淨發電量/裝置容量比%'])
    writer.writerow(['風力'])
    for i in data_list:
        writer.writerow(i)
driver.close()
print(len(data_list))
