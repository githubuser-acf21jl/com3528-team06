# com3528-team06

## Link to Download the Dataset
Download the [Dataset](https://drive.google.com/file/d/1-yfLj6kGllW8euEd0NepM4jNen8-IOrg/view?usp=sharing) here.


_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input (InputLayer)          [(None, 48, 48, 1)]       0         
                                                                 
 conv1_1 (Conv2D)            (None, 48, 48, 64)        640       
                                                                 
 batch_normalization (Batch  (None, 48, 48, 64)        256       
 Normalization)                                                  
                                                                 
 conv1_2 (Conv2D)            (None, 48, 48, 64)        36928     
                                                                 
 batch_normalization_1 (Bat  (None, 48, 48, 64)        256       
 chNormalization)                                                
                                                                 
 pool1_1 (MaxPooling2D)      (None, 24, 24, 64)        0         
                                                                 
 drop1_1 (Dropout)           (None, 24, 24, 64)        0         
                                                                 
 conv2_1 (Conv2D)            (None, 24, 24, 128)       73856     
                                                                 
 batch_normalization_2 (Bat  (None, 24, 24, 128)       512       
 chNormalization)                                                
                                                                 
 conv2_2 (Conv2D)            (None, 24, 24, 128)       147584    
                                                                 
 batch_normalization_3 (Bat  (None, 24, 24, 128)       512       
 chNormalization)                                                
                                                                 
 conv2_3 (Conv2D)            (None, 24, 24, 128)       147584    
                                                                 
 pool2_1 (MaxPooling2D)      (None, 12, 12, 128)       0         
                                                                 
 drop2_1 (Dropout)           (None, 12, 12, 128)       0         
                                                                 
 conv3_1 (Conv2D)            (None, 12, 12, 256)       295168    
                                                                 
 batch_normalization_5 (Bat  (None, 12, 12, 256)       1024      
 chNormalization)                                                
                                                                 
 conv3_2 (Conv2D)            (None, 12, 12, 256)       590080    
                                                                 
 batch_normalization_6 (Bat  (None, 12, 12, 256)       1024      
 chNormalization)                                                
                                                                 
 conv3_3 (Conv2D)            (None, 12, 12, 256)       590080    
                                                                 
 batch_normalization_7 (Bat  (None, 12, 12, 256)       1024      
 chNormalization)                                                
                                                                 
 conv3_4 (Conv2D)            (None, 12, 12, 256)       590080    
                                                                 
 batch_normalization_8 (Bat  (None, 12, 12, 256)       1024      
 chNormalization)                                                
                                                                 
 pool3_1 (MaxPooling2D)      (None, 6, 6, 256)         0         
                                                                 
 drop3_1 (Dropout)           (None, 6, 6, 256)         0         
                                                                 
 conv4_1 (Conv2D)            (None, 6, 6, 256)         590080    
                                                                 
 batch_normalization_9 (Bat  (None, 6, 6, 256)         1024      
 chNormalization)                                                
                                                                 
 conv4_2 (Conv2D)            (None, 6, 6, 256)         590080    
                                                                 
 batch_normalization_10 (Ba  (None, 6, 6, 256)         1024      
 tchNormalization)                                               
                                                                 
 conv4_3 (Conv2D)            (None, 6, 6, 256)         590080    
                                                                 
 batch_normalization_11 (Ba  (None, 6, 6, 256)         1024      
 tchNormalization)                                               
                                                                 
 conv4_4 (Conv2D)            (None, 6, 6, 256)         590080    
                                                                 
 batch_normalization_12 (Ba  (None, 6, 6, 256)         1024      
 tchNormalization)                                               
                                                                 
 pool4_1 (MaxPooling2D)      (None, 3, 3, 256)         0         
                                                                 
 drop4_1 (Dropout)           (None, 3, 3, 256)         0         
                                                                 
 conv5_1 (Conv2D)            (None, 3, 3, 512)         1180160   
                                                                 
 batch_normalization_13 (Ba  (None, 3, 3, 512)         2048      
 tchNormalization)                                               
                                                                 
 conv5_2 (Conv2D)            (None, 3, 3, 512)         2359808   
                                                                 
 batch_normalization_14 (Ba  (None, 3, 3, 512)         2048      
 tchNormalization)                                               
                                                                 
 conv5_3 (Conv2D)            (None, 3, 3, 512)         2359808   
                                                                 
 batch_normalization_15 (Ba  (None, 3, 3, 512)         2048      
 tchNormalization)                                               
                                                                 
 conv5_4 (Conv2D)            (None, 3, 3, 512)         2359808   
                                                                 
 pool5_1 (MaxPooling2D)      (None, 1, 1, 512)         0         
                                                                 
 drop5_1 (Dropout)           (None, 1, 1, 512)         0         
                                                                 
 flatten (Flatten)           (None, 512)               0         
                                                                 
 output (Dense)              (None, 7)                 3591      
                                                                 
=================================================================
Total params: 13111367 (50.02 MB)
Trainable params: 13103431 (49.99 MB)
Non-trainable params: 7936 (31.00 KB)
_________________________________________________________________
None
Epoch 1/100
448/448 [==============================] - 525s 1s/step - loss: 2.0322 - accuracy: 0.2138 - val_loss: 1.9167 - val_accuracy: 0.1895
Epoch 2/100
448/448 [==============================] - 530s 1s/step - loss: 1.7869 - accuracy: 0.2533 - val_loss: 1.7635 - val_accuracy: 0.2662
Epoch 3/100
448/448 [==============================] - 526s 1s/step - loss: 1.7494 - accuracy: 0.2802 - val_loss: 1.8423 - val_accuracy: 0.2539
Epoch 4/100
448/448 [==============================] - 518s 1s/step - loss: 1.7068 - accuracy: 0.3097 - val_loss: 1.7731 - val_accuracy: 0.3326
Epoch 5/100
448/448 [==============================] - 493s 1s/step - loss: 1.6333 - accuracy: 0.3550 - val_loss: 1.6804 - val_accuracy: 0.3739
Epoch 6/100
448/448 [==============================] - 493s 1s/step - loss: 1.5559 - accuracy: 0.3917 - val_loss: 1.7179 - val_accuracy: 0.3929
Epoch 7/100
448/448 [==============================] - 495s 1s/step - loss: 1.5037 - accuracy: 0.4159 - val_loss: 1.5562 - val_accuracy: 0.4294
Epoch 8/100
448/448 [==============================] - 494s 1s/step - loss: 1.4329 - accuracy: 0.4495 - val_loss: 1.4738 - val_accuracy: 0.4484
Epoch 9/100
448/448 [==============================] - 495s 1s/step - loss: 1.3688 - accuracy: 0.4735 - val_loss: 1.3063 - val_accuracy: 0.4975
Epoch 10/100
340/448 [=====================>........] - ETA: 1:54 - loss: 1.3136 - accuracy: 0.4992
448/448 [==============================] - 495s 1s/step - loss: 1.3137 - accuracy: 0.4992 - val_loss: 1.3150 - val_accuracy: 0.5103
Epoch 11/100
448/448 [==============================] - 494s 1s/step - loss: 1.2735 - accuracy: 0.5149 - val_loss: 1.2552 - val_accuracy: 0.5335
Epoch 12/100
448/448 [==============================] - 493s 1s/step - loss: 1.2338 - accuracy: 0.5338 - val_loss: 1.2852 - val_accuracy: 0.5011
Epoch 13/100
448/448 [==============================] - 510s 1s/step - loss: 1.1950 - accuracy: 0.5471 - val_loss: 1.1534 - val_accuracy: 0.5539
Epoch 14/100
448/448 [==============================] - 530s 1s/step - loss: 1.1730 - accuracy: 0.5568 - val_loss: 1.1419 - val_accuracy: 0.5751
Epoch 15/100
448/448 [==============================] - 521s 1s/step - loss: 1.1451 - accuracy: 0.5682 - val_loss: 1.1217 - val_accuracy: 0.5773
Epoch 16/100
448/448 [==============================] - 494s 1s/step - loss: 1.1166 - accuracy: 0.5788 - val_loss: 1.1560 - val_accuracy: 0.5619
Epoch 17/100
448/448 [==============================] - 490s 1s/step - loss: 1.0963 - accuracy: 0.5891 - val_loss: 1.0871 - val_accuracy: 0.5815
Epoch 18/100
448/448 [==============================] - 492s 1s/step - loss: 1.0722 - accuracy: 0.5963 - val_loss: 1.1187 - val_accuracy: 0.5879
Epoch 19/100
448/448 [==============================] - 492s 1s/step - loss: 1.0581 - accuracy: 0.5992 - val_loss: 1.0876 - val_accuracy: 0.6032
Epoch 20/100
448/448 [==============================] - 492s 1s/step - loss: 1.0384 - accuracy: 0.6086 - val_loss: 1.0371 - val_accuracy: 0.6144
Epoch 21/100
448/448 [==============================] - 492s 1s/step - loss: 1.0151 - accuracy: 0.6189 - val_loss: 1.0722 - val_accuracy: 0.6010
Epoch 22/100
448/448 [==============================] - 492s 1s/step - loss: 1.0042 - accuracy: 0.6221 - val_loss: 1.0271 - val_accuracy: 0.6261
Epoch 23/100
448/448 [==============================] - 492s 1s/step - loss: 0.9877 - accuracy: 0.6264 - val_loss: 1.0247 - val_accuracy: 0.6253
Epoch 24/100
448/448 [==============================] - 493s 1s/step - loss: 0.9714 - accuracy: 0.6348 - val_loss: 1.0054 - val_accuracy: 0.6336
Epoch 25/100
448/448 [==============================] - 492s 1s/step - loss: 0.9539 - accuracy: 0.6423 - val_loss: 1.0656 - val_accuracy: 0.6127
Epoch 26/100
448/448 [==============================] - 492s 1s/step - loss: 0.9413 - accuracy: 0.6463 - val_loss: 1.0347 - val_accuracy: 0.6130
Epoch 27/100
448/448 [==============================] - 515s 1s/step - loss: 0.9276 - accuracy: 0.6526 - val_loss: 1.0269 - val_accuracy: 0.6161
Epoch 28/100
448/448 [==============================] - 527s 1s/step - loss: 0.9187 - accuracy: 0.6565 - val_loss: 1.0218 - val_accuracy: 0.6395
Epoch 29/100
448/448 [==============================] - 525s 1s/step - loss: 0.9030 - accuracy: 0.6623 - val_loss: 0.9873 - val_accuracy: 0.6454
Epoch 30/100
448/448 [==============================] - 498s 1s/step - loss: 0.8904 - accuracy: 0.6677 - val_loss: 0.9838 - val_accuracy: 0.6390
Epoch 31/100
448/448 [==============================] - 489s 1s/step - loss: 0.8771 - accuracy: 0.6738 - val_loss: 1.0187 - val_accuracy: 0.6356
Epoch 32/100
448/448 [==============================] - 489s 1s/step - loss: 0.8649 - accuracy: 0.6749 - val_loss: 0.9541 - val_accuracy: 0.6518
Epoch 33/100
448/448 [==============================] - 488s 1s/step - loss: 0.8538 - accuracy: 0.6817 - val_loss: 1.0308 - val_accuracy: 0.6219
Epoch 34/100
448/448 [==============================] - 488s 1s/step - loss: 0.8445 - accuracy: 0.6859 - val_loss: 0.9944 - val_accuracy: 0.6339
Epoch 35/100
448/448 [==============================] - 489s 1s/step - loss: 0.8291 - accuracy: 0.6913 - val_loss: 0.9507 - val_accuracy: 0.6535
Epoch 36/100
448/448 [==============================] - 489s 1s/step - loss: 0.8171 - accuracy: 0.6956 - val_loss: 0.9962 - val_accuracy: 0.6462
Epoch 37/100
448/448 [==============================] - 488s 1s/step - loss: 0.8075 - accuracy: 0.6984 - val_loss: 0.9822 - val_accuracy: 0.6406
Epoch 38/100
448/448 [==============================] - 488s 1s/step - loss: 0.7933 - accuracy: 0.7040 - val_loss: 0.9770 - val_accuracy: 0.6465
Epoch 39/100
448/448 [==============================] - 488s 1s/step - loss: 0.7915 - accuracy: 0.7043 - val_loss: 0.9671 - val_accuracy: 0.6646
Epoch 40/100
448/448 [==============================] - 488s 1s/step - loss: 0.7773 - accuracy: 0.7095 - val_loss: 0.9603 - val_accuracy: 0.6613
Epoch 41/100
448/448 [==============================] - 488s 1s/step - loss: 0.7600 - accuracy: 0.7166 - val_loss: 0.9663 - val_accuracy: 0.6574
Epoch 42/100
448/448 [==============================] - 489s 1s/step - loss: 0.7540 - accuracy: 0.7184 - val_loss: 1.0090 - val_accuracy: 0.6602
Epoch 43/100
448/448 [==============================] - 488s 1s/step - loss: 0.7419 - accuracy: 0.7230 - val_loss: 0.9869 - val_accuracy: 0.6549
Epoch 44/100
448/448 [==============================] - 488s 1s/step - loss: 0.7264 - accuracy: 0.7277 - val_loss: 0.9912 - val_accuracy: 0.6576
Epoch 45/100
448/448 [==============================] - 488s 1s/step - loss: 0.7189 - accuracy: 0.7340 - val_loss: 0.9820 - val_accuracy: 0.6643
Epoch 46/100
448/448 [==============================] - 489s 1s/step - loss: 0.7096 - accuracy: 0.7356 - val_loss: 0.9870 - val_accuracy: 0.6680
Epoch 47/100
448/448 [==============================] - 488s 1s/step - loss: 0.6974 - accuracy: 0.7376 - val_loss: 0.9767 - val_accuracy: 0.6722
Epoch 48/100
448/448 [==============================] - 488s 1s/step - loss: 0.6857 - accuracy: 0.7424 - val_loss: 0.9949 - val_accuracy: 0.6596
Epoch 49/100
448/448 [==============================] - 488s 1s/step - loss: 0.6778 - accuracy: 0.7472 - val_loss: 0.9857 - val_accuracy: 0.6761
Epoch 50/100
448/448 [==============================] - 488s 1s/step - loss: 0.6698 - accuracy: 0.7498 - val_loss: 1.0383 - val_accuracy: 0.6579
Epoch 51/100
448/448 [==============================] - 488s 1s/step - loss: 0.6587 - accuracy: 0.7529 - val_loss: 0.9772 - val_accuracy: 0.6735
Epoch 52/100
448/448 [==============================] - 488s 1s/step - loss: 0.6462 - accuracy: 0.7602 - val_loss: 1.0052 - val_accuracy: 0.6708
Epoch 53/100
448/448 [==============================] - 488s 1s/step - loss: 0.6369 - accuracy: 0.7617 - val_loss: 0.9869 - val_accuracy: 0.6766
Epoch 54/100
448/448 [==============================] - 488s 1s/step - loss: 0.6300 - accuracy: 0.7651 - val_loss: 0.9730 - val_accuracy: 0.6828
Epoch 55/100
448/448 [==============================] - 488s 1s/step - loss: 0.6098 - accuracy: 0.7750 - val_loss: 1.0149 - val_accuracy: 0.6616
Epoch 56/100
448/448 [==============================] - 488s 1s/step - loss: 0.6091 - accuracy: 0.7719 - val_loss: 1.0424 - val_accuracy: 0.6593
Epoch 57/100
448/448 [==============================] - 488s 1s/step - loss: 0.5993 - accuracy: 0.7769 - val_loss: 1.0249 - val_accuracy: 0.6699
Epoch 58/100
448/448 [==============================] - 487s 1s/step - loss: 0.5936 - accuracy: 0.7772 - val_loss: 1.0054 - val_accuracy: 0.6775
Epoch 59/100
448/448 [==============================] - 487s 1s/step - loss: 0.5784 - accuracy: 0.7846 - val_loss: 1.0247 - val_accuracy: 0.6755
Epoch 60/100
448/448 [==============================] - 488s 1s/step - loss: 0.5711 - accuracy: 0.7868 - val_loss: 1.0130 - val_accuracy: 0.6766
Epoch 61/100
448/448 [==============================] - 488s 1s/step - loss: 0.5607 - accuracy: 0.7916 - val_loss: 1.0189 - val_accuracy: 0.6749
Epoch 62/100
448/448 [==============================] - 488s 1s/step - loss: 0.5548 - accuracy: 0.7926 - val_loss: 1.0578 - val_accuracy: 0.6780
Epoch 63/100
448/448 [==============================] - 488s 1s/step - loss: 0.5438 - accuracy: 0.7988 - val_loss: 1.0914 - val_accuracy: 0.6549
Epoch 64/100
448/448 [==============================] - 488s 1s/step - loss: 0.5375 - accuracy: 0.7970 - val_loss: 1.0569 - val_accuracy: 0.6744
Epoch 65/100
448/448 [==============================] - 488s 1s/step - loss: 0.5216 - accuracy: 0.8059 - val_loss: 1.0679 - val_accuracy: 0.6814
Epoch 66/100
448/448 [==============================] - 487s 1s/step - loss: 0.5120 - accuracy: 0.8096 - val_loss: 1.0677 - val_accuracy: 0.6769
Epoch 67/100
448/448 [==============================] - 487s 1s/step - loss: 0.5027 - accuracy: 0.8145 - val_loss: 1.1076 - val_accuracy: 0.6638
Epoch 68/100
448/448 [==============================] - 487s 1s/step - loss: 0.5010 - accuracy: 0.8128 - val_loss: 1.1040 - val_accuracy: 0.6780
Epoch 69/100
448/448 [==============================] - 524s 1s/step - loss: 0.4917 - accuracy: 0.8161 - val_loss: 1.1418 - val_accuracy: 0.6643
Epoch 70/100
448/448 [==============================] - 541s 1s/step - loss: 0.4865 - accuracy: 0.8195 - val_loss: 1.1061 - val_accuracy: 0.6755
Epoch 71/100
448/448 [==============================] - 540s 1s/step - loss: 0.4788 - accuracy: 0.8215 - val_loss: 1.1609 - val_accuracy: 0.6655
Epoch 72/100
448/448 [==============================] - 487s 1s/step - loss: 0.4698 - accuracy: 0.8261 - val_loss: 1.1016 - val_accuracy: 0.6814
Epoch 73/100
448/448 [==============================] - 487s 1s/step - loss: 0.4642 - accuracy: 0.8273 - val_loss: 1.1243 - val_accuracy: 0.6727
Epoch 74/100
448/448 [==============================] - 505s 1s/step - loss: 0.4503 - accuracy: 0.8318 - val_loss: 1.1209 - val_accuracy: 0.6794
Epoch 75/100
448/448 [==============================] - 487s 1s/step - loss: 0.4527 - accuracy: 0.8311 - val_loss: 1.1563 - val_accuracy: 0.6763
Epoch 76/100
448/448 [==============================] - 487s 1s/step - loss: 0.4417 - accuracy: 0.8360 - val_loss: 1.1374 - val_accuracy: 0.6802
Epoch 77/100
448/448 [==============================] - 487s 1s/step - loss: 0.4314 - accuracy: 0.8422 - val_loss: 1.1473 - val_accuracy: 0.6819
Epoch 78/100
448/448 [==============================] - 487s 1s/step - loss: 0.4223 - accuracy: 0.8428 - val_loss: 1.1729 - val_accuracy: 0.6864
Epoch 79/100
448/448 [==============================] - 487s 1s/step - loss: 0.4166 - accuracy: 0.8454 - val_loss: 1.1709 - val_accuracy: 0.6839
Epoch 80/100
448/448 [==============================] - 487s 1s/step - loss: 0.4118 - accuracy: 0.8464 - val_loss: 1.1497 - val_accuracy: 0.6828
Epoch 81/100
448/448 [==============================] - 487s 1s/step - loss: 0.4067 - accuracy: 0.8506 - val_loss: 1.2039 - val_accuracy: 0.6822
Epoch 82/100
448/448 [==============================] - 487s 1s/step - loss: 0.4005 - accuracy: 0.8518 - val_loss: 1.1833 - val_accuracy: 0.6777
Epoch 83/100
448/448 [==============================] - 487s 1s/step - loss: 0.3983 - accuracy: 0.8548 - val_loss: 1.1964 - val_accuracy: 0.6814
Epoch 84/100
448/448 [==============================] - 487s 1s/step - loss: 0.3840 - accuracy: 0.8563 - val_loss: 1.2835 - val_accuracy: 0.6616
Epoch 85/100
448/448 [==============================] - 487s 1s/step - loss: 0.3837 - accuracy: 0.8599 - val_loss: 1.2432 - val_accuracy: 0.6747
Epoch 86/100
448/448 [==============================] - 487s 1s/step - loss: 0.3787 - accuracy: 0.8580 - val_loss: 1.1962 - val_accuracy: 0.6758
Epoch 87/100
448/448 [==============================] - 488s 1s/step - loss: 0.3801 - accuracy: 0.8610 - val_loss: 1.2188 - val_accuracy: 0.6895
Epoch 88/100
448/448 [==============================] - 487s 1s/step - loss: 0.3554 - accuracy: 0.8698 - val_loss: 1.3115 - val_accuracy: 0.6777
Epoch 89/100
448/448 [==============================] - 487s 1s/step - loss: 0.3549 - accuracy: 0.8686 - val_loss: 1.3106 - val_accuracy: 0.6629
Epoch 90/100
448/448 [==============================] - 487s 1s/step - loss: 0.3499 - accuracy: 0.8688 - val_loss: 1.2544 - val_accuracy: 0.6833
Epoch 91/100
448/448 [==============================] - 487s 1s/step - loss: 0.3504 - accuracy: 0.8708 - val_loss: 1.2904 - val_accuracy: 0.6710
Epoch 92/100
448/448 [==============================] - 487s 1s/step - loss: 0.3399 - accuracy: 0.8752 - val_loss: 1.2829 - val_accuracy: 0.6763
Epoch 93/100
448/448 [==============================] - 487s 1s/step - loss: 0.3343 - accuracy: 0.8775 - val_loss: 1.2838 - val_accuracy: 0.6850
Epoch 94/100
448/448 [==============================] - 486s 1s/step - loss: 0.3273 - accuracy: 0.8802 - val_loss: 1.3583 - val_accuracy: 0.6833
Epoch 95/100
448/448 [==============================] - 486s 1s/step - loss: 0.3280 - accuracy: 0.8782 - val_loss: 1.3505 - val_accuracy: 0.6710
Epoch 96/100
448/448 [==============================] - 487s 1s/step - loss: 0.3253 - accuracy: 0.8817 - val_loss: 1.3726 - val_accuracy: 0.6501
Epoch 97/100
448/448 [==============================] - 487s 1s/step - loss: 0.3105 - accuracy: 0.8863 - val_loss: 1.3148 - val_accuracy: 0.6825
Epoch 98/100
448/448 [==============================] - 487s 1s/step - loss: 0.3125 - accuracy: 0.8839 - val_loss: 1.4349 - val_accuracy: 0.6775
Epoch 99/100
448/448 [==============================] - 487s 1s/step - loss: 0.3088 - accuracy: 0.8871 - val_loss: 1.3798 - val_accuracy: 0.6733
Epoch 100/100
448/448 [==============================] - 487s 1s/step - loss: 0.3037 - accuracy: 0.8895 - val_loss: 1.3981 - val_accuracy: 0.6599
Saved model to disk