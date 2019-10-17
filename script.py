train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
#write function to convert F to C
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#write function to convert C to F
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#write function to return mass x acceleration
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " +  str(train_force) + " Newtons of force.")

#write function to calculate energy
def get_energy(mass, c=3*10**8):
  return mass * c**2
bomb_energy = get_energy(bomb_mass, c=3*10**8)
print("A 1kg bomb supplies " + str(bomb_energy) +  " Joules.")

#write function to calculate work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over Y meters.")

  


