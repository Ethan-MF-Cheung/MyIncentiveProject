import pandas as pd
import matplotlib.pyplot as plt

def myinc(file1, file2):
        # This block of code reads the excel files for the data and the point system
        data=pd.read_excel(file1)
        ind=pd.read_excel(file2)
        ipoint = [x for x in ind['1 point'].astype(str).tolist() if pd.notna(x) and x != 'nan']
        iipoint = [x for x in ind['2 points'].astype(str).tolist() if pd.notna(x) and x != 'nan']
        iiipoint = [x for x in ind['3 points'].astype(str).tolist() if pd.notna(x) and x != 'nan']
        # A summative row in the sales data is created for the results
        data.loc[len(data)] = [0]* len(data.columns)
        # Bar team members and Floor team mambers are defined by their index in the table
        bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
        floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
        # This loop converts the sales data into points for each team member above
        for x in range(0, len(data)-1):
            if data['Description'].values[x] in ipoint:
                data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
            elif data['Description'].values[x] in iipoint:
                data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
            elif data['Description'].values[x] in iiipoint:
                data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
        result=data.iloc[len(data)-1, 2:len(data.columns)-1]
        def add_points(series, index_name, points):
            if index_name in result.index:
                result[index_name] += points
            else:
                print(f"Index {index_name} not found in the Series.")
        # Additional points awarded for number of reveiws is manually added using an input
        while True:
            index_name = input("Enter the index to add points to (or 'stop' to end): ")
            if index_name.lower() == 'stop':
                break
            points = int(input("Enter the number of points to add: "))
            add_points(result, index_name, points)
        # Using matplotlib, a 2 bar codes are made: one for the bar results and one for the floor results
        bresult=result.index.isin(bar)
        barseries=result[bresult].sort_values(ascending=False)
        fresult=result.index.isin(floor)
        floorseries=result[fresult].sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        bars = plt.bar(barseries.index, barseries.values, color='blue')
        plt.bar(barseries.index, barseries.values, color='blue')
        plt.title('Bartender Incentive')
        plt.xlabel('Bartender')
        plt.ylabel('Score')
        plt.xticks(barseries.index)
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
 
        plt.figure(figsize=(10, 5))
        bars = plt.bar(floorseries.index, floorseries.values, color='green')
        plt.bar(floorseries.index, floorseries.values, color='green')
        plt.title('Floortender Incentive')
        plt.xlabel('Floortender')
        plt.ylabel('Score')
        plt.xticks(floorseries.index)
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
        plt.tight_layout()
        plt.show()

