# Ultrasonic-Attacker
This is a fun and convenient ultrasonic injection tool.

Used to implement audio injection attacks on microphones.

Ultrasonic-Attacker consists of two parts: **Ultrasonic Modulator** and **Ultrasonic Player**.

You can follow the steps below to learn how to use it.

## Step 1: Ultrasonic Modulator
Ultrasonic Modulator superimposes the audio with a high-frequency carrier, thereby modulating the audio to the inaudible region of the ultrasound.

### Step 1.1: Prepare the environment
- python 3.12
- ffmpeg
- Audacity

### Step 1.2: Installation dependency
1. Clone the project locally

``git clone https://github.com/fangfano/Ultrasonic-Attacker.git``
2. Go to the project folder and install dependencies

``pip install -r requirements.txt``
3. Run modulator

``python Modulator.py``

### Step 1.3: Real-time voice modulation（Method 1）
1. Select the microphone device
【图片】
2. Record the voice and save it
【图片】
3. Selective modulation frequency
25khz is a good start and can attack most microphone devices.
4. Start modulation
【调制完成】

【结果1的图】

### Step 1.4: Selective audio modulation（Method 2）
1. Click the **Select audio file** button

【图片】

2. Select a prepared audio

【图片】

3. Selective modulation frequency
25khz is a good start and can attack most microphone devices.

4. Start modulation

【图片】

### Attention
1. lalala
2. 

## Step 2: Ultrasonic Player
### Step 2.1 Equipment list: 
- Power supply: 12V lithium battery
- Audio amplifier: TPA3116D2 High power digital amplifier board dual channel 150W
- Power display: 5A constant voltage constant current step-down power module
- Playback sound card equipment: 192khz USB sound card (USB to 3.5mm audio interface)
- Audio cable: 3.5mm three-wire male audio cable
- Microphone array:

### Step 2.2 Connection mode
【图片】

### Attention
1. lalala
2. 

## Final: Attack Principle

