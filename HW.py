import cv2
import mediapipe as mp



cap = cv2.VideoCapture(0)
lrtext = ""
finger= ["","","","",""]
#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
myHands=[""]
handsType=[""]
inhand=""

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                for hand in results.multi_handedness:
                    handType=hand.classification[0].label
                    if handType=='Right':
                        inhand="left"
                    else :
                        inhand="right"
                    handsType[0]=inhand
                
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 =cy
                if id == 12:
                    id12 = int(id)
                    cy12 =cy
                if id == 11:
                    id11 = int(id)
                    cy11 =cy
                if id == 16:
                    id16 = int(id)
                    cy16 =cy
                if id == 15:
                    id15 = int(id)
                    cy15 =cy
                if id == 20:
                    id20 = int(id)
                    cy20 =cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
            #the greater cx stands for tip, lower one stands for dip
            #create the condition for left and right hand 
            #Normally, x-axis right tip(cx4) is greater than dip(cx3)
            if inhand=="right":
                if cx4 > cx3:
                    finger[0]="th"
                else:
                    finger[0]="" 
            else:
                if cx4<cx3:
                    finger[0]="th"
                else:
                    finger[0]=""
            #compare with tip and dip if y-axis of tip are lowers than dip that mean you're not raises your finger
            if cy8 <cy7:
                finger[1]="in"
            else:
                finger[1]=""
            if cy12 <cy11:
                finger[2]="mi"
            else:
                finger[2]=""
            if cy16 <cy15:
                finger[3]="ri"
            else:
                finger[3]=""
            if cy20 <cy19:
                finger[4]="pi"
            else:
                finger[4]=""    
                

           
                
            

              

                                         
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
    cv2.putText(img, ', '.join(map(str, finger)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.putText(img, ', '.join(map(str,handsType)), (10, 130), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 255, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    finger=["","","","",""]
    handsType=[""]
#Closeing all open windows
#cv2.destroyAllWindows()
