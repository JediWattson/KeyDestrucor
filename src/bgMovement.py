import numpy as np
import cv2

cap = cv2.VideoCapture('smworld.webm')
cv2.namedWindow("mario1", cv2.WINDOW_NORMAL)
cv2.namedWindow("mario2", cv2.WINDOW_NORMAL)
track_window = (0,0,100,100)
surf = cv2.xfeatures2d.SURF_create(400)
surf.setUpright(True)
fgbg = cv2.createBackgroundSubtractorMOG2(
    history=10,
    varThreshold=2,
    detectShadows=False)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret ,frame = cap.read()
    
    if ret == True:
    
           
        # Converting the image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Extract the foreground
        edges_foreground = cv2.bilateralFilter(gray, 9, 75, 75)
        foreground = fgbg.apply(edges_foreground)
        
        # Smooth out to get the moving area
        kernel = np.ones((50,50),np.uint8)
        foreground = cv2.morphologyEx(foreground, cv2.MORPH_CLOSE, kernel)
        
        # Applying static edge extraction
        edges_foreground = cv2.bilateralFilter(gray, 7, 75, 75)
        edges_filtered = cv2.Canny(edges_foreground, 60, 120)
        
        # Crop off the edges out of the moving area
        cropped = (foreground // 255) * edges_filtered


        # Draw it on image
        x,y,w,h = track_window
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        
        roi_hist = cv2.calcHist([hsv],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        
        # set up the ROI for tracking   
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)


        #print (x,y)
        if x == 0 or y < 100:
            kp, des = surf.detectAndCompute(cropped, None)
            if len(kp) > 0:
                i = 0
                while i < len(kp):
                    r, c = kp[i].pt
                    if r > 200 and c > 200:
                        break
                    if i == len(kp) - 1:
                        r = 200
                        c = 200
                        break
                    i = i + 1
            else:
                r = 200
                c = 200         
            track_window = (int(r), int(c), 60, 60)  
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
        

        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        kp, des = surf.detectAndCompute(cropped, None)
        cv2.drawKeypoints(cropped,kp,cropped,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)        
        cv2.imshow('mario1', frame)
        cv2.imshow('mario2', cropped)

    else:
        break

cv2.destroyAllWindows()
cap.release()

'''

        if False:        
            surf = cv2.xfeatures2d.SURF_create(4000)
            surf.setUpright(True)
            kp, des = surf.detectAndCompute(frame, None)
            print (kp)
            img2 = frame
            cv2.drawKeypoints(frame,kp,img2,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)        

        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)

    

        # apply meanshift to get the new location
        roi = frame[r:r+h, c:c+w]
        hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

         # set up the ROI for tracking   
         ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
         
        
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)

'''