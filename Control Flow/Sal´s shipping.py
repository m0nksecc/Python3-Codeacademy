weight = 1

#Ground shipping
if weight <= 2:
  print("Ground shipping is: " + str(1.50 * weight + 20))
elif weight <= 6:
  print("Ground shipping is: " + str((3.00 * weight + 20)))
elif weight <= 10:
  print("Ground shipping is: " + str(4.00 * weight + 20))
elif weight > 10:
  print("Ground shipping is: " + str(4.75 * weight + 20))

#Cost of premium ground shipping
premium_ground = 125
print("Premium ground is: " + str(premium_ground))

#Drone shipping
if weight <= 2:
  print("Drone shipping: " + str(4.50 * weight))
elif weight <= 6:
  print("Drone shipping: " + str(9 * weight))
elif weight <= 10:
  print("Drone shipping: " + str(12 * weight))
elif weight > 10:
  print("Drone shipping: " + str(14.25 * weight))
