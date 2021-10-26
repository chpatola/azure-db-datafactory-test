# Databricks notebook source
# MAGIC %run ./funnyfunction

# COMMAND ----------

annasGreeting = hiFriend("Anna")

# COMMAND ----------

print(annasGreeting)

# COMMAND ----------

# Creating widgets for leveraging parameters, and printing the parameters

dbutils.widgets.text("name", "","")
y = dbutils.widgets.get("name")
print ("Param -\'input':")
print (y)
