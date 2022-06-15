#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 22:22:23 2022

@author: madhvansharma2003
"""

# Monthly Installments Growth 

annuity = float(input("Monthly Annuity: "))
annual_growth_rate = float(input("Annual growth (in percentage): "))
months = int(input("Months: "))
factor = 1+annual_growth_rate/(100*months)
value = summation = annuity
growth_list = [0]
print("\n")
for i in range(1,months+2):
    print(f"Month {i-1},",f"Value: ${round(value,2)},",
          "Growth:",f"{round(growth_list[i-1],2)}%,")
    value = summation * factor
    growth_list.append(value-annuity*i)
    summation = annuity + value
print(f"Total profit: ${round(value-annuity*i+annuity,2)}")
