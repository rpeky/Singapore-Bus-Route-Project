import JsonProcessingFunctions
import os

#mostly functions for checking stuff

#File Validation

#checks if folders exist, edit as more files are needed
    #_subject_          _index_                                                             _file name template_                            _folder name_               _additional comments_
        #error              - 0 unexpected error // for matching api index with load index      errorindex                                      errorindex  
    
        ## API data

        #arrivals           - 1 API 2.1 Bus Arrival Request                                     _BusArrivalRequest_BusStop_data.json            BusArrivalRequest_data      
        #services           - 2 API 2.2 Bus Services Request                                    _BusServicesRequest_data.json                   BusServicesRequest_data
        #routes             - 3 API 2.3 Bus Routes Request                                      _BusRoutesRequest_data.json                     BusRoutesRequest_data
        #stops              - 4 API 2.4 Bus Stops Request                                       _BusStopsRequest_bus_stop_info.json             BusStopsRequest_data
    
        ## Processed / self made data
        #composite          - 5 Bus Stop Data generated from processing API data                _busstop_data.json                              ProcessedBusStopData
        #mapdata            - 6 Working Map Data Traveller will use                             workingmapdata.json                             WorkingMapData              Identifier will take in None            
        #indvbusroute       - 7 Individual route each bus takes                                 _busserviceroute.json                           ProcessedServiceRouteData   
    #error index removed for file creation
def check_osfolder():
    listoffoldersshouldexist = ['BusArrivalRequest_data', 'BusServicesRequest_data', \
                                'BusRoutesRequest_data', 'BusStopsRequest_data', 'ProcessedBusStopData', \
                                'WorkingMapData','ProcessedServiceRouteData']
    
    for i in listoffoldersshouldexist:
        if(os.path.isdir(i)):
            pass
        else:
            os.mkdir(i)

#------------------------------------------------------------------------------------------------------------------
# File index 1: BusArrivalRequest_data
# 5083 files
def check_ifBusArrivalRequest_data_individual_exist(busstop):
    filename = str(busstop)+'_BusArrivalRequest_BusStop_data.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusArrivalRequest_data')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)
#Use This
def check_ifBusArrivalRequest_allbusarrivalrequestdata_exist():
    busstopslist=JsonProcessingFunctions.return_everyBusStop_busroutesrequest()
    count=0
    for busstop in busstopslist:
        print(busstop, check_ifBusArrivalRequest_data_individual_exist(busstop))
        count+=1
    print(count)
    return

#------------------------------------------------------------------------------------------------------------------
# File index 2: BusServicesRequest_data
# 2 files
def check_ifBusServicesRequest_data_individual_exist(idx):
    filename = str(idx)+'_BusServicesRequest_data.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusServicesRequest_data')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)
#Use This
def check_ifBusServicesRequest_allbusservicesrequestdata_exist():
    for i in range(2):
        print(i, check_ifBusServicesRequest_data_individual_exist(i))
    return

#------------------------------------------------------------------------------------------------------------------
# File index 3: BusRoutesRequest_data
# 51 files
def check_ifBusRoutesRequest_data_individual_exist(idx):
    filename = str(idx)+'_BusRoutesRequest_data.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusRoutesRequest_data')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)
#Use This
def check_ifBusRoutesRequest_allbusroutesrequestdata_exist():
    for i in range(51):
        print(i, check_ifBusRoutesRequest_data_individual_exist(i))
    return

#------------------------------------------------------------------------------------------------------------------
# File index 4: BusStopsRequest_data
# 11 files
def check_ifBusStopsRequest_data_individual_exist(idx):
    filename = str(idx)+'_BusStopsRequest_bus_stop_info.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusStopsRequest_data')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)
#Use This
def check_ifBusStopsRequest_allbusstopsrequestdata_exist():
    for i in range(11):
        print(i, check_ifBusStopsRequest_data_individual_exist(i))
    return

#------------------------------------------------------------------------------------------------------------------
# File index 5: WorkingMapData

#------------------------------------------------------------------------------------------------------------------
# File index 6: ProcessedBusStopData
# 5083 files
def check_ifProcessedBusStopData_individual_exist(busstopno):
    filename = str(busstopno)+'_busstop_data.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'ProcessedBusStopData')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)
#Use This
def check_ProcessedBusStopData_allprocessedbusstopdata_exist():
    busstoplist=JsonProcessingFunctions.return_everyBusStop_busstopsrequest()
    count=0
    for busstop in busstoplist:
        print(busstop, check_ifProcessedBusStopData_individual_exist(busstop))
        count+=1
    print(count)
    return

#------------------------------------------------------------------------------------------------------------------
# File index 7: ProcessedServiceRouteData
# 535 files
def check_ifProcessedServiceRouteData_individual_exist(busserviceno):
    filename = str(busserviceno)+'_busserviceroute.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'ProcessedServiceRouteData')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)
#Use This
def check_ProcessedServiceRouteData_allprocessedserviceroutedata_exist():
    busno=JsonProcessingFunctions.return_everybusserviceno_givesalist()
    count=0
    for bus in busno:
        print(bus, check_ifProcessedServiceRouteData_individual_exist(bus))
        count+=1
    print(count)
    return

