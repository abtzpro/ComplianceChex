# please note the DashboardReports.py file was
# built seperately from the rest of the system
# and will have to be tied into the automation system
# by means of slight modifications

# please note the email report function will need to be
# modified before testing and stands as a placeholder

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import schedule
import time
import smtplib

# function to generate a report
def generate_report():
    # load data from the database
    df = pd.read_csv("data.csv")

    # create a summary report
    summary = df.groupby("Category").agg({"Value": ["sum", "mean"]})

    # create a chart
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.barplot(x="Category", y="Value", data=df)
    plt.title("Information Security Program Effectiveness")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.savefig("chart.png")

    # create a report
    today = datetime.date.today().strftime("%Y-%m-%d")
    report = f"""
    Information Security Program Effectiveness Report ({today})

    Summary:
    {summary}

    Chart:
    """
    # attach the chart to the report
    with open("chart.png", "rb") as f:
        chart_data = f.read()
    report += chart_data

    # send the report via email
    sender_email = "sender@example.com"
    sender_password = "password"
    receiver_email = "receiver@example.com"
    message = f"""\
    Subject: Information Security Program Effectiveness Report ({today})

    {report}
    """
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

# function to schedule report generation
def schedule_report():
    # generate a report every day at 8am
    schedule.every().day.at("08:00").do(generate_report)

    while True:
        schedule.run_pending()
        time.sleep(1)

# call the function to schedule report generation
schedule_report()
