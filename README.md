# Ultrasonic-Attacker  
This is a fun and convenient ultrasonic injection tool.  
Used to implement audio injection attacks on microphones.  

---

## Actual attack Demo  
We played the ultrasonic audio on the computer, and then injected the attack into the microphone device of another computer, although the ultrasonic ear can not be heard, but the microphone can record obvious voice commands.  
[![Actual working condition.png](https://pic1.imgdb.cn/item/67c93953066befcec6debb94.png)](https://pic1.imgdb.cn/item/67c93953066befcec6debb94.png)  
I recorded a voice with my phone that said "Hi Siri, open Wechat". As the original audio, you can listen to it through the link below:  
``https://github.com/fangfano/Ultrasonic-Attacker/raw/main/audio/Original%20audio.mp3``  
The microphone recorded the ultrasonic attack audio as follows:  
``https://github.com/fangfano/Ultrasonic-Attacker/raw/main/audio/Attack%20effect.mp3``  
Speech to text result:  
[![speech to text.png](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf2.png)](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf2.png)  
Or maybe my English pronunciation is not standard (^u^) .  

---

## How to achieve it  
Ultrasonic-Attacker consists of two parts: **Ultrasonic Modulator** and **Ultrasonic Player**.  
[![Ultrasonic-Attacker.png](https://pic1.imgdb.cn/item/67c93a99066befcec6debe26.png)](https://pic1.imgdb.cn/item/67c93a99066befcec6debe26.png)  

If you're interested, You can follow the steps below to learn how to use it.

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
[![interface.png](https://pic1.imgdb.cn/item/67c93a37066befcec6debd44.png)](https://pic1.imgdb.cn/item/67c93a37066befcec6debd44.png)  

### Step 1.3: Real-time voice modulation（Method 1）  
1. Select the microphone device  
[![Select your device.png](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdba.png)](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdba.png)  
2. Record the voice and save it  
[![Recording audio.png](https://pic1.imgdb.cn/item/67c93a6c066befcec6debdb2.png)](https://pic1.imgdb.cn/item/67c93a6c066befcec6debdb2.png)  
3. Selective modulation frequency  
25khz is a good start and can attack most microphone devices.  
4. Start modulation  
[![modulation.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd82.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd82.png)  
Result:  
[![result 1.png](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb3.png)](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb3.png)  
Compare raw audio with ultrasonic audio using Audacity:  
[![ompare result 0.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd85.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd85.png)  

### Step 1.4: Selective audio modulation（Method 2）  
1. Click the **Select audio file** button  
[![click select file button.png](https://pic1.imgdb.cn/item/67c93a36066befcec6debd41.png)](https://pic1.imgdb.cn/item/67c93a36066befcec6debd41.png)  
2. Select a prepared audio  
[![an audio file.png](https://pic1.imgdb.cn/item/67c93954066befcec6debb96.png)](https://pic1.imgdb.cn/item/67c93954066befcec6debb96.png)  
3. Selective modulation frequency  
25khz is a good start and can attack most microphone devices.  
4. Start modulation  
[![start.png](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf3.png)](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf3.png)  
Result:  
[![modulation2.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd83.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd83.png)  
[![result 2.png](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb6.png)](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb6.png)  
Compare raw audio with ultrasonic audio using Audacity:  
[![ompare result 1.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd87.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd87.png)  

### Attention  
1. The frequency of the modulated audio should not be lower than 16khz, which may be heard by human ears.  
The modulated audio frequency should not be higher than 30khz, and it may not be possible to inject microphone devices with a frequency response range of 20hz-16khz.  

## Step 2: Ultrasonic Player  
### Step 2.1 Equipment list:  
- Power supply: 12V lithium battery  
[![12V battery.png](https://pic1.imgdb.cn/item/67c93953066befcec6debb91.png)](https://pic1.imgdb.cn/item/67c93953066befcec6debb91.png)  
- Audio amplifier: TPA3116D2 High power digital amplifier board dual channel 150W  
[![TPA3116D2.png](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdf6.png)](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdf6.png)  
- Power display: 5A constant voltage constant current step-down power module  
[![Power display module.png](https://pic1.imgdb.cn/item/67c93a59066befcec6debd8a.png)](https://pic1.imgdb.cn/item/67c93a59066befcec6debd8a.png)  
- Playback sound card equipment: 192khz USB sound card (USB to 3.5mm audio interface)  
[![192khz sound card.png](https://pic1.imgdb.cn/item/67c93953066befcec6debb92.png)](https://pic1.imgdb.cn/item/67c93953066befcec6debb92.png)  
- Audio cable: 3.5mm three-wire male audio cable  
[![3.5mm Audio cable.png](https://pic1.imgdb.cn/item/67c93952066befcec6debb90.png)](https://pic1.imgdb.cn/item/67c93952066befcec6debb90.png)  
- Microphone array:  
[![Ultrasonic array.jpg](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdfa.jpg)](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdfa.jpg)  

### Step 2.2 Connection mode  
[![Attack system wiring diagram.png](https://pic1.imgdb.cn/item/67c93a36066befcec6debd3f.png)](https://pic1.imgdb.cn/item/67c93a36066befcec6debd3f.png)  

### Attention  
1. The result of amplitude modulation (AM) is 20khz-40khz, and according to Nyquist sampling theorem, the sampling rate of 96khz is sufficient to completely restore the signal.  
If your computer does not support 96khz sampling, we need to support the 96Khz sampling rate of the external sound card connected to the 3.5mm audio cable.  

---

## Attack Principle  
The schematic diagram is as follows:  
[![Attack principle.png](https://pic1.imgdb.cn/item/67c93a35066befcec6debd3e.png)](https://pic1.imgdb.cn/item/67c93a35066befcec6debd3e.png)  
Explain:  
1. Voice capture: First, the microphone receives the sound signal. These sound signals are analog signals that contain a variety of sounds captured from the environment, including human voices, noise, etc. It is assumed that what it receives is the modulated ultrasonic attack audio.  
2. Signal amplification: The analog signal received by the microphone is usually very weak and needs to be amplified by an amplifier to increase the strength of the signal so that it can be further processed. Due to the nonlinear effect of the microphone, low frequency harmonics will be produced in the amplification process of the ultrasonic high frequency signal.  
3. Signal filtering: The amplified signal passes through a low-pass filter (LPF), which removes high-frequency noise from the signal and only allows signals below a certain frequency (such as 20kHz) to pass through. This is to simulate the hearing range of the human ear, which typically cannot hear sounds above 20kHz. Therefore, the ultrasonic part is completely filtered out, leaving only the low-frequency harmonic part, which is the part of the attacker carefully modulated to inject the voice command.  
4. Digitalization: The filtered analog signal is then converted into a digital signal by an analog-to-digital converter (ADC). The ADC samples and quantifies the signal at a set sampling rate (e.g. 192kHz) and bit depth (e.g. 24 bits) to generate a digital signal.  
5. Speech recognition: The digital signal is passed to the speech recognition system. Speech recognition systems use algorithms to convert digital signals into text.  
6. Command execution: Text information is converted into commands that can be recognized by the command execution system. If the command is a pre-defined, identifiable command, then the system will perform the corresponding action.  
**Thus**, we can generate signals that are inaudible to the human ear but can be captured by microphones by modulating voice commands onto an ultrasonic carrier. After these signals pass through the microphone amplifier and ADC, they are converted into digital signals, which are mistakenly recognized by the speech recognition system as human voice commands, so as to execute our preset commands.  

Ultrasonic audio modulation process:  
[![Flow chart of modulator operation.png](https://pic1.imgdb.cn/item/67c93a36066befcec6debd42.png)](https://pic1.imgdb.cn/item/67c93a36066befcec6debd42.png)  
