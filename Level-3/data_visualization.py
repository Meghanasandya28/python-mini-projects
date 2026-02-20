import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv("sales_data.csv")
    return data

def plot_bar(data):
    plt.figure(figsize=(6,4))
    plt.bar(data["Month"], data["Sales"])
    plt.title("Monthly Sales - Bar Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

def plot_line(data):
    plt.figure(figsize=(6,4))
    plt.plot(data["Month"], data["Sales"], marker="o")
    plt.title("Monthly Sales - Line Chart")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

def main():
    data = load_data()

    while True:
        print("\n=== Data Visualization Tool ===")
        print("1. Show Bar Chart")
        print("2. Show Line Chart")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            plot_bar(data)
        elif choice == "2":
            plot_line(data)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()