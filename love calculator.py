name1 = str(input())
name2 = str(input())
combined_names = name1+name2
lower_name = combined_names.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_name = t+r+u+e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_name = l+o+v+e

score = int(str(first_name)+str(second_name))
if score < 10 or score > 90:
    print(f"your score is {score}, you go for coke and mentos")
elif score >= 40 or score <= 50:
    print(f"your score is {score}, you should live together")
else:
    print(f"score is {score}")


