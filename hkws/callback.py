from ctypes import *

filePath = 'D:/project/bblock/db/'

hikFunc = CFUNCTYPE(
    None,
    c_long,  # lRealHandle 当前的预览句柄，NET_DVR_RealPlay_V40的返回值
    c_ulong,  # dwDataType  数据类型 1-系统头数据， 2-流数据（包括符合流或者音视频分开的流数据），3-音频数据，112-私有数据，包括智能信息
    c_byte,  # *pBuffer 存放数据的缓冲区指针
    c_ulong,  # dwBufSize 缓冲区大小
    c_ulong,  # *pUser 用户数据
)


@CFUNCTYPE(None, c_long, c_ulong, c_byte, c_ulong, c_ulong)
def g_real_data_call_back(lRealPlayHandle: c_long,
                          dwDataType: c_ulong,
                          pBuffer: c_byte,
                          dwBufSize: c_ulong,
                          dwUser: c_ulong):
    print(' aaaaaaaaaaa callback pBufSize is ', lRealPlayHandle, dwBufSize)
    # if dwBufSize > 0:
    #     f = open(filePath, 'wb')
    #     f.write(pBuffer)
