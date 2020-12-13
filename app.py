from flask import Flask,render_template,request,flash, redirect
import requests
from pytube import YouTube


app=Flask(__name__)
app.secret_key="93459729573945hegjfgijhgrt9ghkftgj9"


header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/instagram", methods=['POST','GET'])
def instagram():
    if request.method=='POST':
        post_url=request.form.get('url')
        if 'instagram.com/p/' in post_url:
            if '?' in post_url:
                tail='&__a=1'
            else:
                tail='?__a=1'

            url=post_url+tail

            try:
                response=requests.get(url,headers=header).json()
                video=response['graphql']['shortcode_media']['video_url']
                return render_template('download.html', video_url=video)
            except Exception as e:

                flash('Something went wrong')
                return redirect("/")
        elif 'instagram.com/reel/' in post_url:
            if '?' in post_url:
                tail='&__a=1'
            else:
                tail='?__a=1'
            try:
                url=post_url+tail
                response = requests.get(url, headers=header).json()
                video = response['graphql']['shortcode_media']['video_url']
                # ===code from scratch===
                # r = requests.get(post_url).text
                # soup = BeautifulSoup(r, 'lxml')
                # script = soup.find_all('script', attrs={'type': 'text/javascript'})[3].getText()[21:-1]
                # json_dict = json.loads(script)
                # video_url=json_dict['entry_data']['PostPage'][0]['graphql']['shortcode_media']['video_url']

                return render_template('download.html', video_url=video)
            except Exception as e:

                flash('Something went wrong')
                return redirect('/')
        else:
            flash('invalid link, please check')
            return redirect("/")

def checkUrl(obj):
    if obj != None:

        if 'amp;' in obj.url:
            realUrl=""
            for u in obj.url.split('amp;'):
                realUrl+=u
            obj.url=realUrl


@app.route("/youtube", methods=['POST','GET'])
def youtube():
    if request.method=='POST':
        url=request.form.get('url')
        result={}
        if 'you' in url:
            try:
                youtube=YouTube(url)
                result['1080p']=youtube.streams.filter(res="1080p", progressive=True).first()
                checkUrl(result['1080p'])
                if result['1080p'] != None:
                    result['1080psize']=round(result['1080p'].filesize/1048576,2)
                result['720p'] = youtube.streams.filter(res="720p", progressive=True).first()
                checkUrl(result['720p'])
                if result['720p'] != None:
                    result['720psize']=round(result['720p'].filesize/1048576,2)
                result['480p'] = youtube.streams.filter(res="480p", progressive=True).first()
                checkUrl(result['480p'])
                if result['480p'] != None:
                    result['480psize']=round(result['480p'].filesize/1048576,2)
                result['360p'] = youtube.streams.filter(res="360p", progressive=True).first()
                checkUrl(result['360p'])
                if result['360p'] != None:
                    result['360psize']=round(result['360p'].filesize/1048576,2)
                result['audiomp4']=youtube.streams.filter(type='audio',mime_type="audio/mp4").first()
                checkUrl(result['audiomp4'])
                if result['audiomp4'] != None:
                    result['audiomp4size']=round(result['audiomp4'].filesize/1048576,2)
                result['audiowebm'] = youtube.streams.filter(type='audio', mime_type="audio/webm").first()
                checkUrl(result['audiowebm'])
                if result['audiowebm'] != None:
                    result['audiowebmsize'] = round(result['audiowebm'].filesize / 1048576, 2)
                return render_template('youtube.html',result=result)
            except Exception as e:
               
                flash('Something went wrong')

                return redirect('/')
        else:
            flash('invalid link, please check')
            return redirect('/')

@app.route('/download', methods=['POST'])
def download():
    if request.method=='POST':
        url=request.form.get('url')
        return render_template("download.html",video_url=url)

@app.route('/download-audio', methods=['POST'])
def downloadaudio():
    if request.method=='POST':
        url=request.form.get('url')
        return render_template("downloadmp3.html",video_url=url)



if __name__ == '__main__':
    app.run(debug=True)

