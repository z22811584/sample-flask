from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect
from flask import send_from_directory


#data
#import ssl
#from flask.templating import render_template_string

#引入mongoDB資料庫
from model import mongoDB
allprods=mongoDB.allpords()

##分類建立
from model import cate

catedata= cate.catedata
catedata2=cate.catedata2

##flask
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/public"
)

@app.route("/")

def index():

    #aallprod=allprod[0:30] #包前不包後

    # return render_template("index.html",aallprod=aallprod)
    return redirect(url_for('show_records',pagenum=1))


@app.route("/show_records/<int:pagenum>")

def show_records(pagenum):

    ##篩選區
    allprod=mongoDB.Itemsdata.allprod

    #參數呼叫
    aallprod,pagebar,maxpagenum = mongoDB.Items_variance(pagenum,allprod)
    juarje = mongoDB.Itemsdata(pagenum,pagebar,maxpagenum).juarje

    if juarje ==0 :#(len(allprod)/30)+1 < pagenum <1:
        return redirect(url_for('show_records',pagenum=1))
    else:
        return render_template("index.html",
        aallprod=aallprod,
        pagenum=pagenum,
        pagebar=pagebar,
        maxpagenum=maxpagenum,
        catedata2=catedata2)


@app.route("/show_records/<categroy>/<int:pagenum>")

def categroy(pagenum,categroy):

    ##篩選區
    allprod=cate.categoryfilter(categroy)

    #參數呼叫
    aallprod,pagebar,maxpagenum = mongoDB.Items_variance(pagenum,allprod)
    juarje = mongoDB.Itemsdata(pagenum,pagebar,maxpagenum).juarje

    if juarje ==0 :#(len(allprod)/30)+1 < pagenum <1:
        return redirect(url_for('show_records',pagenum=1))
    else:
        return render_template("category.html",
        aallprod=aallprod,
        pagenum=pagenum,
        pagebar=pagebar,
        maxpagenum=maxpagenum,
        catedata2=catedata2,
        categroy=categroy)




@app.route("/search/<int:pagenum>/")

def search(pagenum):

    name = str(request.args.get('q'))

    ##篩選區
    
    allprod=mongoDB.searchfilter(allprods,name)

    ##
    if allprod==[]:
        return redirect(url_for('show_records',pagenum=1))
    else:

        #參數呼叫
        aallprod,pagebar,maxpagenum = mongoDB.Items_variance(pagenum,allprod)
        juarje = mongoDB.Itemsdata(pagenum,pagebar,maxpagenum).juarje

        #二次運算
        tme_pagebar=[]
        for i in pagebar:
            tme_pagebar.append(f"{i}/?q={name}")

        pagebar=tme_pagebar
        searcha=f"?q={name}"

        ##輸出給HTML
        if juarje ==0 :#(len(allprod)/30)+1 < pagenum <1:
            return redirect(url_for('show_records',pagenum=1))
        else:
            return render_template("search.html",searcha=searcha,aallprod=aallprod,pagenum=pagenum,pagebar=pagebar,maxpagenum=maxpagenum,catedata2=catedata2)


@app.route('/sitemap.xml')
@app.route('/robots.txt')
def public_from_root():
    
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=False)
