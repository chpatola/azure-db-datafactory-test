# Databricks notebook source
from datetime import date

# COMMAND ----------

def hiFriend(name):
    today =  date.today().strftime("%m/%d/%Y") 
    messageParts = ["Hi", name, "! Today it is",today]
    message =" ".join(messageParts)
    return message
    
