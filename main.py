import matplotlib.pyplot as plot

# set up your lists

numlist = [8, 6, 5, 3]

namelist = ['Freshman', 'Sophomores', 'Juniors', 'Seniors']

colorlist = ['blue', 'green', 'purple', 'gold' ]

explodelist = [0.5, 0.5, 0.5, 0.5]

# make the pie chart

plot.pie(numlist, labels=namelist, autopct='%2f%%', colors=colorlist,
    	explode = explodelist, startangle = 360)

plot.axis('equal')

plot.savefig('Pie Chart.png')

