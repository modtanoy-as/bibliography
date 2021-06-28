from pattern import pattern
import re

class typefunction():
    def __init__(self) :
        self.test = {}
        self.arry = []
        self.alertMsg = {
        'Name' : 'ไม่มีชื่อผู้แต่ง',
        'Year' : 'ไม่มีปีที่เขียน',
        'Book' : 'ไม่มีชื่อหนังสือ',
        'Pim' : 'ไม่มีครั้งที่พิมพ์',
        'Location':'ไม่มีจังหวัดที่พิมพ์' ,
        'SamNakPim': 'ไม่มีสภานที่พิมพ์' ,
        'NumPage' : 'ไม่มีจำนวนหน้า',
        'article' : 'ไม่มีชื่อบทความ',
        'magazine' :  'ไม่มีชื่อวารสาร' , 
        'numyear' : 'ไม่มีปีที่ (ฉบับที่)' , 
        'page' : 'ไม่มีเลขหน้าที่ปรากฎ',
        'thesis' : 'ไม่มีชื่อวิทยานิพนธ์' , 
        'univer' : 'ไม่มีชื่อวิทยานิพนธ์ปริญญามหาบัณฑิตหรือวิทยานิพนธ์ปริญญาดุษฎีบัณฑิต/ชื่อมหาวิทยาลัย/สถาบันการศึกษา',
        'url' : 'ไม่พบเว็บไซต์ของข้อมูล',
        'urlWIKI' : 'ไม่พบเว็บไซต์ของข้อมูล',
        'day' : 'ไม่มีวันที่สืบค้น',
        'numissue' : 'ไม่มีฉบับที่',
        'year' : 'ไม่มีปีที่'
        }
        self.msg = []

    def checkBOOK(self,txt):
        subject = [txt.strip() for txt in txt.split('.')]
        selectCheck = 'BOOK'

        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                if key not in self.test:
                                    if key == 'SamNakPim':
                                        txtSplit = data.group().split(':')
                                        self.test['Location'] = txtSplit[0].strip()
                                        self.test['SamNakPim'] = txtSplit[1].strip()
                                    else:
                                        if key == 'Name':
                                            if re.search(r""+pattern[selectCheck]['editor']+"",item) is None:
                                                self.test[key] = data.group() 
                                        else:
                                            print( key , ' => ' , data.group())
                                            self.test[key] = data.group()
    

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                else:
                    txt = txt+'.'
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }

    def checkARTICLE(self,txt):
        subject = [txt.strip() for txt in txt.split('.')]

        selectCheck = 'ARTICLE'
        # ดึงเลขหน้า เนื่องจาก น. มีจุดทำให้ ตัดไม่ได้
        if re.search(r""+pattern[selectCheck]['NumPage']+"",txt) is not None:
            self.test['NumPage'] = re.search(r""+pattern[selectCheck]['NumPage']+"",txt).group()

        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                # print( key , ' => ' , data.group() , len(item) == len(data.group()) ,  len(item) , len(data.group()))
                                if key not in self.test:
                                    if key == 'SamNakPim':
                                        txtSplit = data.group().split(':')
                                        self.test['Location'] = txtSplit[0].strip()
                                        self.test['SamNakPim'] = txtSplit[1].strip()
                                    else:
                                        if key == 'Name':
                                            if re.search(r""+pattern[selectCheck]['editor']+"",item) is None:
                                                self.test[key] = data.group() 

                                        elif key == 'editor':
                                            txtSplit = data.group().split(',')
                                            # print(len(txtSplit))
                                            self.test['Book'] = txtSplit[len(txtSplit)-1].strip()
                                            self.test['editor'] = txtSplit[0] if len(txtSplit) <= 2 else ', '.join([name.strip( ) for name in txtSplit[:-1]])
                                            print('editor => ' ,  self.test['editor'])
                                        else:
                                            print( key , ' => ' , data.group())
                                            self.test[key] = data.group()

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                elif  key == 'editor':
                    txt = txt+','
                else:
                    txt = txt+'.'
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }

    def checkJOURNAL(self,txt):
        subject = [txt.strip() for txt in txt.split('.')]
        selectCheck = 'JOURNAL'

        if re.search(r""+pattern[selectCheck]['magazine']+"",txt) is not None:
            self.test['magazine'] = re.search(r""+pattern[selectCheck]['magazine']+"",txt).group().replace(',','')
        if re.search(r""+pattern[selectCheck]['numyear']+"",txt) is not None:
            self.test['numyear'] = re.search(r""+pattern[selectCheck]['numyear']+"",txt).group()
        if re.search(r""+pattern[selectCheck]['page']+"",txt) is not None:
            self.test['page'] = re.search(r""+pattern[selectCheck]['page']+"",txt).group()


        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                # print( key , ' => ' , data.group() , len(item) == len(data.group()) ,  len(item) , len(data.group()))
                                if key not in self.test:
                                    self.test[key] = data.group()

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                elif  key == 'magazine' or key == 'numyear':
                    txt = txt+','
                else:
                    txt = txt+'.'
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }

    def checkTHESES(self,txt):
        subject = [txt.strip() for txt in txt.split('.')]
        selectCheck = 'THESES'

        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                # print( key , ' => ' , data.group() , len(item) == len(data.group()) ,  len(item) , len(data.group()))
                                if key not in self.test:
                                    self.test[key] = data.group()

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                elif  key == 'magazine' or key == 'numyear':
                    txt = txt+','
                else:
                    txt = txt+'.'
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }

    def checkELECTRONICS(self,txt):
        subject = [txt.strip() for txt in txt.split('.')]
        selectCheck = 'ELECTRONICS'

        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                # print( key , ' => ' , data.group() , len(item) == len(data.group()) ,  len(item) , len(data.group()))
                                if key not in self.test:
                                    self.test[key] = data.group()
                checkMagazine = item.split(',')
                if len(checkMagazine) > 1:
                    for mz in checkMagazine:
                        if re.search(r""+pattern[selectCheck]['magazine']+"",mz) is not None:
                            self.test['magazine'] = re.search(r""+pattern[selectCheck]['magazine']+"",mz).group()
                        if re.search(r""+pattern[selectCheck]['numyear']+"",mz) is not None:
                            self.test['numyear'] = re.search(r""+pattern[selectCheck]['numyear']+"",mz).group()
                        if re.search(r""+pattern[selectCheck]['page']+"",mz) is not None:
                            self.test['page'] = re.search(r""+pattern[selectCheck]['page']+"",mz).group()

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                elif  key == 'magazine' or key == 'numyear':
                    txt = txt+','
                else:
                    txt = txt+'.'
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }

    def checkWIKI(self,txt):
        subject = [txt.strip() for txt in txt.split('. ')]
        selectCheck = 'WIKI'

        # ดึงเว็บ สืบค้น/จากวิกิ
        if re.search(r""+pattern[selectCheck]['url']+"",txt) is not None:
            self.test['url'] = re.search(r""+pattern[selectCheck]['url']+"",txt).group()
        # if re.search(r""+pattern[selectCheck]['urlWIKI']+"",txt) is not None:
        #     self.test['urlWIKI'] = re.search(r""+pattern[selectCheck]['urlWIKI']+"",txt).group()
        if re.search(r""+pattern[selectCheck]['day']+"",txt) is not None:
            self.test['day'] = re.search(r""+pattern[selectCheck]['day']+"",txt).group()

        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                if key not in self.test:
                                    self.test[key] = data.group()
        print(self.test)
        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                elif  key == 'magazine' or key == 'numyear':
                    txt = txt+','
                else:
                    txt = txt+'.'
                
                if 'Name' in self.test:
                    if key != 'subject':
                        self.arry.append(txt)
                else:
                    if key != 'article':
                        self.arry.append(txt)

            except:
                if key in self.alertMsg:
                    if 'url' in  self.test:
                        if 'จากวิกิพีเดีย' in self.test['url']:
                            if key != 'article' and key != 'Name':
                                self.msg.append(self.alertMsg[key])
                        elif 'สืบค้นจาก' in self.test['url']:
                            self.msg.append(self.alertMsg[key])
                    else:
                        self.msg.append(self.alertMsg[key])
                            

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }

    def checkPERIODICAL(self,txt):
        subject = [txt.strip().replace('” ','') for txt in txt.split(',')]
        selectCheck = 'PERIODICAL'

        if re.search(r""+pattern[selectCheck]['article']+"",txt) is not None:
            self.test['article'] = re.search(r""+pattern[selectCheck]['article']+"",txt).group()
        if re.search(r""+pattern[selectCheck]['year']+"",txt) is not None:
            self.test['year'] = re.search(r""+pattern[selectCheck]['year']+"",txt).group()

        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                print( key , ' => ' , data.group() , len(item) == len(data.group()) ,  len(item) , len(data.group()))
                                if key not in self.test:
                                    self.test[key] = data.group()
                                

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'article':
                    txt = txt+',”'
                elif  key == 'year':
                    txt = txt+'.'
                else:
                    txt = txt+','
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }
    def checkTHESISHARVARD(self,txt):
        subject = [txt.strip() for txt in txt.split('.')]
        selectCheck = 'THESISHARVARD'

        if re.search(r""+pattern[selectCheck]['magazine']+"",txt) is not None:
            self.test['magazine'] = re.search(r""+pattern[selectCheck]['magazine']+"",txt).group().replace(',','')
        if re.search(r""+pattern[selectCheck]['numyear']+"",txt) is not None:
            self.test['numyear'] = re.search(r""+pattern[selectCheck]['numyear']+"",txt).group()
        if re.search(r""+pattern[selectCheck]['page']+"",txt) is not None:
            self.test['page'] = re.search(r""+pattern[selectCheck]['page']+"",txt).group()


        for item in subject:
            if item != '':
                for key, value in pattern[selectCheck].items():
                    data = re.search(r""+value+"",item)
                    if data is not None:
                        if data.span()[1] > 0:
                            if len(item) == len(data.group()):
                                # print( key , ' => ' , data.group() , len(item) == len(data.group()) ,  len(item) , len(data.group()))
                                if key not in self.test:
                                    self.test[key] = data.group()

        for key, value in pattern[selectCheck].items():
            try:
                txt = self.test[key]
                if key == 'Location':
                    txt = txt+':'
                elif  key == 'magazine' or key == 'numyear':
                    txt = txt+','
                else:
                    txt = txt+'.'
                self.arry.append(txt)
            except:
                if key in self.alertMsg:
                    self.msg.append(self.alertMsg[key])

        if len(self.msg) >0:
            return {'text' : ' '.join(self.arry) , 'feedback' : ', '.join(self.msg)}
        else:
            return {'text' : ' '.join(self.arry) }
