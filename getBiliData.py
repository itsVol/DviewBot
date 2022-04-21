import json
from multiprocessing import shared_memory
import re
import urllib.request

#获取用户的uuid号(UserId)
def getUUID():
    s = input("---请粘贴Bilibili主页的网址：---\n")
    nums= re.findall(r'\d+',s)
    return nums[0]

#获取该用户的订阅数，关注数
def getUserBasicInfo(UserId):
    InforAPI = "https://api.bilibili.com/x/relation/stat?vmid="+UserId+"&jsonp=jsonp"
    InforJson=json.loads(urllib.request.urlopen(InforAPI).read())
    following=InforJson['data']['following']
    follower= InforJson['data']['follower']
    user={'UUID':UserId,'following':following,'follower':follower}
    return user

#获取全部视频的BV号  #todo
def getAllBvid(args):
    pass

#获取单个bvid
#BV1134y167cP   
def getBvid():
    bvidAPI = input("请粘贴Bilibili视频的网址（web端）\n ")
    bvidNum=re.findall(r"[^/]+(?!.*/)",bvidAPI)
    bvid=str(bvidNum[0]).split("?")[0]
    return bvid 

#获取单个视频的状态数
def getVideoInfo(bvid):
    statAPI="http://api.bilibili.com/x/web-interface/archive/stat?bvid="+bvid
    videoJson=json.loads(urllib.request.urlopen(statAPI).read())
    viewNum=videoJson['data']['view']
    danmakuNum=videoJson['data']['damaku']
    replyNum=videoJson['data']['reply']
    favoriteNum=videoJson['data']['favorite']
    coinNum=videoJson['data']['coin']
    shareNum=videoJson['data']['share']
    likeNum=videoJson['data']['like']
    videoInfo={"播放量：":viewNum ,"弹幕数:":+danmakuNum,"评论数：":replyNum,"收藏：":favoriteNum, "投币：":coinNum, "分享：":shareNum, "获赞：" :likeNum}
#
