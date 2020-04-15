#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
#      低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
#      40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
#      超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
profits = int(input('请输入当月利润（单位：万元）：'))
pro_list = [100,60,40,20,10,0]
rate_list = [0.01,0.015,0.03,0.05,0.075,0.1]
awards_sum = 0

awards = 0
if profits <= 10:
    awards = profits*0.1
elif 10 < profits <=20:
    awards = 10*0.1 + (profits-10)*0.075
elif 20 < profits <=40:
    awards = 10*0.1+10*0.05+(profits-20)*0.05
elif 40 < profits <=60:
    awards = 10*0.1+10*0.05+20*0.05+(profits-40)*0.03
elif 60 < profits <=100:
    awards = 10*0.1+10*0.05+20*0.05+20*0.03+(profits-60)*0.015
else: 
    awards = 10*0.1+10*0.05+20*0.05+20*0.03+40*0.015+(profits-100)*0.01
print('应发放奖金总数%d万元'%awards)

#_____________________________________________________________________________________________

for dex in range (6):
    if profits > pro_list[dex]:
        awards_sum += (profits-pro_list[dex])*rate_list[dex]
        profits = pro_list[dex]
print('应发放奖金总数%d万元'%awards_sum)