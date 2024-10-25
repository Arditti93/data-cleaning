import matplotlib.pyplot as plt

years = [2018,2019,2020,2021,2022,2023]
python_postion = [7,4,4,3,4,3]
js_postion = [1,1,1,1,1,1]
sql_position = [4,3,3,4,3,4]
typescript_position = [12,10,9,7,5,5]

# x axis first then the y axis
plt.plot(years, python_postion, label = "Python") 
plt.plot(years, js_postion, label = "JavaScript", linestyle = "dashed")
plt.plot(years,sql_position, label = "SQL", linestyle = "dotted")
plt.plot(years,typescript_position, label = "TypeScript", linestyle ="dashdot")
# Gives our grpah a title
plt.title("Most-Wanted language Ranking")
# lable axsis
plt.xlabel("Year")
plt.ylabel("Postion")
# set the limts of the axsis
plt.ylim(bottom = 20, top = 0)

# plt.legend([
#     "Python",
#     "JavaScript",
#     "SQL",
#     "TypeScript"
# ])
plt.legend()

plt.show()