from playwright.sync_api import sync_playwright
import random
import time

with sync_playwright() as p:
    url ='http://manage.gsei.com.cn/html/1337'

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    res=page.goto(url)

    maxno=page.locator('#page').text_content()
    # print(maxno,type(maxno))
    print(maxno.split('首页')[0].split('条')[0])
    print(maxno.split('首页')[0].split('条')[1].replace('页','').split('/')[-1])
    tiezi =[]
    neirong={}
    for index in  range(0,2351-1):
    #for yeshu in  range(0,3-1):

        tiezi_list =page.locator('.adaplist94 >li')
        for index in range(1,tiezi_list.count()):
            time.sleep(random.randint(20, 40)*0.01)
        
            print(tiezi_list.nth(index).inner_html())
            tiezi_url =tiezi_list.nth(index).locator('a').get_attribute('href')
            mcheng =tiezi_list.nth(index).locator('a').text_content()
            riqi =tiezi_list.nth(index).locator('span').text_content()
            zhengwenpage = browser.new_page()

            zhengwenpage.goto('http://manage.gsei.com.cn'+tiezi_url)
            zhengwen  =zhengwenpage.locator('.artcon').inner_text().replace('\n','')
            neirong['url']=tiezi_url
            neirong['mcheng']=mcheng
            neirong['riqi']=riqi,
            neirong['zhengwen']=zhengwen
            # tiezi.append(neirong)
            with open("tiezi.csv",'a+', encoding='utf-8-sig') as f:
                f.write(str(yeshu*25+index)+','+mcheng+''+riqi+','+zhengwen+'\n')
#    print(len(tiezi),tiezi)
