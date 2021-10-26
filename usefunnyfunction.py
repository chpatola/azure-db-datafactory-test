# Databricks notebook source
# MAGIC %run ./funnyfunction

# COMMAND ----------

annasGreeting = hiFriend("Anna")

# COMMAND ----------

print(annasGreeting)

# COMMAND ----------

# Creating widgets for leveraging parameters, and printing the parameters

dbutils.widgets.text("input", "","")
y = dbutils.widgets.get("input")
print ("Param -\'input':")
print (y)
