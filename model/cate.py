from model import mongoDB

##分類建立
#分類塞選用c1,建立名稱用c2
catedata={"girl":"女性情趣", 
"boy":"男性情趣",
"compagin":"活動專區",
"manga":"漫畫專區",
"clothing":"性感睡衣",
"BDSM":"SM商品專區",
"lubi":"潤滑專區",
"condom":"保險套區",
"doll":"真人娃娃區",
"others":"保健與催情",
}

##分類BAR命名
catedata2={"girl":"女性情趣",
"boy":"男性情趣",
"compagin":"活動專區",
"manga":"漫畫專區",
"clothing":"性感睡衣",
"BDSM":"BDSM專區",##
"lubi":"潤滑液專區",##
"condom":"保險套專區",##
"doll":"真人娃娃",
"others":"保健與催情",
}

    ##篩選區
def categoryfilter(categroy):
    allprod=mongoDB.Itemsdata.allprod #從monogodb抓資料庫
    temp=[]
    
    for i in allprod: ## 目前有些NONE型態的會錯誤，之後要修正 20211222
        try:
            if catedata[categroy] in i["total_cate"]:
                temp.append(i)
        except:
            next
    allprod=temp

    return allprod
    ##