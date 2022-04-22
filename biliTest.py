from getBiliData import *

if __name__ == '__main__':
    userId=str(getUUID())
    #BasicInfo=getUserBasicInfo(userId)
    #print("{}{}\n {}{}\n {}{}\n"
    #.format("用户id： ",BasicInfo['UUID'],"已关注: ",BasicInfo['following'],"被关注",BasicInfo['follower']))
    A=getAllBvid(userId)
    print(A)