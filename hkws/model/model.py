from ctypes import *


# 报警设备信息结构体
class NET_DVR_ALARMER(Structure):
    _fields_ = [
        ("byUserIDValid", c_byte),
        ("bySerialValid", c_byte),
        ("byVersionValid", c_byte),
        ("byDeviceNameValid", c_byte),
        ("byMacAddrValid", c_byte),
        ("byLinkPortValid", c_byte),
        ("byDeviceIPValid", c_byte),
        ("bySocketIPValid", c_byte),
        ("lUserID", c_long),
        ("sSerialNumber", c_byte * 48),
        ("dwDeviceVersion", c_uint32),
        ("sDeviceName", c_char * 32),
        ("byMacAddr", c_char * 6),
        ("wLinkPort", c_uint16),
        ("sDeviceIP", c_char * 128),
        ("sSocketIP", c_char * 128),
        ("byIpProtocol", c_byte),
        ("byRes2", c_byte * 11)
    ]


# 布防
class NET_DVR_SETUPALARM_PARAM(Structure):
    _fields_ = [
        ("dwSize", c_uint32),
        ("beLevel", c_byte),
        ("byAlarmInfoType", c_byte),
        ("byRetAlarmTypeV40", c_byte),
        ("byRetDevInfoVersion", c_byte),
        ("byRetVQDAlarmType", c_byte),
        ("byFaceAlarmDetection", c_byte),
        ("bySupport", c_byte),
        ("byBrokenNetHttp", c_byte),
        ("wTaskNo", c_uint16),
        ("byDeployType", c_byte),
        ("byRes1", c_byte * 3),
        ("byAlarmTypeURL", c_byte),
        ("byCustomCtrl", c_byte)
    ]


# 区域框参数结构体。
class NET_VCA_RECT(Structure):
    _fields_ = [
        ("fX", c_float),
        ("fY", c_float),
        ("fWidth", c_float),
        ("fHeight", c_float)
    ]


# 报警目标信息结构体。
class NET_VCA_TARGET_INFO(Structure):
    _fields_ = [
        ("dwID", c_uint32),
        ("struRect", NET_VCA_RECT),
        ("byRes", c_byte * 4)
    ]


# IP地址结构体。
class NET_DVR_IPADDR(Structure):
    _fields_ = [
        ("sIpV4", c_char * 16),
        ("sIpV6", c_byte * 128)
    ]


# 前端设备信息结构体。
class NET_VCA_DEV_INFO(Structure):
    _fields_ = [
        ("struDevIP", NET_DVR_IPADDR),
        ("wPort", c_uint16),
        ("byChannel", c_byte),
        ("byIvmsChannel", c_byte)
    ]


# 人体属性参数结构体。
class NET_VCA_HUMAN_FEATURE(Structure):
    _fields_ = [
        ("byAgeGroup", c_byte),
        ("bySex", c_byte),
        ("byEyeGlass", c_byte),
        ("byAge", c_byte),
        ("byAgeDeviation", c_byte),
        ("byRes", c_byte * 11)
    ]


# 人脸抓拍结果结构体。
class NET_VCA_FACESNAP_RESULT(Structure):
    _fields_ = [
        ("dwSize", c_uint32),
        ("dwRelativeTime", c_uint32),
        ("dwAbsTime", c_uint32),
        ("dwFacePicID", c_uint32),
        ("dwFaceScore", c_uint32),
        ("struTargetInfo", NET_VCA_TARGET_INFO),
        ("struRect", NET_VCA_RECT),
        ("struDevInfo", NET_VCA_DEV_INFO),
        ("dwFacePicLen", c_uint32),
        ("dwBackgroundPicLen", c_uint32),
        ("bySmart", c_byte),
        ("byAlarmEndMark", c_byte),
        ("byRepeatTimes", c_byte),
        ("byUploadEventDataType", c_byte),
        ("struFeature", NET_VCA_HUMAN_FEATURE),
        ("fStayDuration", c_float),
        ("sStorageIP", c_char * 16),
        ("wStoragePort", c_uint16),
        ("wDevInfoIvmsChannelEx", c_uint16),
        ("byRes1", c_byte * 15),
        ("byBrokenNetHttp", c_byte),
        ("pBuffer1", c_void_p),
        ("pBuffer2", c_void_p)
    ]
