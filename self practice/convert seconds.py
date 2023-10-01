seconds=int(input("enter the seconds:"))

hours=seconds//3600
seconds=seconds%3600

minutes=seconds//60
seconds=seconds%60

second=seconds//1
seconds=seconds%1

print(f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')