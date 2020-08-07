# coding=utf-8
while True:
    print("*" * 10 + "欢迎使用货币转换服务系统" + "*" * 10)
    service_menu = {"1": "人民币转换美元", "2": "美元转换人民币", "3": "人民币转换欧元", "0": "结束程序"}
    for key, values in service_menu.items():
        print('{}.{}'.format(key, values))

    Your_Choice = input("请您选择需要的服务：")
    # 人民币转换美元服务
    if int(Your_Choice) == 1:
        print("~" * 36 + "\n欢迎使用人民币转换美元服务")
        your_money = int(input("请输入您需要转换的人民币金额:"))
        print("您需要转换的人民币为：{}元".format(your_money))
        RMB_to_US = your_money / 6.72
        print("兑换成美元为：{:,.2f}$".format(RMB_to_US))
        print("=" * 30)
    # 美元转换人民币服务
    elif int(Your_Choice) == 2:
        print("~" * 36 + "\n欢迎使用美元转换人民币服务")
        your_money = int(input("请输入您需要转换的美元金额:"))
        print("您需要转换的美元为：{}元".format(your_money))
        US_to_RMB = your_money * 6.72
        print("兑换成人民币为：{:,.2f}元".format(US_to_RMB))
        print("=" * 30)
    #  人民币转换欧元服务
    elif int(Your_Choice) == 3:
        print("~" * 36 + "\n欢迎使用人民币转换欧元服务")
        your_money = int(input("请输入您需要转换的人民币金额:"))
        print("您需要转换的人民币为：{}元".format(your_money))
        RMB_to_EUR = your_money * 0.13
        print("兑换成欧元为：{:,.2f}欧元".format(RMB_to_EUR))
        print("=" * 30)
    #   退出服务
    elif int(Your_Choice) == 0:
        print("感谢您的使用，祝您生活愉快，再见！")
        break
    else:
        print("选择信息有误，请重新输入")
        continue
