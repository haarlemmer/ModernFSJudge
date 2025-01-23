import SimConnect, time, math
from tinyWinToast import tinyWinToast

def begin(sc: SimConnect.SimConnect):
    ae = SimConnect.AircraftEvents(sc)
    ar = SimConnect.AircraftRequests(sc,_time=0)
    setPause = ae.find('PAUSE_SET')
    
    # Set aircraft position
    setPause(1) # Pause the game
    ar.set("PLANE_ALTITUDE",3000)
    ar.set("PLANE_LATITUDE",31.168611)
    ar.set("PLANE_LONGITUDE",121.826111)
    ar.set("PLANE_HEADING_DEGREES_TRUE",5.942033232)
    ar.set("AIRSPEED_TRUE",90)
    
    beginningCountdown()


def subjectOne(sc: SimConnect.SimConnect):
    print("---科目1开始---")
    ae = SimConnect.AircraftEvents(sc)
    ar = SimConnect.AircraftRequests(sc,_time=0)
    toggleEng1Failure = ae.find('TOGGLE_ENGINE1_FAILURE')
    setPause = ae.find('PAUSE_SET')


    t = tinyWinToast.getToast("科目1 - 三边飞行", "保持3000ft高度，357°航向", appId="ModernFSJudge", isMute=False)
    t.show()


    setPause(0)
    maxAltitude = 0
    minAltitude = 9999
    for x in range(1,201):
        altitude = ar.get("PLANE_ALTITUDE")
        if altitude > maxAltitude:
            maxAltitude = altitude
        if minAltitude > altitude:
            minAltitude = altitude
        print(f"Time:{x/10} 当前高度: {altitude}  最大高度: {maxAltitude}  最低高度: {minAltitude}")
        time.sleep(0.1)

    # 算分
    if minAltitude < 2990:
        minOut = math.floor((3000-minAltitude) / 5) * -0.2
    else:
        minOut = 0
    maxOut = math.floor((maxAltitude-3000) / 5) * -0.2
    score = 10 + maxOut + minOut

    # Toast提示
    t = tinyWinToast.getToast("科目1 - 三边飞行", f"三边高度: {score}", appId="ModernFSJudge", isMute=False)
    t.show()

    # Capturing flight information

def subjectTwo(sc: SimConnect.SimConnect):
    print("---科目2开始---")
    ae = SimConnect.AircraftEvents(sc)
    ar = SimConnect.AircraftRequests(sc,_time=0)
    toggleEng1Failure = ae.find('TOGGLE_ENGINE1_FAILURE')


    # 弹个Toast
    t = tinyWinToast.getToast("科目2 - 三转四边", f"转向第四边，坡度小于25° 在 2500ft - 200ft 高度区间内，应保持速度在 65节 - 75节", appId="ModernFSJudge", isMute=False)
    t.show()

    print("触发Aircraft Event: TOGGLE_ENGINE1_FAILURE")
    toggleEng1Failure()

    # 开始监测
    stop = False
    maxBankAngle = 0
    while not stop:
        bankAngle = ar.get("PLANE_BANK_DEGREES")
        if bankAngle > maxBankAngle:
            maxBankAngle = bankAngle
        altitude = ar.get("PLANE_ALTITUDE")
        airspeed = ar.get("AIRSPEED_TRUE")
        maxAirspeed = 0
        minAirspeed = 1000
        if altitude >= 200 and altitude <= 2500:
            if airspeed > maxAirspeed:
                maxAirspeed = airspeed
            elif airspeed < minAirspeed:
                minAirspeed = airspeed
        print(f"Bank Angle: {bankAngle} Altitude: {altitude} Airspeed: {airspeed}")
        if ar.get("PLANE_LONGITUDE") <= 121.816111:
            stop = True
        time.sleep(0.1)

    # 算分
    if minAirspeed < 65:
        minOut = math.floor((65 - minAirspeed)) * -1
    else:
        minOut = 0
    if maxAirspeed > 75:
        maxOut = math.floor(maxAirspeed - 75) * -1
    else: 
        maxOut = 0
    
    airspeedScore = 10 + maxOut + minOut
    if airspeedScore < 0:
        airspeedScore = 0

    if maxBankAngle > 25:
        bankAngleScore = 10 - math.floor((bankAngle - 25) / 5) * -0.2
        if bankAngleScore < 0:
            bankAngleScore = 0
    else:
        bankAngleScore = 10
    
    t = tinyWinToast.getToast("科目2 - 三转四边", f"返场速度: {airspeedScore} 转弯坡度: {bankAngleScore}", appId="ModernFSJudge", isMute=False)

    t.show()

    

    
        


def beginningCountdown():
    t = tinyWinToast.Toast()
    t.setAppID("ModernFSJudge")
    t.setTitle("厕所模拟飞行大赛")
    t.setMessage("准备阶段")
#    t.setDuration()

    t.show()
    time.sleep(10)


def apporach(sc: SimConnect.SimConnect):
    pass
