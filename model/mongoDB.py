import pymongo
#client=pymongo.MongoClient("mongodb+srv://root:*******@cluster0.lqybc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

#抓MONGO資料
def allpords():
    client=pymongo.MongoClient("mongodb+srv://root:********@cluster0.lqybc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.productDB
    collection=db.totaldata6
    data=collection.find({},sort=[("total_pid_score",pymongo.DESCENDING)])#原本PID，改成total_Pid

    allprod=[]
    for doc in data:
        if doc["drq_stock"] == 1 or doc["dp_stock"] ==1 or doc["ii_stock"] == 1 :
            allprod.append(doc)
    return allprod

#吐產品參數
class Itemsdata:
    allprod=allpords()
    
    def __init__(self,pagenum,pagebar,maxpagenum):
        self.pagenum = pagenum
        self.pagebar = pagebar
        self.maxpagenum = maxpagenum
        
    @property    
    def juarje(self):
        if self.pagenum < (len(self.allprod)/30)+1:
            return 1
        else:
            return 0

### bar製作 + 商品欄位製作
def Items_variance(pagenum,allprod):

    pagenum=pagenum
    allprod=allprod

    if pagenum < (len(allprod)/30)+1:
        #商品欄位製作
        x=(pagenum-1)*30
        y=(pagenum*30)
        aallprod=allprod[x:y]

        #列表欄位製作
        curpage=pagenum
        maxpagenum=int(len(allprod)/30)

        pagebar_list=list(range(1,maxpagenum+2))

        curpage

        if curpage < 6:
            pagebar=pagebar_list[0:6]

        elif 5 < curpage < maxpagenum - 2:
            pagebar=pagebar_list[curpage-2:curpage+3]

        else:
            pagebar=pagebar_list[maxpagenum-4:]

        return aallprod,pagebar,maxpagenum
        #return render_template("index.html",aallprod=aallprod,pagenum=pagenum,pagebar=pagebar,maxpagenum=maxpagenum)

    else: #超過頁數給錯誤頁，或者導回首頁
        #aallprod=allprod[0:30]
        return None
        #return redirect(url_for('show_records',pagenum=1))

###

##search
def searchfilter(allprod,name):
    temp=[]
    for i in allprod:
        tempa=[]

        tempa.append(str(i["dp_name"]))
        tempa.append(str(i["drq_name"]))
        tempa.append(str(i["ii_name"]))


        tempb=[]
        for ii in tempa:
            if name in ii:
                tempb.append(i["total_id"])


        tempb=list(set(tempb))

        for iii in allprod:
            for iiii in tempb:
                if iii["total_id"]==iiii:
                    temp.append(iii)
    return temp