min_salary = 2700

salary = int(input("Введи число - заплату после вычета налогов: "))
salary = round(salary / 92)

if salary >= min_salary:
    print(f"Salary is OK. Total: {salary}$")
else:
    print(f"They're greedy. No, thanks. Total: {salary} and my minimum is 2700$")


imployee = str(input("That's the name of the company?: "))
ban_companies = ["Yandex", "SberDevices", "PSB Bank", "Rutube", "VK", "T-Bank", "BetBoom",]

if imployee in list(ban_companies):
    print("Company in the banlist")
else:
    print("Company OK")

vacancy = input("Какая должность?: ")
python_value = input("Есть ли у них задачи на Pyhton? Введите булево значение (True/False): ")

if python_value == "True":
    print(f"Это компания {imployee}, роль {vacancy} и там платят {salary}$"
          f" У них есть автоматизация на Python")
else:
    print(f"Это компания {imployee}, роль {vacancy} и там платят {salary}$"
          f" У них нет автоматизации на Python")