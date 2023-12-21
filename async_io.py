import requests
import asyncio
import time 

async def fun1() :
    print("1st Function is : ")
    url1 = "https://img.freepik.com/free-photo/beautiful-shot-snowy-rocky-steep-mountains-hills_181624-2719.jpg?w=740&t=st=1703162973~exp=1703163573~hmac=f488871a315839b92b930465dad1027709a247eda8ba9f72a27fb0225c6bfde3"
    dwn1 = requests.get(url1)
    open("Pic_1.jpg","wb").write(dwn1.content)

async def fun2() :
    print("2nd Function is : ")
    url2 = "https://img.freepik.com/free-photo/beautiful-scenery-summit-mount-everest-covered-with-snow-white-clouds_181624-21317.jpg?w=740&t=st=1703162790~exp=1703163390~hmac=ab38e413e0a1fafb5eb6b00eb1d0df5ea558528e9ad36661daca7537dac690fd"
    dwn2 = requests.get(url2)
    open("Pic_2.jpg","wb").write(dwn2.content)

async def main() :
    l = await asyncio.gather(fun1(),fun2())
    print(l)

asyncio.run(main())