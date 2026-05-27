# Ultrasonic-Attacker (超声波攻击器)
这是一个有趣且便捷的超声波注入工具。
主要用于对麦克风实施音频注入攻击。

---

## 实际攻击演示
我们在电脑上播放这段超声波音频，然后将其作为攻击信号注入到另一台电脑的麦克风设备中。虽然人耳听不到这些超声波，但麦克风却能录下清晰的语音指令。
[![Actual working condition.png](https://pic1.imgdb.cn/item/67c93953066befcec6debb94.png)](https://pic1.imgdb.cn/item/67c93953066befcec6debb94.png)
我用手机录制了一段说“Hi Siri, open Wechat”的录音作为原始音频，你可以通过下方链接试听：
``https://github.com/fangfano/Ultrasonic-Attacker/raw/main/audio/Original%20audio.mp3``
麦克风录制到的超声波攻击音频如下：
``https://github.com/fangfano/Ultrasonic-Attacker/raw/main/audio/Attack%20effect.mp3``
语音转文字的结果：
[![speech to text.png](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf2.png)](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf2.png)
又或者可能是我的英语发音不太标准吧 (^u^)。

---

## 原理与实现方法
Ultrasonic-Attacker 由两部分组成：**超声波调制器 (Ultrasonic Modulator)** 和 **超声波播放器 (Ultrasonic Player)**。
[![Ultrasonic-Attacker.png](https://pic1.imgdb.cn/item/67c93a99066befcec6debe26.png)](https://pic1.imgdb.cn/item/67c93a99066befcec6debe26.png)

如果你感兴趣，可以按照以下步骤学习如何使用它。

## 第一步：超声波调制器
超声波调制器会将音频与高频载波叠加，从而将原本的音频调制到人耳听不见的超声波频段。

### 1.1：准备环境
- Python 3.12
- ffmpeg
- Audacity

### 1.2：安装依赖
1. 将项目克隆到本地
``git clone https://github.com/fangfano/Ultrasonic-Attacker.git``
2. 进入项目文件夹并安装依赖
``pip install -r requirements.txt``
3. 运行调制器
``python Modulator.py``
操作界面如下：
[![interface.png](https://pic1.imgdb.cn/item/67c93a37066befcec6debd44.png)](https://pic1.imgdb.cn/item/67c93a37066befcec6debd44.png)

### 1.3：实时语音调制（方法一）
1. 选择你的麦克风设备
[![Select your device.png](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdba.png)](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdba.png)
2. 录制语音并保存
[![Recording audio.png](https://pic1.imgdb.cn/item/67c93a6c066befcec6debdb2.png)](https://pic1.imgdb.cn/item/67c93a6c066befcec6debdb2.png)
3. 选择调制频率
25kHz 是个不错的初始选择，能够成功攻击大部分麦克风设备。
4. 开始调制
[![modulation.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd82.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd82.png)
结果：
[![result 1.png](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb3.png)](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb3.png)
使用 Audacity 对比原始音频和超声波音频：
[![ompare result 0.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd85.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd85.png)

### 1.4：选择已有音频进行调制（方法二）
1. 点击 **Select audio file**（选择音频文件）按钮
[![click select file button.png](https://pic1.imgdb.cn/item/67c93a36066befcec6debd41.png)](https://pic1.imgdb.cn/item/67c93a36066befcec6debd41.png)
2. 选择提前准备好的音频
[![an audio file.png](https://pic1.imgdb.cn/item/67c93954066befcec6debb96.png)](https://pic1.imgdb.cn/item/67c93954066befcec6debb96.png)
3. 选择调制频率
同样，25kHz 是个不错的初始选择，可以攻击大部分麦克风。
4. 开始调制
[![start.png](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf3.png)](https://pic1.imgdb.cn/item/67c93a8a066befcec6debdf3.png)
结果：
[![modulation2.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd83.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd83.png)
[![result 2.png](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb6.png)](https://pic1.imgdb.cn/item/67c93a6d066befcec6debdb6.png)
使用 Audacity 对比原始音频和超声波音频：
[![ompare result 1.png](https://pic1.imgdb.cn/item/67c93a58066befcec6debd87.png)](https://pic1.imgdb.cn/item/67c93a58066befcec6debd87.png)

### 注意事项
1. 调制后的音频频率不应低于 16kHz，否则可能会被人耳听到。
同时，调制频率也不应高于 30kHz，否则可能无法成功注入频响范围在 20Hz-16kHz 的麦克风设备。

## 第二步：超声波播放器
### 2.1：设备清单
- 供电：12V 锂电池
[![12V battery.png](https://pic1.imgdb.cn/item/67c93953066befcec6debb91.png)](https://pic1.imgdb.cn/item/67c93953066befcec6debb91.png)
- 音频功放：TPA3116D2 大功率数字功放板（双通道 150W）
[![TPA3116D2.png](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdf6.png)](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdf6.png)
- 电量显示：5A 恒压恒流降压电源模块
[![Power display module.png](https://pic1.imgdb.cn/item/67c93a59066befcec6debd8a.png)](https://pic1.imgdb.cn/item/67c93a59066befcec6debd8a.png)
- 播放声卡设备：192kHz USB 声卡（USB 转 3.5mm 音频接口）
[![192khz sound card.png](https://pic1.imgdb.cn/item/67c93953066befcec6debb92.png)](https://pic1.imgdb.cn/item/67c93953066befcec6debb92.png)
- 音频线：3.5mm 三芯公头音频线
[![3.5mm Audio cable.png](https://pic1.imgdb.cn/item/67c93952066befcec6debb90.png)](https://pic1.imgdb.cn/item/67c93952066befcec6debb90.png)
- 麦克风阵列（超声波阵列）：
[![Ultrasonic array.jpg](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdfa.jpg)](https://pic1.imgdb.cn/item/67c93a8b066befcec6debdfa.jpg)

### 2.2：接线方式
[![Attack system wiring diagram.png](https://pic1.imgdb.cn/item/67c93a36066befcec6debd3f.png)](https://pic1.imgdb.cn/item/67c93a36066befcec6debd3f.png)

### 注意事项
1. 调幅（AM）后的频率范围在 20kHz-40kHz 之间。根据奈奎斯特采样定理，96kHz 的采样率就足以完全还原该信号。
如果你的电脑不支持 96kHz 采样率，我们就需要通过 3.5mm 音频线连接一个支持 96kHz 采样率的外置声卡。

---

## 攻击原理
原理示意图如下：
[![Attack principle.png](https://pic1.imgdb.cn/item/67c93a35066befcec6debd3e.png)](https://pic1.imgdb.cn/item/67c93a35066befcec6debd3e.png)
原理解析：
1. **声音捕获**：首先，麦克风接收声音信号。这些声音信号是包含从环境中捕获的各种声音（人声、噪音等）的模拟信号。假设它现在接收到的就是我们调制好的超声波攻击音频。
2. **信号放大**：麦克风接收到的模拟信号通常非常微弱，需要通过放大器来增强信号强度以便后续处理。由于麦克风的非线性效应，超声波高频信号在放大过程中会产生低频谐波。
3. **信号滤波**：放大后的信号会经过一个低通滤波器（LPF），它会滤除信号中的高频噪声，只允许特定频率（如 20kHz）以下的信号通过。这是为了模拟人耳的听觉范围，因为人耳通常听不到 20kHz 以上的声音。因此，超声波部分被完全滤除，只剩下了低频谐波部分——而这正是攻击者为了注入语音指令精心调制的那部分信号。
4. **数字化转换**：滤波后的模拟信号随后会被模数转换器（ADC）转换为数字信号。ADC 会按照设定的采样率（例如 192kHz）和位深（例如 24 bits）对信号进行采样和量化，最终生成数字信号。
5. **语音识别**：数字信号被传递给语音识别系统。语音识别系统通过算法将这些数字信号转换成文本。
6. **指令执行**：文本信息会被转换为指令执行系统能够识别的命令。如果该命令是预先定义且可识别的，系统就会执行相应的操作。
**综上所述**，通过将语音指令调制到超声波载波上，我们可以生成人耳听不见但能被麦克风捕捉到的信号。当这些信号经过麦克风放大器和 ADC 转换成数字信号后，会被语音识别系统误认作是人类的语音指令，从而执行我们预设的命令。

超声波音频调制流程图如下：
[![Flow chart of modulator operation.png](https://pic1.imgdb.cn/item/67c93a36066befcec6debd42.png)](https://pic1.imgdb.cn/item/67c93a36066befcec6debd42.png)
