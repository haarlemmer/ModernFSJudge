import SimConnect
import subjects

print("ModernFSJudge - 厕所模拟飞行大赛")
print("--------------------")
print("Notice")
print('''Microsoft Flight Simulator © Microsoft Corporation. 
ModernFSJudge was created under Microsoft's "Game Content Usage Rules" using assets from Microsoft Flight Simulator, 
and it is not endorsed by or affiliated with Microsoft.''')
print("--------------------")

print("Connecting to Microsoft Flight Simulator...")
try:
    sc = SimConnect.SimConnect()
    print("Microsoft Flight Simulator Connected.")
    input("Press Enter to start.")
    subjects.begin(sc)
    subjects.subjectOne(sc)
    subjects.subjectTwo(sc)

except ConnectionError:
    print("Error: Unable to connect to Microsoft Flight Simulator.")