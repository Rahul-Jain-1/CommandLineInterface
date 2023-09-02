
import csv
import click
import random
import pandas as pd

@click.group()
def cli():
    pass

used_numbers = set()

@cli.command()
@click.option("--create","--c", prompt="Create the new task", help="Create the new task")
def add(create):  #Adding the task
   global used_numbers

   with open("todo.csv",'a', newline='') as file:
       csvwriter = csv.writer(file)
       values = create.split(',')
       random_number = generate_unique_random_number()
       values.insert(0, str(random_number))
       csvwriter.writerow(values)
   print(f"Task Added Successfully where Assigned id is {random_number} and data is { create}")
def generate_unique_random_number():
    global used_numbers
    random_number = random.randint(1, 100)
    while random_number in used_numbers:
        random_number = random.randint(1, 100)
    used_numbers.add(random_number)
    return random_number
#
@cli.command()
def show():
    df = pd.read_csv("todo.csv")
    print(df)

@cli.command()
@click.option("--taskid", prompt="Enter the task id to remove", help="Enter the task id to remove")
def complete(taskid):
     taskIdConv = int(taskid)
     df = pd.read_csv("todo.csv")
     ##print(df) Actual Dataframe
     df = df.drop(df[df.TaskId == taskIdConv].index,inplace=False)
     df.to_csv("todo.csv", index=False)
     print(f"Task with ID {taskid} removed successfully")
     print("After removal:")
     print(df) #Updated DataFrame

@cli.command()
@click.option("--taskid", type=int)
# @click.option("--title", prompt="Enter the new title", help="New task title")
# @click.option("--description", prompt="Enter the new description", help="New task description")
# @click.option("--due_date", prompt="Enter the new due date", help="New task due date")
def edit(taskid):
    try:
        # Read the CSV file using Pandas
        taskIdConv = int(taskid)
        df = pd.read_csv("todo.csv")
        print("Actual data is ")
        print(df.loc[df['TaskId'] == taskIdConv])
        print("\n")

        ti = input("Do you want to update title (y/n)\t")
        if(ti == 'y'):
            title = input("Enter the new title\t")
            df.loc[df['TaskId'] == taskIdConv, 'Tittle'] = title
        # Find the row with the specified task_id and update the values
        desc = input("Do you want to update description (y/n)\t")
        if (desc == 'y'):
            description = input("Enter the new description\t")
            df.loc[df['TaskId'] == taskIdConv, 'Description'] = description
        dat = input("Do you want to update due_date (y/n)\t")
        if (dat == 'y'):
            due_date = input("Enter the new due_date\t")
            df.loc[df['TaskId'] == taskIdConv, 'DueDate'] = due_date

        # # Write the modified DataFrame back to the CSV file
        df.to_csv("todo.csv", index=False)
        #
        print(f"Task with ID {taskIdConv} edited successfully")
        print("After editing:")
        print(df)

    except pd.errors.EmptyDataError:
        print("CSV file is empty.")


if __name__ == "__main__":
    try:
        file_name = "todo.csv"
        with open(file_name,'r') as file:
            pass
            #print(f'The {file_name} exist')

    except FileNotFoundError:
        # if file does not found, then need to create one
        # and in that the counter variable and a dictioanry needs to be created
        print(f'The {file_name} does not exist, creating a one')

        with open(file_name,'w') as file:
            headers = ['TaskId','Tittle','Description','DueDate']
            std=csv.writer(file)
            std.writerow(headers)
            print(f'The {file_name} has been created and ready to do work')

    cli()
