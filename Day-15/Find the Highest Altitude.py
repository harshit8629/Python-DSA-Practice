gain = [-5,1,5,0,-7]
altitude = [0]
for i in range(len(gain)):
  altitude.append(altitude[-1]+gain[i])
print(max(altitude))