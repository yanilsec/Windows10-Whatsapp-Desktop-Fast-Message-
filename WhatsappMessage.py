#You need Whatsapp Desktop and Windows

import pyautogui as pygui
import time
from termcolor import colored
import pyfiglet


try:
    
        def mesajgonder(numara,mesaj):
            print("message sending!!!!")
            mesaj1=0
            mesaj2=0
            mesaj3=0
            mesaj4=0
            mesaj5=0

            try:
                
                if liste[0] == "":
                    print("PLEASE ENTER NAME OR PHONE NUMBER!!!")
                    sys.exit()
                    
                else:
                        time.sleep(2)
                        pygui.hotkey('Ctrl','f')
                        pygui.write(liste[0])
                        pygui.press('enter')
                        time.sleep(1)
                        
                        while mesaj1 < 20:
                            if mesaj1==20:
                                break
                            else:
                                pygui.write(mesajcoklu)
                                pygui.press('enter')
                            mesaj1 += 1
                
                
                if liste[1] == "":
                    print("PLEASE ENTER NAME OR PHONE NUMBER!!!")
                    sys.exit()
                else:    

                        time.sleep(2)
                        pygui.hotkey('Ctrl','f')
                        pygui.write(liste[1])
                        pygui.press('enter')
                        time.sleep(1)
                            
                        while mesaj2 < 20:
                            if mesaj2==20:
                                break
                            else:

                                pygui.write(mesajcoklu)
                                pygui.press('enter')
                            mesaj2 += 1

            
            
                if liste[2] == "":
                    sys.exit()
                    print("i sent all messages")
                else:
                        time.sleep(2)
                        pygui.hotkey('Ctrl','f')
                        pygui.write(liste[2])
                        pygui.press('enter')
                        time.sleep(1)
                        
                        while mesaj3 < 20:
                            if mesaj3==20:
                                break
                            else:
                        
                                pygui.write(mesajcoklu)
                                pygui.press('enter')

                            mesaj3 += 1


                if liste[3] == "":
                    sys.exit()
                    print("i sent all messages")
                else:


                        time.sleep(2)
                        pygui.hotkey('Ctrl','f')
                        pygui.write(liste[3])
                        pygui.press('enter')
                        time.sleep(1)
                        
                        while mesaj4 < 20:
                            if mesaj4 == 20:
                                break
                            else:

                                pygui.write(mesajcoklu)
                                pygui.press('enter')
                            mesaj4 += 1


                if liste[4] == "":
                    sys.exit()
                    print("i sent all messages")
                else:   


                        time.sleep(2)
                        pygui.hotkey('Ctrl','f')
                        pygui.write(liste[4])
                        pygui.press('enter')
                        time.sleep(1)
                        
                        while mesaj5 < 20:
                            if mesaj5 == 20:
                                break
                            else:

                                pygui.write(mesajcoklu)
                                pygui.press('enter')
                            mesaj5 += 1


            except IndexError:
                print("i sent all messages")

        banner = pyfiglet.figlet_format("YANIL SEC")
        print(colored(banner,'green'))
        print(colored("Pr4Nk S0ftW4r3",'green'))
        print(colored("yanilsec | https://github.com/yanilsec",'red'))
        print(colored("you can send just 20 message",'red'))

        liste=[]

        kullanicigirdisi = input("multi message(YES/NO): ")



        if kullanicigirdisi == "yes" or kullanicigirdisi == "YES":


            for i in range(4):
                usergirdi = input(f"you can send message max 5 people:({i}) " )
                if usergirdi == "":
                    break

                liste.append(usergirdi)

            
            mesajcoklu = input("your message: ")

            time.sleep(2)

            pygui.hotkey('Win','s')
            pygui.press(['W','h','a','t','s','a','p','p'])
            pygui.press('enter')

            time.sleep(10)

            mesajgonder(liste,mesajcoklu)

            


        elif kullanicigirdisi == "no" or kullanicigirdisi == "NO":

            teklimesaj = input("who?: ")
            kimemesaj = input("your message: ")

            time.sleep(2)

            pygui.hotkey('Win','s')
            pygui.press(['W','h','a','t','s','a','p','p'])
            pygui.press('enter')

            time.sleep(10)

            pygui.hotkey('Ctrl','f')
            pygui.write(teklimesaj)
            pygui.press('enter')
            
            time.sleep(3)

            sayi = 0

            while sayi < 20:
                
                if sayi == 20:
                    break
                else:   
                    
                    pygui.write(kimemesaj)
                    pygui.press('enter')

                sayi += 1


except KeyboardInterrupt:
    print("\nOK I STOPPED PROGRAM")