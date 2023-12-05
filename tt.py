import os 
os.system('cls')
import streamlit as st
import turtle
import numpy as np
import random
import pandas as pd
import sys
import matplotlib.pyplot as plt


# 1번
# n1 = np.zeros((4,5))
# n1
# for i in range (4):
#     for j in range(5):
#         n1[i,j] = 10
# n1

# 2번
# n2 = []
# n2.append(10)
# n2
# n2 = np.append(n2,15)
# n2

# 3번
# n = 5
# arr = np.full((n,n),'')
# arr

#4번
# for i in range(n):
#     for j in range(n):
#         arr[i,j] = '나머지'
#         if i == j:
#             arr[i,j] = "대"
#         if i + j == n - 1:
#             arr[i,j] = "대"


# arr

#5번
# n = 100
# for i in range(1,n+1):
#     if i %7 == 3:
#         i
col1, col2 = st.columns([1, 2])
with col1:
    st.image('토끼.jpg')
with col2:
    st.write('놓치면 후회할 인재(신수인👍, 시급 5만원, 대박 쩔어~~)')
    '전화번호(☎) : 010-8773-4080'
    '이메일(📧) : strustar@konuang.ac.kr'
    '주소(🏠) : 충남 논산시 대학로121'
col = st.columns(4)
with col[0]:
    st.link_button("구글🌐", "https://www.google.co.kr/?hl=ko")
with col[1]:
    st.link_button("네이버🇳", "https://www.naver.com/")
with col[2]:
    st.link_button("다음", "https://www.daum.net/")
with col[3]:
    st.link_button("링크인", "https://kr.linkedin.com/")

fig, ax = plt.subplots()

a = 2
b = -5
c = 3
d = -7

x = []
y = []

for i in range(-100, 101, 50):
    x.append(i)
    y.append(a*i**3 + b*i**2 + c*i + d)
col1, col2, col3 = st.columns(3)
with col1:
    color = st.radio('색을 선택하시오.', ('red','green','blue'))
with col2:
    linestyle = st.radio('선의 스타일을 선택하시오.', ('-','-.',':'))
with col3:
    marker = st.radio('마카의 스타일을 선택하시오.', ('s','^','o'))
# # if 'red' in color:
# #     t = '-.r^'
# # if 'green' in color:
# #     t = '-.g^'
# # if 'blue' in color:
# #     t = '-.b^'


plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)

st.pyplot(fig)

st.write('Hello, *World!* 😎')

print('Hello, *World!* :sunglasses:')
# *하나는 기울림
# **진하게
# ***기울림 진하게
sys.exit() # 밑에꺼 안 읽는거임






list1 = list([['한빛', '남자', '20', '180'],
    ['한결', '남자', '21', '177'],
    ['김한결', '중성', '51', '155'],
    ['한라', '여자', '20', '160']])

    
n = np.array(list1)
col_names = ['이름', '성별', '나이', '키']
df = pd.DataFrame(list1, columns = col_names, index=['1행', '2행', '3행', '4행'])
df

genre = st.radio("선택히시오.",
    ["오름차순", "내림차순", "기타"],
    horizontal=True, index=2)

number = st.number_input('Insert a number',value= 20,step=1)
df.iloc[3,2] = number


if '오름' in genre:
    st.dataframe(df.sort_value(by=['키']))
if '내림' in genre:
     st.dataframe(df.sort_value(by=['키'], ascending = False))
if '기타' in genre:
    st.dataframe(df)


# list1 = list([['한빛','남자','20','180']],
#               []



# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li)
# li
# n
# p









# li = [1, 2, 3, 4]
# li


# for i in range(4):
#     li[i] = li[i] + 3

# li

# li = np.array([7, 2, 6, 4])
# li

# li_sort = np.sort(li)[::-1]
# li_sort




#cls 는 클리어 스크린

# a = np.arange(8)
# a
# a.shape = (4,2)
# a
# b = a.flatten()
# b
# b.resize((2,4))
# b
# c = np.resize(b, (2,4))
# c


# a = np.array([1,10,-5,2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(np.square(a))





# t = turtle.Turtle()
# t.shape('turtle')
# t.width(3)
# # t.color('red')
# t.color((random.random(),random.random(),random.random()))

# n = 6
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)



# turtle.done()

# for i in range(6):
#     r = random.randint(1, 45)

#     r 

# list1 = [[1, 2, 3, 4], [3,5,7,9]]
# a = np.array(list1)
# a

# a.ndim
# n = np.ndim(a)
# np.size(a)
# a.size
# a.shape
# a.T






# def sta(arr):
#     s = 0  # 초기값
#     mx = -1e10
#     mn = 1e10
#     for i in arr:    
#         s = s + i
#         if mx < i:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     'sum = ', s, 'min = ', mn, 'max = ', mx
#     return s, mx, mn

# # list_1 = [1, 2, 7, 4, 50, 33]
# # s = sum(list_1)
# # mx = max(list_1)
# # mn = min(list_1)
# # s, mx, mn

# list_1 = [5, 13, 7, 4, 11]
# [s1, mx1, mn1] = sta(list_1)
# s1, mx1, mn1

# s = sum(list_1)
# mx = max(list_1)
# mn = min(list_1)

# s, mn, mx




# sum


# s = 0
# for i in range(2, 10+1, 2):
#     s = s + i
    
# s


# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)


# turtle.done()



# dict = {'name':'신수인',
#         'weight':69,
#         'height':172,
#         'address':'충남 논산시 대학로 121'
#         }
# dict

# for key in dict.keys():
#     key

# for v in dict.values():
#     v

# '================================================'
# for k, v in dict.items():
#     k
#     v

# ty = type(dict)
# ty


# list_1 = [1, 2, 3, 4, 5, 1, 3]
# list_1[1]
# for a in range(2,10):
#     ''
#     '============================================='
#     str(a), '단 입니다'    
#     for i in range(1,10,1):
#         b = str(a) + ' X ' + str(i) + ' = ' + str(a*i)
#         b
    



# grade = 52

# if grade >= 90:    
#     'A'
# elif grade >= 80:
#     'B'
# elif grade >= 70:
#     'C'
# elif grade >= 60:
#     'D'
# else:
#     'F'