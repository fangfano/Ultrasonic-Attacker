# Ultrasonic-Attacker  
This is a fun and convenient ultrasonic injection tool.  
Used to implement audio injection attacks on microphones.   

Ultrasonic-Attacker consists of two parts: **Ultrasonic Modulator** and **Ultrasonic Player**.  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Ultrasonic-Attacker.png)  

You can follow the steps below to learn how to use it.  

## Step 1: Ultrasonic Modulator  
Ultrasonic Modulator superimposes the audio with a high-frequency carrier, thereby modulating the audio to the inaudible region of the ultrasound.  

### Step 1.1: Prepare the environment
- Python 3.12
- ffmpeg
- Audacity  

### Step 1.2: Installation dependency  
1. Clone the project locally  
``git clone https://github.com/fangfano/Ultrasonic-Attacker.git``  
2. Go to the project folder and install dependencies  
``pip install -r requirements.txt``  
3. Run modulator  
``python Modulator.py``  
Interface as follow:  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/interface.png)  

### Step 1.3: Real-time voice modulation（Method 1）  
1. Select the microphone device  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Select%20your%20device.png)  
2. Record the voice and save it  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Recording%20audio.png)  
3. Selective modulation frequency  
25khz is a good start and can attack most microphone devices.  
4. Start modulation    
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/modulation.png)   
Result:  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/result%201.png)  
Compare raw audio with ultrasonic audio using Audacity:
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/ompare%20result%200.png)   

### Step 1.4: Selective audio modulation（Method 2）  
1. Click the **Select audio file** button  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/click%20select%20file%20button.png)   
2. Select a prepared audio  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/an%20audio%20file.png)  
3. Selective modulation frequency  
25khz is a good start and can attack most microphone devices.  
4. Start modulation  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/start.png)  
Result:   
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/modulation2.png)  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/result%202.png)  
Compare raw audio with ultrasonic audio using Audacity:  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/ompare%20result%201.png)  

### Attention  
1. lalala
2. 

## Step 2: Ultrasonic Player  
### Step 2.1 Equipment list:   
- Power supply: 12V lithium battery    

- Audio amplifier: TPA3116D2 High power digital amplifier board dual channel 150W  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/TPA3116D2.png)  
- Power display: 5A constant voltage constant current step-down power module  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Power%20display%20module.png)  
- Playback sound card equipment: 192khz USB sound card (USB to 3.5mm audio interface)  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/192khz%20sound%20card.png)  
- Audio cable: 3.5mm three-wire male audio cable   
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/3.5mm%20Audio%20cable.png)  
- Microphone array:  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Ultrasonic%20array.jpg)  

### Step 2.2 Connection mode  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Attack%20system%20wiring%20diagram.png)  

### Attention  
1. lalala
2. 

## Step 3: Actual attack case  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Actual%20working%20condition.png)   

## Final: Attack Principle  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Attack%20principle.png)  
Flow chart of modulator operation:  
![](https://github.com/fangfano/Ultrasonic-Attacker/blob/main/picture/Flow%20chart%20of%20modulator%20operation.png)  