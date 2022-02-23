#!/usr/bin/env python3
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

uav = connect('127.0.0.1:14550', wait_ready = True) # uav bağlantısının olusturulması

#takeoff fonksiyonu
def takeoff(irtifa):
    
    while uav.is_armable is not True: #iha arm edilebilir durumda True değilse bilgi yazdırır
        print('IHA arm edilebilir durumda değil.')
        time.sleep(1)
        
    print('IHA arm edilebilir.') 
    uav.mode = VehicleMode('GUIDED') #iha guided moduna alinir
    uav.armed = True # iha arm edilir
    
    while uav.armed is not True: #iha hemen arm edilemediği icin ihanın arm edilmesi beklenir
        print('IHA arm ediliyor...')
        time.sleep(1)
    
    print('IHA arm edildi')
    uav.simple_takeoff(irtifa) #irtifa verilerek ihanın yükselmesi beklenir
    
    while uav.location.global_relative_frame.alt < irtifa * 0.9: # ihanın irtifası ve hedef irtifa 0.9 hata payı bırakılarak yükselmesi beklenir
        print('IHA hedefe yukseliyor')
        time.sleep(1)
        
    print('IHA hedefe yukseldi')
    
#simple_goto fonksiyonu    
def goto(lat,lon,alt):
    print('IHA belirlenen konuma gitmek icin hazirlaniyor.')
    time.sleep(2)
    konum = LocationGlobalRelative(lat, lon, alt) #hedef konum bilgisi alınır.
    uav.simple_goto(konum)
    #while ile hedef konuma ulaşıp ulaşılamadığı kontrol edilir.
    while konum.lat != uav.location.global_relative_frame.lat and konum.lon != uav.location.global_relative_frame.lon and konum.alt != uav.location.global_relative_frame.alt:
        print('IHA hedefe dogru gidiyor.')
        time.sleep(1)
    print("IHA hedef ulasti")
    
    
def land():
    
    uav.mode = VehicleMode('LAND')
    
#MAIN
takeoff(3)
time.sleep(2)
goto(-35.36277797, 149.16513873, 3)
time.sleep(2)  
land()




