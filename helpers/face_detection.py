import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import mediapipe as mp
from time import strftime as stime
from datetime import datetime 
from helpers.database import *
from flask import session

def timeStamp(x):
        return datetime.timestamp(x)

def faceDetection():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture("./recording.webm")#'')
    get_speed = cap.get(cv2.CAP_PROP_POS_FRAMES)
    cap.set(cv2.CAP_PROP_POS_FRAMES,get_speed-1000)
    head_position = [0, 0, 0, 0]
    head_distance_movement = []
    center_prev = (0, 0)
    # current = int(stime('%H'))*3600 + int(stime('%M'))*60 + float(stime('%S')+'.'+str(datetime.now().microsecond))
    current = timeStamp(datetime.now())
    temp = ""
    end_time = 0
    end_movement = ""
    listOfMvmt = []
    temp_list = []
    while True:
        ret, frame = cap.read()
        if ret is False:
            break
        success, image = cap.read()
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_scale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray_scale = cv2.bilateralFilter(gray_scale, 5, 1, 1)
        faces = face_cascade.detectMultiScale(gray_scale, 1.3, 5, minSize=(200, 200))
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                eye_face = gray_scale[y:y + h, x:x + w]
                eye_face_clr = image[y:y + h, x:x + w]
                eyes = eyes_cascade.detectMultiScale(eye_face, 1.3, 5, minSize=(50, 50))
                if len(eyes) >= 2:
                    cv2.putText(image, "Eye's Open", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (255, 255, 255), 2)
                else:
                    cv2.putText(image, "Eye's close", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (255, 255, 255), 2)
        else:
            cv2.putText(image, "No Face Detected.", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = face_mesh.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        img_h, img_w, img_c = image.shape
        face_3d = []
        face_2d = []
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for idx, lm in enumerate(face_landmarks.landmark):
                    
                    if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                        if idx == 1:
                            nose_2d = (lm.x * img_w, lm.y * img_h)
                            nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                        x, y = int(lm.x * img_w), int(lm.y * img_h)
                        face_2d.append([x, y])
                        face_3d.append([x, y, lm.z])       
                
                format_ct = stime('%H:%M:%S')+'.'+str(datetime.now().microsecond)
                ct = timeStamp(datetime.now())
                # ct = int(stime('%H'))*3600 + int(stime('%M'))*60 + float(stime('%S')+'.'+str(datetime.now().microsecond))

                face_2d = np.array(face_2d, dtype=np.float64)
                face_3d = np.array(face_3d, dtype=np.float64)
                focal_length = 1 * img_w

                cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                        [0, focal_length, img_w / 2],
                                        [0, 0, 1]])
                dist_matrix = np.zeros((4, 1), dtype=np.float64)
                success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
                rmat, jac = cv2.Rodrigues(rot_vec)
                angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)
                x = angles[0] * 360
                y = angles[1] * 360

                if y < -10:
                    text = "Left"
                    head_position[0] += 1
                elif y > 10:
                    text = "Right"
                    head_position[1] += 1
                elif x < -10:
                    text = "Down"
                    head_position[3] += 1
                else:
                    text = "Forward"
                    head_position[2] += 1

                nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)

                p1 = (int(nose_2d[0]), int(nose_2d[1]))
                p2 = (int(nose_3d_projection[0][0][0]), int(nose_3d_projection[0][0][1]))
                
                cv2.circle(image, p1, 5, (0,0,255), 3)

                cv2.putText(image, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                x, y = p2
                distance = math.hypot(x - center_prev[0], y - center_prev[1])
                head_distance_movement.append(distance)
                center_prev = p2
                temp_time = ct-current
                if temp==text:
                    temp_time += ct-current
                else:
                    temp_list.append((text,abs(ct-current)))
                    listOfMvmt.append((text,format_ct))
                end_time = format_ct
                temp = text
                end_movement = text


        cv2.imshow('Head Pose Estimation', image)
        
    # cap.release()
    # cv2.destroyAllWindows()
    listOfMvmt.append((end_movement,end_time))
    upper = [int(listOfMvmt[-1][1].split(':')[0])*3600, int(listOfMvmt[-1][1].split(':')[1])*60, float(listOfMvmt[-1][1].split(':')[2])]
    lower = [int(listOfMvmt[-2][1].split(':')[0])*3600, int(listOfMvmt[-2][1].split(':')[1])*60, float(listOfMvmt[-2][1].split(':')[2])]
    temp_list.append((end_movement,upper[0]-lower[0]+upper[1]-lower[1]+upper[2]-lower[2]))
    temp_log = []
    for i in range(len(temp_list)-1):
        if i!=len(temp_list)-1:
            temp_log.append([temp_list[i][1],temp_list[i+1][1],temp_list[i][0]]) # dataset
    
    log = []
    for i in range(len(listOfMvmt)-1):
        if i!=len(listOfMvmt)-1:
            log.append([listOfMvmt[i][1], listOfMvmt[i+1][1], listOfMvmt[i][0], abs(temp_log[i][1]-temp_log[i][0])]) # dataset
    work = studb.worksheet(session["username"])
    for x in log:
        work.append_row(x,value_input_option="USER_ENTERED")